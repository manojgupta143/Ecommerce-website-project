# Generated by Django 3.0 on 2022-03-22 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sweetvillaApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcetegory',
        ),
    ]
