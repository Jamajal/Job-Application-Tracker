# Generated by Django 5.0.3 on 2024-03-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='observation',
            field=models.TextField(null=True),
        ),
    ]