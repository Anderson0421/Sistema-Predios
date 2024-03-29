# Generated by Django 4.2.5 on 2023-10-03 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0010_alter_profile_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuc', models.CharField(max_length=50, unique=True)),
                ('cod_ref_catastral', models.CharField(max_length=13)),
                ('departamento', models.CharField(max_length=50)),
                ('provincia', models.CharField(max_length=50)),
                ('distrito', models.CharField(max_length=50)),
                ('sector', models.CharField(max_length=50)),
                ('manzana', models.CharField(max_length=50)),
                ('lote', models.CharField(max_length=50)),
                ('propietario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='userauths.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Deuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deuda', models.BooleanField()),
                ('monto_deuda', models.PositiveIntegerField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('fecha_edit', models.DateTimeField(auto_now=True)),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('cancelado', 'Cancelado'), ('vencido', 'vencido')], default='pendiente', max_length=20)),
                ('contribuyente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauths.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Construccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_piso', models.PositiveIntegerField()),
                ('material_estructural_predominante', models.CharField(max_length=50)),
                ('estado_conservacion', models.CharField(max_length=50)),
                ('estado_construccion', models.CharField(max_length=50)),
                ('predio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauths.predio')),
            ],
        ),
    ]
