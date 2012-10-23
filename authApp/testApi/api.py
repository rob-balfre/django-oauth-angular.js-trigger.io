from tastypie.resources import ModelResource
from testApi.models import FoodOption

class FoodResource(ModelResource):
    class Meta:
        queryset = FoodOption.objects.all()
        resource_name = 'food'