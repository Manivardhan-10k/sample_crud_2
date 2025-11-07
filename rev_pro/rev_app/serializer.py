from rest_framework import serializers 

#normal serializers

#model serializers
from .models import UserDetails
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields="__all__" ##["field1", field2.....]