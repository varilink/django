# Migrations linked to release two of derbyartsandtheatre.org.uk
# Changes as follows:
# 1. Change of possible event states from Placholder and Confirmed to
# Placeholder and Published;
# 2. Publication of news item announcing that automatic Facebook posts are now
# live;
# 3. Publication of news item giving an update on the Council's plans to reopen
# the Assembly Rooms and DATA's perspective on it;
# 4. Change of type for all rowid primary keys from Integer to AutoField so that
# Django receives the assigned rowid on object save.

import datetime
from django.db import migrations, models

def event_status ( apps , schema_editor ) :

    # Updates event status of existing events

    Event = apps.get_model ( 'whatson' , 'Event' )

    for event in Event.objects.all ( ) :

        if event.status == 'CONFIRMED' :

            event.status = 'PUBLISHED'

            event.save ( )

        elif event.status == 'PLACEHOLDER' :

            pass

        else :

            raise ValueError ( 'Unexpected event status detected' )

def news_item_1 ( apps , schema_editor ) :

    # Publish news item announcing Facebook integration

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Event Posts to Facebook Live' ,
        image = 'assets/img/news_items/facebook.jpg' ,
        precis = """
Automatic posting of event details to Facebook from the DATA Diary enabled
        """ ,
        item_text = """\
<div class="rows columns">
<img src="/assets/img/news_items/facebook.jpg" class="float-left"
style="margin-right: 1em;">
<p>
We have implemented the automatic posting of event details from the DATA Diary
to the <a href="https://www.facebook.com/DerbyArtsAndTheatreAssociation/"
target="_blank">DATA Facebook page</a>. This follows the implementation of
automatic Tweets from the DATA Diary from 15th September.
</p>
<p>
Events on the DATA Diary website are now automatically publicised via Twitter,
Facebook and a monthly email bulletin - all from the same source information
that members can upload to the website themselves by <a
href="https://www.derbyartsandtheatre.org.uk/account/begin_registration">
registering a user account with us</a>.
</p>
</div>\
"""
    )

    news_item.save ( )

def news_item_2 ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Proposals to Reopen the Assembly Rooms' ,
        image = 'assets/img/news_items/assembly_rooms_card.jpg' ,
        precis = """
DATA gives cautious welcome to proposals detailed in Council's Cabinet report
        """ ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="640px" height="360px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="225px"
src="/assets/img/news_items/ground-floor-entrance-area.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/ground-floor-entrance-area.jpg"
width="550px" height="310px">
<p>
Derby Arts and Theatre Association (DATA) has given a cautious welcome to Derby
City Council's recently announced proposals to reopen the Assembly Rooms which
have been closed since a fire in March 2014. The Council's Cabinet approved a
report on 12th December 2018 which recommended refurbishing the Assembly Rooms
and reopening the building by Autumn 2020.
</p>
<p>
DATA Chair, Steve Dunning, said:
</p>
<p>
"Although we would have preferred to have a brand new theatre and concert hall
built, we are pleased now to see firm proposals to not only repair but also
enhance the Assembly Rooms. As part of the consultation process, DATA made
several practical suggestions for improving the facilities and audience
experience, based on our members' experience of putting on shows and concerts at
the venue. We are glad to see that many of our suggestions have been taken on
board.
</p>
<p>
Of course, the devil will be in the detail and we look forward to futher input
into the development of the project. We are especially keen that the operating
arrangements and hire charges provide an incentive to amateur theatre and
concert groups to use the newly refurbished venue."
</p>
<p>
Further information on the scheme can be found via these links:
<br>
<a target="_blank"
href="https://news.derby.gov.uk/next-steps-for-derbys-assembly-rooms-revealed/">
Next steps for Derby's Assembly Rooms revealed
</a>
<br>
<a target="_blank"
href="https://cmis.derby.gov.uk/CMIS5/Document.ashx?czJKcaeAi5tUFL1DTL2UE4zNRBcoShgo=QkqSmXVpfDn8XtB9JIcnHfgWJUDoegYwFS%2bTmmAHIWATEjKM4NAPDg%3d%3d&rUzwRPf%2bZ3zd4E7Ikn8Lyw%3d%3d=pwRE6AGJFLDNlh225F5QMaQWCtPHwdhUfCZ%2fLUQzgA2uL5jNRG4jdQ%3d%3d&mCTIbCubSFfXsDGW9IXnlg%3d%3d=hFflUdN3100%3d&kCx1AnS9%2fpWZQ40DXFvdEw%3d%3d=hFflUdN3100%3d&uJovDxwdjMPoYv%2bAJvYtyA%3d%3d=ctNJFf55vVA%3d&FgPlIEJYlotS%2bYGoBi5olA%3d%3d=NHdURQburHA%3d&d9Qjj0ag1Pd993jsyOJqFvmyB7X0CSQK=ctNJFf55vVA%3d&WGewmoAfeNR9xqBux0r1Q8Za60lavYmz=ctNJFf55vVA%3d&WGewmoAfeNQ16B2MHuCpMRKZMwaG1PaO=ctNJFf55vVA%3d">
Council Cabinet 12th December 2018 - The New Assembly Rooms
</a>
</div>
"""
    )

    news_item.save ( )

class Migration(migrations.Migration):

    dependencies = [
        ( 'whatson' , '0009_auto_20181018_1616' ) ,
    ]

    operations = [

        migrations.AlterField (
            model_name = 'event' ,
            name = 'status' ,
            field = models.CharField (
                choices = [
                    ( 'PLACEHOLDER' , 'Placeholder' ) ,
                    ( 'PUBLISHED' , 'Published' )
                ] ,
                help_text ="""\
Indicates whether the event has been published or not. Only published events \
are advertised to the public. Placeholder events are only visible to DATA \
Diary administrators, as a planning aid.""" ,
                max_length = 11
            ) ,
        ) ,

        migrations.RunPython ( event_status ) ,

        migrations.RunPython ( news_item_1 ) ,

        migrations.RunPython ( news_item_2 ) ,

        migrations.AlterField (
            model_name = 'event' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

        migrations.AlterField (
            model_name = 'organisation' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

        migrations.AlterField (
            model_name = 'organisationfunction' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

        migrations.AlterField (
            model_name = 'person' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

        migrations.AlterField (
            model_name = 'personinorganisation' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

        migrations.AlterField (
            model_name = 'newsitem' ,
            name = 'rowid' ,
            field = models.AutoField (
                editable = False ,
                primary_key = True ,
                serialize = False
            ) ,
        ) ,

    ]