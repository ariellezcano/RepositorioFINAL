# Generated by Django 3.0 on 2021-08-17 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('genericos', '0001_initial'),
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='subrubro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='genericos.SubRubro'),
        ),
    ]
