import datetime
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponseRedirect, Http404, HttpResponse
import datetime
from website.forms import EquipamentoForm, RefeicaoForm, FuncionarioForm, Grupo_RefeicaoForm, VisitanteForm, BuscaForm, EventoForm
from website.models import Equipamento, Refeicao, Funcionario, Grupo_Refeicao, Inter_grup_ref, Visitante, Evento
class HomeViewer(TemplateView):
    template_name = 'website/home/home.html'


status = ''

# Tela de Cadastro de Equipamentos
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
            id = requisicao.POST['id']
            refeicao = Refeicao.objects.get(id=id)
            refeicao = RefeicaoForm(requisicao.POST, instance=refeicao)
            refeicao.save()
            refeicao = Refeicao.objects.all()
            return render(requisicao, template_name='website/home/refeicao/salvo.html',
                              context={'refeicao': refeicao})


        if status == 'excluir':
            print('entrou no excluir ')
            print(f"este é a requisicao.POST = {requisicao.POST}")
            id = requisicao.POST['id']
            id_int = int(id)
            print(f'este é o id = {id_int}')
            refeicao = Refeicao.objects.get(id=id_int)
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

        funcionario = '2'
        grupo_refeicao = '2'

        func = Funcionario.objects.filter(matricula=funcionario)
        grup_ref = Grupo_Refeicao.objects.filter(id_grup_ref=grupo_refeicao)

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
        #completo = Funcionario.objects.all()
        context = {
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

            evento_cafe = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                    .filter(hora__range=('06:00:00', '08:00:00'))

            evento_almoco = Evento.objects.filter(data__range=(data_inicial, data_final)) \
                                    .filter(hora__range=('11:00:00', '13:00:00'))


            refeicao = Refeicao.objects.all()
            #evento = Evento.objects.all()
            context = {
                'evento_cafe': evento_cafe,
                'evento_almoco': evento_almoco,
                'refeicao':refeicao
            }
            return render(requisicao, template_name='website/home/relatorio/refeicoes/resultado.html',
                      context=context)


def tot_func(requisicao: HttpRequest):
    #print(f"este é o GET = {requisicao.method == 'GET'}")
    if requisicao.method == 'GET':
        print('entrou no get relatorio de tot_func')
        form = EventoForm()
        return render(requisicao, template_name='website/home/relatorio/tot_func/tot_func.html', context={'form': form})
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
            nome_v = requisicao.POST['nome']
            data_inicial = requisicao.POST['data_inicio']
            print(f'data inicial {data_inicial}')
            data_final = requisicao.POST.get('data_final')
            print(f' data final {data_final}')

            #evento =  Evento.objects.filter(data__range=(data_inicial, data_final)), (nome__startswith=nome_v) #Evento.objects.filter(nome__istartswith=nome).values(),
            evento = Evento.objects.filter(data__range=(data_inicial, data_final))\
                    .filter(nome__istartswith=(nome_v))\
                    .order_by('data')


            return render(requisicao, template_name='website/home/relatorio/tot_func/resultado.html',
                          context={'evento': evento})




