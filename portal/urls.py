from django.urls import path
from . import views

urlpatterns = [
	# Url para Página Inicial
	path('', views.index, name='index'),

	# Urls Área
	path('area/', views.lista_area, name='lista_area'),
	path('area/<int:pk>', views.detalhes_area, name='detalhes_area'),
	path('area/add', views.adicionar_area, name='adicionar_area'),
	path('area/<int:pk>/editar/', views.alterar_area, name='alterar_area'),
	path('area/<int:pk>/excluir/', views.excluir_area, name='excluir_area'),
	path('area/<int:pk>/ativar/', views.ativar_area, name='ativar_area'),
	path('area/<int:pk>/desativar/', views.desativar_area, name='desativar_area'),

	# Urls Notícia
	path('noticias/', views.lista_noticia, name='lista_noticia'),	
	path('noticia/<int:pk>/', views.detalhes_noticia, name='detalhes_noticia'),	
	path('noticia/add', views.adicionar_noticia, name='adicionar_noticia'),
	path('noticia/<int:pk>/editar/', views.alterar_noticia, name='alterar_noticia'),
	path('noticia/<int:pk>/excluir/', views.excluir_noticia, name='excluir_noticia'),
	path('noticia/<int:pk>/publicar/', views.publicar_noticia, name='publicar_noticia'),
]