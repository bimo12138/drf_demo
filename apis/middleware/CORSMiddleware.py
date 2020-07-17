"""
@author:      13716
@date-time:   2020/2/9-12:50
@ide:         PyCharm
@name:        CORSMiddleware.py
"""
from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["Access-Control-Allow-Origin"] = '*'
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response
