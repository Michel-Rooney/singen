# Generated by Django 4.1 on 2022-10-14 00:23

import cnpj_field.models
import cpf_field.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiasDisponiveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '18'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='DiasSemanaisDisponiveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semanal', models.CharField(choices=[('Seg', 'Segunda'), ('Ter', 'Terça'), ('Qua', 'Quarta'), ('Qui', 'Quinta'), ('Sex', 'Sexta')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='HorariosDisponiveis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarios', models.CharField(choices=[('09', '09:00'), ('10', '10:00'), ('11', '11:00'), ('12', '12:00'), ('13', '13:00'), ('14', '14:00'), ('15', '15:00'), ('16', '16:00')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.CharField(max_length=30)),
                ('mantenedor', models.CharField(choices=[('Mantenedor', 'Mantenedor'), ('Residente Startup', 'Residente Startup'), ('Time Operacional', 'Time Operacional')], max_length=30)),
                ('empresa', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=30)),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('cnpj', cnpj_field.models.CNPJField(max_length=14, verbose_name='CNPJ')),
                ('nome_evento', models.CharField(max_length=300)),
                ('descricao', models.TextField(max_length=1000)),
                ('lista_participantes', models.FileField(blank=True, upload_to='lista_participantes/%Y/%m/%d/')),
                ('espacos', models.CharField(choices=[('Espaço01', 'Espaço01'), ('Espaço02', 'Espaço02'), ('Espaço03', 'Espaço03')], max_length=30)),
                ('data_reserva', models.DateField(default='2022-02-02')),
                ('hora_inicio', models.TimeField(default='22:22')),
                ('hora_fim', models.TimeField(default='23:23')),
            ],
        ),
    ]
