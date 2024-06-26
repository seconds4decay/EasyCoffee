# Generated by Django 5.0.4 on 2024-04-24 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_cafe_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafe',
            name='aroma',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cafe',
            name='intensidade',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cafe',
            name='tamanho',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cafe',
            name='foto',
            field=models.ImageField(upload_to='cafes/'),
        ),
    ]
