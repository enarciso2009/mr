from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from website.api import viewsets as eventoviewset
from website.api_func import viewsets as funcionarioviewset
from django.contrib.auth import views as auth_views
from . import views


from website.views import (HomeViewer, cria_equipamento, cria_refeicao, cria_funcionario, cria_grupo_refeicao, cria_visitante, cria_busca, relatorio_refeicoes,
                           monitoramento, tot_func, tot_refeicao, sobre, modelo, MrLoginView, logout_view, MrDashboardView, cria_usuario)


app_name = 'website'

#API

route = routers.DefaultRouter()
route.register(r'website/api', eventoviewset.EventoViewSet, basename="website/api")

route.register(r'website/api_func', funcionarioviewset.FuncViewSet, basename='website/api_func')


# urlpatterns contem a lista de roteamentos de URLs
urlpatterns = [
    #Home
    path('home/', HomeViewer.as_view(), name='home'),

    # login

    path('login/', MrLoginView.as_view(), name='login'),

    path('logout/', logout_view, name='logout'),

    path('home/dashboard/', MrDashboardView.as_view(), name='dashboard'),

    #Equipamento
    path('home/equipamento/', cria_equipamento, name='equipamento'),

    #Refeicao
    path('home/refeicao/', cria_refeicao, name='grupo_refeicao.html'),

    #Funcionario
    path('home/funcionario/', cria_funcionario, name='funcionario.html'),

    #Grupo_Refeicao
    path('home/grupo_refeicao/', cria_grupo_refeicao, name='grupo_refeicao.html'),

    #Visitante
    path('home/visitante/', cria_visitante, name='visitante.html'),

    #Busca
    path('home/busca/', cria_busca, name='busca.html'),

    #Monitoramento
    path('home/relatorio/monitoramento/', monitoramento, name='resultado.html'),

    #Relatorio Refeicoes
    path('home/relatorio/refeicoes/', relatorio_refeicoes, name='refeicoes.html'),

    #Relatorio Tot_func
    path('home/relatorio/tot_func/', tot_func, name='tot_refeicao.html'),

    # Relatorio Totalizado por Refeição
    path('home/relatorio/tot_refeicao/', tot_refeicao, name='tot_refeicao.html'),

    # sobre
    path('home/ajuda/sobre/', sobre, name='sobre.html'),

    # configurações
    path('home/configuracoes/modelos/', modelo, name='modelo.html'),

    #logins
    path('home/configuracoes/logins/', cria_usuario, name='logins.html'),


    #API
    path('', include(route.urls)),
    path('', include(route.urls))

]



