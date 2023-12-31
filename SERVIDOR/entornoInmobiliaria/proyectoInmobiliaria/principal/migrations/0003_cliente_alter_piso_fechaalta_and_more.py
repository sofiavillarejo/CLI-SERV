# Generated by Django 5.0 on 2023-12-12 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_alter_piso_cp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.IntegerField(max_length=9)),
            ],
        ),
        migrations.AlterField(
            model_name='piso',
            name='fechaAlta',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de alta'),
        ),
        migrations.AlterField(
            model_name='piso',
            name='fechaModificacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de modificacion'),
        ),
    ]
