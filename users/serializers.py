from urllib import request
from rest_framework import serializers
from .models import MyUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = '__all__'
     

    def save(self):

    

        user = MyUser(
            gender=self.validated_data['gender'],
            country_code=self.validated_data['country_code'],
            last_name=self.validated_data['last_name'], 
            first_name=self.validated_data['first_name'],
            email=self.validated_data['email'], 
            birthdate=self.validated_data['birthdate'], 
            phone_number=self.validated_data['phone_number'],
            avatar = self.validated_data['avatar']   
        )

        password = self.validated_data['password']

    
        user.set_password(password)
        user.save()
        return user

class MyUserSerializer(serializers.ModelSerializer):

   class Meta:
        model = MyUser
        fields = '__all__'
        
