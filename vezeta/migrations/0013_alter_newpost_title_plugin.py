# Generated by Django 4.1.3 on 2022-11-23 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vezeta', '0012_newpost_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newpost',
            name='title_plugin',
            field=models.TextField(),
        ),
    ]
