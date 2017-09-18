from django.conf.urls import url    #引入url解析
from . import views   #引入视图函数

app_name='users' #设置命名空间
urlpatterns=[
    url(r'^register/',views.register,name='register'),
]