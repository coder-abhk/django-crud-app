from django.urls import path
from . import views

urlpatterns = [
    path("", views.app_view, name="home"),
    path("create/", views.create_view, name="createpost"),
    path("update/<int:pk>", views.update_view, name="update"),
    path("delete/<int:pk>", views.delete_view, name="delete")
]
