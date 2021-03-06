# Generated by Django 3.0 on 2022-03-15 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prodname', models.CharField(max_length=50, verbose_name='productName ')),
                ('cetegory', models.CharField(default='', max_length=60, verbose_name='Cetegory')),
                ('subcetegory', models.CharField(default='', max_length=60, verbose_name='Sub_Cetegory')),
                ('price', models.IntegerField(default=0)),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('publish_date', models.DateField(verbose_name='publishDate')),
                ('images', models.ImageField(default='', upload_to='EcommerceApp/images', verbose_name='Images')),
            ],
        ),
    ]
