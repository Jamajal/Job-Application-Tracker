# Generated by Django 5.0.3 on 2024-03-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=50)),
                ('local', models.CharField(max_length=70)),
                ('modality', models.CharField(max_length=10)),
                ('link', models.CharField(blank=True, max_length=300, null=True)),
                ('observation', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
