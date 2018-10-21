from django.contrib import admin

# Register your models here.
from whatson.models import Event
from whatson.models import NewsItem
from whatson.models import Organisation
from whatson.models import OrganisationFunction
from whatson.models import Person
from whatson.models import PersonInOrganisation
from whatson.models import SocialMediaHandle
from whatson.models import SocialMediaPlatform
from whatson.models import User

import datetime
from dateutil.relativedelta import relativedelta

################################################################################
#                                                                              #
# Filters                                                                      #
#                                                                              #
################################################################################

class EventStartDateListFilter ( admin.SimpleListFilter ):

    title = 'start date'

    parameter_name = 'start_date'

    def lookups ( self , request , model_admin ):

        return (
            ( 'Month' , ( 'Next Month' ) ) ,
            ( 'SixMonths' , ( 'Next Six Months' ) ) ,
        )

    def queryset ( self , request , queryset ):

        if self.value ( ) == 'Month':
            return queryset.filter (
                start_date__gte = datetime.date.today ( ) ,
                start_date__lte = \
                    datetime.date.today ( ) + relativedelta ( months=1 )
            )

        if self.value ( ) == 'SixMonths':
            return queryset.filter (
                start_date__gte = datetime.date.today ( ) ,
                start_date__lte = \
                    datetime.date.today ( ) + relativedelta ( months=6 )
            )

################################################################################
#                                                                              #
# Inlines                                                                      #
#                                                                              #
################################################################################

class FunctionInline ( admin . TabularInline ) :
    model = OrganisationFunction

class OrganisationInline ( admin . TabularInline ) :
    model = Organisation

class SocialMediaHandles ( admin . TabularInline ) :
    model = SocialMediaHandle

class OrganisationsPersons ( admin . TabularInline ) :
    model = PersonInOrganisation
    exclude = ( 'status' , )

class PersonsOrganisations ( admin . TabularInline ) :
    model = PersonInOrganisation
    exclude = ( 'status' , )
    verbose_name = 'Organisation the Person is associated with'
    verbose_name_plural = 'Organisations the Person is associated with'

################################################################################
#                                                                              #
# Admins                                                                       #
#                                                                              #
################################################################################

class EventAdmin ( admin.ModelAdmin ):
    fields = (
        'name', 'dates', 'start_date', 'end_date', 'times', 'society_rowid',
        'presented_by', 'venue_rowid', 'box_office', 'status', 'card', 'image' ,
        'description'
    )
    list_filter = (
        EventStartDateListFilter , (
            'society_rowid' , admin.RelatedOnlyFieldListFilter
        )
    )

admin.site.register ( Event, EventAdmin )

class SocialMediaPlatformAdmin ( admin . ModelAdmin ) :
    pass

admin.site.register ( SocialMediaPlatform, SocialMediaPlatformAdmin )

class NewsItemAdmin ( admin.ModelAdmin ):
    fields = (
        'published_date' , 'title' , 'image' , 'mailchimp_image' , 'precis' ,
        'item_text'
)
    list_display = ( 'published_date' , 'title' )
admin.site.register ( NewsItem , NewsItemAdmin )

class OrganisationAdmin(admin.ModelAdmin):
    fields = (
        'name', 'type', 'email', 'website', 'status', 'description', 'address1',
        'address2', 'address3', 'address4', 'postcode'
    )
    inlines = [ FunctionInline , OrganisationsPersons , SocialMediaHandles , ]
    list_display = ( 'name' , 'type' , 'status' )
    list_filter = ( 'type', 'status' )
    search_fields = [ 'name' ]
admin.site.register(Organisation, OrganisationAdmin)

class PersonAdmin(admin.ModelAdmin):
    fields = (
        'surname' , 'first_name' , 'title', 'email', 'subscriber', 'address1',
			'address2', 'address3', 'address4', 'postcode'
    )
    inlines = [ PersonsOrganisations, ]
    list_display = ( 'surname' , 'first_name' , 'email' )
    search_fields = [ 'surname' , 'first_name' ]
admin.site.register(Person, PersonAdmin)

#class PersonInOrganisationAdmin(admin.ModelAdmin):
#    pass
#admin.site.register(PersonInOrganisation, PersonInOrganisationAdmin)

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
