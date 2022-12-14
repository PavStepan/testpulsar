from rest_framework import serializers
from app_items.models import ItemModel
import os


class ItemSerializer(serializers.ModelSerializer):
    """ Класс сериализатор модели Item """
    image = serializers.SerializerMethodField()

    class Meta:
        model = ItemModel
        fields = '__all__'

    def get_image(self, instance):
        """ Метод сериализации поля image """
        if instance.image:
            path_file = os.path.splitext(instance.image.url)[0]
            formats = instance.formats.values_list('name_format', flat=True)
        else:
            path_file = 'Нет изображения'
            formats = None

        return {
                'path': path_file,
                'formats': formats
                }
