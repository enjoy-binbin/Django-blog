#### 调用django的ORM

一吧可以直接 python manage shell 进入django环境进行调试



单纯记录一下

	import sys
	import os
	import pymongo
	
	client = pymongo.MongoClient('localhost')
	db = client['suning']
	goods = db['goods'].find()


​	
	pwd = os.path.dirname(os.path.realpath(__file__))
	sys.path.append(pwd+"../")
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "binshop.settings")
	
	import django
	django.setup()
	
	from goods.models import Goods, GoodsCategory, GoodsImage


​	
	for goods_detail in goods:
	    goods = Goods()
	    goods.name = goods_detail["good_name"].replace('苏宁超市自营', '').strip()
	    goods.market_price = float(goods_detail['good_price'].replace('¥','').replace('起', ''))
	    goods.shop_price = goods.market_price * 0.91
	    goods.goods_front_image = 'goods/images/' + goods.name.replace(':','比').replace('/', ' ').replace('（', '').replace('）', '').replace('*', 'X').replace('|', ' ').strip() + '.jpg'
	
	    category_name = '奶粉'  # 只取最后一个，最细的类别
	    # get的话，没有获取到是会抛异常的，filter获取不到会返回一个空数组
	    category = GoodsCategory.objects.filter(name=category_name)
	    if category:
	        goods.category = category[0]
	    goods.save()
	    print(goods.name + '添加成功')
	
	    goods_image_instance = GoodsImage()
	    goods_image_instance.image = goods.goods_front_image
	    goods_image_instance.goods = goods
	    goods_image_instance.save()