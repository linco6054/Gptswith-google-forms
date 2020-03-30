# Generated by Django 3.0.4 on 2020-03-30 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gforms', '0003_auto_20200330_1203'),
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='champions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_date', models.DateField(auto_now_add=True)),
                ('year_won', models.DateField()),
                ('category_won', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='front.category')),
                ('school_won', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gforms.school')),
            ],
        ),
    ]
