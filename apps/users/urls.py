from django.urls import path

from .views import MeUserView, UserListCreateView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path("/me", MeUserView.as_view(), name='me_info'),
]
