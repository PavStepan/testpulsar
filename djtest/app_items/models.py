import os
from django.db import models, transaction
from decimal import Decimal


def directory_path(instance, filename):
    return f'media/images/{instance.title}{os.path.splitext(filename)[1]}'


class StatusModel(models.Model):
    status = models.CharField(max_length=128, verbose_name='Статус')

    def __str__(self):
        return self.status


class ItemModel(models.Model):
    title = models.CharField(max_length=128, verbose_name='Название')
    code = models.CharField(max_length=10, verbose_name='Артикул', unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=Decimal('0.00'))
    image = models.ImageField(upload_to=directory_path, verbose_name='Изображение', blank=True)
    status = models.ForeignKey(StatusModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(ItemModel, self).save(*args, **kwargs)

        with transaction.atomic():
            list_format = ItemModel.objects.get(id=self.id).formats.values_list('name_format', flat=True)
            extension = os.path.splitext(os.path.basename(self.image.name))[1]
            if extension.lower() not in list_format:
                self.formats.create(name_format=extension[1:])
                if extension.lower() in ['.jpg', '.png']:
                    self.formats.create(name_format='webp')


class FormatModel(models.Model):
    name_format = models.CharField(max_length=4, verbose_name='Формат', blank=True)
    item = models.ForeignKey(ItemModel, on_delete=models.CASCADE, related_name='formats')

    def __str__(self):
        return self.name_format


