from django.db import models


class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    cod_docente = models.CharField(max_length=200, blank=True, null=True)
    nome_docente = models.CharField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.nome_docente


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    cod_curso = models.CharField(max_length=200, blank=True, null=True)
    turma_curso = models.CharField(max_length=200, blank=True, null=True)
    nome_curso = models.CharField(max_length=200, blank=True, null=True)
    turno_curso = models.CharField(max_length=200, blank=True, null=True)
    periodo_curso = models.CharField(max_length=200, blank=True, null=True)


class Campi(models.Model):
    id_campi = models.AutoField(primary_key=True)
    cod_campi = models.CharField(max_length=200, blank=True, null=True)
    nome_campi = models.CharField(max_length=200, blank=True, null=True)


class Nivel(models.Model):
    id_nivel = models.AutoField(primary_key=True)
    nome_nivel = models.CharField(max_length=200, blank=True, null=True)


class Periodo(models.Model):
    id_periodo = models.AutoField(primary_key=True)
    ano_periodo = models.CharField(max_length=200, blank=True, null=True)
    semestre_periodo = models.CharField(max_length=200, blank=True, null=True)

class Disciplina(models.Model):
    id_disc = models.AutoField(primary_key=True)
    sigla_disc = models.CharField(max_length=200, blank=True, null=True)
    nome_disc = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_disc


class Discente(models.Model):
    id_discente = models.AutoField(primary_key=True)
    mat_discente = models.CharField(max_length=200, blank=True, null=True)
    nome_discente = models.CharField(max_length=200, blank=True, null=True)
    ingresso_discente = models.CharField(max_length=200, blank=True, null=True)
    campus_discente = models.CharField(max_length=200, blank=True, null=True)
    cidade_discente = models.CharField(max_length=200, blank=True, null=True)
    curso_discente = models.CharField(max_length=200, blank=True, null=True)
    nascimento_discente = models.CharField(max_length=200, blank=True, null=True)
    desc_curso_discente = models.CharField(max_length=200, blank=True, null=True)
    email_discente = models.CharField(max_length=200, blank=True, null=True)
    endereco_discente = models.CharField(max_length=200, blank=True, null=True)
    estado_discente = models.CharField(max_length=200, blank=True, null=True)
    fomr_ing_discente = models.CharField(max_length=200, blank=True, null=True)
    mun_res_discente = models.CharField(max_length=200, blank=True, null=True)
    naturalidade_discente = models.CharField(max_length=200, blank=True, null=True)
    resp_discente = models.CharField(max_length=200, blank=True, null=True)
    sexo_discente = models.CharField(max_length=200, blank=True, null=True)
    status_discente = models.CharField(max_length=200, blank=True, null=True)
    tel_discente = models.CharField(max_length=200, blank=True, null=True)
    origem_discente =models.CharField(max_length=200, blank=True, null=True)
    turma_discente =models.CharField(max_length=200, blank=True, null=True)
    zona_discente =models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nome_discente





class Avadoc(models.Model):
    id_avadoc = models.AutoField(primary_key=True)
    assid_avadoc =models.CharField(max_length=200, blank=True, null=False)
    pont_avadoc =models.CharField(max_length=200, blank=True, null=False)
    plan_avadoc =models.CharField(max_length=200, blank=True, null=False)
    realiza_avadoc =models.CharField(max_length=200, blank=True, null=False)
    avaliacao_avadoc =models.CharField(max_length=200, blank=True, null=False)
    postura_avadoc =models.CharField(max_length=200, blank=True, null=False)
    id_doc= models.CharField(max_length=200, blank=True, null=True)
    user_avadoc= models.CharField(max_length=200, blank=True, null=True)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', blank=True, null=False)



class Componente(models.Model):
    id_comp = models.AutoField(primary_key=True)
    id_disc = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='id_disc', blank=True, null=True)
    id_periodo = models.ForeignKey(Periodo, models.DO_NOTHING, db_column='id_periodo', blank=True, null=True)
    id_curso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_nivel = models.ForeignKey(Nivel, models.DO_NOTHING, db_column='id_nivel', blank=True, null=True)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', blank=True, null=True)
    id_discente = models.ForeignKey(Discente, models.DO_NOTHING, db_column='id_discente', blank=True, null=True)
    id_campi = models.ForeignKey(Campi, models.DO_NOTHING, db_column='id_campi', blank=True, null=True)




class Diario(models.Model):
    id_diario = models.AutoField(primary_key=True)
    cod_diario =models.CharField(max_length=200, blank=True, null=True)
    sigla_diario = models.CharField(max_length=200, blank=True, null=True)
    nome_diario_componente = models.CharField(max_length=200, blank=True, null=True)
    siape_diario = models.CharField(max_length=200, blank=True, null=True)
    nivel_diario = models.CharField(max_length=200, blank=True, null=True)
    docente_diario = models.CharField(max_length=200, blank=True, null=True)
    ch_diario =models.CharField(max_length=200, blank=True, null=True)
    ch_aula_diario =models.CharField(max_length=200, blank=True, null=True)
    cod_curso_diario =models.CharField(max_length=200, blank=True, null=True)
    turma_diario= models.CharField(max_length=200, blank=True, null=True)
    nome_curso_diario = models.CharField(max_length=200, blank=True, null=True)
    turno_curso_diario = models.CharField(max_length=200, blank=True, null=True)
    periodo_diario = models.CharField(max_length=200, blank=True, null=True)
    campus_diario =models.CharField(max_length=200, blank=True, null=True)
    qtd_aluno_diario =models.CharField(max_length=200, blank=True, null=True)
    turma_discente = models.ForeignKey(Discente, models.DO_NOTHING, db_column='turma_discente', blank=True, null=True)


    def __str__(self):
        return self.docente_diario