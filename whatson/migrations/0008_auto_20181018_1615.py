# Generated by Django 2.1.1 on 2018-10-18 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whatson', '0007_auto_20181005_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaHandle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('handle', models.URLField(help_text="\nThe handle, e.g. '@AllestreeAmDram'. These can be entered with or without the\n@ prefix.\n        ")),
            ],
            options={
                'db_table': 'whatson_social_media_handle',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SocialMediaPlatform',
            fields=[
                ('name', models.CharField(help_text='\nThe name of the social media platform, e.g. Facebook", "Twitter", etc.\n                  ', max_length=10, primary_key=True, serialize=False, unique=True)),
                ('icon', models.CharField(help_text='\nThe name of the font-awesome icon that we use to represent this social media\nplatform.\n        ', max_length=10)),
            ],
            options={
                'db_table': 'whatson_social_media_platform',
                'managed': True,
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='box_office',
            field=models.CharField(blank=True, help_text='\nEnter the contact details for Box Office enquiries for the event; for example:\n<br />\n"01332 593939"<br />\n"01773 829248 - Free"<br />\n"Derby Live Box Office - 01332 255800"\n                  ', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='card',
            field=models.IntegerField(choices=[(2, 'Yes (without image)'), (1, 'Yes (with image)'), (0, 'No')], db_column='use_desc', help_text='\nIndicates whether the event has a custom card associated with it and (if it\ndoes) whether that custom card is associated with an image or not.\n                  ', verbose_name='Custom card and image choice'),
        ),
        migrations.AlterField(
            model_name='event',
            name='dates',
            field=models.CharField(blank=True, help_text='\nThe dates for the event in one of the following formats:<br />\nA single date "dd - mon"; for example "2 Jul"<br />\nA range of dates as "dd - dd mon"; for example "3 - 6 Sep"<br />\n"November" (placeholder)<br />\nWe use this condensed format for inclusion in programmes.\n                  ', max_length=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateField(blank=True, help_text='\nEnter the end date of the event in DD/MM/YYYY format or leave blank to default\nto start date for a one day event.<br />\nEnsure that this is consistent with the value entered for "Dates" above.<br />\nThe end date isn\'t displayed but controls the listing of events.\n                  '),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.TextField(blank=True, default='', help_text='\nThe URL associated with the card image. Where this refers to an image from\nanother webiste it must be the full URL, including the scheme (http or https),\ne.g.\n"http://www.nlpca.co.uk/blog/wp-content/uploads/2016/10/Theatre-825x510.jpg".\nFor uploaded images it must be the path to the image relative to the root URL of\nour site, e.g. "/upload/img/2018_09_24-20:18:11.jpg".\n                  '),
        ),
        migrations.AlterField(
            model_name='event',
            name='presented_by',
            field=models.CharField(blank=True, help_text='\nEnter who the event is Presented By if it isn\'t just the member Society.<br />\nUsually this can be left to default to the member Society but not always; for\nexample:<br />\n"Derby East Scout & Guide Gang Show" overrides member Society "Flying High\n2016"<br />\n"Derby Cathedral Concerts, with Derby Cathedral Choir" overrides member Society\n"Derby Cathedral Concerts"<br />\n"Derby Theatre" where no member Society is specified for The Eagle Awards\n                  ', max_length=50),
        ),
        migrations.AlterField(
            model_name='event',
            name='society_rowid',
            field=models.ForeignKey(blank=True, db_column='society_rowid', help_text='\nSelect the member society that is presenting this event.<br />\nVery occassionally this may be left blank; for example "The Eagle Awards"\npresented by Derby\tTheatre.\nIf you do leave this blank then something must be entered in "Presented by".\n                  ', limit_choices_to={'type': 'whatson_society'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='society', to='whatson.Organisation', verbose_name='Society'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(help_text='\nEnter the start date of the event in DD/MM/YYYY format.<br />\nEnsure that this is consistent with the value entered for "Dates" above.<br />\nThe start date isn\'t displayed but controls the listing of events.\n                  '),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('PLACEHOLDER', 'Placeholder'), ('CONFIRMED', 'Confirmed')], help_text='\nIndicate whether this is a placeholder or whether the event details are\nconfirmed.<br />\nOnly when the details are confirmed will an event be visible to the public in\nthe DATA Diary.<br />\nPlaceholders are only visible to DATA Diary administrators as a planning aid.\n', max_length=11),
        ),
        migrations.AlterField(
            model_name='event',
            name='times',
            field=models.CharField(blank=True, help_text='\nIf any of the performances do not start at 7.30pm, enter the times for event;\nfor example:<br />\n"Sat matinee 2.30pm"<br />\n"Wed - Fri 7.15pm; Sat 1.30pm & 6pm"<br />\n"7pm"\n                  ', max_length=12),
        ),
        migrations.AlterField(
            model_name='event',
            name='venue_rowid',
            field=models.ForeignKey(blank=True, db_column='venue_rowid', help_text='\nThe venue for the event.\n                  ', limit_choices_to={'type': 'whatson_venue'}, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='venue', to='whatson.Organisation', verbose_name='Venue'),
        ),
        migrations.AlterField(
            model_name='organisation',
            name='type',
            field=models.CharField(choices=[('whatson_society', 'Society'), ('whatson_venue', 'Venue'), ('whatson_organisation', 'Organisation')], help_text='\nThe type of the organisation, which is one of<br />\nSociety = A DATA member society presenting events;<br />\nVenue = A venue hosting events;<br />\nOrganisation = Neither of the above but linked to some of our contacts.\n                  ', max_length=20),
        ),
        migrations.AlterField(
            model_name='personinorganisation',
            name='primary_contact',
            field=models.IntegerField(choices=[(1, 'Yes'), (0, 'No')], default=0, help_text='\nIndicates if somebody is the primary contact for their organisation.\n        '),
        ),
        migrations.AlterField(
            model_name='user',
            name='datetime',
            field=models.DateTimeField(blank=True, editable=False, help_text='\nA datetime that can be set to limit the time that certain options are available;\nfor example to restrict a password reset to within a day following the time that\nthe password reset link was requested.\n                  ', null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(editable=False, help_text="\nA hash of the users' password. We do <b>not</b> store passwords in plain text.\n                    ", max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='secret',
            field=models.TextField(blank=True, editable=False, help_text='\nUsed to store a randomly generated secret for security purposes; for example\nif an email is sent out with a link to confirm a user account, then a secret is\ngenerated and stored and is also used in the URL of the link in the email. That\nWay we know that it truly is the recipient of the email that is confirming the\naccount.\n                  '),
        ),
        migrations.AddField(
            model_name='socialmediahandle',
            name='organisation',
            field=models.ForeignKey(db_column='organisation_rowid', help_text='The organisation that the handle is associated with.', on_delete=django.db.models.deletion.PROTECT, to='whatson.Organisation', verbose_name='organisation'),
        ),
        migrations.AddField(
            model_name='socialmediahandle',
            name='platform',
            field=models.ForeignKey(db_column='platform_name', help_text="\nThe social media platform that the handle is for e.g. 'Facebook', 'Twitter',\netc.\n        ", on_delete=django.db.models.deletion.PROTECT, to='whatson.SocialMediaPlatform', verbose_name='platform name'),
        ),
        migrations.AlterUniqueTogether(
            name='socialmediahandle',
            unique_together={('organisation', 'platform')},
        ),
    ]