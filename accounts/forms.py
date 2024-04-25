from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class DonorSignUpForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ['email', 'password1', 'password2']

  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data['email']
    user.set_password(self.cleaned_data['password1'])

    if commit:
      user.save()
