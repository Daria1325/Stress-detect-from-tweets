# Generated by Django 3.2.17 on 2023-03-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_employee_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.CharField(choices=[('L', 'Low'), ('M', 'Moderate'), ('H', 'High'), ('N', 'No data')], default='N', max_length=10),
        ),
    ]
