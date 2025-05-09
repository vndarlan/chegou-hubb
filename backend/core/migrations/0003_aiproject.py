# Generated by Django 5.2 on 2025-04-27 02:23

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_managedcalendar_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome do Projeto')),
                ('creation_date', models.DateField(default=django.utils.timezone.now, verbose_name='Data de Criação')),
                ('finalization_date', models.DateField(blank=True, null=True, verbose_name='Data de Finalização')),
                ('description', models.TextField(blank=True, verbose_name='Descrição Curta')),
                ('status', models.CharField(choices=[('Ativo', 'Ativo'), ('Em Manutenção', 'Em Manutenção'), ('Arquivado', 'Arquivado'), ('Backlog', 'Backlog'), ('Em Construção', 'Em Construção'), ('Período de Validação', 'Período de Validação')], default='Em Construção', max_length=50, verbose_name='Status')),
                ('project_link', models.URLField(blank=True, max_length=500, verbose_name='Link do Projeto')),
                ('tools_used', models.CharField(blank=True, max_length=300, verbose_name='Ferramentas Utilizadas')),
                ('project_version', models.CharField(blank=True, default='v1', max_length=20, verbose_name='Versão do Projeto')),
                ('creator_names', models.CharField(blank=True, help_text='Nomes dos responsáveis pelo projeto, separados por vírgula.', max_length=255, verbose_name='Criador(es) do Projeto (Nomes)')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Adicionado em')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_ai_projects', to=settings.AUTH_USER_MODEL, verbose_name='Criador (Registrado por)')),
            ],
            options={
                'verbose_name': 'Projeto de IA',
                'verbose_name_plural': 'Projetos de IA',
                'ordering': ['-creation_date', 'name'],
            },
        ),
    ]
