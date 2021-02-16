from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('plus_two', views.add_two),
	path('custom_increment', views.add_custom),
	path('destroy_session', views.reset)
]