# Generated by Django 3.1.2 on 2020-10-09 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
