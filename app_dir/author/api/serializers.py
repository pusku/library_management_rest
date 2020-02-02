from rest_framework import serializers
from ...core.loading import get_model

TABLE = get_model('author', 'Author')
APP = 'author_api'
fields = ('name',)


class AuthorSerializer(serializers.ModelSerializer):
    update_url = serializers.HyperlinkedIdentityField(view_name=APP + ':update')
    delete_url = serializers.HyperlinkedIdentityField(view_name=APP + ':delete')

    class Meta:
        model = TABLE

        fields = fields + ('update_url', 'delete_url')

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()

        return instance


class AuthorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TABLE

        fields = fields

    def create(self, validated_data):
        TABLE.objects.create(**validated_data)
        return validated_data

