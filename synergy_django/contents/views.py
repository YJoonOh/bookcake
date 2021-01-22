from django.shortcuts import render, redirect
from .models import Content
from .serializers import ContentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

# 한글 인코딩
import urllib.request
import urllib.parse

from django.utils import timezone
from datetime import datetime, date
from random import *

''' Base Settings START '''

''' Base Setting END '''

''' REST API START '''
# API Overview
@api_view(['GET'])
def apiOverview(request):
    api_urls = { 
        # 'All Tips' : '/all/',
        'All Contents' : '/home/',
        'Create' : '/create/<str:>/',
    }
    return Response(api_urls)

# home : 카테고리 선택
@api_view(['GET'])
def selectCategory(request):
    result = Content.objects.all()
    serialized = ContentSerializer(result, many=True)
    return Response(serialized.data)

# 선택된 카테고리의 컨텐츠를 랜덤으로 추출
@api_view(['GET'])
def result(request, cat_id):
    ''' 
    
    '''
    ##### 랜덤으로 contents 추출 #####
    # 1) 선택된 category로 filter => Queryset
    cat_filter = Content.objects.filter(category=cat_id)
    # 2) 해당 category의 contents 갯수 count => int
    howMany = Content.objects.filter(category=cat_id).count()
    # 3) 0부터 갯수-1 중 정수 랜덤 추출 => int
    randomIndex = randint(0, howMany-1)
    # 4) 랜덤 추출된 정수로 QuerySet 인덱싱
    randomContent = cat_filter[randomIndex]
    # 5) 선택된 쿼리 serialize
    serialized = ContentSerializer(randomContent)

    return Response(serialized.data)

# yourTip : 사용자가 자신의 팁 공유
@api_view(['POST'])
def yourTip(request):
    # modelForm을 쓸 때는 request.POST를 쓰지만, api에서는 request.data를 사용!
    serialized = TipSerializer(data=request.data)
    
    if serialized.is_valid():
        serialized.save()

    return Response(serialized.data)

# Share 가능한 팁
@api_view(['GET'])
def canShare(request):
    canShares = Tip.objects.filter(can_share=True)

    serialized = TipSerializer(canShares, many=True)
    return Response(serialized.data)

# 아직 share 가능하지 않은 팁
@api_view(['GET'])
def cannotShare(request):
    cannotShares = Tip.objects.filter(can_share=False)

    serialized = TipSerializer(cannotShares, many=True)
    return Response(serialized.data)

''' REST API END '''