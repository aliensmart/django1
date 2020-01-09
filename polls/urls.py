from django.urls import path
from . import views

urlpatterns = [
    # ex: /pools/
    path('', views.index, name='index')
     # ex: /pools/5/
    path('/<int:question_id>/', views.index, name='detail')
    # ex: /pools/5/result/
    path('/<int:question_id>/result/', views.index, name='result')
    # ex: /pools/5/vote/
    path('/<int:question_id>/vote/', views.index, name='vote')
    
]