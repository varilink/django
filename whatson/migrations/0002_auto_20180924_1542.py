# Generated by Django 2.1.1 on 2018-09-24 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='subscriber',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=0, help_text='\nWhether or not the person is subscribed to receive the monthly DATA Diary email.\n                  '),
        ),
        migrations.AlterField(
            model_name='personinorganisation',
            name='organisation_rowid',
            field=models.ForeignKey(db_column='organisation_rowid', on_delete=django.db.models.deletion.PROTECT, to='whatson.Organisation', verbose_name='Organisation'),
        ),
        migrations.AlterField(
            model_name='personinorganisation',
            name='role',
            field=models.CharField(blank=True, help_text='\nThe role that the person has in the organisation; for example "Treasurer" of a\nDATA member society.\n                  ', max_length=20, null=True),
        ),
    ]
