from rest_framework import serializers
from ...core.loading import get_model

TABLE = get_model('book', 'Book')
APP = 'book_api'
fields = ('title', 'author')
from app_dir.book.models import Book


class BookSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name=APP + ':update')
    delete_url = serializers.HyperlinkedIdentityField(view_name=APP + ':delete')

    class Meta:
        model = TABLE

        fields = fields + ('update_url', 'delete_url')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        return instance


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TABLE

        fields = fields

    def create(self, validated_data):
        TABLE.objects.create(**validated_data)
        return validated_data

class TimeSeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author']