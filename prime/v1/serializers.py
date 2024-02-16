from rest_framework import serializers
from prime.models import (
    Address,
    Category,
    Store,
    Item
)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = Category
        fields = ["id", "name", "created_at"]


class StoreSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "image",
            "address",
            "created_at"
        ]

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address, _ = Address.objects.get_or_create(**address_data)
        return Store.objects.create(**validated_data, address=address)

    def update(self, instance, validated_data):
        if 'address' in validated_data.keys():
            address_data = validated_data.pop('address')
            address, _ = Address.objects.get_or_create(**address_data)
            instance.address = address
        instance.name = validated_data.get("name", instance.name)
        instance.image = validated_data.get("image", instance.image)
        instance.save()
        return instance


class ItemSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, required=True)
    image = serializers.ImageField(required=False)

    class Meta:
        model = Item
        fields = [
            "id",
            "name",
            "image",
            "description",
            "price",
            "discount",
            "promo",
            "sell_price",
            "store",
            "categories"
        ]

    def get_categories(self, categories):
        ids = []
        for category in categories:
            category_instance = Category.objects.get(
                    pk=category.get("id")
                )
            ids.append(category_instance.pk)
        return ids

    def create(self, validated_data):
        categories = validated_data.pop("categories", [])
        print(categories)
        item = Item.objects.create(**validated_data)
        item.categories.set(self.get_categories(categories))
        item.save()
        return item

    def update(self, instance, validated_data):
        categories = validated_data.pop("categories", [])
        instance.categories.set(self.get_categories(categories))
        fields = ["name", "description", "price", "discount", "store"]
        for field in fields:
            setattr(instance, field, validated_data[field])
        instance.save()
        return instance


class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = [
            "id",
            "name",
            "image",
            "address",
            "items"
        ]
