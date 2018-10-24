# Generated by Django 2.1.1 on 2018-10-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0009_auto_20181018_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('DRAFT', 'Draft'), ('PUBLISHED', 'Published')], help_text='\nIndicates whether the event has been published or not. Only published events are\nadvertised to the public. Draft events are only visible to DATA Diary\nadministrators, as a planning aid.\n                  ', max_length=11),
        ),
    ]
