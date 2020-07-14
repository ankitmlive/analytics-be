from django.urls import include, path
from . import views

urlpatterns = [

    #objectives
    path('objectives/', views.ObjectiveAPIView.as_view(), name='all-objective'),
    path('objectives/create/', views.ObjectiveCreateAPIView.as_view(), name='add-objective'),
    path('objectives/<int:pk>/', views.ObjectiveDetailAPIView.as_view(), name='objective-detail'),

    #keyresults
    path('key/create/', views.KeyCreateAPIView.as_view(), name='add-key'),
    path('key/<int:pk>/', views.KeyDetailAPIView.as_view(), name='key-detail'),

]