from django.urls import path
from .views import IndexView, DetailView
# from weather import views


urlpatterns = [
    path('', IndexView.as_view()),
    path('detail/<int:city_id>/', DetailView.as_view, name='detail'),
]

# urlpatterns = [
#     path('', views.index),
#     path('detail/<int:city_id>/', views.detail, name='detail'),
# ]