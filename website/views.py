import datetime
from re import purge
from statistics import pvariance
from xml.dom import NoModificationAllowedErr

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
# validação de usuarios

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse
from django.db.models import Sum, Count, Max, Min

from django.contrib.auth import logout
from django.shortcuts import redirect

import datetime
from website.forms import EquipamentoForm, RefeicaoForm, FuncionarioForm, Grupo_RefeicaoForm, VisitanteForm, BuscaForm, EventoForm, ParametroForm
from website.models import Equipamento, Refeicao, Funcionario, Grupo_Refeicao, Inter_grup_ref, Visitante, Evento, Parametro

# criação de logins

class MrLoginView(LoginView):
    template_name = 'website/login.html'
    success_url = reverse_lazy('home:home')
    redirect_authenticated_user = True

def logout_view(requisicao):
    logout(requisicao)
    return redirect('/login')

class MrDashboardView(TemplateView):
    template_name = '/website/home/home.html'


class HomeViewer(TemplateView):
    template_name = 'website/home/home.html'


status = ''

# Tela de Cadastro de Equipamentos
@login_required
def cria_equipamento(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get equipamento')
        form = EquipamentoForm()
        return render(requisicao, template_name='website/home/equipamento/equipamento.html', context={'form': form})
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        #print(f'este é o botao incluir {requisicao.form.get()}')
        form = EquipamentoForm(requisicao.POST)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')

        if status == 'incluir':
            print('entrou no incluir')
            if form.is_valid():
                equipamento = Equipamento(**form.cleaned_data)
                print(f'este é o form.is_valid = {equipamento}')
                print(f'este é o POST = {requisicao.POST}')
                print(f'este é a separacao do id pelo post = {requisicao.POST}')
                equipamento.save()
                equipamento = Equipamento.objects.all()
                return render(requisicao, template_name='website/home/equipamento/salvo.html',
                              context={'equipamento': equipamento})
                cria_equipamento()

        if status == 'alterar':
            print('entrou no alterar')
            id_equip = requisicao.POST['id_equip']
            equipamento = Equipamento.objects.get(id_equip=id_equip)
            equipamento = EquipamentoForm(requisicao.POST, instance=equipamento)
            equipamento.save()
            equipamento = Equipamento.objects.all()
            return render(requisicao, template_name='website/home/equipamento/salvo.html',
                              context={'equipamento': equipamento})


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            id_equip = requisicao.POST['id_equip']
            id_int = int(id_equip)
            print(f'este é o id = {id_int}')
            equipamento = Equipamento.objects.get(id_equip=id_int)
            print(f'exemplo da apostila {equipamento}')
            equipamento.delete()
            equipamento = Equipamento.objects.all()
            return render(requisicao, template_name='website/home/equipamento/salvo.html',
                          context={'equipamento': equipamento})

        if status == 'consultar':
            print('entrou no consultar')
            equipamento = Equipamento.objects.all()
            return render(requisicao, template_name='website/home/equipamento/salvo.html',
                          context={'equipamento': equipamento})

# Tela de cadastro de Refeições
@login_required
def cria_refeicao(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get refeicao')
        form = RefeicaoForm()
        return render(requisicao, template_name='website/home/refeicao/refeicao.html', context={'form': form})
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        #print(f'este é o botao incluir {requisicao.form.get()}')
        form = RefeicaoForm(requisicao.POST)
        ref = requisicao.POST
        for r in ref.values():
            status = r
        print(f'este é o status =  {status}')

        if status == 'incluir':
            print('entrou no incluir')
            if form.is_valid():
                refeicao = Refeicao(**form.cleaned_data)
                print(f'este é o form.is_valid = {refeicao}')
                print(f'este é o POST = {requisicao.POST}')
                print(f'este é a separacao do id pelo post = {requisicao.POST}')
                refeicao.save()
                refeicao = Refeicao.objects.all()
                return render(requisicao, template_name='website/home/refeicao/salvo.html',
                              context={'refeicao': refeicao})


        if status == 'alterar':
            print('entrou no alterar')
            print(requisicao.POST)
            id_ref = requisicao.POST['id_ref']
            refeicao = Refeicao.objects.get(id_ref=id_ref)
            refeicao = RefeicaoForm(requisicao.POST, instance=refeicao)
            refeicao.save()
            refeicao = Refeicao.objects.all()
            return render(requisicao, template_name='website/home/refeicao/salvo.html',
                              context={'refeicao': refeicao})


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            id_ref = requisicao.POST['id_ref']
            id_int = int(id_ref)
            print(f'este é o id = {id_int}')
            refeicao = Refeicao.objects.get(id_ref=id_int)
            print(f'exemplo da apostila {refeicao}')
            refeicao.delete()
            refeicao = Refeicao.objects.all()
            return render(requisicao, template_name='website/home/refeicao/salvo.html',
                          context={'refeicao': refeicao})

        if status == 'consultar':
            print('entrou no consultar')
            refeicao = Refeicao.objects.all()
            return render(requisicao, template_name='website/home/refeicao/salvo.html',
                          context={'refeicao': refeicao})
# Cadastro de Funcionarios
@login_required
def cria_funcionario(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get funcionarios')
        form = FuncionarioForm()
        return render(requisicao, template_name='website/home/funcionario/funcionario.html', context={'form': form})
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        #print(f'este é o botao incluir {requisicao.form.get()}')
        form = FuncionarioForm(requisicao.POST)
        fun = requisicao.POST
        for f in fun.values():
            status = f
        print(f'este é o status =  {status}')

        if status == 'incluir':
            print('entrou no incluir')
            if form.is_valid():
                funcionario = Funcionario(**form.cleaned_data)
                print(f'este é o form.is_valid = {funcionario}')
                print(f'este é o POST = {requisicao.POST}')
                print(f'este é a separacao do id pelo post = {requisicao.POST}')
                funcionario.save()
                funcionario = Funcionario.objects.all()
                return render(requisicao, template_name='website/home/funcionario/salvo.html',
                              context={'funcionario': funcionario})


        if status == 'alterar':
            print('entrou no alterar')
            matricula = requisicao.POST['matricula']
            funcionario = Funcionario.objects.get(matricula=matricula)
            funcionario = FuncionarioForm(requisicao.POST, instance=funcionario)
            funcionario.save()
            funcionario = Funcionario.objects.all()
            return render(requisicao, template_name='website/home/funcionario/salvo.html',
                              context={'funcionario': funcionario})


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            matricula = requisicao.POST['matricula']
            matricula = int(matricula)
            print(f'este é o id = {matricula}')
            funcionario = Funcionario.objects.get(matricula=matricula)
            print(f'exemplo da apostila {funcionario}')
            funcionario.delete()
            funcionario = Funcionario.objects.all()
            return render(requisicao, template_name='website/home/funcionario/salvo.html',
                          context={'funcionario': funcionario})

        if status == 'consultar':
            print('entrou no consultar')
            funcionario = Funcionario.objects.all()
            return render(requisicao, template_name='website/home/funcionario/salvo.html',
                          context={'funcionario': funcionario})


# Cadastro de Visitantes
@login_required
def cria_visitante(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        print(requisicao.GET)
        print('entrou no get visitante')
        form = VisitanteForm()
        print(f'este é o Get = {requisicao.GET}')
        print(f"este é o get com o funciona = {requisicao.GET.get('funciona')}")
        lista = requisicao.GET
        for l in lista:
            print(l)
        query = requisicao.GET.get('nome')
        grup_ref = requisicao.GET.get('grup_ref')

        print(f'nome = {query}')
        print(f'grupo_refeicao = {grup_ref}')
        func = None
        grup_ref = None
        print(f'este é o func = {func}')
        if query:
            print('entrou no if do get')
            func = Funcionario.objects.filter(nome__istartswhith=query)  # istartswith
            grup_ref = Grupo_Refeicao.objects.filter(nome__istartswhith=grup_ref)
        else:
            print('entrou no else do get')
            print(f"requisição do get {requisicao.GET.get('funciona')}")
            func = Funcionario.objects.all()
        completo = Funcionario.objects.all()
        grupo_refeicao = Grupo_Refeicao.objects.all()
        context = {
            'func': func,
            'grup_ref': grup_ref,
            'form': form,
            'grupo_refeicao': grupo_refeicao,
            'completo': completo
        }
        return render(requisicao, template_name='website/home/visitante/visitante.html', context=context)

    elif requisicao.method == 'POST':
        print('entrou no post')
        form = VisitanteForm()

        matricula= requisicao.POST['matricula']
        nome = requisicao.POST['nome']
        documento = requisicao.POST['documento']
        credencial = requisicao.POST['credencial']
        data_inicio = '2024-05-31'
        hora_inicio = requisicao.POST['hora_inicio']
        data_fim = requisicao.POST['data_fim']
        hora_fim = requisicao.POST['hora_fim']

        funcionario = requisicao.POST['matricula']
        grupo_refeicao = '2'

        func = Funcionario.objects.filter(matricula=funcionario)
        grup_ref = Grupo_Refeicao.objects.filter(id_grup_ref=grupo_refeicao)

        for g in grup_ref:
            print(f'este é o g {g.id_grup_ref}')

        print(f'este é matricula do post= {matricula}')
        print(f'este é nome post= {nome}')
        print(f'este é documento do post= {documento}')
        print(f'este é credencial do post= {credencial}')
        print(f'este é o data inicio do post= {data_inicio}')
        print(f'este é o hora inicio do post= {hora_inicio}')
        print(f'este é o data fim  do post= {data_fim}')
        print(f'este é o hora fim  do post= {hora_fim}')

        print(f'este é o func do post= {func}')
        print(f'este é o grup_ref do post= {grup_ref}')
        visitante = (matricula, nome, documento, credencial, func, grup_ref, data_inicio, hora_inicio, data_fim, hora_fim)
        print(f'este é o form = {visitante}')
        completo = Funcionario.objects.all()
        grupo_comp = Grupo_Refeicao.objects.all()
        context = {
            'completo': completo,
            'grupo_comp': grupo_comp,
            'form': form,
            'funcionario': funcionario,
            'grupo_refeicao': grupo_refeicao
        }
        return render(requisicao, template_name='website/home/visitante/visitante.html', context=context)

        if status == 'incluir':
            print('entrou no incluir')
            if form.is_valid():
                visitante = Visitante(**form.cleaned_data)
                print(f'este é o form.is_valid = {visitante}')
                print(f'este é o POST = {requisicao.POST}')
                print(f'este é a separacao do id pelo post = {requisicao.POST}')
                print(f"este é o func = {requisicao.POST.get('func')}")
                visitante.save()
                visitante = Visitante.objects.all()
                context = {
                    'visitante': visitante
                          }
                return render(requisicao, template_name='website/home/visitante/salvo.html',
                              context=context)


        if status == 'alterar':
            print('entrou no alterar')
            matricula = requisicao.POST['matricula']
            visitante = Visitante.objects.get(matricula=matricula)
            visitante = FuncionarioForm(requisicao.POST, instance=visitante)
            visitante.save()
            visitante = Visitante.objects.all()
            return render(requisicao, template_name='website/home/visitante/salvo.html',
                              context={'visitante': visitante})


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            matricula = requisicao.POST['matricula']
            matricula = int(matricula)
            print(f'este é o id = {matricula}')
            visitante = Visitante.objects.get(matricula=matricula)
            print(f'exemplo da apostila {visitante}')
            visitante.delete()
            visitante = Visitante.objects.all()
            return render(requisicao, template_name='website/home/visitante/salvo.html',
                          context={'visitante': visitante})

        if status == 'consultar':
            print('entrou no consultar')
            visitante = Visitante.objects.all()
            return render(requisicao, template_name='website/home/visitante/salvo.html',
                          context={'visitante': visitante})



# cadastro de Grupo de Refeicao
@login_required
def cria_grupo_refeicao(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get grupo de refeição')
        form = Grupo_RefeicaoForm()
        return render(requisicao, template_name='website/home/grupo_refeicao/grupo_refeicao.html', context={'form': form})
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        #print(f'este é o botao incluir {requisicao.form.get()}')
        form = Grupo_RefeicaoForm(requisicao.POST)
        gru_ref = requisicao.POST
        for gr in gru_ref.values():
            status = gr
        print(f'este é o status =  {status}')

        if status == 'incluir':
            print('entrou no incluir')
            id_grup_ref = requisicao.POST.get('id_grup_ref')
            nome = requisicao.POST.get('nome')
            # ref = requisicao.POST.get('ref')
            print(f'objetos = {id_grup_ref} {nome}')
            print(f'form é valido? {form.is_valid()}')
            if form.is_valid():
                grupo_refeicao = Grupo_Refeicao(**form.cleaned_data)
                print(f'este é o form.is_valid = {grupo_refeicao}')
                print(f'este é o POST = {requisicao.POST}')
                print(f'este é a separacao do id pelo post = {requisicao.POST}')
                id_grup_ref = requisicao.POST.get('id_grup_ref')
                nome = requisicao.POST.get('nome')
                ref= requisicao.POST.get('ref')
                print(f'{id_grup_ref}')
                print(f'{nome}')
                print(f'{ref}')
                list_refeicoes = requisicao.POST.getlist('tipos_refeicao')
                print(f'objetos = {id_grup_ref} = {nome} = {ref} = {list_refeicoes}')
                for l in list_refeicoes:
                    print(f'este é o id = {id_grup_ref}')
                    print(f'este é o i = {l}')
                    print(Refeicao.objects.get(id_ref=l))
                    inter = Inter_grup_ref(grup_ref=id_grup_ref, ref=l)
                    inter.save()
                grupo_refeicao.save()
            grupo_refeicao = Grupo_Refeicao.objects.all()
            refeicao = Refeicao.objects.all()
            print(f'este é o grupo de refeicao {grupo_refeicao}')
            context = {
                'grupo_refeicao': grupo_refeicao,
                'refeicao': refeicao

            }
            return render(requisicao, template_name='website/home/grupo_refeicao/salvocomp.html',
                              context=context)


        if status == 'alterar':
            print('entrou no alterar')
            id_grup_ref = requisicao.POST.get('id_grup_ref')
            nome = requisicao.POST.get('nome')
            ref = requisicao.POST.get('ref')
            print(f'estes são os objetos = {id_grup_ref} {nome} {ref}')
            list_refeicoes = (requisicao.POST.getlist('tipos_refeicao'))
            inter = Inter_grup_ref.objects.filter(grup_ref=id_grup_ref).delete()
            print(f'este é o inter = {inter}')
            print(f'este é o list_refeicoes = {list_refeicoes}')
            for i in list_refeicoes:
                print(f'este é o id_grup_ref = {id_grup_ref}')
                print(f'este é o i = {i}')
                print(f'este é o id_ref {ref}')
                inter = Inter_grup_ref(grup_ref=id_grup_ref, ref=i)
                print(f'este é o inter gravou no banco = {inter}')
                inter.save()
            grupo_refeicao = Grupo_Refeicao.objects.get(id_grup_ref=id_grup_ref)
            grupo_refeicao = Grupo_RefeicaoForm(requisicao.POST, instance=grupo_refeicao)
            grupo_refeicao.save()
            grupo_refeicao = Grupo_Refeicao.objects.all()
            ref1 = Refeicao.objects.all()
            context = {
                'grupo_refeicao': grupo_refeicao,
                #'ref1': ref1
            }
            return render(requisicao, template_name='website/home/grupo_refeicao/salvocomp.html',
                              context=context)


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            id_grup_ref = requisicao.POST['id_grup_ref']
            id_grup_ref = int(id_grup_ref)
            print(f'este é o id = {id_grup_ref}')
            grupo_refeicao = Grupo_Refeicao.objects.get(id_grup_ref=id_grup_ref)
            print(f'exemplo da apostila {grupo_refeicao}')
            grupo_refeicao.delete()
            Inter_grup_ref.objects.filter(grup_ref=id_grup_ref).delete()
            grupo_refeicao = Grupo_Refeicao.objects.all()

            return render(requisicao, template_name='website/home/grupo_refeicao/salvocomp.html',
                          context={'grupo_refeicao': grupo_refeicao})

        if status == 'consultar':
            print('entrou no consultar')
            print(requisicao.POST)
            id_grup_ref = requisicao.POST.get('id_grup_ref')
            print(f'este é o id {id_grup_ref}')
            grupo_refeicao = Grupo_Refeicao.objects.filter(id_grup_ref=id_grup_ref)
            inter = Inter_grup_ref.objects.filter(grup_ref=id_grup_ref)
            refeicao = Refeicao.objects.all()
            var = []
            ref = []
            ref1 = []
            refe = []
            for i in inter:
                print(f'este é o i {i.ref}')
                var.append(i.ref)
            print(f'este é o var = {var}')
            for r in var:
                ref.append(Refeicao.objects.filter(id_ref=r))
            for i in ref:
                print(f'este é o correto = {i[0]}')
                ref1.append(i[0])
            for x in ref1:
                print(x)
            print(f'este é o ref = {ref}')
            print(type(ref))
            print(f'este é o ref1 = {ref1}')
            print(f'este é o refe = {refe}')
            print(f'este é o var = {var}')
            print(f'este é o inter = {inter}')
            print(f'este é o grupo_refeicao = {grupo_refeicao}')
            print(f'este é o refeicao = {refeicao}')
            context = {
                'grupo_refeicao': grupo_refeicao,
                'ref1': ref1
            }
            return render(requisicao, template_name='website/home/grupo_refeicao/salvo.html',
                          context=context)

@login_required
def cria_busca(requisicao: HttpRequest):
    # print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get busca')
        form = BuscaForm()
        return render(requisicao, template_name='website/home/busca/busca.html',
                      context={'form': form})

    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        # print(f'este é o botao incluir {requisicao.form.get()}')
        form = BuscaForm(requisicao.POST)
        print(form)


# Relatorios

# monitoramento
@login_required
def monitoramento(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get monitoramento')
        form = EventoForm()
        import datetime
        data_atual = datetime.date.today()
        print(data_atual)
        evento = Evento.objects.filter(data=(data_atual))
        context = {
            'form': form,
            'evento': evento
        }
        return render(requisicao, template_name='website/home/relatorio/monitoramento/resultado.html', context=context)


# Relatorio de Refeições
@login_required
def relatorio_refeicoes(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get relatorio de refeicoes')
        form = EventoForm()
        return render(requisicao, template_name='website/home/relatorio/refeicoes/refeicoes.html', context={'form': form})
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        #print(f'este é o botao incluir {requisicao.form.get()}')
        form = EventoForm(requisicao.POST)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')


        if status == 'consultar':
            print('entrou no consultar')
            print(f'este é o post {requisicao.POST}')
            data_inicial = requisicao.POST['data_inicio']
            print(f'data inicial {data_inicial}')
            data_final = requisicao.POST.get('data_final')
            print(f' data final {data_final}')
            id = Refeicao.objects.values_list('id_ref', flat=True)
            hora_i = Refeicao.objects.values_list('hora_inicio', flat=True)
            hora_f = Refeicao.objects.values_list('hora_fim', flat=True)
            print(f'dados de refeicao = {id, hora_i, hora_f}')
            tabela_total = Refeicao.objects.all()
            print(f'total = {tabela_total}')
            horas = []
            for tab in tabela_total:
                print('Este é o for do tab')
                id = tab.id_ref
                print(id)
                hi = tab.hora_inicio
                print(hi)
                hf = tab.hora_fim
                print(hf)
                horas += id, hi, hf
                tipo_ref = tab.nome
                valor = tab.valor
                print(f'estes são nomes e valores de refeicao = {tipo_ref}, {valor}')

            idr = horas[0]
            refrr = []
            refeicao_1 = Refeicao.objects.filter(id_ref=idr)
            for refr in refeicao_1:
                ref_nome_1 = refr.nome
                ref_valor_1 = str(refr.valor)
                refrr += ref_nome_1, ref_valor_1

            evento_cafe= Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                    .filter(hora__range=(horas[1], horas[2])) \
                                    .order_by('data')

            idr = horas[3]
            refrr = []
            refeicao_3 = Refeicao.objects.filter(id_ref=idr)
            for refr in refeicao_3:
                ref_nome_3 = refr.nome
                ref_valor_3 = str(refr.valor)
                refrr += ref_nome_3, ref_valor_3

            evento_almoco = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                   .filter(hora__range=(horas[4], horas[5])) \
                                   .order_by('data')

            idr = horas[6]
            refrr = []
            refeicao_6 = Refeicao.objects.filter(id_ref=idr)
            for refr in refeicao_6:
                ref_nome_6 = refr.nome
                ref_valor_6 = str(refr.valor)
                refrr += ref_nome_6, ref_valor_6

            evento_cafe_tarde = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                  .filter(hora__range=(horas[7], horas[8])) \
                                  .order_by('data')

            idr = horas[9]
            refrr = []
            refeicao_9 = Refeicao.objects.filter(id_ref=idr)
            for refr in refeicao_9:
                ref_nome_9 = refr.nome
                ref_valor_9 = str(refr.valor)
                refrr += ref_nome_9, ref_valor_9

            evento_jantar = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                  .filter(hora__range=(horas[10], horas[11])) \
                                  .order_by('data')

            idr = horas[12]
            refrr = []
            refeicao_12 = Refeicao.objects.filter(id_ref=idr)
            for refr in refeicao_12:
                ref_nome_12 = refr.nome
                ref_valor_12 = str(refr.valor)
                refrr += ref_nome_12, ref_valor_12


            evento_ceia = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                  .filter(hora__range=(horas[13], horas[14])) \
                                  .order_by('data')


            context = {

                
                'evento_almoco': evento_almoco,
                'evento_cafe': evento_cafe,
                'evento_cafe_tarde': evento_cafe_tarde,
                'evento_jantar': evento_jantar,
                'evento_ceia': evento_ceia,
                'ref_nome_1': ref_nome_1,
                'ref_valor_1': ref_valor_1,
                'ref_nome_3': ref_nome_3,
                'ref_valor_3': ref_valor_3,
                'ref_nome_6': ref_nome_6,
                'ref_valor_6': ref_valor_6,
                'ref_nome_9': ref_nome_9,
                'ref_valor_9': ref_valor_9,
                'ref_nome_12': ref_nome_12,
                'ref_valor_12': ref_valor_12
            }
            return render(requisicao, template_name='website/home/relatorio/refeicoes/resultado.html',
                      context=context)

# Relatorio refeições totalizado por funcionario
@login_required
def tot_func(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get relatorio de tot_func')
        form = EventoForm()
        query = requisicao.GET.get('func')
        print(f'nome = {query}')

        print(f'este é o func = {query}')
        if query:
            print('entrou no if da query')
            func = Funcionario.objects.filter(nome__istartswhith=query)
        else:
            print('entrou no else do get')
            func = Funcionario.objects.all()
        completo = Funcionario.objects.all()

        context = {
            'func': func,
            'form': form,
            'completo': completo
        }
        return render(requisicao, template_name='website/home/relatorio/tot_func/tot_func.html', context=context)
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        func = requisicao.POST.get('func')
        print(f'este é o func {func}')
        form = EventoForm(requisicao.POST)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')


        if status == 'consultar':
            print('entrou no consultar')
            print(f'este é o post consulta {requisicao.POST}')
            data_inicial = requisicao.POST['data_inicio']
            print(f'data inicial {data_inicial}')
            data_final = requisicao.POST.get('data_final')
            print(f' data final {data_final}')
            funcionario = requisicao.POST.get('func')
            print(f'funcionario = {funcionario}')
            tabela_total = Refeicao.objects.all()
            print(f'tabela total = {tabela_total}')
            refeicoes = Refeicao.objects.aggregate(Count('id_ref'))
            tot_ref = refeicoes["id_ref__count"]

            eventos = []
            horas = []
            tot = []
            total_eventos = []
            n = 0

            while n != tot_ref:

                for tab in tabela_total:
                    print('Este é o for do tab')
                    id = tab.id_ref
                    print(id)
                    hi = tab.hora_inicio
                    print(hi)
                    hf = tab.hora_fim
                    print(hf)
                    horas += id, hi, hf
                    tipo_ref = tab.nome
                    valor = tab.valor
                    print(f'estes são nomes e valores de refeicao = {tipo_ref}, {valor}')

                    # pega todas as refeicoes
                    idr = id
                    refrr = []
                    refeicao_12 = Refeicao.objects.filter(id_ref=idr)
                    for refr in refeicao_12:
                        ref_nome_12 = refr.nome
                        ref_valor_12 = str(refr.valor)
                        ref_hi = refr.hora_inicio
                        ref_hf = refr.hora_fim
                        refrr += ref_nome_12, ref_valor_12, ref_hi, ref_hf
                        print(f'este é o refrr = {refrr}')
                        print(f'este é o horario = {ref_hi} {ref_hf}')
                        evento = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                            .filter(nome__startswith=funcionario) \
                            .filter(hora__range=(ref_hi, ref_hf))


                        eventos += evento
                        som_eventos = eventos, tipo_ref, valor
                        print(f'este é o evento {evento}')
                        total = len(evento)
                        print(f'total de eventos = {total}')
                        tot_t = total * float(ref_valor_12)


                        total_eventos.append((funcionario, ref_nome_12, f'{str(total)}', ref_valor_12, f'{tot_t:.2f}'))


                    n += 1

            #total geral


            eve_0 = total_eventos[0]
            eve_1 = total_eventos[1]
            eve_2 = total_eventos[2]
            eve_3 = total_eventos[3]
            eve_4 = total_eventos[4]

            total_geral = float(eve_0[4]) + float(eve_1[4]) + float(eve_2[4]) + float(eve_3[4]) + float(eve_4[4])
            tot_geral = (f'{total_geral:.2f}')
            context = {
                'funcionario': funcionario,
                'eve_0': eve_0,
                'eve_1': eve_1,
                'eve_2': eve_2,
                'eve_3': eve_3,
                'eve_4': eve_4,
                'tot_geral': tot_geral


                }
            return render(requisicao, template_name='website/home/relatorio/tot_func/resultado.html',
                              context=context)


        return render(requisicao, template_name='website/home/relatorio/tot_func/semdados.html')


# Relatorios Refeições Totalizadas
@login_required
def tot_refeicao(requisicao: HttpRequest):
    print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get relatorio de tot_refeicoes')
        return render(requisicao, template_name='website/home/relatorio/tot_refeicao/tot_refeicao.html')
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        form = EventoForm(requisicao.POST)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')

        if status == 'consultar':
            print('entrou no consultar')
            print(f'este é o post consulta {requisicao.POST}')
            data_inicial = requisicao.POST['data_inicio']
            print(f'data inicial {data_inicial}')
            data_final = requisicao.POST.get('data_final')
            print(f' data final {data_final}')
            tabela_total = Refeicao.objects.all()
            print(f'tabela total = {tabela_total}')
            refeicoes = Refeicao.objects.aggregate(Count('id_ref'))
            tot_ref = refeicoes["id_ref__count"]

            n = 0
            eventos = []
            horas = []
            total_eventos = []

            while n != tot_ref:

                for tab in tabela_total:
                    print('Este é o for do tab')
                    id = tab.id_ref
                    print(id)
                    hi = tab.hora_inicio
                    print(hi)
                    hf = tab.hora_fim
                    print(hf)
                    horas += id, hi, hf
                    tipo_ref = tab.nome
                    valor = tab.valor
                    print(f'estes são nomes e valores de refeicao = {tipo_ref}, {valor}')

                    # pega todas as refeicoes
                    idr = id
                    refrr = []
                    refeicao_12 = Refeicao.objects.filter(id_ref=idr)
                    for refr in refeicao_12:
                        ref_nome_12 = refr.nome
                        ref_valor_12 = str(refr.valor)
                        ref_hi = refr.hora_inicio
                        ref_hf = refr.hora_fim
                        refrr += ref_nome_12, ref_valor_12, ref_hi, ref_hf
                        print(f'este é o refrr = {refrr}')
                        print(f'este é o horario = {ref_hi} {ref_hf}')
                        evento = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                            .filter(hora__range=(ref_hi, ref_hf))

                        eventos += evento
                        som_eventos = eventos, tipo_ref, valor
                        print(f'este é o evento {evento}')
                        total = len(evento)
                        print(f'total de eventos = {total}')
                        tot_t = total * float(ref_valor_12)

                        total_eventos.append((ref_nome_12, f'{str(total)}', ref_valor_12, f'{tot_t:.2f}'))

                    n += 1

            print(f'este é o total eventos {total_eventos}')
            eve_0 = total_eventos[0]
            eve_1 = total_eventos[1]
            eve_2 = total_eventos[2]
            eve_3 = total_eventos[3]
            eve_4 = total_eventos[4]

            total_geral = float(eve_0[3]) + float(eve_1[3]) + float(eve_2[3]) + float(eve_3[3]) + float(eve_4[3])
            tot_geral = (f'{total_geral:.2f}')

            context= {
                'eve_0': eve_0,
                'eve_1': eve_1,
                'eve_2': eve_2,
                'eve_3': eve_3,
                'eve_4': eve_4,
                'tot_geral': tot_geral

            }

            return render(requisicao, template_name='website/home/relatorio/tot_refeicao/resultado.html',
                          context=context)

# Sobre
@login_required
def sobre(requisicao: HttpRequest):
    print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print(f'entrou no if do get')
        return render(requisicao, template_name='website/home/ajuda/sobre/sobre.html')

# Configurações


# Modelo de Refeições
@login_required
def modelo(requisicao: HttpRequest):
    print(f"este é o Get do Modelo = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print(f'entrou no if do get')
        return render(requisicao, template_name='website/home/configuracoes/modelos/modelo.html')

    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        form = ParametroForm(requisicao.POST)

        print(form)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')


        if status == 'incluir':
            print('entrou no incluir')
            print(f'este é o post incluir {requisicao.POST}')

            if form.is_valid():
                print(f'entrou no form.is_valid()')

                padrao_usu = form.cleaned_data.get('mod_padrao_usu', False)
                padrao_visi = form.cleaned_data.get('mod_padrao_visi', False)
                credito_usu = form.cleaned_data.get('mod_credito_usu', False)
                credito_visi = form.cleaned_data.get('mod_credito_usu', False)
                id_param = requisicao.POST['id_param']
                nome = requisicao.POST['nome']

                print(f'estes sao os campos acima = {id_param, nome, padrao_usu, padrao_visi, credito_usu, credito_visi}')



                parametro = Parametro(id_param, id_param, nome, padrao_usu, padrao_visi, credito_usu, credito_visi)
                parametro.save()
                parametro = Parametro.objects.all()

                print(f'este é o parametro = {parametro}')
                context = {
                    'parametro': parametro

                }

                return render(requisicao, template_name='website/home/configuracoes/modelos/salvo.html', context=context)


@login_required
def cria_usuario(requisicao: HttpRequest):
    if requisicao.method == 'GET':
        print(f'entrou no if do get usuario')

        return render(requisicao, template_name='website/home/configuracoes/logins/logins.html')
    # Verifique se a requisição é POST
    elif requisicao.method == 'POST':
        print('entrou no post')
        print(f'este é o post = {requisicao.method == "POST"}')
        form = ParametroForm(requisicao.POST)
        req = requisicao.POST
        for r in req.values():
            status = r
        print(f'este é o status =  {status}')

        if status == 'incluir':
            username = requisicao.POST['username']
            password = requisicao.POST['password']
            email = requisicao.POST.get('email', '')

            # Crie o usuário
            user = User.objects.create_user(username=username, password=password, email=email)

            # Adicione informações adicionais
            user.first_name = requisicao.POST.get('first_name', '')
            user.last_name = requisicao.POST.get('last_name', '')
            user.save()

            logins = User.objects.all()

            context = {
                'logins': logins
            }

            return render(requisicao, template_name='website/home/configuracoes/logins/salvo.html', context=context)

        if status == 'alterar':
            print('entrou no alterar')
            username = requisicao.POST['username']
            nova_senha = requisicao.POST['password']
            user = User.objects.get(username=username)
            user.set_password(nova_senha)
            user.save()


            logins = User.objects.all()

            context = {
                'logins': logins
            }

            return render(requisicao, template_name='website/home/configuracoes/logins/alterado.html', context=context)

        if status == 'excluir':
            print('entrou no excluir')
            username = requisicao.POST['username']
            user = User.objects.get(username=username)
            user.delete()


            logins = User.objects.all()
            context = {
                'logins': logins
            }

            return render(requisicao, template_name='website/home/configuracoes/logins/excluido.html', context=context)

        if status == 'consultar':
            print('entrou no consultar')

            logins = User.objects.all()
            context = {
                'logins': logins
            }

            return render(requisicao, template_name='website/home/configuracoes/logins/salvo.html', context=context)




