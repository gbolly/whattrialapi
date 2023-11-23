from django.urls import path

from . import views

urlpatterns = [
    path("", views.ProductViewSet.as_view()),
    path("<int:pk>", views.ProductViewSet.as_view()),
]
