
# LOGIN APP --- MODELS

from __future__ import unicode_literals

from django.db import models

from time import gmtime,strftime

from ..login_app.models import User


class CheckItem(models.Manager):
    def validateItem(self, post_data):                                   # RECIEVES AND VALIDATES POST DATA
        results = {                                                     # APPENDS MESSAGES TO 'ERRORS'
            'errors' : [],                                              # BOOLEAN SHOWS INPUT VALIDITY
            'status' : True,                                            # TRUE --> CREATE
        }                                                               # FALSE --> DISPLAY ERRORS
        if len(post_data['name']) < 3:
            results['status'] = False
            results['errors'].append("You must enter a longer name")         
                                                                            
        
        return results                                                      # RETURNS 'RESULTS' OBJECT
            

class Item(models.Model):
    name = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, related_name="created_item")
    all_users = models.ManyToManyField(User, related_name="all_items")
    objects = CheckItem()
    


