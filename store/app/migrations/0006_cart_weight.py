# Generated by Django 5.1.4 on 2024-12-30 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='weight',
            field=models.ForeignKey(default=1000, on_delete=django.db.models.deletion.CASCADE, to='app.weight'),
            preserve_default=False,
        ),
    ]
