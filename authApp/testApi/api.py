from django.contrib.auth.models import User
from tastypie import fields
from tastypie.resources import ModelResource
from testApi.models import FoodOption, Vote
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication
from tastypie.constants import ALL, ALL_WITH_RELATIONS

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        trailing_slash = False
        fields = ['username','id']

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        #authentication = ApiKeyAuthentication()
        trailing_slash = False

class VoteResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user', full=True)
    food_option = fields.ForeignKey(FoodResource, 'food_option', full=True)

    class Meta:
        queryset = Vote.objects.all()
        filtering = {
            "food_option": ('exact')
        }
        resource_name = 'vote'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        #authentication = ApiKeyAuthentication()
        trailing_slash = False