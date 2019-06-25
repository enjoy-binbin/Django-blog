from blog.models import Setting


def get_setting():
    """ 返回一个setting实例 """
    if Setting.objects.count():
        return Setting.objects.first()
    else:
        # 但站点内没有配置实例时候, 会默认创建一个
        s = Setting()
        s.name = 'BinBlog'
        s.desc = '彬彬博客'
        s.keyword = 'python3, django2, blog, binblog'
        s.article_desc_len = 250
        s.sidebar_article_count = 5
        s.github_user = 'enjoy-binbin'
        s.github_repository = 'Django-blog'
        s.save()
        return s
