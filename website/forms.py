from django import forms
from website.models import Equipamento, Refeicao, Funcionario, Grupo_Refeicao, Visitante, Evento, Parametro



class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'matricula', 'nome', 'admissao', 'departamento', 'centro_de_custo', 'cargo', 'documento', 'credencial', 'grup_ref', 'ativo'
        ]
class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            'matricula', 'nome', 'documento', 'credencial', 'func', 'grup_ref', 'data_inicio', 'hora_inicio', 'data_fim', 'hora_fim'

        ]

# Forms Equipamento
class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = [
            'id_equip','nome', 'ip', 'mask'
        ]

class RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Refeicao
        fields = [
            'id_ref', 'nome', 'valor', 'data_inicio', 'hora_inicio', 'data_fim', 'hora_fim'
        ]


class Grupo_RefeicaoForm(forms.ModelForm):
    class Meta:
        model = Grupo_Refeicao
        fields = [
            'id_grup_ref', 'nome', 'ref'
        ]


class BuscaForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = [
            'matricula', 'nome'
        ]

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = [
            'id_evento', 'matricula', 'nome', 'data', 'hora', 'equip_id', 'equip_nome'
        ]


class ParametroForm(forms.ModelForm):
    class Meta:
        model = Parametro
        fields = [
            'id_param', 'nome', 'mod_padrao_usu', 'mod_credito_usu', 'mod_padrao_visi', 'mod_credito_visi',
        ]

