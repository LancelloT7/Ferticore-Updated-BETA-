# Generated by Django 5.1.1 on 2024-10-20 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_remove_produto_formula'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='formula',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
