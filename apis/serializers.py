"""
@author:      13716
@date-time:   2019/12/18-17:01
@ide:         PyCharm
@name:        serializers.py
"""

from .models import Base, HeroClassify, HeroList
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class HeroClassifySerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroClassify
        fields = "__all__"


class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"


class HeroListSerializer(serializers.ModelSerializer):

    class Meta:
        model = HeroList
        fields = "__all__"
