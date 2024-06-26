from rest_framework import serializers
from .models import User 
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, smart_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import send_email
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class UserRegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(max_length=68, min_length=6, write_only=True )
  password2 = serializers.CharField(max_length=68, min_length=6, write_only=True )

  class Meta:
    model = User
    fields=['username', 'email', 'first_name', 'last_name', 'password', 'password2'] 
  def validate(self, attrs):
    password = attrs.get('password', '')
    password2 = attrs.get('password2', '')
    if password != password2:
      raise serializers.ValidationError("Password do not match.")
    return attrs

  def create(self, validated_data):
    user = User.objects.create_user(
      username=validated_data['username'],
      email = validated_data['email'],
      password = validated_data['password'],
      first_name = validated_data['first_name'],
      last_name = validated_data['last_name']
    )
    return user
  
class LoginSerializer(serializers.ModelSerializer):
  username = serializers.CharField( max_length=55 )
  password = serializers.CharField( max_length=60, write_only=True )
  access_token = serializers.CharField( max_length=255, read_only=True )
  refresh_token = serializers.CharField( max_length=255, read_only=True )
  class Meta:
    model=User
    fields=['username', 'full_name', 'password', 'access_token', 'refresh_token']

  def validate( self, attrs ):
    username = attrs.get('username')
    password = attrs.get('password')
    request = self.context.get('request')
    user = authenticate(request, username=username, password = password )

    if not user:
      raise AuthenticationFailed("Invalid user credentials") 
    token = user.user_token()

    return {
      'username' : user.username,
      'full_name' : user.full_name,
      'access_token' : str(token.get('access')),
      'refresh_token' : str(token.get('refresh')),
    }
    
class PasswordResetSerializer(serializers.Serializer):
  email = serializers.EmailField( max_length=255 )
  class Meta:
    Fields = ["email"]
  
  def validate(self, attrs):
    email = attrs.get('email')
    if User.objects.filter(email=email).exists():
      user = User.objects.get(email=email)
      uidb64 = urlsafe_base64_encode(smart_bytes(user.id)) 
      token = PasswordResetTokenGenerator().make_token(user) 
      request = self.context.get('request')
      site_domain = get_current_site(request).domain
      relative_link = reverse('reset-password-confirm', kwargs={'uidb64' : uidb64, 'token' : token})
      absolute_link = f"http://{site_domain}{relative_link}"
      email_body = f"Hi use this link below to reset your password \n {absolute_link}" 
      data= {
        "email_body": email_body,
        "email_subject": "Reset your password",
        "to_email": user.email
      }
      send_email(data)
    return super().validate(attrs)

class SetNewPasswordSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=100, min_length=6, write_only=True) 
  confirm_password = serializers.CharField(max_length=100, min_length=6, write_only=True)
  uidb64 = serializers.CharField(write_only=True)
  token = serializers.CharField(write_only=True) 
  class Meta:
    Fields = ["password", "confirm_password", "uidb64", "token"] 

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      confirm_password = attrs.get('confirm_password') 
      uidb64 = attrs.get('uidb64') 
      token = attrs.get('token') 

      user_id = force_str(urlsafe_base64_decode(uidb64))
      user = User.objects.get(id = user_id) 
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise AuthenticationFailed("Password link is invalid or has expired", 401) 
      if password != confirm_password:
        raise AuthenticationFailed("Password didn't match") 
      user.set_password(password)
      user.save()
      return user
    except Exception as e:
      raise AuthenticationFailed("Password link is invalid or has expired")
    
class LogoutSerializer(serializers.Serializer):
  refresh_token = serializers.CharField() 

  default_error_message={
    'Bad_Token': ('Token is invalid or expired')
  }

  def validate(self, attrs):
    self.token = attrs.get('resfresh_token') 
    return attrs
  
  def save(self, **kwargs):
    try:
      token = RefreshToken(self.token) 
      token.blacklist()
      
    except TokenError:
      return self.fail("Bad_Token")