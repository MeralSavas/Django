from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):


    email = serializers.EmailField(
        required=True,
        validators = [UniqueValidator(queryset=User.objects.all())]
        )

    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password],
        style = {"input_type" : "password"}
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
        style = {"input_type" : "password"}
    )


    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'password2']
        
    #1. passwordle 2. si birbiryle ayni mi onun icin yazildi
    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError(
                {"message" : "Password fields didnt match!"}
            )
        return data

    #DB ye passwordu kaydetmek icin
    def create(self, validated_data):
        password = validated_data.get("password")
        validated_data.pop("password2")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user

#* ModelSerializer kullanınca create metodu yazmaya gerek yok aslında fakat, User model içinde olmayan bir field 
#* (password2) kullandığımız için creat metodunu override etmek gerekli;