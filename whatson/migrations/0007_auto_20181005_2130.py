# Generated by Django 2.1.1 on 2018-10-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0006_auto_20181005_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(blank=True, help_text='\nA datetime that can be set to limit the time that certain options are available;\nfor example to restrict a password reset to within a day following the time that\nthe password reset link was requested.\n                  ', null=True),
        ),
    ]
