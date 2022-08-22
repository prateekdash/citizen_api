from rest_framework import serializers

from .models import citizens

class citizensserilizer(serializers.ModelSerializer):
    class Meta:
        model = citizens
        fields = '__all__'