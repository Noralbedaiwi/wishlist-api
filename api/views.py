from django.shortcuts import render
from .serializers import ItemListSerializer, ItemDetailSerializer

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView
from items.models import Item

from .permissions import IsOwner

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name']

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsOwner]












# from rest_framework.generics import ListAPIView, RetrieveAPIView
# from items.models import Item
# from .serializers import DetailSerializer, ListSerializer
# from rest_framework.filters import SearchFilter, OrderingFilter
# from rest_framework import serializers
# from rest_framework.permissions import AllowAny

# class ItemsDetailView(RetrieveAPIView):
#     queryset = Item.objects.all()
#     serializer_class = DetailSerializer
#     lookup_field = 'id'
#     lookup_url_kwarg = 'object_id'



# class ItemsListView(ListAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ListSerializer
#     filter_backends = [SearchFilter, OrderingFilter,]
#     search_fields = ['image', 'name' ,'description']
#     permission_classes = [AllowAny]




