from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register_student, name="register_student"),
    path(
        "student/<int:student_id>/update/", views.update_student, name="update_student"
    ),
    path(
        "student/<int:student_id>/delete/", views.delete_student, name="delete_student"
    ),
]
