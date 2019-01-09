# Create test set up for dev

import datetime
from django.core.management.base import BaseCommand , CommandError
from whatson.models import Event , Person , Organisation , PersonInOrganisation

class Command ( BaseCommand ) :

    def handle ( self , *args , **options ) :

        venue = Organisation (
            name = 'Auntie Dora\'s front room' ,
            type = 'whatson_venue' ,
            status = 'ACTIVE'
        )

        venue.save ( )

        society = Organisation (
            name = 'Derby Theatre Types' ,
            type = 'whatson_society' ,
            status = 'ACTIVE'
        )

        society.save ( )

        person = Person.objects.get (
            email = 'david.williamson1964@googlemail.com'
        )

        personInOrganisation = PersonInOrganisation.objects.filter (
            person_rowid = person
        )

        personInOrganisation.delete ( )

        personInOrganisation = PersonInOrganisation (
            person_rowid = person ,
            organisation_rowid = society ,
            primary_contact = 1
        )

        personInOrganisation.save ( )

        event = Event (
            name = 'A Totally Awesome Production' ,
            start_date = datetime.date ( year = 2019 , month = 5 , day = 14 ) ,
            end_date = datetime.date ( year = 2019 , month = 5 , day = 18 ) ,
            times = '7.30pm and 2.30pm Sat matinee' ,
            society_rowid = society ,
            venue_rowid = venue ,
            box_office = 'Tickets 50p plus a bag of crisps' ,
            status = 'PUBLISHED' ,
            card = 0
        )

        event.save ( )