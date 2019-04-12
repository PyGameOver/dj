# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json


def add(request):
    '''
    根据请求方法返回不同结果
    :param request:
    :return:
    '''
    if request.method == "GET":
        return render(request, "add.html")
    else:
        array = request.POST.get("array")
        array_dict = json.loads(array)
        value_list = array_dict["value_array"]
        value_list_sum = sum([item["value"] for item in value_list])
        return HttpResponse('{"result":%s}' % (value_list_sum))


def chat(request):
    '''

    :param request:
    :return: 根据输入内容是否包含该字符串返回相应页面
    '''
    if request.method == "GET":
        return render(request, "chat.html")
    else:
        if "您好" in request.POST.get("content") and "再见" in request.POST.get("content"):
            return HttpResponse('{"result":"%s"}' % ("天气不错。"))
        elif "再见" in request.POST.get("content"):
            return HttpResponse('{"result":"%s"}' % ("回见了您内。"))
        elif "您好" in request.POST.get("content"):
            return HttpResponse('{"result":"%s"}' % ("您好，您吃了吗？"))
        else:
            return HttpResponse('{"result":"%s"}' % ("请重新输入"))
