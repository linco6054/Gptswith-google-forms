# Generated by Django 3.0.4 on 2020-03-29 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0005_period_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='input_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='period',
            name='modified_date',
            field=models.DateField(),
        ),
    ]
