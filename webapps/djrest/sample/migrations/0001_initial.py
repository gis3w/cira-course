# Generated by Django 3.1.3 on 2020-11-13 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Sample name')),
                ('a_value', models.FloatField(verbose_name='Value A')),
                ('b_value', models.FloatField(blank=True, null=True, verbose_name='Value B')),
                ('c_value', models.BooleanField(default=False, verbose_name='Value boolean c')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Comment')),
            ],
        ),
    ]
