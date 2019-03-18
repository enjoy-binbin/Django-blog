# -*- coding: utf-8 -*-
from .models import Category
from utils.get_setting import get_setting
from django.contrib.sites.models import Site

def setting(requests):
    """ 自定义一些模板全局变量 """
    s = get_setting()
    site = Site.objects.get(id=1)
    return {
        'SITE_NAME': s.name,  # 站点名称
        'SITE_DESC': s.desc,  # 站点描述
        'SITE_KEYWORD': s.keyword,  # 站点关键字
        'SITE_URL': site.domain,

        'nav_category_list': Category.objects.all(),  # 导航栏-> 所有分类，nav.html模板里调用

        'top_categorys': Category.top_objects.all()  # 对manager的应用，所有的一级分类
    }
