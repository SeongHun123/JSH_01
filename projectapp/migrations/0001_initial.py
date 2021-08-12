# Generated by Django 3.2.4 on 2021-08-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='project/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
