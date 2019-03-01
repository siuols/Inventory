from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
# from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL
# Create your models here.

class Brand(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    brand_name              = models.CharField(max_length = 255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.brand_name)

    # @property
    # def slug_title(self):
    #     return '{}'.format(self.brand_name)

