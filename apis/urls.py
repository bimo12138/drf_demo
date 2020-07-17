"""
@author:      13716
@date-time:   2019/12/18-16:53
@ide:         PyCharm
@name:        urls.py
"""
from django.urls import path
from . import views
from rest_framework import routers

app_name = "index"
router = routers.DefaultRouter()


urlpatterns = router.urls + [
    path(r"index", views.IndexView.as_view()),
    path(r"hero-classify", views.HeroClassifyView.as_view()),
    path(r"hero-list", views.HeroListView.as_view())
]
