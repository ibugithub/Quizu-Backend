import pytest 
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db 
def test_valid_email():
  manager = User.objects
  valid_email = 'test@example.com'
  manager.email_validator(valid_email)


@pytest.mark.django_db
def test_invalid_email():
  manager = User.objects
  invalid_email = 'testexample.com'
  with pytest.raises(ValueError) as exc_info:
    manager.email_validator(invalid_email)
  assert str(exc_info.value) == 'Please enter a valid email address'


@pytest.mark.django_db
def test_empty_email():
  manager = User.objects
  empty_email = ''
  with pytest.raises(ValueError) as exc_info:
    manager.email_validator(empty_email)
  assert str(exc_info.value) == 'Please enter a valid email address'


@pytest.mark.django_db
def test_none_email():
  manager = User.objects
  none_email = None
  with pytest.raises(ValueError) as exc_info:
    manager.email_validator(none_email)
  assert str(exc_info.value) == 'Please enter a valid email address'

@pytest.mark.django_db
def test_create_user_success():
    user = User.objects.create_user(
        email='test@example.com',
        username = 'test',
        first_name='John',
        last_name='Doe',
        password='testpassword'
    )

    assert user.email == 'test@example.com'
    assert user.first_name == 'John'
    assert user.last_name == 'Doe'
    assert user.check_password('testpassword')
    assert not user.is_staff
    assert not user.is_superuser


@pytest.mark.django_db
def test_create_user_no_email():
    with pytest.raises(ValueError) as exc_info:
        User.objects.create_user(
            email='',
            username = 'test',
            first_name='John',
            last_name='Doe',
            password='testpassword'
        )
    assert str(exc_info.value) == 'email must be specified'

@pytest.mark.django_db
def test_create_user_invalid_email():
    with pytest.raises(ValueError) as exc_info:
        User.objects.create_user(
            email='invalid_email',
            username = 'test',
            first_name='John',
            last_name='Doe',
            password='testpassword'
        )
    assert str(exc_info.value) == 'Please enter a valid email address'

@pytest.mark.django_db
def test_create_user_extra_fields():
    user = User.objects.create_user(
        email='test@example.com',
        username = 'test',
        first_name='John',
        last_name='Doe',
        password='testpassword',
        is_writer=True
    )

    assert user.is_writer


@pytest.mark.django_db
def test_create_superuser_creation_success():
  user = User.objects.create_superuser(
  email='test@example.com',
  username = 'test',
  first_name='John',
  last_name='Doe',
  password='testpassword',
  )
  assert user.email == 'test@example.com'
  assert user.first_name == 'John'
  assert user.last_name == 'Doe'
  assert user.username == 'test'
  assert user.check_password('testpassword')
  assert user.is_staff
  assert user.is_superuser
  assert user.is_verified


@pytest.mark.django_db
def test_create_superuser_no_is_staff():
    with pytest.raises(ValueError) as exc_info:
        User.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            first_name='Admin',
            last_name='User',
            password='adminpassword',
            is_staff=False
        )
    assert str(exc_info.value) == 'is_stafff must be true for admin users'

@pytest.mark.django_db
def test_create_superuser_no_is_superuser():
    with pytest.raises(ValueError) as exc_info:
        User.objects.create_superuser(
            email='admin@example.com',
            username='admin',
            first_name='Admin',
            last_name='User',
            password='adminpassword',
            is_superuser=False
        )
    assert str(exc_info.value) == 'is_superuser must be true for admin users'

@pytest.mark.django_db
def test_create_superuser_extra_fields():
    superuser = User.objects.create_superuser(
        email='admin@example.com',
        username='admin',
        first_name='Admin',
        last_name='User',
        password='adminpassword',
        is_writer=True
    )

    assert superuser.is_writer