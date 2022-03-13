from rest_framework import serializers
from hood.models import UserProfile

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('bio', 'birth_date','picture','email','picture')