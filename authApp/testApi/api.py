from tastypie.resources import ModelResource
from testApi.models import FoodOption
from tastypie.serializers import Serializer

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'
        serializer = Serializer(formats=['jsonp'])