from rest_framework import serializers
from items.models import Item
from django.contrib.auth.models import User


class AddedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ItemListSerializer(serializers.ModelSerializer):
    item_wish_count = serializers.SerializerMethodField()
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'item-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    added_by = AddedBySerializer()
    class Meta:
        model = Item
        fields = ['image', 'added_by', 'name', 'detail', 'item_wish_count']
    
    def get_item_wish_count(self, obj):
        return "This item has been wished by %s users"%(obj.favoriteitem_set.count())

class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'










# from rest_framework.generics import ListAPIView
# from items.models import Item
# from rest_framework import serializers
# from django.contrib.auth.models import User


# class ListSerializer(serializers.ModelSerializer):
#     detail = serializers.HyperlinkedIdentityField(
#         view_name = "detail",
#         lookup_field = "id",
#         lookup_url_kwarg = "object_id"
#         )

#     class Meta:
#         model = Item
#         fields = ['image', 'name' ,'description','detail']


# class UserSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = User
# 		fields = ['first_name', 'last_name',]


# class DetailSerializer(serializers.ModelSerializer):
# 	added_by = UserSerializer()
#     class Meta:
#         model = Item
#         fields = ['image', 'name' ,'description', 'added_by']









