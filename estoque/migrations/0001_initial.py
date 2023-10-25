# Generated by Django 4.2.6 on 2023-10-25 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('dataDeUltimaCompra', models.DateField()),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PratoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.prato')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
        migrations.AddField(
            model_name='prato',
            name='produtos',
            field=models.ManyToManyField(to='estoque.produto'),
        ),
    ]