from django.urls import include, path
from . import views

urlpatterns = [
    # team
    path('', views.TeamAPIView.as_view(), name='all-teams'),
    path('create/', views.TeamCreateAPIView.as_view(), name='add-team'),

    #add employee to team
    path('add-member/', views.AddMemberAPIView.as_view(), name='add-member'),
]