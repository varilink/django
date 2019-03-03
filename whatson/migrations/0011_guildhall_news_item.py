# News item related to Guildhall Theatre closure

import datetime
from django.db import migrations , models

def news_item ( apps , schema_editor ) :

    NewsItem = apps.get_model ( 'whatson' , 'NewsItem' )

    news_item = NewsItem (
        published_date = datetime.datetime.now ( ) ,
        title = 'Guildhall Theatre Closure' ,
        image = '/assets/img/news_items/guildhall_card.jpg' ,
        precis = """\
DATA coordinates member society action in response to the Guildhall Theatre
closure\
""" ,
        item_text = """\
<div class="rows columns">
<img class="hide-for-medium" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="640px" height="525px">
<img class="float-left show-for-medium hide-for-large"
style="margin-right: 1em;" width="400px" height="328px"
src="/assets/img/news_items/guildhall.jpg">
<img class="float-left show-for-large" style="margin-right: 1em;"
src="/assets/img/news_items/guildhall.jpg"
width="550px" height="451px">
<p>
Derby City Council has announced that the Guildhall Theatre, Derby will be
closed temporarily for essential repairs to the roof.  The closure was
originally to have been to 31st January but this has now been extended to 30th
September 2019, subject to a review in May.  About 60 amateur and professional
bookings will be affected.
</p>
<p>
This is a major blow for the amateur theatre groups who have shows booked in the
Guildhall during the period of closure.  It is also another setback for the
cultural offer of Derby, given that the Assembly Rooms has now been closed for
almost five years, and that venue is not expected to reopen until Autumn 2020 at
the earliest.
</p>
<p>
Derby Arts and Theatre Association (DATA) represents a number of the amateur
groups affected by the Guildhall closure and an urgent meeting with affected
amateur organisations was held on 25 January to share concerns, issues and ideas
and provide a forum for mutual support.  The meeting agreed a number of actions
to try to ameliorate the serious repercussions of the closure on amateur
companies.  A request has been made for a delegation from DATA to meet
Councillor Alan Grimadell, Cabinet Member for Leisure, Culture and Tourism, and
Peter Ireson, Head of Derby Live to raise some specific areas of concern.
</p>
</div>\
"""
    )

    news_item.save ( )

class Migration ( migrations.Migration ) :

    dependencies = [
        ( 'whatson' , '0010_release_two' ) ,
    ]

    operations = [

        migrations.RunPython ( news_item ) ,

    ]