# -*- coding: utf-8 -*-
from .models import Category
from utils.get_setting import get_setting


def setting(requests):
    """ 自定义一些模板全局变量 """
    s = get_setting()
    return {
        'SITE_NAME': s.name,  # 站点名称
        'SITE_DESC': s.desc,  # 站点描述
        'SITE_KEYWORD': s.keyword,  # 站点关键字

        'nav_category_list': Category.objects.all()  # 导航栏-> 所有分类
    }
