from django.db import models
from django.utils.safestring import mark_safe



class Category(models.Model) :
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=260)
    description = models.CharField(blank=True, max_length=260)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class Car(models.Model):
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=260)
    description = models.CharField(blank=True, max_length=260)
    image = models.ImageField(blank=True, upload_to='images/')
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    vites = models.CharField(max_length=10)
    price = models.FloatField()
    fuel = models.CharField(max_length=10)
    engine = models.CharField(max_length=260)
    color = models.CharField(max_length=20)
    seats = models.IntegerField()
    luggage = models.CharField(max_length=10)
    detail = models.CharField(max_length=260)
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(blank=True, max_length=150)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

class Images(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'




