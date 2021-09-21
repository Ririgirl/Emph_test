from django.urls import path
from authentication.views import RegisterView, LoginView, UserGUD, \
    UserGUDUsername, UserGUDid

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login_token/', LoginView.as_view(), name='login'),
    path('user/all/', UserGUD.as_view()),
    path('user/<str:username>/', UserGUDUsername.as_view()),
    path('user/int/<int:id>/', UserGUDid.as_view(), name='RetrieveUpdateDestroy'),
]
