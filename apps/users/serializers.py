from django.contrib.auth import get_user_model
from django.db.transaction import atomic

from rest_framework import serializers

from core.dataclasses.user_dataclass import User

from apps.users.models import ProfileModel

UserModel = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ("id", "name", "surname", "age", "phone_number", "created_at", "updated_at")


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            "id",
            "email",
            "password",
            "is_active",
            "is_staff",
            "is_superuser",
            "role",
            "account_type",
            "last_login",
            "created_at",
            "updated_at",
            "profile"
        )
        read_only_fields = (
            "id", "is_active", "is_staff", "is_superuser",
            "role", "account_type", "last_login", "created_at", "updated_at")

        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }

    @atomic
    def create(self, validated_data: dict):
        profile = validated_data.pop("profile")
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user, )
        return user
