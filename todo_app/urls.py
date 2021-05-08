from django.urls import path
from . import views
urlpatterns = [
    path('',views.TaskCreateView.as_view(),name = 'list'),
    path('update/<int:pk>/$',views.TaskUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>/$',views.TaskDeleteView.as_view(),name = 'delete'),
]
