from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,  name='index'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>', views.delete, name='delete')
]
