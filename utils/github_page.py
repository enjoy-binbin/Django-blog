import logging
import os

from django.conf import settings
from django.template import Template, Context
from git import Repo

from utils.mistune_markdown import article_markdown

# from markdown import markdown

logger = logging.getLogger('debug')


class SyncGit:
    """ Git上传, 需要有对应setting里的项目目录, 且可以经过ssh上传github """

    def __init__(self):
        self.repo = Repo(settings.GITHUB_PAGE_DIR)

    def sync(self, add_all=True, commit='add post', name='origin'):
        """ 同步文章到github page的仓库 """
        if not settings.GITHUB_PAGE:
            return False, 'Do not enable GITHUB_PAGE'

        try:
            self.add(add_all)
            self.commit(commit)
            self.push(name)
            return True, 'Github page synced Successful'

        except Exception as e:
            logging.error(str(e))
            return False, str(e)

    def add(self, add_all=True):
        self.repo.git.add(A=add_all)

    def commit(self, commit):
        self.repo.index.commit(commit)

    def push(self, name='origin'):
        self.repo.remote(name=name).push()


template = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1"/>
    <meta name="copyright" content="©2020 Binblog所有"/>
    <link rel="stylesheet" href="/static/style.min.css" media="screen" type="text/css"/>

    <!-- Begin SEO tag -->
    <title>{{ title }}</title>
    <meta property="og:locale" content="zh_CN"/>
    <meta property="og:type" content="article"/>
    <meta property="og:title" content="{{ title }}"/>
    <meta property="og:description" content="{{ description }}"/>
    <meta property="og:site_name" content="{{ title }}"/>
    <meta name="description" content="{{ description }}"/>
    <!-- End SEO tag -->
</head>

<body>
<header>
    <div class="inner">
        <a href="/">
            <h1>彬彬同学丶</h1>
        </a>
        <h2>Choose what you love. Love what you choose.</h2>
    </div>
</header>

<div id="content-wrapper">
    <div class="inner clearfix">
        <section id="main-content">
        
            {% if display_title %}
                <h1 id="art-title">{{ title }}</h1>
            {% endif %}
            
            {% if content %}
                {{ content|safe }}
            {% endif %}
            
            {% if article_list %}
                <div class="entry-content">
                    {% regroup article_list by add_time.year as year_list %}
                    <ul>
                        {% for year in year_list %}
                        <li>{{ year.grouper }} 年
                            {% regroup year.list by add_time.month as month_list %}
                            <ul>
                                {% for month in month_list %}
                                <li>{{ month.grouper }} 月
                                    <ul>
                                        {% for article in month.list %}
                                        <li><a href="{{ article.get_github_page_url }}">{{ article.title }}</a></li>
                                        {% endfor %}
                                    </ul>
                                </li>
                                {% endfor %}
                            </ul>
                        </li>
                        {% endfor %}
                    </ul>
                </div>
            {% endif %}

        </section>

        <aside id="sidebar">
            <blockquote class="route">关于我</blockquote>
            <p>{{ about_me }}</p>
            
            <blockquote class="route">Github地址</blockquote>
            <a href="https://github.com/{{ github_user }}">
                <img border="0" src="{{ github_avatar }}" width="100%" height="100%" alt="{{ github_user }}"/>
            </a>
            
            {% if link_list %}
                <blockquote class="route">友情链接</blockquote>
                {% for link in link_list %}
                    <div class="sidebar-list"><a href="{{ link.url }}"> {{ link.name }}</a></div>
                {% endfor %}
            {% endif %}
        </aside>
    </div>
</div>
</body>

</html>
"""


class HtmlRender:
    def __init__(self):
        self.blog_dir = settings.GITHUB_PAGE_DIR

    def index(self, blog_setting, article_list, link_list):
        """
        渲染首页的HTML, 也就是文章归档页
        :param blog_setting 一些配置项
        :param article_list 文章列表(需要按照时间有序)
        :param link_list    友情链接列表
        """
        if not settings.GITHUB_PAGE:
            return False, 'Do not enable GITHUB_PAGE'

        try:
            context = Context({
                "title": blog_setting.name,
                "content": "文章归档页",
                "description": blog_setting.desc,
                "github_user": blog_setting.github_user,
                "github_avatar": blog_setting.github_avatar,
                "about_me": blog_setting.about_me,
                "article_list": article_list,
                "link_list": link_list,
            })
            with open(self.blog_dir + '/index.html', 'w', encoding='utf8') as ff:
                ff.write(Template(template).render(context))

            return SyncGit().sync()

        except Exception as e:
            return False, str(e)

    def detail(self, blog_setting, article):
        """
        渲染文章详情页的HTML, FIXME: 更好的markdown渲染效果
        :param blog_setting 一些配置项
        :param article      文章
        """
        if not settings.GITHUB_PAGE:
            return False, 'Do not enable GITHUB_PAGE'

        if not article:
            return False, f'No match article: {article}'

        try:
            # 判断分类目录是否存在, 不存在则创建
            if not os.path.isdir(self.blog_dir + '/' + article.category.name.strip()):
                os.mkdir(self.blog_dir + '/' + article.category.name.strip())

            context = Context({
                "display_title": True,
                "title": article.title,
                "description": article.title,
                "content": article_markdown(article.content),
                "github_user": blog_setting.github_user,
                "github_avatar": blog_setting.github_avatar,
                "about_me": blog_setting.about_me,
                # "category_tree": article.get_category_tree(),
                # "author": article.author,
                # "content": markdown(article.content, extensions=['extra', 'codehilite', 'tables', 'toc'])
            })

            file = self.blog_dir + '/' + article.category.name.strip() + '/' + article.title.strip() + '.html'
            with open(file, 'w', encoding='utf8') as f:
                return True, f.write(Template(template).render(context))

        except Exception as e:
            return False, str(e)
