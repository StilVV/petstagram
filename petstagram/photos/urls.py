from django.urls import path, include
from petstagram.photos import views

urlpatterns = [
    path('add/', views.photos_add, name='photos-add'),
    path('<int:pk>/', include([
        path('', views.photos_details, name='photos-details'),
        path('edit/', views.photos_edit, name='photos-edit'),
    ]))
]
