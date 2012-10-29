from tastypie.resources import ModelResource
from testApi.models import FoodOption
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'
        serializer = Serializer(formats=['jsonp', 'json'])
        authorization = Authorization()
        authentication = ApiKeyAuthentication()
        trailing_slash = False