# Generated by Django 2.1.1 on 2018-10-04 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0003_auto_20180924_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='mailchimp_image',
            field=models.URLField(blank=True, help_text="\nThe full URL of the image for the news item that's been uploaded to the\nMailchimp content manager. This is so that it can be included in Mailchimp\nmailshots.\n                  "),
        ),
    ]
