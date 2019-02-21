/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50636
Source Host           : 127.0.0.1:3306
Source Database       : binblog

Target Server Type    : MYSQL
Target Server Version : 50636
File Encoding         : 65001

Date: 2019-02-21 22:58:24
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
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article
-- ----------------------------
INSERT INTO `blog_article` VALUES ('1', '2019-02-21 22:08:30.870515', '2019-02-21 22:08:30.876027', '全文搜索', '### 使用django-haystack进行搜索\r\n\r\n```python\r\npip install django-haystack==2.8.1\r\n```\r\n\r\n### github地址: Modular search for Django\r\n\r\n​	https://github.com/django-haystack/django-haystack\r\n\r\n​	https://django-haystack.readthedocs.io/en/v2.4.1/tutorial.html\r\n\r\n\r\n\r\n### 安装搜索引擎\r\n\r\n文档:https://django-haystack.readthedocs.io/en/v2.4.1/installing_search_engines.html\r\n\r\n这里选择 Whoosh，Tolearn: Elasticsearch\r\n\r\npip install whoosh==2.7.4\r\n\r\n\r\n\r\n### 这里注意 :\r\n\r\nhaystack只对在安装完毕后，重新添加的有效，之前创建的数据是没有建立索引无法搜索出来的(测试了好久/捂脸)\r\n\r\n\r\n\r\n### 添加jieba作为中文分词\r\n\r\npip install jieba==0.39\r\n\r\n复制一份 haystack.backends.whoosh_backend.py出来到utils目录下 `个人设置`\r\n\r\n```python\r\n# 修改其源代码\r\nfrom jieba.analyse import ChineseAnalyzer\r\n......\r\n......\r\n# 找到build_schema这个函数的\r\nschema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=StemmingAnalyzer()\r\n# 将StemmingAnalyzer替换为jieba的ChineseAnalyzer\r\nschema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer()\r\n```\r\n\r\n\r\n\r\n添加 haystack 到 `INSTALLED_APPS`\r\n\r\nsettings里设置引擎:\r\n\r\n```\r\nHAYSTACK_CONNECTIONS = {\r\n    \'default\': {\r\n        \'ENGINE\': \'haystack.backends.whoosh_backend.WhooshEngine\',\r\n        \'ENGINE\': \'haystack.backends.whoosh_backend.WhooshEngine\',\r\n        \'PATH\': os.path.join(os.path.dirname(__file__), \'whoosh_index\'),\r\n    },\r\n}\r\n```\r\n\r\n\r\n\r\n在blog目录下创建 search_indexes.py\r\n\r\n```python\r\nfrom haystack import indexes\r\nfrom .models import Article\r\n\r\n\r\nclass ArticleIndex(indexes.SearchIndex, indexes.Indexable):\r\n    text = indexes.CharField(document=True, use_template=True)\r\n\r\n    def get_model(self):\r\n        return Article\r\n```\r\n\r\n\r\n\r\n模板文件:\r\n\r\n`search/indexes/myapp/aitilce_text.txt`\r\n\r\n```\r\n{{ object.title }}\r\n{{ object.author.username }}\r\n{{ object.content }}\r\n```\r\n\r\n\r\n\r\n```html\r\n{% extends \'base.html\' %}\r\n\r\n{% block content %}\r\n    <h2>Search</h2>\r\n\r\n    <form method=\"get\" action=\".\">\r\n        <table>\r\n            {{ form.as_table }}\r\n            <tr>\r\n                <td>&nbsp;</td>\r\n                <td>\r\n                    <input type=\"submit\" value=\"Search\">\r\n                </td>\r\n            </tr>\r\n        </table>\r\n\r\n        {% if query %}\r\n            <h3>Results</h3>\r\n\r\n            {% for result in page.object_list %}\r\n                <p>\r\n                    <a href=\"{{ result.object.get_absolute_url }}\">{{ result.object.title }}</a>\r\n                </p>\r\n            {% empty %}\r\n                <p>No results found.</p>\r\n            {% endfor %}\r\n\r\n            {% if page.has_previous or page.has_next %}\r\n                <div>\r\n                    {% if page.has_previous %}<a href=\"?q={{ query }}&amp;page={{ page.previous_page_number }}\">{% endif %}&laquo; Previous{% if page.has_previous %}</a>{% endif %}\r\n                    |\r\n                    {% if page.has_next %}<a href=\"?q={{ query }}&amp;page={{ page.next_page_number }}\">{% endif %}Next &raquo;{% if page.has_next %}</a>{% endif %}\r\n                </div>\r\n            {% endif %}\r\n        {% else %}\r\n            {# Show some example queries to run, maybe query syntax, something else? #}\r\n        {% endif %}\r\n    </form>\r\n{% endblock %}\r\n```\r\n\r\n\r\n\r\n\r\n\r\nurl设置', '0', '0', null, '1', '1');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article_tags
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_category
-- ----------------------------
INSERT INTO `blog_category` VALUES ('1', '2019-02-21 22:06:58.170830', '2019-02-21 22:06:58.173822', '分类一', 'fen-lei-yi', null);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_comment
-- ----------------------------

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_tag
-- ----------------------------

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-02-21 22:06:58.174823', '1', '分类一', '1', '[{\"added\": {}}]', '7', '1');
INSERT INTO `django_admin_log` VALUES ('2', '2019-02-21 22:08:32.463530', '1', '全文搜索', '1', '[{\"added\": {}}]', '6', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_userprofile
-- ----------------------------
INSERT INTO `user_userprofile` VALUES ('1', 'pbkdf2_sha256$120000$eco4Txv29Emu$FYyFvBvgTBQmBhrzcb84YRFTaLpADZzA/Jy0ox1sNyQ=', '2019-02-21 22:06:06.909580', '1', 'bin', '', '', 'bin@qq.com', '1', '1', '2019-02-21 22:06:01.368395', '', 'male', '2019-02-21 22:06:01.368395', '2019-02-21 22:06:01.368395');

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
