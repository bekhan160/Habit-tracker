from rest_framework import serializers
from .models import User, Habit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password', 'email')

        def update(self, instance, validated_data):
            instance.password = validated_data.get("password", instance.password)
            instance.email = validated_data.get("email", instance.email)
            instance.save()
            return instance


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
