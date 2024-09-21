from django.urls import path
from authentication.views import signup, question, login_user, logout_user

urlpatterns = [
    path('', question, name="question"),
    path('signup/', signup, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout")
]
