from rest_framework import serializers

from .models import Tv, Phone, Laptop, Earbud

class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ['pk', 'brand', 'model', 'price']


class TvSerializer(BaseProductSerializer):
    size = serializers.IntegerField(source='screeen_size')
    class Meta(BaseProductSerializer.Meta):
        model = Tv
        fields = BaseProductSerializer.Meta.fields + ['screen_size']

class PhoneSerializer(BaseProductSerializer):
    color = serializers.CharField()

    class Meta(BaseProductSerializer.Meta):
        model = Phone
        fields = BaseProductSerializer.Meta.fields + ['color']

class LaptopSerializer(BaseProductSerializer):
    size = serializers.CharField(source='screen_size')
    class Meta(BaseProductSerializer.Meta):
        model = Laptop
        fields = BaseProductSerializer.Meta.fields + ['size']

class EarbudSerializer(BaseProductSerializer):
    has_lcd = serializers.BooleanField(source='with_lcd')

    class Meta(BaseProductSerializer.Meta):
        model = Earbud
        fields = BaseProductSerializer.Meta.fields + ['has_lcd', 'sale_price']