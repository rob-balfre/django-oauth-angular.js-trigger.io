from tastypie.resources import ModelResource
from testApi.models import FoodOption
from tastypie.serializers import Serializer
from tastypie.authorization import Authorization, DjangoAuthorization

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'
        serializer = Serializer(formats=['jsonp'])
        authorization = Authorization()