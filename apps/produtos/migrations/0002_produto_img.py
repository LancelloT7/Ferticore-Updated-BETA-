# Generated by Django 5.1.5 on 2025-01-17 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='img',
            field=models.ImageField(default=0, upload_to='produtos/'),
            preserve_default=False,
        ),
    ]
