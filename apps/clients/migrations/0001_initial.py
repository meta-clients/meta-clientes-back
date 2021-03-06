# Generated by Django 4.0.3 on 2022-03-23 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clients.basemodel')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('phone', models.CharField(max_length=13, verbose_name='celular')),
                ('birthdate', models.DateField()),
                ('has_child', models.BooleanField(default=False)),
                ('number_of_children', models.IntegerField(default=0)),
            ],
            bases=('clients.basemodel',),
        ),
        migrations.CreateModel(
            name='ChildrenModel',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clients.basemodel')),
                ('gender', models.CharField(max_length=9)),
                ('clother_size', models.CharField(max_length=4)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children_id', to='clients.clientmodel')),
            ],
            bases=('clients.basemodel',),
        ),
    ]
