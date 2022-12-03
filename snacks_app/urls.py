from django.urls import path
from .views import SnackListView,SnackDetail
urlpatterns=[
    path('',SnackListView.as_view(), name='Snacks'),
    path('<int:pk>',SnackDetail.as_view(), name='Detail')

]