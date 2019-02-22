2019年2月07日 14:44:54

在app下创建 xadmin.py文件

	# -*- coding: utf-8 -*-
	import xadmin
	from xadmin import views
	
	from .models import EmailVerifyCode, UserAddress


​	
	class BaseSetting(object):
	    """ 基本adminView配置 """
	    enable_themes = True  # 启动主题
	    use_bootswatch = True  # 主题列表


​	
	class CommSetting(object):
	    """ commonView配置 """
	    site_title = '彬彬商场后台管理系统'  # 后台标题
	    site_footer = 'Binbin Mall'  # 后台脚注
	    # menu_style = "accordion"  # 可以收缩菜单栏


​	
	class EmailVerifyCodeAdmin(object):
	    """邮箱验证码"""
	    list_display = ['email', 'id', 'code', 'type', 'add_time']  # 列表页显示的字段
	    search_fields = ['code', 'email', 'type']  # 可以用来搜索的字段
	    list_filter = ['code', 'email', 'type', 'add_time']  # 过滤器能过滤的字段


​	
	class AddressAdmin(object):
	    list_display = ['user', 'signer', 'signer_mobile', 'address']
	    search_fields = ['user', 'signer', 'signer_mobile', 'address']
	    list_filter = ['user', 'signer', 'signer_mobile', 'address']


​	
	# 注册xadmin全局设置
	xadmin.site.register(views.BaseAdminView, BaseSetting)
	xadmin.site.register(views.CommAdminView, CommSetting)
	
	# 注册app
	xadmin.site.register(EmailVerifyCode, EmailVerifyCodeAdmin)
	xadmin.site.register(UserAddress, AddressAdmin)


# 后台页 app显示 verbosename
	在app下的 apps.py下
		from django.apps import AppConfig


​		
		class UsersConfig(AppConfig):
		    name = 'users'
		    verbose_name = '用户管理'


​	
​	
	在app下的 __init__.py
		default_app_config = 'goods.apps.GoodsConfig'


# xadmin后台左侧app排序设置
	在源码中 xadmin\view\base.py 注释下一行代码，便会根据settings里installed_app排序	
	# nav_menu.sort(key=lambda x: x['title'])



refresh_times = (3, 5)
list_editable = ['price']  # 列可编辑
show_detail_fields = [] # 显示数据详情，外键详情
list_export = ('xls', 'xml', 'json')

