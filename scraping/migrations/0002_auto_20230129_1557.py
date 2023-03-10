# Generated by Django 3.2.16 on 2023-01-29 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Язык программирования')),
                ('slug', models.SlugField(blank=True, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'Язык программирования',
                'verbose_name_plural': 'Языки программирования',
            },
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Населенный пункт', 'verbose_name_plural': 'Населенные пункты'},
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название населенного пункта'),
        ),
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(blank=True, unique=True, verbose_name='slug'),
        ),
    ]
