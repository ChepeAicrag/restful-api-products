from rest_framework import serializers
from .models import Category, Product, Provider


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ['status_delete', ]

    def to_representation(self, instance):

        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "price_s": instance.price_s,
            "price_c": instance.price_c,
            "category": {
                "id": instance.category.id,
                "name": instance.category.name,
            },
            "provider": {
                "id": instance.provider.id,
                "name": instance.provider.name,
            }
        }


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        exclude = ['status_delete', ]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ['status_delete', ]
