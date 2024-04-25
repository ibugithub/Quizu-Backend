import pytest
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken


User = get_user_model()

@pytest.mark.django_db
def test_user_creation():
  user = User.objects.create_user(username = 'testuser', email = 'test@gmail.com', first_name='Md Test', last_name="Hossain", password = 'testpassword')

  assert user.username == 'testuser'
  assert user.email == 'test@gmail.com'
  assert user.check_password('testpassword')
  assert user.is_active
  assert not user.is_verified
  assert not user.is_superuser
  assert not user.is_staff
  assert not user.is_writer

@pytest.mark.django_db
def test_full_name():
  user = User.objects.create_user(username = 'testuser', email = 'test@gmail.com', first_name='Md Test', last_name="Hossain", password = 'testpassword')
  
  assert user.full_name == 'Md Test Hossain'

@pytest.mark.django_db
def test_user_token():
  user = User.objects.create_user(username = 'testuser', email = 'test@gmail.com', first_name='Md Test', last_name="Hossain", password = 'testpassword')

  tokens = user.user_token()
  assert 'refresh' in tokens
  assert 'access' in tokens

