/*
Navicat MySQL Data Transfer

Source Server         : 127.0.0.1
Source Server Version : 50644
Source Host           : localhost:3306
Source Database       : binblog

Target Server Type    : MYSQL
Target Server Version : 50644
File Encoding         : 65001

Date: 2019-05-31 14:25:34
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
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8;

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
INSERT INTO `auth_permission` VALUES ('21', 'Can add site', '6', 'add_site');
INSERT INTO `auth_permission` VALUES ('22', 'Can change site', '6', 'change_site');
INSERT INTO `auth_permission` VALUES ('23', 'Can delete site', '6', 'delete_site');
INSERT INTO `auth_permission` VALUES ('24', 'Can view site', '6', 'view_site');
INSERT INTO `auth_permission` VALUES ('25', 'Can add 2-文章', '7', 'add_article');
INSERT INTO `auth_permission` VALUES ('26', 'Can change 2-文章', '7', 'change_article');
INSERT INTO `auth_permission` VALUES ('27', 'Can delete 2-文章', '7', 'delete_article');
INSERT INTO `auth_permission` VALUES ('28', 'Can view 2-文章', '7', 'view_article');
INSERT INTO `auth_permission` VALUES ('29', 'Can add 1-文章分类', '8', 'add_category');
INSERT INTO `auth_permission` VALUES ('30', 'Can change 1-文章分类', '8', 'change_category');
INSERT INTO `auth_permission` VALUES ('31', 'Can delete 1-文章分类', '8', 'delete_category');
INSERT INTO `auth_permission` VALUES ('32', 'Can view 1-文章分类', '8', 'view_category');
INSERT INTO `auth_permission` VALUES ('33', 'Can add 3-文章评论', '9', 'add_comment');
INSERT INTO `auth_permission` VALUES ('34', 'Can change 3-文章评论', '9', 'change_comment');
INSERT INTO `auth_permission` VALUES ('35', 'Can delete 3-文章评论', '9', 'delete_comment');
INSERT INTO `auth_permission` VALUES ('36', 'Can view 3-文章评论', '9', 'view_comment');
INSERT INTO `auth_permission` VALUES ('37', 'Can add 8-友情链接', '10', 'add_link');
INSERT INTO `auth_permission` VALUES ('38', 'Can change 8-友情链接', '10', 'change_link');
INSERT INTO `auth_permission` VALUES ('39', 'Can delete 8-友情链接', '10', 'delete_link');
INSERT INTO `auth_permission` VALUES ('40', 'Can view 8-友情链接', '10', 'view_link');
INSERT INTO `auth_permission` VALUES ('41', 'Can add 0-站点配置', '11', 'add_setting');
INSERT INTO `auth_permission` VALUES ('42', 'Can change 0-站点配置', '11', 'change_setting');
INSERT INTO `auth_permission` VALUES ('43', 'Can delete 0-站点配置', '11', 'delete_setting');
INSERT INTO `auth_permission` VALUES ('44', 'Can view 0-站点配置', '11', 'view_setting');
INSERT INTO `auth_permission` VALUES ('45', 'Can add 5-侧边栏', '12', 'add_sidebar');
INSERT INTO `auth_permission` VALUES ('46', 'Can change 5-侧边栏', '12', 'change_sidebar');
INSERT INTO `auth_permission` VALUES ('47', 'Can delete 5-侧边栏', '12', 'delete_sidebar');
INSERT INTO `auth_permission` VALUES ('48', 'Can view 5-侧边栏', '12', 'view_sidebar');
INSERT INTO `auth_permission` VALUES ('49', 'Can add 4-文章标签', '13', 'add_tag');
INSERT INTO `auth_permission` VALUES ('50', 'Can change 4-文章标签', '13', 'change_tag');
INSERT INTO `auth_permission` VALUES ('51', 'Can delete 4-文章标签', '13', 'delete_tag');
INSERT INTO `auth_permission` VALUES ('52', 'Can view 4-文章标签', '13', 'view_tag');
INSERT INTO `auth_permission` VALUES ('53', 'Can add 6-相册图片', '14', 'add_photo');
INSERT INTO `auth_permission` VALUES ('54', 'Can change 6-相册图片', '14', 'change_photo');
INSERT INTO `auth_permission` VALUES ('55', 'Can delete 6-相册图片', '14', 'delete_photo');
INSERT INTO `auth_permission` VALUES ('56', 'Can view 6-相册图片', '14', 'view_photo');
INSERT INTO `auth_permission` VALUES ('57', 'Can add 7-留言板', '15', 'add_guestbook');
INSERT INTO `auth_permission` VALUES ('58', 'Can change 7-留言板', '15', 'change_guestbook');
INSERT INTO `auth_permission` VALUES ('59', 'Can delete 7-留言板', '15', 'delete_guestbook');
INSERT INTO `auth_permission` VALUES ('60', 'Can view 7-留言板', '15', 'view_guestbook');
INSERT INTO `auth_permission` VALUES ('61', 'Can add 0-用户', '16', 'add_userprofile');
INSERT INTO `auth_permission` VALUES ('62', 'Can change 0-用户', '16', 'change_userprofile');
INSERT INTO `auth_permission` VALUES ('63', 'Can delete 0-用户', '16', 'delete_userprofile');
INSERT INTO `auth_permission` VALUES ('64', 'Can view 0-用户', '16', 'view_userprofile');
INSERT INTO `auth_permission` VALUES ('65', 'Can add 1-邮箱验证码', '17', 'add_emailverifycode');
INSERT INTO `auth_permission` VALUES ('66', 'Can change 1-邮箱验证码', '17', 'change_emailverifycode');
INSERT INTO `auth_permission` VALUES ('67', 'Can delete 1-邮箱验证码', '17', 'delete_emailverifycode');
INSERT INTO `auth_permission` VALUES ('68', 'Can view 1-邮箱验证码', '17', 'view_emailverifycode');
INSERT INTO `auth_permission` VALUES ('69', 'Can add 0-OAuth配置', '18', 'add_oauthconfig');
INSERT INTO `auth_permission` VALUES ('70', 'Can change 0-OAuth配置', '18', 'change_oauthconfig');
INSERT INTO `auth_permission` VALUES ('71', 'Can delete 0-OAuth配置', '18', 'delete_oauthconfig');
INSERT INTO `auth_permission` VALUES ('72', 'Can view 0-OAuth配置', '18', 'view_oauthconfig');
INSERT INTO `auth_permission` VALUES ('73', 'Can add 1-Oauth用户', '19', 'add_oauthuser');
INSERT INTO `auth_permission` VALUES ('74', 'Can change 1-Oauth用户', '19', 'change_oauthuser');
INSERT INTO `auth_permission` VALUES ('75', 'Can delete 1-Oauth用户', '19', 'delete_oauthuser');
INSERT INTO `auth_permission` VALUES ('76', 'Can view 1-Oauth用户', '19', 'view_oauthuser');

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
  `author_id` int(11) NOT NULL,
  `category_id` int(11) NOT NULL,
  `type` varchar(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  KEY `blog_article_author_id_905add38_fk_user_userprofile_id` (`author_id`),
  KEY `blog_article_category_id_7e38f15e_fk_blog_category_id` (`category_id`),
  CONSTRAINT `blog_article_author_id_905add38_fk_user_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `user_userprofile` (`id`),
  CONSTRAINT `blog_article_category_id_7e38f15e_fk_blog_category_id` FOREIGN KEY (`category_id`) REFERENCES `blog_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article
-- ----------------------------
INSERT INTO `blog_article` VALUES ('1', '2019-05-31 14:24:07.528600', '2019-05-31 14:24:08.291600', '我是测试标题 1', '我是测试内容 1', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('2', '2019-05-31 14:24:08.308600', '2019-05-31 14:24:08.338600', '我是测试标题 2', '我是测试内容 2', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('3', '2019-05-31 14:24:08.357600', '2019-05-31 14:24:08.593600', '我是测试标题 3', '我是测试内容 3', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('4', '2019-05-31 14:24:08.611600', '2019-05-31 14:24:08.647600', '我是测试标题 4', '我是测试内容 4', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('5', '2019-05-31 14:24:08.667600', '2019-05-31 14:24:08.701600', '我是测试标题 5', '我是测试内容 5', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('6', '2019-05-31 14:24:08.925600', '2019-05-31 14:24:08.982600', '我是测试标题 6', '我是测试内容 6', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('7', '2019-05-31 14:24:09.001600', '2019-05-31 14:24:09.032600', '我是测试标题 7', '我是测试内容 7', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('8', '2019-05-31 14:24:09.051600', '2019-05-31 14:24:09.288600', '我是测试标题 8', '我是测试内容 8', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('9', '2019-05-31 14:24:09.305600', '2019-05-31 14:24:09.336600', '我是测试标题 9', '我是测试内容 9', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('10', '2019-05-31 14:24:09.355600', '2019-05-31 14:24:09.388600', '我是测试标题 10', '我是测试内容 10', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('11', '2019-05-31 14:24:09.612600', '2019-05-31 14:24:09.641600', '我是测试标题 11', '我是测试内容 11', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('12', '2019-05-31 14:24:09.660600', '2019-05-31 14:24:09.693600', '我是测试标题 12', '我是测试内容 12', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('13', '2019-05-31 14:24:09.714600', '2019-05-31 14:24:09.964600', '我是测试标题 13', '我是测试内容 13', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('14', '2019-05-31 14:24:09.982600', '2019-05-31 14:24:10.011600', '我是测试标题 14', '我是测试内容 14', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('15', '2019-05-31 14:24:10.030600', '2019-05-31 14:24:10.061600', '我是测试标题 15', '我是测试内容 15', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('16', '2019-05-31 14:24:10.285600', '2019-05-31 14:24:10.312600', '我是测试标题 16', '我是测试内容 16', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('17', '2019-05-31 14:24:10.330600', '2019-05-31 14:24:10.362600', '我是测试标题 17', '我是测试内容 17', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('18', '2019-05-31 14:24:10.382600', '2019-05-31 14:24:10.619600', '我是测试标题 18', '我是测试内容 18', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('19', '2019-05-31 14:24:10.635600', '2019-05-31 14:24:10.667600', '我是测试标题 19', '我是测试内容 19', '0', '0', '1', '2', 'a');
INSERT INTO `blog_article` VALUES ('20', '2019-05-31 14:24:10.687600', '2019-05-31 14:24:10.712600', '彬彬博客', '\n### 支持Markdown\n\n```python\nprint(\'支持语法高亮\')\n```\n            ', '0', '0', '1', '2', 'a');

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
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_article_tags
-- ----------------------------
INSERT INTO `blog_article_tags` VALUES ('2', '1', '1');
INSERT INTO `blog_article_tags` VALUES ('1', '1', '2');
INSERT INTO `blog_article_tags` VALUES ('4', '2', '1');
INSERT INTO `blog_article_tags` VALUES ('3', '2', '3');
INSERT INTO `blog_article_tags` VALUES ('6', '3', '1');
INSERT INTO `blog_article_tags` VALUES ('5', '3', '4');
INSERT INTO `blog_article_tags` VALUES ('8', '4', '1');
INSERT INTO `blog_article_tags` VALUES ('7', '4', '5');
INSERT INTO `blog_article_tags` VALUES ('10', '5', '1');
INSERT INTO `blog_article_tags` VALUES ('9', '5', '6');
INSERT INTO `blog_article_tags` VALUES ('12', '6', '1');
INSERT INTO `blog_article_tags` VALUES ('11', '6', '7');
INSERT INTO `blog_article_tags` VALUES ('14', '7', '1');
INSERT INTO `blog_article_tags` VALUES ('13', '7', '8');
INSERT INTO `blog_article_tags` VALUES ('16', '8', '1');
INSERT INTO `blog_article_tags` VALUES ('15', '8', '9');
INSERT INTO `blog_article_tags` VALUES ('18', '9', '1');
INSERT INTO `blog_article_tags` VALUES ('17', '9', '10');
INSERT INTO `blog_article_tags` VALUES ('20', '10', '1');
INSERT INTO `blog_article_tags` VALUES ('19', '10', '11');
INSERT INTO `blog_article_tags` VALUES ('22', '11', '1');
INSERT INTO `blog_article_tags` VALUES ('21', '11', '12');
INSERT INTO `blog_article_tags` VALUES ('24', '12', '1');
INSERT INTO `blog_article_tags` VALUES ('23', '12', '13');
INSERT INTO `blog_article_tags` VALUES ('26', '13', '1');
INSERT INTO `blog_article_tags` VALUES ('25', '13', '14');
INSERT INTO `blog_article_tags` VALUES ('28', '14', '1');
INSERT INTO `blog_article_tags` VALUES ('27', '14', '15');
INSERT INTO `blog_article_tags` VALUES ('30', '15', '1');
INSERT INTO `blog_article_tags` VALUES ('29', '15', '16');
INSERT INTO `blog_article_tags` VALUES ('32', '16', '1');
INSERT INTO `blog_article_tags` VALUES ('31', '16', '17');
INSERT INTO `blog_article_tags` VALUES ('34', '17', '1');
INSERT INTO `blog_article_tags` VALUES ('33', '17', '18');
INSERT INTO `blog_article_tags` VALUES ('36', '18', '1');
INSERT INTO `blog_article_tags` VALUES ('35', '18', '19');
INSERT INTO `blog_article_tags` VALUES ('38', '19', '1');
INSERT INTO `blog_article_tags` VALUES ('37', '19', '20');
INSERT INTO `blog_article_tags` VALUES ('39', '20', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_category
-- ----------------------------
INSERT INTO `blog_category` VALUES ('1', '2019-05-31 14:24:07.506600', '2019-05-31 14:24:07.508600', 'python学习', 'pythonxue-xi', null);
INSERT INTO `blog_category` VALUES ('2', '2019-05-31 14:24:07.514600', '2019-05-31 14:24:07.514600', 'django学习', 'djangoxue-xi', '1');

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
-- Table structure for blog_guestbook
-- ----------------------------
DROP TABLE IF EXISTS `blog_guestbook`;
CREATE TABLE `blog_guestbook` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `content` longtext NOT NULL,
  `author_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blog_guestbook_author_id_a34aaf0d_fk_user_userprofile_id` (`author_id`),
  CONSTRAINT `blog_guestbook_author_id_a34aaf0d_fk_user_userprofile_id` FOREIGN KEY (`author_id`) REFERENCES `user_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_guestbook
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
-- Table structure for blog_photo
-- ----------------------------
DROP TABLE IF EXISTS `blog_photo`;
CREATE TABLE `blog_photo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `title` varchar(50) NOT NULL,
  `desc` longtext,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_photo
-- ----------------------------
INSERT INTO `blog_photo` VALUES ('1', '2019-05-31 14:24:00.000000', '2019-05-31 14:25:00.940600', '宠物狗', '', 'photo/宠物狗.宠物狗.宠物狗.jpg');

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
  `enable_photo` tinyint(1) NOT NULL,
  `user_verify_email` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_setting
-- ----------------------------
INSERT INTO `blog_setting` VALUES ('1', 'BinBlog', '彬彬博客', 'python3, django2, blog, binblog', '250', '5', 'enjoy-binbin', 'binblog-Django', '1', '0');

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
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of blog_tag
-- ----------------------------
INSERT INTO `blog_tag` VALUES ('1', '2019-05-31 14:24:07.521600', '2019-05-31 14:24:07.521600', 'Django');
INSERT INTO `blog_tag` VALUES ('2', '2019-05-31 14:24:08.278600', '2019-05-31 14:24:08.278600', '标签1');
INSERT INTO `blog_tag` VALUES ('3', '2019-05-31 14:24:08.325600', '2019-05-31 14:24:08.325600', '标签2');
INSERT INTO `blog_tag` VALUES ('4', '2019-05-31 14:24:08.581600', '2019-05-31 14:24:08.581600', '标签3');
INSERT INTO `blog_tag` VALUES ('5', '2019-05-31 14:24:08.632600', '2019-05-31 14:24:08.632600', '标签4');
INSERT INTO `blog_tag` VALUES ('6', '2019-05-31 14:24:08.687600', '2019-05-31 14:24:08.687600', '标签5');
INSERT INTO `blog_tag` VALUES ('7', '2019-05-31 14:24:08.970600', '2019-05-31 14:24:08.970600', '标签6');
INSERT INTO `blog_tag` VALUES ('8', '2019-05-31 14:24:09.021600', '2019-05-31 14:24:09.021600', '标签7');
INSERT INTO `blog_tag` VALUES ('9', '2019-05-31 14:24:09.275600', '2019-05-31 14:24:09.275600', '标签8');
INSERT INTO `blog_tag` VALUES ('10', '2019-05-31 14:24:09.323600', '2019-05-31 14:24:09.323600', '标签9');
INSERT INTO `blog_tag` VALUES ('11', '2019-05-31 14:24:09.375600', '2019-05-31 14:24:09.375600', '标签10');
INSERT INTO `blog_tag` VALUES ('12', '2019-05-31 14:24:09.629600', '2019-05-31 14:24:09.629600', '标签11');
INSERT INTO `blog_tag` VALUES ('13', '2019-05-31 14:24:09.680600', '2019-05-31 14:24:09.680600', '标签12');
INSERT INTO `blog_tag` VALUES ('14', '2019-05-31 14:24:09.953600', '2019-05-31 14:24:09.953600', '标签13');
INSERT INTO `blog_tag` VALUES ('15', '2019-05-31 14:24:09.999600', '2019-05-31 14:24:09.999600', '标签14');
INSERT INTO `blog_tag` VALUES ('16', '2019-05-31 14:24:10.049600', '2019-05-31 14:24:10.049600', '标签15');
INSERT INTO `blog_tag` VALUES ('17', '2019-05-31 14:24:10.302600', '2019-05-31 14:24:10.302600', '标签16');
INSERT INTO `blog_tag` VALUES ('18', '2019-05-31 14:24:10.348600', '2019-05-31 14:24:10.348600', '标签17');
INSERT INTO `blog_tag` VALUES ('19', '2019-05-31 14:24:10.607600', '2019-05-31 14:24:10.607600', '标签18');
INSERT INTO `blog_tag` VALUES ('20', '2019-05-31 14:24:10.653600', '2019-05-31 14:24:10.653600', '标签19');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_admin_log
-- ----------------------------
INSERT INTO `django_admin_log` VALUES ('1', '2019-05-31 14:25:00.943600', '1', '宠物狗', '1', '[{\"added\": {}}]', '14', '1');

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
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_content_type
-- ----------------------------
INSERT INTO `django_content_type` VALUES ('1', 'admin', 'logentry');
INSERT INTO `django_content_type` VALUES ('3', 'auth', 'group');
INSERT INTO `django_content_type` VALUES ('2', 'auth', 'permission');
INSERT INTO `django_content_type` VALUES ('7', 'blog', 'article');
INSERT INTO `django_content_type` VALUES ('8', 'blog', 'category');
INSERT INTO `django_content_type` VALUES ('9', 'blog', 'comment');
INSERT INTO `django_content_type` VALUES ('15', 'blog', 'guestbook');
INSERT INTO `django_content_type` VALUES ('10', 'blog', 'link');
INSERT INTO `django_content_type` VALUES ('14', 'blog', 'photo');
INSERT INTO `django_content_type` VALUES ('11', 'blog', 'setting');
INSERT INTO `django_content_type` VALUES ('12', 'blog', 'sidebar');
INSERT INTO `django_content_type` VALUES ('13', 'blog', 'tag');
INSERT INTO `django_content_type` VALUES ('4', 'contenttypes', 'contenttype');
INSERT INTO `django_content_type` VALUES ('18', 'oauth', 'oauthconfig');
INSERT INTO `django_content_type` VALUES ('19', 'oauth', 'oauthuser');
INSERT INTO `django_content_type` VALUES ('5', 'sessions', 'session');
INSERT INTO `django_content_type` VALUES ('6', 'sites', 'site');
INSERT INTO `django_content_type` VALUES ('17', 'user', 'emailverifycode');
INSERT INTO `django_content_type` VALUES ('16', 'user', 'userprofile');

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
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_migrations
-- ----------------------------
INSERT INTO `django_migrations` VALUES ('1', 'contenttypes', '0001_initial', '2019-05-31 14:23:39.382600');
INSERT INTO `django_migrations` VALUES ('2', 'contenttypes', '0002_remove_content_type_name', '2019-05-31 14:23:39.449600');
INSERT INTO `django_migrations` VALUES ('3', 'auth', '0001_initial', '2019-05-31 14:23:39.643600');
INSERT INTO `django_migrations` VALUES ('4', 'auth', '0002_alter_permission_name_max_length', '2019-05-31 14:23:39.682600');
INSERT INTO `django_migrations` VALUES ('5', 'auth', '0003_alter_user_email_max_length', '2019-05-31 14:23:39.690600');
INSERT INTO `django_migrations` VALUES ('6', 'auth', '0004_alter_user_username_opts', '2019-05-31 14:23:39.699600');
INSERT INTO `django_migrations` VALUES ('7', 'auth', '0005_alter_user_last_login_null', '2019-05-31 14:23:39.710600');
INSERT INTO `django_migrations` VALUES ('8', 'auth', '0006_require_contenttypes_0002', '2019-05-31 14:23:39.715600');
INSERT INTO `django_migrations` VALUES ('9', 'auth', '0007_alter_validators_add_error_messages', '2019-05-31 14:23:39.725600');
INSERT INTO `django_migrations` VALUES ('10', 'auth', '0008_alter_user_username_max_length', '2019-05-31 14:23:39.735600');
INSERT INTO `django_migrations` VALUES ('11', 'auth', '0009_alter_user_last_name_max_length', '2019-05-31 14:23:39.745600');
INSERT INTO `django_migrations` VALUES ('12', 'user', '0001_initial', '2019-05-31 14:23:39.999600');
INSERT INTO `django_migrations` VALUES ('13', 'admin', '0001_initial', '2019-05-31 14:23:40.105600');
INSERT INTO `django_migrations` VALUES ('14', 'admin', '0002_logentry_remove_auto_add', '2019-05-31 14:23:40.117600');
INSERT INTO `django_migrations` VALUES ('15', 'admin', '0003_logentry_add_action_flag_choices', '2019-05-31 14:23:40.131600');
INSERT INTO `django_migrations` VALUES ('16', 'blog', '0001_initial', '2019-05-31 14:23:40.794600');
INSERT INTO `django_migrations` VALUES ('17', 'blog', '0002_auto_20190310_1511', '2019-05-31 14:23:40.852600');
INSERT INTO `django_migrations` VALUES ('18', 'blog', '0003_auto_20190318_2034', '2019-05-31 14:23:40.867600');
INSERT INTO `django_migrations` VALUES ('19', 'blog', '0004_article_type', '2019-05-31 14:23:40.909600');
INSERT INTO `django_migrations` VALUES ('20', 'blog', '0005_photo', '2019-05-31 14:23:40.937600');
INSERT INTO `django_migrations` VALUES ('21', 'blog', '0006_guestbook', '2019-05-31 14:23:41.076600');
INSERT INTO `django_migrations` VALUES ('22', 'blog', '0007_auto_20190512_2311', '2019-05-31 14:23:41.196600');
INSERT INTO `django_migrations` VALUES ('23', 'blog', '0008_auto_20190512_2347', '2019-05-31 14:23:41.266600');
INSERT INTO `django_migrations` VALUES ('24', 'blog', '0009_auto_20190528_1022', '2019-05-31 14:23:41.373600');
INSERT INTO `django_migrations` VALUES ('25', 'blog', '0010_setting_user_verify_email', '2019-05-31 14:23:41.410600');
INSERT INTO `django_migrations` VALUES ('26', 'oauth', '0001_initial', '2019-05-31 14:23:41.522600');
INSERT INTO `django_migrations` VALUES ('27', 'oauth', '0002_auto_20190512_1129', '2019-05-31 14:23:41.532600');
INSERT INTO `django_migrations` VALUES ('28', 'oauth', '0003_auto_20190531_0914', '2019-05-31 14:23:41.550600');
INSERT INTO `django_migrations` VALUES ('29', 'sessions', '0001_initial', '2019-05-31 14:23:41.601600');
INSERT INTO `django_migrations` VALUES ('30', 'sites', '0001_initial', '2019-05-31 14:23:41.628600');
INSERT INTO `django_migrations` VALUES ('31', 'sites', '0002_alter_domain_unique', '2019-05-31 14:23:41.648600');
INSERT INTO `django_migrations` VALUES ('32', 'user', '0002_auto_20190530_1341', '2019-05-31 14:23:41.685600');
INSERT INTO `django_migrations` VALUES ('33', 'user', '0003_auto_20190531_0914', '2019-05-31 14:23:41.732600');

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
INSERT INTO `django_session` VALUES ('uzxxjcnamzg8t229hncta2r5z2a5row9', 'OGE0MmEwYmExMmFiMTA5ZGJmMWVmNzlmM2ViNTRhY2Y3MGU4Mjg2OTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5BbGxvd0FsbFVzZXJzTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNmY2ODhkYzMwYTkzYjMwOGNkYzYwMmEyOGM4MTBmNjZiN2EyODJjYSJ9', '2019-06-14 14:24:31.878600');

-- ----------------------------
-- Table structure for django_site
-- ----------------------------
DROP TABLE IF EXISTS `django_site`;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of django_site
-- ----------------------------
INSERT INTO `django_site` VALUES ('1', 'example.com', 'example.com');

-- ----------------------------
-- Table structure for oauth_oauthconfig
-- ----------------------------
DROP TABLE IF EXISTS `oauth_oauthconfig`;
CREATE TABLE `oauth_oauthconfig` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(10) NOT NULL,
  `app_key` varchar(200) NOT NULL,
  `app_secret` varchar(200) NOT NULL,
  `callback_url` varchar(200) NOT NULL,
  `is_enable` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oauth_oauthconfig
-- ----------------------------

-- ----------------------------
-- Table structure for oauth_oauthuser
-- ----------------------------
DROP TABLE IF EXISTS `oauth_oauthuser`;
CREATE TABLE `oauth_oauthuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) NOT NULL,
  `nickname` varchar(50) NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `avatar_url` varchar(350) DEFAULT NULL,
  `user_info` longtext,
  `openid` varchar(50) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `oauth_oauthuser_user_id_fe2a59af_fk_user_userprofile_id` (`user_id`),
  CONSTRAINT `oauth_oauthuser_user_id_fe2a59af_fk_user_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `user_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of oauth_oauthuser
-- ----------------------------

-- ----------------------------
-- Table structure for user_emailverifycode
-- ----------------------------
DROP TABLE IF EXISTS `user_emailverifycode`;
CREATE TABLE `user_emailverifycode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `email` varchar(50) NOT NULL,
  `type` varchar(20) NOT NULL,
  `is_used` tinyint(1) NOT NULL,
  `add_time` datetime(6) NOT NULL,
  `modify_time` datetime(6) NOT NULL,
  `task_id` varchar(36) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user_emailverifycode
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
INSERT INTO `user_userprofile` VALUES ('1', 'pbkdf2_sha256$120000$BEz96qKEQgHb$fc2MW/YeWQwuvs9Qnw5hzdNaYGBVdF2QI8uvVepNqpw=', '2019-05-31 14:24:31.845600', '1', 'fake_admin', '', '', 'fake_admin@qq.com', '1', '1', '2019-05-31 14:24:07.412600', '', 'male', '2019-05-31 14:24:07.412600', '2019-05-31 14:24:07.412600');

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
