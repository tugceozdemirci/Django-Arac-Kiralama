from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel
from mptt.fields import TreeForeignKey
from ckeditor_uploader.fields import RichTextUploadingField


class Category(MPTTModel):
    STATUS = {
        ('True', 'Evet'),
        ('False', 'Hayır'),
    }
    title = models.CharField(max_length=40)
    keywords = models.CharField(max_length=260)
    description = models.CharField(blank=True, max_length=260)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k = k.parent
        return '>>'.join(full_path[::-1])

    def image_tag(self):
        if self.image:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'


def get_absolute_url(self):
    return reverse('category_detail', kwargs={'slug': self.slug})


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
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('car_detail', kwargs={'slug': self.slug})

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
