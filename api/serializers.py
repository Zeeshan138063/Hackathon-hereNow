from rest_framework import serializers

from api.models import Location, User


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'name', 'email', 'address', 'phone',
                    'related_users', 'created', 'role')

