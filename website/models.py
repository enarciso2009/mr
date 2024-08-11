from django.db import models

class Funcionario(models.Model):
    matricula = models.CharField(max_length=15, null=False, blank=False)
    nome = models.CharField(max_length=100, null=True, blank=True)
    admissao = models.DateField(null=True, blank=True)
    departamento = models.CharField(max_length=100, null=True, blank=True)
    centro_de_custo = models.CharField(max_length=100, null=True, blank=True)
    cargo = models.CharField(max_length=50, null=True, blank=True)
    documento = models.CharField(max_length=50, null=True, blank=True)
    credencial = models.CharField(max_length=50, null=True, blank=True)
    grup_ref = models.ForeignKey('Grupo_Refeicao', on_delete=models.CASCADE)
    ativo = models.SlugField(null=True, blank=True)
    object = None
    def __str__(self):
        return f"{self.matricula} {self.nome}"
        #return f"{self.matricula} {self.nome} {self.admissao} {self.departamento} {self.centro_de_custo} {self.cargo} {self.cargo} {self.documento} {self.credencial} {self.grup_ref} {self.ativo}"

class Visitante(models.Model):
    matricula = models.CharField(max_length=100, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    documento = models.CharField(max_length=50, null=True, blank=True)
    credencial = models.CharField(max_length=50, null=True, blank=True)
    func = models.ForeignKey('Funcionario', on_delete=models.CASCADE)
    grup_ref = models.ForeignKey('Grupo_Refeicao', on_delete=models.CASCADE)
    data_inicio = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    object = None
    def __str__(self):
        return f"{self.matricula} {self.nome} {self.documento} {self.credencial} {self.credencial} {self.func} {self.grup_ref} {self.data_inicio} {self.hora_inicio} {self.data_fim} {self.hora_fim}"
class Refeicao(models.Model):
    id_ref = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=100, null=True,blank=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    data_inicio = models.DateField(null=True, blank=True)
    data_fim = models.DateField(null=True, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fim = models.TimeField(null=True, blank=True)
    object = None
    def __str__(self):
        return f"{self.id_ref} {self.valor} {self.nome} {self.hora_inicio} {self.hora_fim}"

class Grupo_Refeicao(models.Model):
    id_grup_ref = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    ref = models.ForeignKey('Refeicao', on_delete=models.CASCADE)
    object = None
    def __str__(self):
        return f"{self.id_grup_ref} {self.nome}"


class Equipamento(models.Model):
    object = None
    id_equip = models.CharField(max_length=100, null=False, blank=False, primary_key=id)
    nome = models.CharField(max_length=100, null=True, blank=True)
    ip = models.CharField(max_length=15, null=True, blank=True)
    mask = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.id_equip} {self.nome}"


class Inter_grup_ref(models.Model):
    object = None
    grup_ref = models.CharField(max_length=10, null=False, blank=False)
    ref = models.CharField(max_length=10, null=False, blank=False)
    def __str__(self):
        return f"{self.grup_ref} {self.ref}"

class Evento(models.Model):
    id_evento = models.CharField(max_length=15, null=False, blank=False)
    matricula = models.CharField(max_length=15, null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    data = models.DateField(null=True, blank=True)
    hora = models.TimeField(null=True, blank=True)
    equip_id = models.CharField(max_length=10, null=True, blank=True)
    equip_nome = models.CharField(max_length=100, null=True, blank=True)
    object = None
    def __str__(self):
        return f'{self.id_evento} {self.matricula} {self.nome} {self.data} {self.hora} {self.equip_id} {self.equip_nome}'

class Usuario(models.Model):
    id_user = models.CharField(max_length=10, null=False, blank=False, primary_key=True)
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    usuario = models.CharField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    permissao = models.CharField(max_length=50, null=True, blank=True)
    object = None

class Parametro(models.Model):
    id_param = models.CharField(max_length=15, null=False, blank=False)
    nome = models.CharField(max_length=100, null=True, blank=True)
    mod_padrao_usu = models.BooleanField(null=True, blank=True)
    mod_credito_usu = models.BooleanField(null=True, blank=True)
    mod_padrao_visi = models.BooleanField(null=True, blank=True)
    mod_credito_visi = models.BooleanField(null=True, blank=True)
    object = None
    def __str__(self):
        return f'{self.id_param} {self.nome} {self.mod_padrao_usu} {self.mod_credito_usu} {self.mod_padrao_visi} {self.mod_credito_visi}'

