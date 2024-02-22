from rest_framework import serializers

from .models import Tv, Phone, Laptop, Earbud


class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        abstract = True
        fields = ["pk", "brand", "model", "price"]


class TvSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Tv
        fields = BaseProductSerializer.Meta.fields + ["screen_size"]


class PhoneSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Phone
        fields = BaseProductSerializer.Meta.fields + ["color"]


class LaptopSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Laptop
        fields = BaseProductSerializer.Meta.fields + ["screen_size"]


class EarbudSerializer(BaseProductSerializer):

    class Meta(BaseProductSerializer.Meta):
        model = Earbud
        fields = BaseProductSerializer.Meta.fields + ["with_lcd"]
