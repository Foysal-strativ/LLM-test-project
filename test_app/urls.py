from django.urls import path
from test_app.views import TestView

urlpatterns = [
    path('api/v1/', TestView.as_view(), name='index'),
]