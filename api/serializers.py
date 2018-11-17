from rest_framework import serializers
from .models import Activity

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id','name','date_created','date_modified')
        read_only_fields = ('date_created','date_modified')
        