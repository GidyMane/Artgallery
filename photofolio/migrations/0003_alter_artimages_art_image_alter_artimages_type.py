# Generated by Django 4.1.3 on 2022-11-10 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photofolio', '0002_artimages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artimages',
            name='art_image',
            field=models.ImageField(upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='artimages',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
