from rest_framework import viewsets
from .models import Base, HeroClassify, HeroList
from .serializers import HeroClassifySerializer, IndexSerializer, HeroListSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User, Group
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class IndexView(APIView):

    def get(self, request):

        return Response(IndexSerializer(User.objects.all(), many=True).data)


class HeroClassifyView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request):
        return Response(HeroClassifySerializer(HeroClassify.objects.all(), many=True).data)

    def post(self, request):
        serializer = HeroClassifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"result": "添加成功！"})
        else:
            return Response(data={"result": "格式错误，添加失败！"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                HeroClassify.objects.get(id=id).delete()
                return Response(data={"result": str(id) + "删除成功！"})
            except HeroClassify.DoesNotExist:
                return Response(data={"result": "ID 不存在，请重试！"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(data={"result": "格式错误，请重试！"}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request):
        id = request.data.get("id", None)
        name = request.data.get("name", None)
        if id and name:
            try:
                result = HeroClassify.objects.get(id=id)
                result.name = name
                result.save()
                return Response(data={"result": str(id) + "修改成功！"})
            except HeroClassify.DoesNotExist:
                return Response(data={"result": "ID 不存在，请重试！"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(data={"result": "数据不完整，请重试！"}, status=status.HTTP_403_FORBIDDEN)


class HeroListView(APIView):

    def get(self, request):
        return Response(HeroListSerializer(HeroList.objects.all(), many=True).data)

    def post(self, request):
        serializer = HeroListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data={"result": "添加成功！"})
        else:
            return Response(data={"result": "格式错误，添加失败！"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request):
        id = request.data.get("id", None)
        if id:
            try:
                HeroList.objects.get(id=id).delete()
                return Response(data={"result": str(id) + "删除成功！"})
            except HeroList.DoesNotExist:
                return Response(data={"result": "ID 不存在，请重试！"}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(data={"result": "格式错误，请重试！"}, status=status.HTTP_403_FORBIDDEN)