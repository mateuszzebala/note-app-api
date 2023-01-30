from django.urls import path, re_path, include
from . import views

app_name = "notes"


urlpatterns = [
    path("", views.home, name="home"),
    path("csrf/", views.csrf, name="csrf"),
    path("signin/", views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("notes/", views.notes, name="notes"),
    path("notes/search/", views.search_notes, name="notes"),
    path("note/new/", views.new_note, name="new_note"),
    path("note/delete/", views.delete_note, name="new_note"),
    path("note/update/", views.update_note, name="update_note"),
    path("note/", views.get_note, name="get_note"),
]

