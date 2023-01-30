from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    template_name = "accounts/signup.html"
    form_class = UserCreationForm # どんなフォームを使用していくか
    success_url = reverse_lazy("task-list")