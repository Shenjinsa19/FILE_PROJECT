from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import(PhotoEntryDeleteView,PhotoEntryUpdateView)



urlpatterns = [
    path('upload/',views.upload_photo,name='upload_photo'),
    path('login/',auth_views.LoginView.as_view(template_name='diary/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',views.register, name='register'),
    path('photo/<int:pk>/edit/', PhotoEntryUpdateView.as_view(), name='photo_edit'),
    path('photo/<int:pk>/delete/', PhotoEntryDeleteView.as_view(), name='photo_delete'),
]
