# Generated by Django 4.1.3 on 2022-12-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='imgs/Default.jpg', upload_to='imgs'),
        ),
    ]