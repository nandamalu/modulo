from django.urls import path

from main.models import Aluno
from . import views
from .views import AlunoCreateView, AlunoUpdateView

urlpatterns = [
    path('', views.alunoView, name='aluno-lista'),


    path('alunoID/<int:id>', views.alunoIDview, name='aluno-detalhe'),


path('aluno/create/', AlunoCreateView.as_view(), name='aluno-create'),
path('aluno/<int:pk>/update/', AlunoUpdateView.as_view(), name='aluno-update'),
]