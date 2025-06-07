from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy

from avadocApp.forms import DiscenteForm, AvadocForm, DiarioForm, ComponenteForm, DocenteForm
from . import models
from .models import Discente, Docente, Diario, Curso, Campi, Componente, Nivel, Avadoc
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.core.paginator import Paginator

import sqlite3


# Create your views here.
# página de erro
def pag_sem_prof(request):
    if request.user.is_authenticated:
        return render(request, 'avadoc/pag_sem_prof.html')
    else:
        return render(request, "avadoc/pag_erro.html")


def prof_avaliado(request):
    if request.user.is_authenticated:
        return render(request, 'avadoc/pag_prof_avaliado.html')
    else:
        return render(request, "avadoc/pag_erro.html")


def home(request):
    return render(request, 'avadoc/home.html')

#def logout(request):
 #   return render(request, 'avadoc/home.html')


def pag_sem_ava(request):
    if request.user.is_authenticated:
        return render(request, 'avadoc/pag_sem_ava.html')
    else:
        return render(request, "avadoc/pag_erro.html")


# principal teste
def index_t(request, turma):
    if request.user.is_authenticated:

        # avaliados = Avadoc.objects.all()
        # profs =Docente.objects.all()
        docentes = Diario.objects.all().filter(turma_diario=turma).values()
        form = DiarioForm()
        if request.method == 'POST':
            form = DiarioForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save()
                obj.save()
                form = DiarioForm()

        # discentes = Discente.objects.all()
        if len(docentes) == 0:
            return redirect('pag_sem_prof')
        else:
            return render(request, 'avadoc/index_div_t.html', {'docentes': docentes, 'form': form})
    else:
        return render(request, "avadoc/pag_erro.html")


# principal funcionando
def index(request, turma):

    if request.user.is_authenticated:
        msg = ":"

        avaliados = Avadoc.objects.all()
        profs = Docente.objects.all()

        docentes = Diario.objects.all().filter(turma_diario=turma).values()
        discentes = Discente.objects.all()


        if len(docentes) == 0:
            return redirect('pag_sem_prof')
        else:

            return render(request, 'avadoc/index_div_r.html',
                          {'avaliados': avaliados, 'docentes': docentes, 'discentes': discentes, 'profs': profs, 'msg':msg})

    else:
        return render(request, "avadoc/pag_erro.html")


# páginas de inserção
def new_discente(request):
    if request.user.is_authenticated:
        form = DiscenteForm()

        if request.method == 'POST':
            form = DiscenteForm(request.POST, request.FILES)

            if form.is_valid():
                obj = form.save()
                obj.save()
                form = DiscenteForm()  # Redefine o formulário após o salvamento bem-sucedido

        return render(request, 'avadoc/new_discente.html', {'form': form})

    else:
        return render(request, "avadoc/pag_erro.html")


def new_docente(request):
    if request.user.is_authenticated:
        form = DocenteForm()

        if request.method == 'POST':
            form = DocenteForm(request.POST, request.FILES)

            if form.is_valid():
                obj = form.save()
                obj.save()
                form = DiscenteForm()  # Redefine o formulário após o salvamento bem-sucedido

        return render(request, 'avadoc/new_docente.html', {'form': form})

    else:
        return render(request, "avadoc/pag_erro.html")


# páginas de edição

def editar_discente(request, id):
    aluno = get_object_or_404(Discente, pk=id)
    form = DiscenteForm(instance=aluno)
    alunos = Discente.objects.all()

    if (request.method == "POST"):
        form = DiscenteForm(request.POST, request.FILES, instance=aluno)

        if form.is_valid():
            form.save()
            return redirect('ver_discente')

        else:

            return render(request, "avadoc/editar_discente.html", {'form': form, 'aluno': aluno, 'alunos': alunos})
    else:
        return render(request, "avadoc/editar_discente.html", {'form': form, 'aluno': aluno, 'alunos': alunos})


def editar_docente(request, id):
    docente = get_object_or_404(Docente, pk=id)
    form = DocenteForm(instance=docente)
    docentes = Docente.objects.all()

    if request.method == "POST":
        form = DocenteForm(request.POST, request.FILES, instance=docente)

        if form.is_valid():
            form.save()

            # Add a success message
            messages.success(request, 'Docente editado com sucesso!')

            return redirect('ver_docente')
        else:
            # Add an error message if the form is not valid
            messages.error(request, 'Erro ao editar o docente. Verifique os campos.')

    return render(request, "avadoc/editar_docente.html", {'form': form, 'docente': docente, 'docentes': docentes})



def ver_discente(request):
    if request.user.is_authenticated:

        us = request.user.last_name
        discentes = Discente.objects.all().filter(nome_discente__icontains=us)
        return render(request, 'avadoc/ver_discente.html', {'discentes': discentes})


    else:
        return render(request, "avadoc/pag_erro.html")


# Docente

def ver_docente(request):
    if request.user.is_authenticated:
        docentes = Docente.objects.all()
        return render(request, 'avadoc/ver_docente.html', {'docentes': docentes})
    else:
        return render(request, "avadoc/pag_erro.html")


# campi
def ver_campi(request):
    if request.user.is_authenticated:
        campi = Campi.objects.all()
        return render(request, 'avadoc/ver_campi.html', {'campi': campi})
    else:
        return render(request, "avadoc/pag_erro.html")


# componente
def ver_componente(request):
    if request.user.is_authenticated:
        comp = Componente.objects.all()
        return render(request, 'avadoc/ver_componente.html', {'comp': comp})
    else:
        return render(request, "avadoc/pag_erro.html")


# dirio
def ver_diario(request):
    if request.user.is_authenticated:
        us = request.user.last_name
        diarios = Diario.objects.all()
        return render(request, 'avadoc/ver_diario.html', {'diarios': diarios})
    else:
        return render(request, "avadoc/pag_erro.html")


# curso
def ver_curso(request):
    if request.user.is_authenticated:
        cursos = Curso.objects.all()
        return render(request, 'avadoc/ver_curso.html', {'cursos': cursos})
    else:
        return render(request, "avadoc/pag_erro.html")


# base
def base(request):
    if request.user.is_authenticated:
        return render(request, 'avadoc/base.html')
    else:
        return render(request, "avadoc/pag_erro.html")


# avadoc


def avadoc(request):
    if request.user.is_authenticated:

        formulario = AvadocForm(request.POST)
        if request.method == "POST":
            formulario = AvadocForm(request.POST, request.FILES)
            if formulario.is_valid():
                obj = formulario.save()
                obj.save()
                formulario = AvadocForm()
        return render(request, 'avadoc/avalia_doc.html', {'formulario': formulario})
    else:
        return render(request, "avadoc/pag_erro.html")


def avalia(request, id_docente):
    if request.user.is_authenticated:
        p_ava = Avadoc.objects.all()
        docente = get_object_or_404(Docente, cod_docente=id_docente)
        if p_ava.filter(id_doc=id_docente, user_avadoc=request.user).exists():
            return redirect('prof_avaliado')
        #for p in p_ava:
        #    usu = p.user_avadoc
        #    doc = p.id_doc
         #   if id_docente == doc:
               #return redirect('prof_avaliado')

        # docente = get_object_or_404(Diario, siape_diario=id_docente)

        us = request.user.username
        # form = AvadocForm(instance=docente)
        # if request.method == "POST":
        #  form = AvadocForm(request.POST, request.FILES)
        # if form.is_valid():
        ##     obj = form.save()
        #    obj.save()
        #   return redirect('ver_discente')
        #  else:
        #  return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente, 'us':us, 'p_ava':p_ava})
        # else:
        # return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente})
        # else:
        #    return render(request, "avadoc/pag_erro.html")

        # ...
        form = AvadocForm(instance=docente)
        if request.method == "POST":
            form = AvadocForm(request.POST, request.FILES)
            if form.is_valid():
                # Lógica de processamento quando o formulário é válido
                obj = form.save()
                obj.save()
                return redirect('ver_discente')
            else:
                # Lógica quando o formulário não é válido
                return render(request, 'avadoc/avalia.html',
                              {'form': form, 'docente': docente, 'us': us, 'p_ava': p_ava})
        else:
            # Restante da sua lógica para o método GET
            return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente})
    else:
        return render(request, "avadoc/pag_erro.html")




def avaliaa(request, id_docente):
    if request.user.is_authenticated:
        p_ava = Avadoc.objects.all()
        docente = get_object_or_404(Docente, cod_docente=id_docente)

        # Verifica se o usuário já avaliou o docente
        if p_ava.filter(id_doc=id_docente, user_avadoc=request.user).exists():
            return redirect('prof_avaliado')

        us = request.user.username

        # Lógica para processar o formulário quando o método da requisição é POST
        if request.method == "POST":
            form = AvadocForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user_avadoc = request.user
                obj.id_doc = docente
                obj.save()
                return redirect('ver_discente')
            else:
                return render(request, 'avadoc/avalia.html',
                              {'form': form, 'docente': docente, 'us': us, 'p_ava': p_ava})
        else:
            form = AvadocForm(instance=docente)
            return render(request, 'avadoc/avalia.html', {'form': form, 'docente': docente, 'us': us, 'p_ava': p_ava})
    else:
        return render(request, "avadoc/pag_erro.html")



def ver_avaliaa(request):
    if request.user.is_authenticated:
        # avas =Docente.objects.all().values('id_docente','cod_docente','nome_docente')and Avadoc.objects.all().values('id_docente_id').distinct()
        if request.user.is_superuser:
            avas =Avadoc.objects.all()
            return render(request, 'avadoc/ver_avalia.html', {'avas': avas})
        else:
            avas = Avadoc.objects.all().filter(id_doc=request.user.username)
        if len(avas) == 0:
            return redirect('pag_sem_ava')
        else:
            return render(request, 'avadoc/ver_avalia.html', {'avas': avas})
    else:
        return render(request, "avadoc/pag_erro.html")


def ver_avalia(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            # If the user is a superuser, retrieve all Avadoc objects
            avas = Avadoc.objects.all()
        else:
            # If the user is not a superuser, filter Avadoc objects based on user's id_doc
            avas = Avadoc.objects.filter(id_doc=request.user.username)

        # Check if there are no Avadoc objects for the user
        if not avas.exists():
            return redirect('pag_sem_ava')  # Redirect to the appropriate page when no Avadoc objects are found
        else:
            return render(request, 'avadoc/ver_avalia.html', {'avas': avas})
    else:
        return render(request, "avadoc/pag_erro.html")



# ---------individual-----

def avindividual(request, id_docente):
    if request.user.is_authenticated:
        # avas = Avadoc.objects.all()
        # id_docente = request.GET.get('search')
        avaliados = Docente.objects.all()
        # avas=Docente.objects.filter(avadoc__id_docente=id_docente) #and Avadoc.objects.all().filter(id_docente__cod_docente=id_docente)

        avas = Avadoc.objects.filter(
            id_docente__id_docente=id_docente)  # and Avadoc.objects.all().filter(id_docente__cod_docente=id_docente)

        assiduidade = Avadoc.objects.all().filter(id_docente__id_docente=id_docente)
        if assiduidade == 0:
            return redirect('pag_sem_ava')
        else:

            planejamento = 0
            aulas = 0
            avaliacao = 0
            postura = 0
            assi_total = 0
            pontulidade = 0
            m_assiduidade = 0
            m_planejamento = 0
            m_aulas = 0
            m_avaliacao = 0
            m_postura = 0
            m_pontualidade = 0
            m_geral = 0

            for dado in assiduidade:
                assi_total += int(dado.assid_avadoc)
                pontulidade += int(dado.pont_avadoc)
                planejamento += int(dado.plan_avadoc)
                aulas += int(dado.realiza_avadoc)
                avaliacao += int(dado.avaliacao_avadoc)
                postura += int(dado.postura_avadoc)
                qtd = assi_total.bit_length()

            qt = len(assiduidade)

            m_assiduidade = ((assi_total) / (qt))
            m_pontualidade = ((pontulidade) / (qt))
            m_planejamento = ((planejamento) / (qt))
            m_aulas = ((aulas) / (qt))
            m_avaliacao = ((avaliacao) / (qt))
            m_postura = ((postura) / (qt))
            m_geral = (m_assiduidade + m_pontualidade + m_planejamento + m_aulas + m_avaliacao + m_postura) / 6

            m_consolidada = ((assi_total + pontulidade + planejamento + aulas + avaliacao + postura)/qt)/2

            print(m_assiduidade)
            print(m_geral)

            context = {'avas': avas,
                       'avaliados': avaliados,
                       'assi_total': assi_total,
                       'pontulidade': pontulidade,
                       'planejamento': planejamento,
                       'aulas': aulas,
                       'avaliacao': avaliacao,
                       'postura': postura,
                       'm_assiduidade': m_assiduidade,
                       'm_pontualidade': m_planejamento,
                       'm_planejamento': m_pontualidade,
                       'm_aulas': m_aulas,
                       'm_avaliacao': m_avaliacao,
                       'm_postura': m_postura,
                       'qt': qt,
                       'm_geral': m_geral,
                       'm_consolidada': m_consolidada,
                       }
        return render(request, 'avadoc/ver_avindivual.html', context)
    else:
        return render(request, "avadoc/pag_erro.html")


def new_componente(request):
    if request.user.is_authenticated:
        form = ComponenteForm(request.POST)
        if request.method == 'POST':
            form = ComponenteForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save()
                obj.save()
                form = DiscenteForm()

        return render(request, 'avadoc/new_componente.html', {'form': form})

    return render(request, "avadoc/pag_erro.html")


def filtro_avalia(request):
    if request.user.is_authenticated:
        docentes = Diario.objects.all().filter(Discente.objects.all().filter(turma_discente='turma_diario'))
        for d in docentes:
            f = d.turma_diario
            print(f)

        return render(request, 'avadoc/index.html', {'f': f})
    else:
        return render(request, "avadoc/pag_erro.html")

def media_con(request):
    return render()

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')  # Redirecione para a página inicial ou de login
