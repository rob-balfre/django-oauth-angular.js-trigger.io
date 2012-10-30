from django.db import models
from django.contrib.auth.models import User    
from django.db import models  
from tastypie.models import create_api_key 
from django.db.models.signals import post_delete, post_save

models.signals.post_save.connect(create_api_key, sender=User)

class FoodOption(models.Model):
    name = models.CharField(max_length=30)
    votes = models.IntegerField()
    
    def __unicode__(self):
        return self.name

class Vote(models.Model):
    food_option = models.ForeignKey(FoodOption)
    user = models.ForeignKey(User)
    
    class Meta:
        unique_together = ('food_option', 'user',)
    
    def __unicode__(self):
        return self.food_option.name

def add_vote(sender, **kwargs):
    obj = kwargs['instance']
    obj.food_option.votes +=1
    obj.food_option.save()
    
def remove_vote(sender, **kwargs):
    obj = kwargs['instance']
    obj.food_option.votes -=1
    obj.food_option.save()
    
post_save.connect(add_vote, sender=Vote)
post_delete.connect(remove_vote, sender=Vote)
