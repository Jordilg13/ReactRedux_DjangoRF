from rest_framework import serializers
from .models import Testt


class TesttSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testt
        fields = [
            "slug",
            "owner",
            "name",
            "desc",
            "number"
        ]
        read_only_fields = [
            "owner"
        ]
