# Generated by Django 3.1.5 on 2021-01-05 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Icecream',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Мороженное',
                'verbose_name_plural': 'Мороженное',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Слоган')),
                ('description', models.TextField(verbose_name='Описание')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('name', models.ManyToManyField(related_name='name_icecream', to='company.Icecream', verbose_name='Мороженое')),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
            },
        ),
    ]
