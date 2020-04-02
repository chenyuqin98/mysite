from django.db.models import Q
from django.shortcuts import render

from django.core import serializers
from .models import books
from wxapp import models
from django.http import HttpResponse, JsonResponse


# Create your views here.
def wxapp(request):
    if request.method == 'GET':
        lists = books.objects.filter(website='libgen.lc')
        json_data = serializers.serialize("json", lists)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)


def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        lists = books.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
        json_data = serializers.serialize("json", lists)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)
