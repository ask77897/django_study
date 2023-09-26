# Generated by Django 4.2.5 on 2023-09-19 07:16

from django.db import migrations

def create_initial_data(apps, schema_editer):
    NewModel = apps.get_model('newapp', 'NewModel')
    NewModel.objects.create(name='park', skill='django')
    NewModel.objects.create(name='lee', skill='react')
    
    NewModel.objects.create(name='lee', skill='react')
    NewModel.objects.create(name='lee', skill='react')
    
class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_auto_20230919_1555'),
    ]

    operations = [
        migrations.RunPython(create_initial_data)
    ]
