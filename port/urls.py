from django.urls import include, path
from port import views
from .views import submit_form

urlpatterns = [
    
    path("", views.index, name="index"),
    path("about",views.about,name="about"),
    path("projects", views.projects, name="projects"),
    path("contact", views.contact, name="contact"),
    path("forms", views.forms, name="forms"),
    path('submit_form/', submit_form, name='submit_form'),

]