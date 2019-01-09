# Create test set up for dev

from django.core.management.base import BaseCommand , CommandError
from whatson.models import Person , Organisation , PersonInOrganisation

class Command ( BaseCommand ) :

    def handle ( self , *args , **options ) :

        society = Organisation.objects.get ( name = 'Derby Theatre Types' )

        print ( "Created rowid=" + society.rowid )