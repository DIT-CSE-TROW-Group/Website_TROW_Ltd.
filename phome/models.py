
import datetime
import os
from django.db import models



def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('admin/Cuisines_category', filename)

class Cuisines_category(models.Model):
    name=models.CharField(null=True,max_length=50)
    actual_price=models.CharField(default=None, null=True,max_length=50)
    price_range=models.CharField(default=None, null=True,max_length=50)
    extra_offer=models.CharField(default=None,null=True,blank=True,max_length=100)
    image = models.ImageField(default=None, upload_to=filepath, null=True, blank=True)
    discount=models.CharField(default=None, null=True,max_length=50)
    
    def __str__(self):
        return self.name
    