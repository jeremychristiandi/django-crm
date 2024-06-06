from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    # path("/login", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("records/<int:pk>/", views.customer_record, name="record"),
    path("delete-record/<int:pk>/", views.delete_record, name="delete-record"),
    path("add-record/", views.add_record, name='add-record'),
    path("edit-record/<int:pk>/", views.edit_record, name='edit-record'),
]