import pytest
from django.urls import reverse, resolve
from accounts.views import (
    RegisterUserView,
    VerifyEmailView,
    LoginApiView,
    TestAuthenticationView,
    PasswordResetView,
    PasswordResetConfirm,
    SetNewPassword,
    LogoutView,
)
from rest_framework_simplejwt.views import TokenRefreshView


@pytest.mark.django_db
class TestAccountsUrls:
  def test_register_url(self):
    url = reverse('register')
    assert resolve(url).func.view_class == RegisterUserView
  
  def test_verify_email_url(self):
    url = reverse('verify-email')
    assert resolve(url).func.view_class == VerifyEmailView

  def test_login_url(self):
    url = reverse('login')
    assert resolve(url).func.view_class == LoginApiView

  def test_check_auth_url(self):
    url = reverse('check-auth')
    assert resolve(url).func.view_class == TestAuthenticationView

  def test_reset_password_url(self):
    url = reverse('reset-password')
    assert resolve(url).func.view_class == PasswordResetView

  def test_reset_password_confirm_url(self):
    url = reverse('reset-password-confirm', args=['uidb64', 'token'])
    assert resolve(url).func.view_class == PasswordResetConfirm

  def test_set_new_password_url(self):
    url = reverse('set-new-password')
    assert resolve(url).func.view_class == SetNewPassword

  def test_logout_url(self):
    url = reverse('logout')
    assert resolve(url).func.view_class == LogoutView

  def test_refresh_token_url(self):
    url = reverse('refresh')
    assert resolve(url).func.view_class == TokenRefreshView

