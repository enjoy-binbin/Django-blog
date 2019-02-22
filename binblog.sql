/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50636
Source Host           : 127.0.0.1:3306
Source Database       : binblog

Target Server Type    : MYSQL
Target Server Version : 50636
File Encoding         : 65001

Date: 2019-02-27 16:24:49
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for auth_group
-- ----------------------------
DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group
-- ----------------------------

-- ----------------------------
-- Table structure for auth_group_permissions
-- ----------------------------
DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_group_permissions
-- ----------------------------

-- ----------------------------
-- Table structure for auth_permission
-- ----------------------------
DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of auth_permission
-- ----------------------------
INSERT INTO `auth_permission` VALUES ('1', 'Can add log entry', '1', 'add_logentry');
INSERT INTO `auth_permission` VALUES ('2', 'Can change log entry', '1', 'change_logentry');
INSERT INTO `auth_permission` VALUES ('3', 'Can delete log entry', '1', 'delete_logentry');
INSERT INTO `auth_permission` VALUES ('4', 'Can view log entry', '1', 'view_logentry');
INSERT INTO `auth_permission` VALUES ('5', 'Can add permission', '2', 'add_permission');
INSERT INTO `auth_permission` VALUES ('6', 'Can change permission', '2', 'change_permission');
INSERT INTO `auth_permission` VALUES ('7', 'Can delete permission', '2', 'delete_permission');
INSERT INTO `auth_permission` VALUES ('8', 'Can view permission', '2', 'view_permission');
INSERT INTO `auth_permission` VALUES ('9', 'Can add group', '3', 'add_group');
INSERT INTO `auth_permission` VALUES ('10', 'Can change group', '3', 'change_group');
INSERT INTO `auth_permission` VALUES ('11', 'Can delete group', '3', 'delete_group');
INSERT INTO `auth_permission` VALUES ('12', 'Can view group', '3', 'view_group');
INSERT INTO `auth_permission` VALUES ('13', 'Can add content type', '4', 'add_contenttype');
INSERT INTO `auth_permission` VALUES ('14', 'Can change content type', '4', 'change_contenttype');
INSERT INTO `auth_permission` VALUES ('15', 'Can delete content type', '4', 'delete_contenttype');
INSERT INTO `auth_permission` VALUES ('16', 'Can view content type', '4', 'view_contenttype');
INSERT INTO `auth_permission` VALUES ('17', 'Can add session', '5', 'add_session');
INSERT INTO `auth_permission` VALUES ('18', 'Can change session', '5', 'change_session');
INSERT INTO `auth_permission` VALUES ('19', 'Can delete session', '5', 'delete_session');
INSERT INTO `auth_permission` VALUES ('20', 'Can view session', '5', 'view_session');
INSERT INTO `auth_permission` VALUES ('21', 'Can add 文章', '6', 'add_article');
INSERT INTO `auth_permission` VALUES ('22', 'Can change 文章', '6', 'change_article');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete 文章', '6', 'delete_article');
INSERT INTO `auth_permission` VALUES ('24', 'Can view 文章', '6', 'view_article');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 文章分类', '7', 'add_category');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 文章分类', '7', 'change_category');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 文章分类', '7', 'delete_category');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 文章分类', '7', 'view_category');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 文章评论', '8', 'add_comment');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 文章评论', '8', 'change_comment');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 文章评论', '8', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 文章评论', '8', 'view_comment');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 友情链接', '9', 'add_link');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 友情链接', '9', 'change_link');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 友情链接', '9', 'delete_link');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 友情链接', '9', 'view_link');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 站点配置', '10', 'add_setting');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 站点配置', '10', 'change_setting');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 站点配置', '10', 'delete_setting');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 站点配置', '10', 'view_setting');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 侧边栏', '11', 'add_sidebar');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 侧边栏', '11', 'change_sidebar');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 侧边栏', '11', 'delete_sidebar');
INSERT INTO `auth_permission` VALUES ('44', 'Can view 侧边栏', '11', 'view_sidebar');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 标签', '12', 'add_tag');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 标签', '12', 'change_tag');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 标签', '12', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 标签', '12', 'view_tag');
INSERT INTO `auth_permission` VALUES ('49', 'Can add user', '13', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('50', 'Can change user', '13', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete user', '13', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('52', 'Can view user', '13', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('53', 'Can add site', '14', 'add_site');
INSERT INTO `auth_permission` VALUES ('54', 'Can change site', '14', 'change_site');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete site', '14', 'delete_site');
INSERT INTO `auth_permission` VALUES ('56', 'Can view site', '14', 'view_site');

-- ----------------------------
-- Table structure for blog_article
-- ----------------------------
DROP TABLE IF EXISTS `blog_article`;
CREATE TABLE `blog_article` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `title` varchar(100) NOT NULL,
  `content` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `views` int(10) unsigned NOT NULL,
  `pub_time` datetime(6) DEFAULT NULL,
  `author_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `blog_article_author_id_905add38_fk_user_userprofile_id` (`author_id`),
  KEY `blog_article_category_id_7e38f15e_fk_blog_category_id` (`category_id`),
  CONSTRAINT `blog_article_author_id_905add38_fk_user_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `user_userprofile` (`id`),
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=96 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article
-- ----------------------------
INSERT INTO `blog_article` VALUES ('14', '2019-02-24 22:39:38.044277', '2019-02-25 19:02:02.307127', 'Django里的Sitemap', '# 为Django博客添加sitemap功能\r\n\r\n`sitemap`是 Google 最先引入的网站地图协议，维基百科的定义-> A Sitemap is an [XML](https://en.wikipedia.org/wiki/XML) file that lists the URLs for a site. 简单说就是个列出站点所有url的xml文件，方便网络爬虫抓去网站页面，它的作用简而言之就是优化搜索引擎的索引效率，详细的解释可以参考 维基百科。`https://en.wikipedia.org/wiki/Sitemaps`。网站地图sitemap一般放在域名根目录下，例如`www.xxxx.com/sitemap.xml`\r\n\r\nDjango文档地址:` https://docs.djangoproject.com/en/2.1/ref/contrib/sitemaps/`\r\n\r\n### 启用sitemap\r\n\r\n在django的settings.py中的INSTALL_APPS中添加:\r\n\r\n```\r\n\'django.contrib.sites\',\r\n\'django.contrib.sitemaps\',\r\n```\r\n\r\n确认settings.py中的`TEMPLATES`设置包含`DjangoTemplates`后端，并将`APP_DIRS`选项设置为True。其实django默认配置就是这样的，只有当你曾经修改过这些设置，才需要调整回来。\r\n\r\n然后进行数据迁移\r\n\r\n```shell\r\npython ./manage.py makemigrations\r\npython ./manage.py migrate\r\n```\r\n\r\n在settings.py里添加一行设置 `SITE_ID = 1`制定当前站点，这个是数据库中django_site表对应的ID值\r\n\r\n而后登陆django后台，修改SITE为自己网站的域名和名称，或者在数据库端直接修改。之后在admin右上角会多一个查看站点的功能，点击后会自动跳转到对应的项目页面。\r\n\r\n```python\r\n# admin后台配置注册 Site\r\nfrom django.contrib.sites.models import Site\r\nfrom django.contrib.sites.admin import SiteAdmin\r\n\r\nadmin.register(Site, SiteAdmin)  # 站点, sitemap使用\r\n```\r\n\r\n### 官网中的使用 [`GenericSitemap`](https://docs.djangoproject.com/en/2.1/ref/contrib/sitemaps/#django.contrib.sitemaps.GenericSitemap)的例子，直接在url里配置\r\n\r\n```python\r\n# urls.py\r\nfrom django.contrib.sitemaps import GenericSitemap\r\nfrom django.contrib.sitemaps.views import sitemap\r\nfrom django.urls import path\r\nfrom blog.models import Article\r\n\r\ninfo_dict = {\r\n    \'queryset\': Article.objects.all(),\r\n    \'date_field\': \'add_time\',\r\n}\r\n\r\nurlpatterns = [\r\n    # some generic view using info_dict\r\n    # ...\r\n\r\n    # the sitemap\r\n    path(\'sitemap.xml\', sitemap,\r\n         {\'sitemaps\': {\'blog\': GenericSitemap(info_dict, priority=0.6)}},\r\n         name=\'django.contrib.sitemaps.views.sitemap\'),\r\n]\r\n# 之后访问 127.0.0.1:8000/sitemap.xml\r\n```\r\n\r\n\r\n\r\n### 结合自己博客的代码编写\r\n\r\n在项目目录下创建sitemaps.py文件（和settings.py同级）\r\n\r\n```python\r\n# sitemaps.py\r\nfrom django.contrib.sitemaps import Sitemap\r\nfrom django.urls import reverse\r\nfrom blog.models import Article\r\n\r\nclass ArticleSitemap(Sitemap):\r\n    \"\"\" 指向所有文章条目链接的Sitemap \"\"\"\r\n    changefreq = \'daily\'  # 更改频率，文档里查找可使用的属性值\r\n    priority = 0.6  # 优先级\r\n\r\n    def items(self):\r\n        # 必需，返回一个对象列表，可以自己filter过滤, 被其他方法属性调用\r\n        return Article.objects.all()\r\n\r\n    def lastmod(self, obj):\r\n        # 可选，返回个datetime类型，表示items返回的每个对象的最后修改时间\r\n        return obj.modify_time\r\n    \r\n    def location(self, obj):\r\n        # 可选，返回每个obj对象的绝对路径，默认会调用obj.get_absolute_url方法\r\n        return reverse(\'blog:article_detail\', kwargs={\'article_id\': obj.id})\r\n    \r\n# urls.py\r\nfrom django.contrib.sitemaps.views import sitemap\r\nfrom .sitemaps import ArticleSitemap\r\n\r\nsitemaps = {\r\n    \'article\': ArticleSitemap,\r\n}\r\n\r\nurlpatterns = [\r\n    ....\r\n    path(\'sitemap.xml\', sitemap, {\'sitemaps\': sitemaps}),\r\n]\r\n\r\n# 之后访问 127.0.0.1:8000/sitemap.xml，看到一个xml文档\r\n```\r\n\r\n\r\n\r\n### 静态视图的Sitemap\r\n\r\n```python\r\n# sitemaps.py\r\nfrom django.contrib import sitemaps\r\nfrom django.urls import reverse\r\n\r\nclass StaticViewSitemap(sitemaps.Sitemap):\r\n    \"\"\" 静态视图，例如抓取index和关于我页 \"\"\"\r\n    priority = 0.5\r\n    changefreq = \'daily\'\r\n\r\n    def items(self):\r\n        # 在items里显式列出静态视图名称\r\n        return [\'index\', \'about\']\r\n\r\n    def location(self, item):\r\n        # 在location里用reverse调用, obj是一个个items返回后的对象\r\n        return reverse(item)\r\n\r\n# urls.py\r\nfrom django.contrib.sitemaps.views import sitemap\r\nfrom django.urls import path\r\n\r\nfrom .sitemaps import StaticViewSitemap\r\nfrom . import views\r\n\r\nsitemaps = {\r\n    \'static\': StaticViewSitemap,\r\n}\r\n\r\nurlpatterns = [\r\n    path(\'\', views.main, name=\'main\'),\r\n    path(\'about/\', views.about, name=\'about\'),\r\n    path(\'license/\', views.license, name=\'license\'),\r\n    # ...\r\n    path(\'sitemap.xml\', sitemap, {\'sitemaps\': sitemaps},\r\n         name=\'django.contrib.sitemaps.views.sitemap\')\r\n]\r\n```', '0', '39', null, '1', '1');
INSERT INTO `blog_article` VALUES ('15', '2019-02-25 22:04:11.114434', '2019-02-25 22:04:12.378735', 'nice title 1', 'nice content 1', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('16', '2019-02-25 22:04:12.498468', '2019-02-25 22:04:12.770948', 'nice title 2', 'nice content 2', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('17', '2019-02-25 22:04:12.828365', '2019-02-25 22:04:13.112053', 'nice title 3', 'nice content 3', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('18', '2019-02-25 22:04:13.167298', '2019-02-25 22:04:13.362755', 'nice title 4', 'nice content 4', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('19', '2019-02-25 22:04:13.417150', '2019-02-25 22:04:13.603846', 'nice title 5', 'nice content 5', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('20', '2019-02-25 22:04:13.749176', '2019-02-25 22:04:13.995765', 'nice title 6', 'nice content 6', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('21', '2019-02-25 22:04:14.133885', '2019-02-25 22:04:14.303839', 'nice title 7', 'nice content 7', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('22', '2019-02-25 22:04:14.359610', '2019-02-25 22:04:14.696131', 'nice title 8', 'nice content 8', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('23', '2019-02-25 22:04:14.792331', '2019-02-25 22:04:15.021395', 'nice title 9', 'nice content 9', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('24', '2019-02-25 22:04:15.079899', '2019-02-25 22:04:15.270943', 'nice title 10', 'nice content 10', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('25', '2019-02-25 22:04:15.460656', '2019-02-25 22:04:15.629554', 'nice title 11', 'nice content 11', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('26', '2019-02-25 22:04:15.735008', '2019-02-25 22:04:16.029576', 'nice title 12', 'nice content 12', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('27', '2019-02-25 22:04:16.090127', '2019-02-25 22:04:16.412846', 'nice title 13', 'nice content 13', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('28', '2019-02-25 22:04:16.469138', '2019-02-25 22:04:16.662498', 'nice title 14', 'nice content 14', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('29', '2019-02-25 22:04:16.719798', '2019-02-25 22:04:16.962628', 'nice title 15', 'nice content 15', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('30', '2019-02-25 22:04:17.116331', '2019-02-25 22:04:17.395863', 'nice title 16', 'nice content 16', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('31', '2019-02-25 22:04:17.452583', '2019-02-25 22:04:17.646624', 'nice title 17', 'nice content 17', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('32', '2019-02-25 22:04:17.702667', '2019-02-25 22:04:17.979326', 'nice title 18', 'nice content 18', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('33', '2019-02-25 22:04:18.035613', '2019-02-25 22:04:18.204774', 'nice title 19', 'nice content 19', '0', '0', null, '9', '4');
INSERT INTO `blog_article` VALUES ('34', '2019-02-25 22:18:52.230736', '2019-02-25 22:20:12.356010', '我是标题 1', '我是内容 1', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('35', '2019-02-25 22:20:13.255768', '2019-02-25 22:20:13.456146', '我是标题 2', '我是内容 2', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('36', '2019-02-25 22:20:13.513455', '2019-02-25 22:20:13.739492', '我是标题 3', '我是内容 3', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('37', '2019-02-25 22:20:13.830071', '2019-02-25 22:20:14.131673', '我是标题 4', '我是内容 4', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('38', '2019-02-25 22:20:14.186678', '2019-02-25 22:20:14.456419', '我是标题 5', '我是内容 5', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('39', '2019-02-25 22:20:14.513504', '2019-02-25 22:20:14.706426', '我是标题 6', '我是内容 6', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('40', '2019-02-25 22:20:14.880707', '2019-02-25 22:20:15.097554', '我是标题 7', '我是内容 7', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('41', '2019-02-25 22:20:15.154514', '2019-02-25 22:20:15.631619', '我是标题 8', '我是内容 8', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('42', '2019-02-25 22:20:15.691582', '2019-02-25 22:20:15.989830', '我是标题 9', '我是内容 9', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('43', '2019-02-25 22:20:16.087985', '2019-02-25 22:20:16.256370', '我是标题 10', '我是内容 10', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('44', '2019-02-25 22:20:16.355007', '2019-02-25 22:20:16.523214', '我是标题 11', '我是内容 11', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('45', '2019-02-25 22:20:16.708071', '2019-02-25 22:20:16.906317', '我是标题 12', '我是内容 12', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('46', '2019-02-25 22:20:16.963854', '2019-02-25 22:20:17.206524', '我是标题 13', '我是内容 13', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('47', '2019-02-25 22:20:17.264040', '2019-02-25 22:20:17.681057', '我是标题 14', '我是内容 14', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('48', '2019-02-25 22:20:17.737997', '2019-02-25 22:20:17.931475', '我是标题 15', '我是内容 15', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('49', '2019-02-25 22:20:17.988842', '2019-02-25 22:20:18.156599', '我是标题 16', '我是内容 16', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('50', '2019-02-25 22:20:18.328406', '2019-02-25 22:20:18.522924', '我是标题 17', '我是内容 17', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('51', '2019-02-25 22:20:18.579788', '2019-02-25 22:20:18.764976', '我是标题 18', '我是内容 18', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('52', '2019-02-25 22:20:18.821778', '2019-02-25 22:20:19.181718', '我是标题 19', '我是内容 19', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('53', '2019-02-25 22:20:19.240765', '2019-02-25 22:20:19.323276', 'I am the big title', '### 支持markdown', '0', '0', null, '10', '4');
INSERT INTO `blog_article` VALUES ('55', '2019-02-26 10:32:31.743778', '2019-02-26 10:33:06.796234', '我是测试标题 1', '我是测试内容 1', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('56', '2019-02-26 10:32:33.003042', '2019-02-26 10:33:07.614294', '我是测试标题 2', '我是测试内容 2', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('57', '2019-02-26 10:32:33.197858', '2019-02-26 10:33:07.710327', '我是测试标题 3', '我是测试内容 3', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('58', '2019-02-26 10:32:33.382611', '2019-02-26 10:33:07.763382', '我是测试标题 4', '我是测试内容 4', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('59', '2019-02-26 10:32:33.688398', '2019-02-26 10:33:07.820419', '我是测试标题 5', '我是测试内容 5', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('60', '2019-02-26 10:32:33.931139', '2019-02-26 10:33:07.908655', '我是测试标题 6', '我是测试内容 6', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('61', '2019-02-26 10:32:34.363019', '2019-02-26 10:33:07.971337', '我是测试标题 7', '我是测试内容 7', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('62', '2019-02-26 10:32:34.572274', '2019-02-26 10:33:08.030817', '我是测试标题 8', '我是测试内容 8', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('63', '2019-02-26 10:32:34.764708', '2019-02-26 10:33:08.105252', '我是测试标题 9', '我是测试内容 9', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('64', '2019-02-26 10:32:35.096670', '2019-02-26 10:33:08.181545', '我是测试标题 10', '我是测试内容 10', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('65', '2019-02-26 10:32:35.281272', '2019-02-26 10:33:08.278671', '我是测试标题 11', '我是测试内容 11', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('66', '2019-02-26 10:32:35.650885', '2019-02-26 10:33:08.348437', '我是测试标题 12', '我是测试内容 12', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('67', '2019-02-26 10:32:35.880853', '2019-02-26 10:33:08.405788', '我是测试标题 13', '我是测试内容 13', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('68', '2019-02-26 10:32:36.056838', '2019-02-26 10:33:08.497763', '我是测试标题 14', '我是测试内容 14', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('69', '2019-02-26 10:32:36.249457', '2019-02-26 10:33:08.574274', '我是测试标题 15', '我是测试内容 15', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('70', '2019-02-26 10:32:36.456053', '2019-02-26 10:33:08.675499', '我是测试标题 16', '我是测试内容 16', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('71', '2019-02-26 10:32:36.666547', '2019-02-26 10:33:08.741386', '我是测试标题 17', '我是测试内容 17', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('72', '2019-02-26 10:32:36.865159', '2019-02-26 10:33:08.796045', '我是测试标题 18', '我是测试内容 18', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('73', '2019-02-26 10:32:37.049816', '2019-02-26 10:33:08.881558', '我是测试标题 19', '我是测试内容 19', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('75', '2019-02-26 10:33:09.185104', '2019-02-26 10:33:09.411529', '彬彬博客', '### 支持markdown\r\n            ```python\r\n            支持语法高亮\r\n```', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('76', '2019-02-26 10:35:46.717388', '2019-02-26 10:35:47.639586', '我是测试标题1 1', '我是测试内容1 1', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('77', '2019-02-26 10:35:47.699974', '2019-02-26 10:35:47.856237', '我是测试标题1 2', '我是测试内容1 2', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('78', '2019-02-26 10:35:47.947751', '2019-02-26 10:35:48.081222', '我是测试标题1 3', '我是测试内容1 3', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('79', '2019-02-26 10:35:48.139498', '2019-02-26 10:35:48.289569', '我是测试标题1 4', '我是测试内容1 4', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('80', '2019-02-26 10:35:48.349800', '2019-02-26 10:35:48.531573', '我是测试标题1 5', '我是测试内容1 5', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('81', '2019-02-26 10:35:48.595525', '2019-02-26 10:35:48.781328', '我是测试标题1 6', '我是测试内容1 6', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('82', '2019-02-26 10:35:48.837895', '2019-02-26 10:35:49.065162', '我是测试标题1 7', '我是测试内容1 7', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('83', '2019-02-26 10:35:49.182905', '2019-02-26 10:35:49.373374', '我是测试标题1 8', '我是测试内容1 8', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('84', '2019-02-26 10:35:49.421328', '2019-02-26 10:35:49.573122', '我是测试标题1 9', '我是测试内容1 9', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('85', '2019-02-26 10:35:49.631323', '2019-02-26 10:35:50.029844', '我是测试标题1 10', '我是测试内容1 10', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('86', '2019-02-26 10:35:50.172298', '2019-02-26 10:35:50.323496', '我是测试标题1 11', '我是测试内容1 11', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('87', '2019-02-26 10:35:50.371511', '2019-02-26 10:35:50.523509', '我是测试标题1 12', '我是测试内容1 12', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('88', '2019-02-26 10:35:50.618175', '2019-02-26 10:35:50.748556', '我是测试标题1 13', '我是测试内容1 13', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('89', '2019-02-26 10:35:50.796069', '2019-02-26 10:35:50.965475', '我是测试标题1 14', '我是测试内容1 14', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('90', '2019-02-26 10:35:51.022357', '2019-02-26 10:35:51.207242', '我是测试标题1 15', '我是测试内容1 15', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('91', '2019-02-26 10:35:51.254755', '2019-02-26 10:35:51.382141', '我是测试标题1 16', '我是测试内容1 16', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('92', '2019-02-26 10:35:51.437899', '2019-02-26 10:35:51.623796', '我是测试标题1 17', '我是测试内容1 17', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('93', '2019-02-26 10:35:51.724806', '2019-02-26 10:35:51.865626', '我是测试标题1 18', '我是测试内容1 18', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('94', '2019-02-26 10:35:51.921416', '2019-02-26 10:35:52.065515', '我是测试标题1 19', '我是测试内容1 19', '0', '0', null, '11', '6');
INSERT INTO `blog_article` VALUES ('95', '2019-02-26 10:35:52.113385', '2019-02-26 10:35:52.282016', '彬彬博客21223', '### 支持Markdown\n\n```python\nprint(\'支持语法高亮\')\n```\n            ', '0', '0', null, '11', '6');

-- ----------------------------
-- Table structure for blog_article_tags
-- ----------------------------
DROP TABLE IF EXISTS `blog_article_tags`;
CREATE TABLE `blog_article_tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `article_id` int(11) NOT NULL,
  `tag_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_article_tags_article_id_tag_id_b78a22e9_uniq` (`article_id`,`tag_id`),
  KEY `blog_article_tags_tag_id_88eb3ed9_fk_blog_tag_id` (`tag_id`),
  CONSTRAINT `blog_article_tags_article_id_82c02dd6_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_article_tags_tag_id_88eb3ed9_fk_blog_tag_id` FOREIGN KEY (`tag_id`) REFERENCES `blog_tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=157 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article_tags
-- ----------------------------
INSERT INTO `blog_article_tags` VALUES ('1', '14', '1');
INSERT INTO `blog_article_tags` VALUES ('3', '15', '2');
INSERT INTO `blog_article_tags` VALUES ('2', '15', '3');
INSERT INTO `blog_article_tags` VALUES ('5', '16', '2');
INSERT INTO `blog_article_tags` VALUES ('4', '16', '4');
INSERT INTO `blog_article_tags` VALUES ('7', '17', '2');
INSERT INTO `blog_article_tags` VALUES ('6', '17', '5');
INSERT INTO `blog_article_tags` VALUES ('9', '18', '2');
INSERT INTO `blog_article_tags` VALUES ('8', '18', '6');
INSERT INTO `blog_article_tags` VALUES ('11', '19', '2');
INSERT INTO `blog_article_tags` VALUES ('10', '19', '7');
INSERT INTO `blog_article_tags` VALUES ('13', '20', '2');
INSERT INTO `blog_article_tags` VALUES ('12', '20', '8');
INSERT INTO `blog_article_tags` VALUES ('15', '21', '2');
INSERT INTO `blog_article_tags` VALUES ('14', '21', '9');
INSERT INTO `blog_article_tags` VALUES ('17', '22', '2');
INSERT INTO `blog_article_tags` VALUES ('16', '22', '10');
INSERT INTO `blog_article_tags` VALUES ('19', '23', '2');
INSERT INTO `blog_article_tags` VALUES ('18', '23', '11');
INSERT INTO `blog_article_tags` VALUES ('21', '24', '2');
INSERT INTO `blog_article_tags` VALUES ('20', '24', '12');
INSERT INTO `blog_article_tags` VALUES ('23', '25', '2');
INSERT INTO `blog_article_tags` VALUES ('22', '25', '13');
INSERT INTO `blog_article_tags` VALUES ('25', '26', '2');
INSERT INTO `blog_article_tags` VALUES ('24', '26', '14');
INSERT INTO `blog_article_tags` VALUES ('27', '27', '2');
INSERT INTO `blog_article_tags` VALUES ('26', '27', '15');
INSERT INTO `blog_article_tags` VALUES ('29', '28', '2');
INSERT INTO `blog_article_tags` VALUES ('28', '28', '16');
INSERT INTO `blog_article_tags` VALUES ('31', '29', '2');
INSERT INTO `blog_article_tags` VALUES ('30', '29', '17');
INSERT INTO `blog_article_tags` VALUES ('33', '30', '2');
INSERT INTO `blog_article_tags` VALUES ('32', '30', '18');
INSERT INTO `blog_article_tags` VALUES ('35', '31', '2');
INSERT INTO `blog_article_tags` VALUES ('34', '31', '19');
INSERT INTO `blog_article_tags` VALUES ('37', '32', '2');
INSERT INTO `blog_article_tags` VALUES ('36', '32', '20');
INSERT INTO `blog_article_tags` VALUES ('39', '33', '2');
INSERT INTO `blog_article_tags` VALUES ('38', '33', '21');
INSERT INTO `blog_article_tags` VALUES ('41', '34', '1');
INSERT INTO `blog_article_tags` VALUES ('40', '34', '3');
INSERT INTO `blog_article_tags` VALUES ('43', '35', '1');
INSERT INTO `blog_article_tags` VALUES ('42', '35', '4');
INSERT INTO `blog_article_tags` VALUES ('45', '36', '1');
INSERT INTO `blog_article_tags` VALUES ('44', '36', '5');
INSERT INTO `blog_article_tags` VALUES ('47', '37', '1');
INSERT INTO `blog_article_tags` VALUES ('46', '37', '6');
INSERT INTO `blog_article_tags` VALUES ('49', '38', '1');
INSERT INTO `blog_article_tags` VALUES ('48', '38', '7');
INSERT INTO `blog_article_tags` VALUES ('51', '39', '1');
INSERT INTO `blog_article_tags` VALUES ('50', '39', '8');
INSERT INTO `blog_article_tags` VALUES ('53', '40', '1');
INSERT INTO `blog_article_tags` VALUES ('52', '40', '9');
INSERT INTO `blog_article_tags` VALUES ('55', '41', '1');
INSERT INTO `blog_article_tags` VALUES ('54', '41', '10');
INSERT INTO `blog_article_tags` VALUES ('57', '42', '1');
INSERT INTO `blog_article_tags` VALUES ('56', '42', '11');
INSERT INTO `blog_article_tags` VALUES ('59', '43', '1');
INSERT INTO `blog_article_tags` VALUES ('58', '43', '12');
INSERT INTO `blog_article_tags` VALUES ('61', '44', '1');
INSERT INTO `blog_article_tags` VALUES ('60', '44', '13');
INSERT INTO `blog_article_tags` VALUES ('63', '45', '1');
INSERT INTO `blog_article_tags` VALUES ('62', '45', '14');
INSERT INTO `blog_article_tags` VALUES ('65', '46', '1');
INSERT INTO `blog_article_tags` VALUES ('64', '46', '15');
INSERT INTO `blog_article_tags` VALUES ('67', '47', '1');
INSERT INTO `blog_article_tags` VALUES ('66', '47', '16');
INSERT INTO `blog_article_tags` VALUES ('69', '48', '1');
INSERT INTO `blog_article_tags` VALUES ('68', '48', '17');
INSERT INTO `blog_article_tags` VALUES ('71', '49', '1');
INSERT INTO `blog_article_tags` VALUES ('70', '49', '18');
INSERT INTO `blog_article_tags` VALUES ('73', '50', '1');
INSERT INTO `blog_article_tags` VALUES ('72', '50', '19');
INSERT INTO `blog_article_tags` VALUES ('75', '51', '1');
INSERT INTO `blog_article_tags` VALUES ('74', '51', '20');
INSERT INTO `blog_article_tags` VALUES ('77', '52', '1');
INSERT INTO `blog_article_tags` VALUES ('76', '52', '21');
INSERT INTO `blog_article_tags` VALUES ('78', '53', '1');
INSERT INTO `blog_article_tags` VALUES ('80', '55', '1');
INSERT INTO `blog_article_tags` VALUES ('79', '55', '3');
INSERT INTO `blog_article_tags` VALUES ('82', '56', '1');
INSERT INTO `blog_article_tags` VALUES ('81', '56', '4');
INSERT INTO `blog_article_tags` VALUES ('84', '57', '1');
INSERT INTO `blog_article_tags` VALUES ('83', '57', '5');
INSERT INTO `blog_article_tags` VALUES ('86', '58', '1');
INSERT INTO `blog_article_tags` VALUES ('85', '58', '6');
INSERT INTO `blog_article_tags` VALUES ('88', '59', '1');
INSERT INTO `blog_article_tags` VALUES ('87', '59', '7');
INSERT INTO `blog_article_tags` VALUES ('90', '60', '1');
INSERT INTO `blog_article_tags` VALUES ('89', '60', '8');
INSERT INTO `blog_article_tags` VALUES ('92', '61', '1');
INSERT INTO `blog_article_tags` VALUES ('91', '61', '9');
INSERT INTO `blog_article_tags` VALUES ('94', '62', '1');
INSERT INTO `blog_article_tags` VALUES ('93', '62', '10');
INSERT INTO `blog_article_tags` VALUES ('96', '63', '1');
INSERT INTO `blog_article_tags` VALUES ('95', '63', '11');
INSERT INTO `blog_article_tags` VALUES ('98', '64', '1');
INSERT INTO `blog_article_tags` VALUES ('97', '64', '12');
INSERT INTO `blog_article_tags` VALUES ('100', '65', '1');
INSERT INTO `blog_article_tags` VALUES ('99', '65', '13');
INSERT INTO `blog_article_tags` VALUES ('102', '66', '1');
INSERT INTO `blog_article_tags` VALUES ('101', '66', '14');
INSERT INTO `blog_article_tags` VALUES ('104', '67', '1');
INSERT INTO `blog_article_tags` VALUES ('103', '67', '15');
INSERT INTO `blog_article_tags` VALUES ('106', '68', '1');
INSERT INTO `blog_article_tags` VALUES ('105', '68', '16');
INSERT INTO `blog_article_tags` VALUES ('108', '69', '1');
INSERT INTO `blog_article_tags` VALUES ('107', '69', '17');
INSERT INTO `blog_article_tags` VALUES ('110', '70', '1');
INSERT INTO `blog_article_tags` VALUES ('109', '70', '18');
INSERT INTO `blog_article_tags` VALUES ('112', '71', '1');
INSERT INTO `blog_article_tags` VALUES ('111', '71', '19');
INSERT INTO `blog_article_tags` VALUES ('114', '72', '1');
INSERT INTO `blog_article_tags` VALUES ('113', '72', '20');
INSERT INTO `blog_article_tags` VALUES ('116', '73', '1');
INSERT INTO `blog_article_tags` VALUES ('115', '73', '21');
INSERT INTO `blog_article_tags` VALUES ('117', '75', '1');
INSERT INTO `blog_article_tags` VALUES ('119', '76', '1');
INSERT INTO `blog_article_tags` VALUES ('118', '76', '3');
INSERT INTO `blog_article_tags` VALUES ('121', '77', '1');
INSERT INTO `blog_article_tags` VALUES ('120', '77', '4');
INSERT INTO `blog_article_tags` VALUES ('123', '78', '1');
INSERT INTO `blog_article_tags` VALUES ('122', '78', '5');
INSERT INTO `blog_article_tags` VALUES ('125', '79', '1');
INSERT INTO `blog_article_tags` VALUES ('124', '79', '6');
INSERT INTO `blog_article_tags` VALUES ('127', '80', '1');
INSERT INTO `blog_article_tags` VALUES ('126', '80', '7');
INSERT INTO `blog_article_tags` VALUES ('129', '81', '1');
INSERT INTO `blog_article_tags` VALUES ('128', '81', '8');
INSERT INTO `blog_article_tags` VALUES ('131', '82', '1');
INSERT INTO `blog_article_tags` VALUES ('130', '82', '9');
INSERT INTO `blog_article_tags` VALUES ('133', '83', '1');
INSERT INTO `blog_article_tags` VALUES ('132', '83', '10');
INSERT INTO `blog_article_tags` VALUES ('135', '84', '1');
INSERT INTO `blog_article_tags` VALUES ('134', '84', '11');
INSERT INTO `blog_article_tags` VALUES ('137', '85', '1');
INSERT INTO `blog_article_tags` VALUES ('136', '85', '12');
INSERT INTO `blog_article_tags` VALUES ('139', '86', '1');
INSERT INTO `blog_article_tags` VALUES ('138', '86', '13');
INSERT INTO `blog_article_tags` VALUES ('141', '87', '1');
INSERT INTO `blog_article_tags` VALUES ('140', '87', '14');
INSERT INTO `blog_article_tags` VALUES ('143', '88', '1');
INSERT INTO `blog_article_tags` VALUES ('142', '88', '15');
INSERT INTO `blog_article_tags` VALUES ('145', '89', '1');
INSERT INTO `blog_article_tags` VALUES ('144', '89', '16');
INSERT INTO `blog_article_tags` VALUES ('147', '90', '1');
INSERT INTO `blog_article_tags` VALUES ('146', '90', '17');
INSERT INTO `blog_article_tags` VALUES ('149', '91', '1');
INSERT INTO `blog_article_tags` VALUES ('148', '91', '18');
INSERT INTO `blog_article_tags` VALUES ('151', '92', '1');
INSERT INTO `blog_article_tags` VALUES ('150', '92', '19');
INSERT INTO `blog_article_tags` VALUES ('153', '93', '1');
INSERT INTO `blog_article_tags` VALUES ('152', '93', '20');
INSERT INTO `blog_article_tags` VALUES ('155', '94', '1');
INSERT INTO `blog_article_tags` VALUES ('154', '94', '21');
INSERT INTO `blog_article_tags` VALUES ('156', '95', '1');

-- ----------------------------
-- Table structure for blog_category
-- ----------------------------
DROP TABLE IF EXISTS `blog_category`;
CREATE TABLE `blog_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `name` varchar(30) NOT NULL,
  `slug` varchar(50) NOT NULL,
  `parent_category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `blog_category_parent_category_id_f50c3c0c_fk_blog_category_id` (`parent_category_id`),
  KEY `blog_category_slug_92643dc5` (`slug`),
  CONSTRAINT `blog_category_parent_category_id_f50c3c0c_fk_blog_category_id` FOREIGN KEY (`parent_category_id`) REFERENCES `blog_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_category
-- ----------------------------
INSERT INTO `blog_category` VALUES ('1', '2019-02-21 22:06:58.170830', '2019-02-21 22:06:58.173822', '分类一', 'fen-lei-yi', null);
INSERT INTO `blog_category` VALUES ('2', '2019-02-22 14:37:49.754989', '2019-02-22 14:37:49.759490', '分类二', 'fen-lei-er', null);
INSERT INTO `blog_category` VALUES ('3', '2019-02-25 22:04:10.745642', '2019-02-25 22:04:10.752641', '一级分类', 'yi-ji-fen-lei', null);
INSERT INTO `blog_category` VALUES ('4', '2019-02-25 22:04:10.855579', '2019-02-25 22:04:10.929169', '子分类', 'zi-fen-lei', '3');
INSERT INTO `blog_category` VALUES ('5', '2019-02-26 10:31:15.728996', '2019-02-26 10:31:15.732001', 'python学', 'pythonxue-xi', null);
INSERT INTO `blog_category` VALUES ('6', '2019-02-26 10:31:15.779875', '2019-02-26 10:31:15.779875', 'django学习', 'djangoxue-xi', '5');

-- ----------------------------
-- Table structure for blog_comment
-- ----------------------------
DROP TABLE IF EXISTS `blog_comment`;
CREATE TABLE `blog_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `is_enable` tinyint(1) NOT NULL,
  `article_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL,
  `parent_comment_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_comment_article_id_3d58bca6_fk_blog_article_id` (`article_id`),
  KEY `blog_comment_author_id_4f11e2e0_fk_user_userprofile_id` (`author_id`),
  KEY `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_id` (`parent_comment_id`),
  CONSTRAINT `blog_comment_article_id_3d58bca6_fk_blog_article_id` FOREIGN KEY (`article_id`) REFERENCES `blog_article` (`id`),
  CONSTRAINT `blog_comment_author_id_4f11e2e0_fk_user_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `user_userprofile` (`id`),
  CONSTRAINT `blog_comment_parent_comment_id_26791b9a_fk_blog_comment_id` FOREIGN KEY (`parent_comment_id`) REFERENCES `blog_comment` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_comment
-- ----------------------------
INSERT INTO `blog_comment` VALUES ('3', '2019-02-24 22:40:24.374181', '2019-02-24 22:40:24.384201', '牛逼呀小伙子', '1', '14', '1', null);

-- ----------------------------
-- Table structure for blog_link
-- ----------------------------
DROP TABLE IF EXISTS `blog_link`;
CREATE TABLE `blog_link` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `name` varchar(30) NOT NULL,
  `order` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `is_enable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_link
-- ----------------------------

-- ----------------------------
-- Table structure for blog_setting
-- ----------------------------
DROP TABLE IF EXISTS `blog_setting`;
CREATE TABLE `blog_setting` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `desc` longtext NOT NULL,
  `keyword` longtext NOT NULL,
  `article_desc_len` int(11) NOT NULL,
  `sidebar_article_count` int(11) NOT NULL,
  `github_user` varchar(50) NOT NULL,
  `github_repository` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_setting
-- ----------------------------
INSERT INTO `blog_setting` VALUES ('1', 'BinBlog', '彬彬博客', 'python3, django2, blog, binblog', '250', '5', 'enjoy-binbin', 'binblog-Django');

-- ----------------------------
-- Table structure for blog_sidebar
-- ----------------------------
DROP TABLE IF EXISTS `blog_sidebar`;
CREATE TABLE `blog_sidebar` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `title` varchar(30) NOT NULL,
  `content` longtext NOT NULL,
  `order` int(11) NOT NULL,
  `is_enable` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_sidebar
-- ----------------------------

-- ----------------------------
-- Table structure for blog_tag
-- ----------------------------
DROP TABLE IF EXISTS `blog_tag`;
CREATE TABLE `blog_tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `name` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_tag
-- ----------------------------
INSERT INTO `blog_tag` VALUES ('1', '2019-02-25 19:01:48.316697', '2019-02-25 19:01:48.328197', 'django');
INSERT INTO `blog_tag` VALUES ('2', '2019-02-25 22:04:11.052827', '2019-02-25 22:04:11.052827', '标签');
INSERT INTO `blog_tag` VALUES ('3', '2019-02-25 22:04:12.062397', '2019-02-25 22:20:12.204367', '标签1');
INSERT INTO `blog_tag` VALUES ('4', '2019-02-25 22:04:12.612658', '2019-02-25 22:20:13.347407', '标签2');
INSERT INTO `blog_tag` VALUES ('5', '2019-02-25 22:04:13.001815', '2019-02-25 22:20:13.581744', '标签3');
INSERT INTO `blog_tag` VALUES ('6', '2019-02-25 22:04:13.237049', '2019-02-25 22:20:14.007369', '标签4');
INSERT INTO `blog_tag` VALUES ('7', '2019-02-25 22:04:13.479184', '2019-02-25 22:20:14.249185', '标签5');
INSERT INTO `blog_tag` VALUES ('8', '2019-02-25 22:04:13.870398', '2019-02-25 22:20:14.582875', '标签6');
INSERT INTO `blog_tag` VALUES ('9', '2019-02-25 22:04:14.193882', '2019-02-25 22:20:14.959049', '标签7');
INSERT INTO `blog_tag` VALUES ('10', '2019-02-25 22:04:14.573131', '2019-02-25 22:20:15.507527', '标签8');
INSERT INTO `blog_tag` VALUES ('11', '2019-02-25 22:04:14.898764', '2019-02-25 22:20:15.880747', '标签9');
INSERT INTO `blog_tag` VALUES ('12', '2019-02-25 22:04:15.150143', '2019-02-25 22:20:16.147868', '标签10');
INSERT INTO `blog_tag` VALUES ('13', '2019-02-25 22:04:15.518677', '2019-02-25 22:20:16.413733', '标签11');
INSERT INTO `blog_tag` VALUES ('14', '2019-02-25 22:04:15.852654', '2019-02-25 22:20:16.782612', '标签12');
INSERT INTO `blog_tag` VALUES ('15', '2019-02-25 22:04:16.287633', '2019-02-25 22:20:17.032355', '标签13');
INSERT INTO `blog_tag` VALUES ('16', '2019-02-25 22:04:16.537964', '2019-02-25 22:20:17.522574', '标签14');
INSERT INTO `blog_tag` VALUES ('17', '2019-02-25 22:04:16.787947', '2019-02-25 22:20:17.807484', '标签15');
INSERT INTO `blog_tag` VALUES ('18', '2019-02-25 22:04:17.187858', '2019-02-25 22:20:18.047629', '标签16');
INSERT INTO `blog_tag` VALUES ('19', '2019-02-25 22:04:17.522094', '2019-02-25 22:20:18.402130', '标签17');
INSERT INTO `blog_tag` VALUES ('20', '2019-02-25 22:04:17.869295', '2019-02-25 22:20:18.644321', '标签18');
INSERT INTO `blog_tag` VALUES ('21', '2019-02-25 22:04:18.094166', '2019-02-25 22:20:19.014508', '标签19');

-- ----------------------------
-- Table structure for django_admin_log
-- ----------------------------
DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `user_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-02-21 22:06:58.174823', '1', '分类一', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-02-21 22:08:32.463530', '1', '全文搜索', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('3', '2019-02-22 12:46:03.487558', '2', '压缩静态资源', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('4', '2019-02-22 14:19:24.995577', '3', '111111111', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('5', '2019-02-22 14:26:31.609799', '4', '11111', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('6', '2019-02-22 14:26:41.549733', '5', '11112', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('7', '2019-02-22 14:37:49.760491', '2', '分类二', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('8', '2019-02-22 14:37:57.503152', '6', '`111111111111', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('9', '2019-02-22 14:43:09.565075', '6', '`111111111111', '2', '[{\"changed\": {\"fields\": [\"content\"]}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('10', '2019-02-22 14:43:23.901613', '7', '4141', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('11', '2019-02-22 14:44:06.478218', '6', '`111111111111', '2', '[]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('12', '2019-02-22 14:44:26.426471', '8', '13123', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('13', '2019-02-22 14:44:34.369846', '9', '1111111', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('14', '2019-02-22 14:44:55.902071', '10', '88', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('15', '2019-02-22 14:45:03.522779', '11', '999', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('16', '2019-02-22 14:45:17.377325', '12', '10', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('17', '2019-02-22 14:45:28.195129', '13', '11', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('18', '2019-02-24 22:18:47.047792', '12', '10', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('19', '2019-02-24 22:18:47.141107', '11', '999', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('20', '2019-02-24 22:18:47.180751', '10', '88', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('21', '2019-02-24 22:18:47.230279', '9', '1111111', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('22', '2019-02-24 22:18:47.313267', '8', '13123', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('23', '2019-02-24 22:18:47.396562', '7', '4141', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('24', '2019-02-24 22:18:47.447265', '6', '`111111111111', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('25', '2019-02-24 22:18:47.488770', '5', '11112', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('26', '2019-02-24 22:18:47.530271', '4', '11111', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('27', '2019-02-24 22:18:55.444475', '3', '111111111', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('28', '2019-02-24 22:18:55.497074', '2', '压缩静态资源', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('29', '2019-02-24 22:18:55.539089', '1', '全文搜索', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('30', '2019-02-24 22:37:23.182744', '13', '`21`', '3', '', '6', '1');
INSERT INTO `django_admin_log` VALUES ('31', '2019-02-24 22:39:38.944548', '14', 'Django里的Sitemap', '1', '[{\"added\": {}}]', '6', '1');
INSERT INTO `django_admin_log` VALUES ('32', '2019-02-25 19:01:48.428707', '1', 'django', '1', '[{\"added\": {}}]', '12', '1');
INSERT INTO `django_admin_log` VALUES ('33', '2019-02-25 19:02:12.410660', '14', 'Django里的Sitemap', '2', '[{\"changed\": {\"fields\": [\"tags\"]}}]', '6', '1');

-- ----------------------------
-- Table structure for django_content_type
-- ----------------------------
DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('6', 'blog', 'article');
INSERT INTO `django_content_type` VALUES ('7', 'blog', 'category');
INSERT INTO `django_content_type` VALUES ('8', 'blog', 'comment');
INSERT INTO `django_content_type` VALUES ('9', 'blog', 'link');
INSERT INTO `django_content_type` VALUES ('10', 'blog', 'setting');
INSERT INTO `django_content_type` VALUES ('11', 'blog', 'sidebar');
INSERT INTO `django_content_type` VALUES ('12', 'blog', 'tag');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('14', 'sites', 'site');
INSERT INTO `django_content_type` VALUES ('13', 'user', 'userprofile');

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-02-21 22:05:08.440501');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-02-21 22:05:09.665229');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-02-21 22:05:13.765832');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-02-21 22:05:14.556361');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-02-21 22:05:14.602054');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-02-21 22:05:14.644099');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-02-21 22:05:14.686086');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-02-21 22:05:14.723250');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-02-21 22:05:14.812783');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-02-21 22:05:14.895977');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2019-02-21 22:05:14.944269');
INSERT INTO `django_migrations` VALUES ('12', 'user', '0001_initial', '2019-02-21 22:05:20.033062');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0001_initial', '2019-02-21 22:05:21.799127');
INSERT INTO `django_migrations` VALUES ('14', 'admin', '0002_logentry_remove_auto_add', '2019-02-21 22:05:21.838088');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0003_logentry_add_action_flag_choices', '2019-02-21 22:05:21.879940');
INSERT INTO `django_migrations` VALUES ('16', 'blog', '0001_initial', '2019-02-21 22:05:31.743203');
INSERT INTO `django_migrations` VALUES ('17', 'sessions', '0001_initial', '2019-02-21 22:05:32.559362');
INSERT INTO `django_migrations` VALUES ('18', 'sites', '0001_initial', '2019-02-23 17:08:51.508578');

-- ----------------------------
-- Table structure for django_session
-- ----------------------------
DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_session
-- ----------------------------
INSERT INTO `django_session` VALUES ('46tcsmj9jbajapo4oq1ektbacensiwg9', 'ZTRmMTVmNzNmYjJlYzBiYjEyYTM3NjY2ZTNkYzg5ZDQxZGM0MjVmZjp7Il9hdXRoX3VzZXJfaWQiOiI3IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiOWUyNDE0ZDQ4YjYzODM1ZTY1ZjU4ZDRlNzlkODc1MzBiZTZmMjA2ZSJ9', '2019-03-09 10:50:35.879249');
INSERT INTO `django_session` VALUES ('4a8oxqd1a3of1hnkemae5w28ktek7tx8', 'ZmFlODRlOGJmYWRiNDNjYTg5NjhiYWM3OGJjNzY5YzI1NTVjZGZkNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDVlZTAxMzFkNTNlOWU4YjZmNTFlMWE2MTI1ZDMxMmUyYTlmYmRmOSJ9', '2019-03-11 18:43:40.426579');
INSERT INTO `django_session` VALUES ('s0nk2brtjhtkndugdrawgdftvuoiwoq1', 'ZmFlODRlOGJmYWRiNDNjYTg5NjhiYWM3OGJjNzY5YzI1NTVjZGZkNDp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNDVlZTAxMzFkNTNlOWU4YjZmNTFlMWE2MTI1ZDMxMmUyYTlmYmRmOSJ9', '2019-03-09 17:26:11.768575');

-- ----------------------------
-- Table structure for django_site
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_site
-- ----------------------------
INSERT INTO `django_site` VALUES ('1', 'localhost:8000', 'localhost:8000');

-- ----------------------------
-- Table structure for user_userprofile
-- ----------------------------
DROP TABLE IF EXISTS `user_userprofile`;
CREATE TABLE `user_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `nickname` varchar(30) NOT NULL,
  `gender` varchar(6) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_userprofile
-- ----------------------------
INSERT INTO `user_userprofile` VALUES ('1', 'pbkdf2_sha256$120000$eco4Txv29Emu$FYyFvBvgTBQmBhrzcb84YRFTaLpADZzA/Jy0ox1sNyQ=', '2019-02-25 18:43:40.342820', '1', 'bin', '', '', 'bin@qq.com', '1', '1', '2019-02-21 22:06:01.368395', '222', 'male', '2019-02-21 22:06:01.368395', '2019-02-21 22:06:01.368395');
INSERT INTO `user_userprofile` VALUES ('7', 'pbkdf2_sha256$120000$7jvFV6MQo731$0ZWAGNDpEYTfOv6zeTGGVBuH18CMH5Fg2MMse63949U=', '2019-02-23 10:50:35.791087', '0', 'admin12345', '', '', 'binloveplay1314@qq.com', '0', '1', '2019-02-23 10:50:30.182892', '', 'male', '2019-02-23 10:50:30.182892', '2019-02-23 10:50:30.182892');
INSERT INTO `user_userprofile` VALUES ('8', 'pbkdf2_sha256$120000$ZKDGU95iMuC9$OVK2ad7SX7PRQfSukHOce5QXiIHVmK217L/0de1ZMHg=', '2019-02-25 18:41:30.608265', '0', 'aaa', '', '', '1111@123456qq.com', '0', '1', '2019-02-25 18:41:25.336668', '', 'male', '2019-02-25 18:41:25.337169', '2019-02-25 18:41:25.337169');
INSERT INTO `user_userprofile` VALUES ('9', 'abc123456.0', null, '0', '测试用户', '', '', 'test@qq.com', '0', '1', '2019-02-25 22:04:10.637114', '', 'male', '2019-02-25 22:04:10.637114', '2019-02-25 22:04:10.637114');
INSERT INTO `user_userprofile` VALUES ('10', 'abc123456.0', null, '0', 'testuser', '', '', 'test@qq.com', '0', '1', '2019-02-25 22:18:52.149637', '', 'male', '2019-02-25 22:18:52.149637', '2019-02-25 22:18:52.149637');
INSERT INTO `user_userprofile` VALUES ('11', 'abc123456.0', null, '1', 'testadmin', '', '', 'test@qq.com', '1', '1', '2019-02-26 10:31:15.624781', '', 'male', '2019-02-26 10:31:15.625282', '2019-02-26 10:31:15.625282');

-- ----------------------------
-- Table structure for user_userprofile_groups
-- ----------------------------
DROP TABLE IF EXISTS `user_userprofile_groups`;
CREATE TABLE `user_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_userprofile_groups_userprofile_id_group_id_52847a61_uniq` (`userprofile_id`,`group_id`),
  KEY `user_userprofile_groups_group_id_98cc4038_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_userprofile_gro_userprofile_id_49724c40_fk_user_user` FOREIGN KEY (`userprofile_id`) REFERENCES `user_userprofile` (`id`),
  CONSTRAINT `user_userprofile_groups_group_id_98cc4038_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_userprofile_groups
-- ----------------------------

-- ----------------------------
-- Table structure for user_userprofile_user_permissions
-- ----------------------------
DROP TABLE IF EXISTS `user_userprofile_user_permissions`;
CREATE TABLE `user_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_userprofile_user_pe_userprofile_id_permissio_2e86ceca_uniq` (`userprofile_id`,`permission_id`),
  KEY `user_userprofile_use_permission_id_7f559b23_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_userprofile_use_permission_id_7f559b23_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_userprofile_use_userprofile_id_68dc814c_fk_user_user` FOREIGN KEY (`userprofile_id`) REFERENCES `user_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_userprofile_user_permissions
-- ----------------------------
