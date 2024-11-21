from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response


@api_view(['GET'])
@renderer_classes([JSONRenderer])
@permission_classes([IsAuthenticated])
def categories_list(request):
    categories = CategoryModel.objects.all().order_by("-id")
    serializer = CategoriesSerializer(categories, many=True)
    return Response(serializer.data)