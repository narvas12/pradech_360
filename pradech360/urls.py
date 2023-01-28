from django.urls import path
from .views import Creatives, Partnerships
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("form", views.forms, name="form"),
    path("creatives-form", Creatives.as_view(), name="creative"),
    path("partnership-form", Partnerships.as_view(), name="partnership"),
    path("blog", views.blog, name="blog"),
    path("inner-page", views.inner_page, name="inner_page"),
    path("portfolio_details", views.portfolio_details, name="portfolio_details"),
    path("blog_single", views.blog_single, name="blog_single"),
    path("blog_entry", views.blog_entry, name="blog_entry")
]
