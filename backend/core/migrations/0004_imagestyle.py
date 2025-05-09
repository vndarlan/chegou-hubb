# Generated by Django 5.2 on 2025-04-28 01:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_aiproject'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageStyle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Um nome curto e descritivo para o estilo (Ex: Anúncio Luxo, Desenho Animado).', max_length=100, unique=True, verbose_name='Nome do Estilo')),
                ('instructions', models.TextField(help_text='Instruções detalhadas que serão pré-anexadas ao prompt do usuário para guiar a IA.', verbose_name='Instruções do Estilo')),
                ('added_at', models.DateTimeField(auto_now_add=True, verbose_name='Adicionado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_image_styles', to=settings.AUTH_USER_MODEL, verbose_name='Criador (Registrado por)')),
            ],
            options={
                'verbose_name': 'Estilo de Imagem',
                'verbose_name_plural': 'Estilos de Imagem',
                'ordering': ['name'],
            },
        ),
    ]
