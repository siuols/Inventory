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
    ('5th', '5th'),
)

STATUS_CHOICES = (
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Separeted', 'Separeted'),
    ('Widow', 'Widow'),
)

class Brand(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    @property
    def slug_title(self):
        return '{}'.format(self.brand_name)

class Category(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

class Item(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    brand                   = models.ForeignKey('Brand', on_delete=models.CASCADE)
    category                = models.ForeignKey('Category', on_delete=models.CASCADE)
    barcode                 = models.ImageField(upload_to='media')
    number                  = models.CharField(max_length=255)
    name                    = models.CharField(max_length=255)
    description             = models.TextField()
    quantity                = models.IntegerField()
    unit_cost               = models.IntegerField()
    total                   = models.IntegerField()
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.number)

class Course(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    code                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

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
                                                default='1st'
                                            )
    status                  = models.CharField(
                                                max_length=9,
                                                choices=STATUS_CHOICES,
                                                default='single'
                                            )
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.id_number)

class Office(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    name                    = models.CharField(max_length=255)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

class Release(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.CASCADE)
    id_number               = models.ForeignKey('Customer', on_delete=models.CASCADE)
    number                  = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity                = models.IntegerField()
    total                   = models.IntegerField()
    office                  = models.ForeignKey('Office', on_delete=models.CASCADE)
    date_created            = models.DateTimeField(auto_now_add=True)
    date_modified           = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.number)    