from django.urls import path
from aladin import views
from .views import base_views

urlpatterns = [
    # path('', views.main, name='main'),
    # base_views.py
    path('',base_views.main, name='main'),
    # path('<int:question_id>/',
    #      base_views.detail, name='detail'),

    # question_views.py
    # path('',
    #      recommend_views.question_create, name='question_create'),
    # path('',
    #      recommend_views.question_modify, name='question_modify'),
    # path('',
    #      recommend_views.question_delete, name='question_delete'),

    path('detailbook/<str:id>/', base_views.Detailbook.as_view(), name='detailbook'),
    path('detailbook/', base_views.Detailbook.as_view(), name='detailbook'),
    path('search/', base_views.Search.as_view(), name='search'),
    path('change/', base_views.change, name='change')
]