from django.db import models
from django.db.models.signals import pre_save
from django.conf import settings
# from .utils import unique_slug_generator

User = settings.AUTH_USER_MODEL
# Create your models here.

YEAR_CHOICES = (
    ('1st', '1st'),
    ('2nd', '2nd'),
    ('3rd', '3rd'),
    ('4th', '4th'),
)

STATUS_CHOICES = (
    ('single', 'single'),
    ('married', 'married'),
    ('separeted', 'separeted'),
    ('widow', 'widow'),
)

class ItemCode(models.Model):
    number                  = models.CharField(max_length=255)
    barcode                 = models.ImageField()

    def __str__(self):
        return '{}'.format(self.number)

class Brand(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

    # @property
    # def slug_title(self):
    #     return '{}'.format(self.brand_name)

class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)

class Item(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    brand                   = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE)
    number                  = models.CharField(max_length=255)
    name                    = models.CharField(max_length=255)
    description             = models.CharField(max_length=500)
    quantity                = models.CharField(max_length=255)
    unit_cost               = models.CharField(max_length=255)
    total                   = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.number)

class Course(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    code                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.code)

class Customer(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number               = models.CharField(max_length=255)
    last_name               = models.CharField(max_length=255)
    first_name              = models.CharField(max_length=255)
    middle_name             = models.CharField(max_length=255)
    course                  = models.ForeignKey('Course', on_delete=models.CASCADE)
    year                    = models.CharField(
                                                max_length=9,
                                                choices=YEAR_CHOICES,
                                                default='published'
                                            )
    status                  = models.CharField(
                                                max_length=9,
                                                choices=STATUS_CHOICES,
                                                default='published'
                                            )
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.id_number)

class Offiice(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)
    slug                    = models.SlugField(null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.number)

class Released(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number               = models.ForeignKey('Customer', on_delete=models.CASCADE)
    number                  = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity                = models.CharField(max_length=255)
    office                  = models.ForeignKey('Offiice', on_delete=models.CASCADE)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.number)