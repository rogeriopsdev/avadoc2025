"""
URL configuration for avadoc project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from avadocApp.views import new_discente, ver_discente, ver_docente, ver_diario, ver_campi, ver_curso,ver_componente, base
from avadocApp.views import avadoc, avalia,ver_avalia,avindividual, index, new_componente,home, pag_sem_ava,pag_sem_prof, prof_avaliado,new_docente
from avadocApp.views import editar_discente, editar_docente
from django.urls import path
from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new_discente/', new_discente, name='new_discente'),
    path('new_docente/', new_docente, name='new_docente'),
    path('editar_discente/<str:id>', editar_discente, name='editar_discente '),
    path('editar_docente/<int:id>', editar_docente, name='editar_docente'),
    path('', home, name='home'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/<str:turma>', index, name='index'),
    path('ver_discente/', ver_discente, name='ver_discente'),
    path('ver_docente/', ver_docente, name='ver_docente'),
    #path('ver_docente/', ver_docente, name='ver_docente'),
    path('ver_diario/', ver_diario, name='ver_diario'),
    path('ver_campi/', ver_campi, name='ver_campi'),
    path('ver_curso/', ver_curso, name='ver_curso'),
    path('ver_componente/', ver_componente, name='ver_componente'),
    path('avadoc/', avadoc, name='avadoc'),
    #path('avalia/<int:id_docente>', avalia, name='avalia'),
    path('avalia/<str:id_docente>', avalia, name='avalia'),
    path('avindividual/<int:id_docente>', avindividual, name='avindividual'),
    path('avindividual/', avindividual, name='avindividual'),
    #re_path(r'^avindividual/(?P<id_docente>\d+)$', avindividual, name='avindividual'),
    path('base/', base, name='base'),
    path('ver_avalia/', ver_avalia, name='ver_avalia'),
    path('new_componente/', new_componente, name='new_componente'),
    path('pag_sem_ava/', pag_sem_ava, name='pag_sem_ava'),
    path('pag_sem_prof/', pag_sem_prof, name='pag_sem_prof'),
    path('prof_avaliado/', prof_avaliado, name='prof_avaliado'),
    path('', include('usuarios.urls')),

    #path('ver_avalia/<int:id_docente>', ver_avalia, name='ver_avalia'),
]
