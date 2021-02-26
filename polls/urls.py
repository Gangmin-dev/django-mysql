from django.urls import path
from . import views

app_name = 'polls'
# urlpatterns = [
#     # ex : /polls/
#     path('', views.index, name = 'index'),
#     # ex : /polls/5/
#     # question_id는 view에 있는 parameter인 question_id와 일치해야함
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex : /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex : /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/delete/', views.delete, name='delete'),
    path('create/', views.create, name='create'),
    path('create_process/', views.create_process, name='create_process'),
]