from django.contrib.auth import authenticate
from django.core.validators import EmailValidator
from rest_framework import serializers
from new_app.models import User

class UserSerializer (serializers.ModelSerializer):
    class meta:
        model=User
        fields=['email','password']
        read_only_feild=['id']
        extra_kwargs={"password":{"write_only":True},
                      "is_active":{"write_only":True}}
        
    def create(self,validated_data):
        password=validated_data.pop("password", None)
        instance=self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    def update (self,instance,validated_data):
        for attr,value in validated_data.items():
            if attr=="password":
                instance.set_password(value)
            else:
                setattr(instance,attr,value)
        instance.save()
        return instance
                                    