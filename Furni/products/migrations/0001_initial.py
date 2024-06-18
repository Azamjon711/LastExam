# Generated by Django 5.0.6 on 2024-06-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='media/product/')),
                ('price', models.FloatField()),
                ('last_update', models.DateField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
