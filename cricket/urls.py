from django.urls import path
from . import views
app_name = "cricket"
urlpatterns = [
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("", views.home, name="home"),
    path("logout", views.logout_request, name="logout"),
    path('list', views.list_view, name='list_teams'),
    # path('player_name', views.addplayer_name, name='player_name'),
    path('team_name', views.team_name, name='team_name'),
    path("newmatch", views.addnewmatch, name="newmatch"),
    path("update_score", views.update_score, name="update_score"),
    path("extrarun", views.extrarun, name="extrarun"),
    path("matchdetail", views.matchdetail, name="matchdetail"),
    path("plyerdetails", views.plyerdetails, name="plyerdetails"),
]
