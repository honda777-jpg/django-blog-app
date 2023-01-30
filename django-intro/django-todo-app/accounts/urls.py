from django.urls import path
from accounts.views import SignUpView
from django.contrib.auth.views import LoginView, LogoutView # ログイン、ログアウト用

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(template_name="accounts/login.html",redirect_authenticated_user = True), # このように引数を入れると、viewの方に書く必要はなくなる
        name="login",                                                                              # redirect_authenticated_user = Trueで、ログインされてる状態でログインのURLを打っても、ログイン画面に飛ばず、設定した画面に飛ぶ
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup")
]