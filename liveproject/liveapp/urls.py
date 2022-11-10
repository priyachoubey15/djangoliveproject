from django.urls import path
from liveapp import views

urlpatterns=[
    path("",views.Navbar,name="home"),
    path("form/",views.Register,name="form"),
    path("data/",views.Data,name="data"),
    path("Delete/<int:id>/",views.Delete,name="delete"),
    path("update/<int:id>/",views.update,name="update"),
    path("signup/",views.signup,name="signup"),
    path("logged/",views.logIn,name="logged"),
    path("loggout/",views.log_out,name="loggout")
]

