# Model for the whatson application, though I haven't thought much about
# splitting this application in to smaller components, which is possibly whats
# should happen.

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Classes following:
# - Address (abstract class to provide address fields to other classes)
# - Event (core whatson class holding the actual events)
# - Organisation (holds societies, venues and other organisations)
# - OrganisationFunction (a function within the organisation)
# - Person (a person known to us - a "contact")
# - PersonInOrganisation (the membership of a person in an organisation)
# - User (as subclass of person, which is persons who have a user account)
# - NewsItem (DATA membership related news items published on the website)
# - LinkType (types of hyperlink, e.g. website, Facebook, etc.)

################################################################################

class Address(models.Model):

    """
A location is essentially an address. It will be renamed to address at some
point for greater clarity. Addresses can be linked to either organisations or
people. Currently there is an issue whereby every organisation or person is
linked to an address, whether we know their address or not. In those instances
the fields of the address are blank. This issue will be resolved at some point.
    """

    def __str__ ( self ) : return \
        ( self.address1 if self.address1 else "" ) + \
        ( ', ' + self.postcode if self.postcode else "" )

    rowid = models.IntegerField (primary_key=True)

    address1 = models.CharField(
        blank=True,
        help_text="The first line of the address.",
        max_length=30,
    )

    address2 = models.CharField(
        blank=True,
        help_text="The second line of the address.",
        max_length=30,
    )

    address3 = models.CharField(
        blank=True,
        help_text="The third line of the address.",
        max_length=30,
    )

    address4 = models.CharField(
        blank=True,
        help_text="The fourth line of the address.",
        max_length=30,
    )

    postcode = models.CharField(
        blank=True,
        help_text="The postcode for the address.",
        max_length=10,
    )

    class Meta:
        abstract = True
        verbose_name_plural = 'Addresses'

################################################################################

class Event ( models.Model ) :

    """
Holds a single DATA Diary Event. An event can consist of a number of
performances over several days. Events are usually (but not always) presented by
a DATA member society.
    """

    def __str__ ( self ) :
        return self.start_date.strftime ( '%d/%m/%Y' ) + '-' + \
               self.end_date.strftime ( '%d/%m/%Y' ) + ' ' + self.name

    rowid = models.IntegerField (
        primary_key=True
    )

    name = models.CharField (
        max_length=100 ,
        help_text="The name of the event, limited to 100 characters."
    )

    dates = models.CharField (
        blank=True ,
        max_length=12 ,
        help_text="""
The dates for the event in one of the following formats:<br />
A single date "dd - mon"; for example "2 Jul"<br />
A range of dates as "dd - dd mon"; for example "3 - 6 Sep"<br />
"November" (placeholder)<br />
We use this condensed format for inclusion in programmes.
                  """
    )

    start_date = models.DateField (
        help_text="""
Enter the start date of the event in DD/MM/YYYY format.<br />
Ensure that this is consistent with the value entered for "Dates" above.<br />
The start date isn't displayed but controls the listing of events.
                  """
    )

    end_date = models.DateField (
        blank=True , # If left blank in forms then default to start_date
        help_text="""
Enter the end date of the event in DD/MM/YYYY format or leave blank to default
to start date for a one day event.<br />
Ensure that this is consistent with the value entered for "Dates" above.<br />
The end date isn't displayed but controls the listing of events.
                  """
    )

    times = models.CharField (
        max_length=12,
        blank=True,
        help_text="""
If any of the performances do not start at 7.30pm, enter the times for event;
for example:<br />
"Sat matinee 2.30pm"<br />
"Wed - Fri 7.15pm; Sat 1.30pm & 6pm"<br />
"7pm"
                  """
    )

    society_rowid = models.ForeignKey (
        'Organisation',
        on_delete=models.PROTECT,
        related_name='society',
        blank=True,
        null=True,
        db_column='society_rowid',
        limit_choices_to={'type': 'whatson_society'},
        verbose_name='Society',
        help_text="""
Select the member society that is presenting this event.<br />
Very occassionally this may be left blank; for example "The Eagle Awards"
presented by Derby	Theatre.
If you do leave this blank then something must be entered in "Presented by".
                  """
    )

    presented_by = models.CharField (
        max_length=50,
        blank=True,
        help_text="""
Enter who the event is Presented By if it isn't just the member Society.<br />
Usually this can be left to default to the member Society but not always; for
example:<br />
"Derby East Scout & Guide Gang Show" overrides member Society "Flying High
2016"<br />
"Derby Cathedral Concerts, with Derby Cathedral Choir" overrides member Society
"Derby Cathedral Concerts"<br />
"Derby Theatre" where no member Society is specified for The Eagle Awards
                  """
    )

    venue_rowid = models.ForeignKey (
        'Organisation',
        blank=True,
        db_column='venue_rowid',
        help_text="""
The venue for the event.
                  """,
        limit_choices_to={'type': 'whatson_venue'},
        null=True,
        on_delete=models.PROTECT,
        related_name='venue',
        verbose_name='Venue'
    )

    box_office = models.CharField (
        blank=True,
        max_length=50,
        help_text="""
Enter the contact details for Box Office enquiries for the event; for example:
<br />
"01332 593939"<br />
"01773 829248 - Free"<br />
"Derby Live Box Office - 01332 255800"
                  """
    )

    STATUS_CHOICES = (
        ( 'PLACEHOLDER' , 'Placeholder' ) ,
        ( 'PUBLISHED' , 'Published' ) ,
    )
    status = models.CharField (
        max_length=11,
        choices=STATUS_CHOICES,
        help_text="""
Indicates whether the event has been published or not. Only published events are
advertised to the public. Placeholder events are only visible to DATA Diary
administrators, as a planning aid.
                  """
    )

    CARD_CHOICES = (
        ( 2 , 'Yes (without image)' ) ,
        ( 1 , 'Yes (with image)' ) ,
        ( 0 , 'No' ) ,
    )
    card = models.IntegerField (
        db_column="use_desc",
        choices=CARD_CHOICES,
        verbose_name="Custom card and image choice",
        help_text="""
Indicates whether the event has a custom card associated with it and (if it
does) whether that custom card is associated with an image or not.
                  """
    )

    image = models.TextField (
        blank=True,
        default="",
        help_text="""
The URL associated with the card image. Where this refers to an image from
another webiste it must be the full URL, including the scheme (http or https),
e.g.
"http://www.nlpca.co.uk/blog/wp-content/uploads/2016/10/Theatre-825x510.jpg".
For uploaded images it must be the path to the image relative to the root URL of
our site, e.g. "/upload/img/2018_09_24-20:18:11.jpg".
                  """
    )

    description = models.TextField (
        blank=True,
        help_text="""
Enter a free text description of the event in HTML.
                  """
    )

    def clean ( self ):

        if self.end_date is None:
            self.end_date = self.start_date

        if self.society_rowid and not self.presented_by:
            self.presented_by = str ( self.society_rowid )
        elif not self.society_rowid and not self.presented_by:
            raise ValidationError ( _ ( \
'You must enter "Presented by" if no "Society" is selected.' \
            ) )

        if self.status == 'Confirmed' and \
            ( not self.venue_rowid or not self.box_office ):
            raise ValidationError ( _ (\
'If "Status" is "Confirmed" then a "Venue" must be selected' + \
' and "Box office" details must be provided.'\
            ) )

        if self.card and not self.description:
            raise ValidationError ( _ ( \
'If a custom card is specified then an event description must be entered' \
        ) )

    class Meta:
        managed = True
        db_table = 'event'
        ordering = [ 'start_date' , 'end_date' ]

################################################################################

class Organisation( Address ):

    """
Any type of organisation. The DATA Diary uses three different types of
organisation; member societies who present events, venues that host events and
other organisations that are neither of those. The DATA Diary only holds details
of those other organisations to link them to persons.
    """

    def __str__ ( self ) :
        return self.name

    rowid = models.IntegerField (
        primary_key=True
    )

    name = models.CharField(
        unique=True,
        max_length=80,
        help_text="The name of the organisation, limited to 80 characters."
    )

    TYPE_CHOICES = (
        ( 'whatson_society' , 'Society' ) ,
        ( 'whatson_venue' , 'Venue' ) ,
        ( 'whatson_organisation' , 'Organisation' ) ,
    )
    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=20,
        help_text="""
The type of the organisation, which is one of<br />
Society = A DATA member society presenting events;<br />
Venue = A venue hosting events;<br />
Organisation = Neither of the above but linked to some of our contacts.
                  """
    )

    email = models.EmailField(
        blank=True,
        help_text="A contact email address for the organisation.",
        max_length=254,
    )

    website = models.URLField(
        blank=True,
        help_text="A web site address for the organisation."
    )

    STATUS_CHOICES = (
        ( 'ACTIVE' , 'Active' ) ,
        ( 'INACTIVE' , 'Inactive' ) ,
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        max_length=8,
        help_text="""
The status of the organisation, which can be "Active" or "Inactive".<br />
Organisations in inactive status will not be listed for selection in drop-down
lists.<br />
Member societies that are inactive can not list events.
                  """
    )

    paid_in_period = models.BooleanField(
        null=True,
        help_text="""
A flag that is only applicable to organisations that correspond to member
societies. It indicates whether or not the member society has paid its DATA
subscription fee in the current subscription period.
                  """
    )

    description = models.TextField(
        blank=True,
        max_length=500,
        help_text="""
An optional description for the organisation. This should be plain text, i.e. no
HTML markup. Ideally a single paragraph. It must be less that 500 characters.
                  """
    )

    persons = models.ManyToManyField (
        'Person',
        through='PersonInOrganisation',
    )

    class Meta:
        managed = True
        db_table = 'organisation'
        ordering = [ 'name' ]

################################################################################

class OrganisationFunction ( models . Model ) :

    """
An organisation function is just a discrete part of an organisation; for example
the Major's office of Derby City Council. Organisation functions can have their
own email address.
    """

    def __str__ ( self ) :
        return self . name

    rowid = models . IntegerField (
        editable = False ,
        primary_key = True ,
    )

    name = models.CharField (
        max_length=50,
        help_text="The name of the function, limited to 50 characters."
    )

    email = models.EmailField(
        blank=True,
        help_text="An email address associated with the function.",
        null=True,
        unique=True
    )

    organisation_rowid = models.ForeignKey (
        'Organisation',
        db_column='organisation_rowid',
        on_delete=models.CASCADE,
    )

    class Meta:
        managed = True
        db_table = 'organisation_function'
        unique_together = (('organisation_rowid', 'name'),)

################################################################################

class Person ( Address ) :

    """
A person known to the DATA Diary.
    """

    def __str__ ( self ) :
        return self.surname + ', ' + self.first_name

    rowid = models.IntegerField(
        editable=False,
        primary_key=True,
    )

    email = models.EmailField(
        blank=True,
        help_text="The email address associated with the person.",
        null=True,
        unique=True
    )

    first_name = models.CharField (
        help_text="The person's first name.",
        max_length=30,
    )

    surname = models.CharField(
        help_text="The person's surname.",
        max_length=30,
    )

    title = models.CharField(
        blank=True,
        help_text="A title that the person has.",
        max_length=30,
    )

    telephone = models.CharField(
        blank=True,
        help_text="The person's telephone number.",
        max_length=15,
    )

    SUBSCRIBER_CHOICES = (
        ( 1, 'Yes' ) ,
        ( 0, 'No' ) ,
    )
    subscriber = models.BooleanField(
        default=0,
        choices=SUBSCRIBER_CHOICES,
        help_text="""
Whether or not the person is subscribed to receive the monthly DATA Diary email.
                  """
    )

    secret = models.TextField(
        blank=True,
        editable=False,
        help_text="""
Stores a randomly generated secret for security purposes; for example to protect
against malicious unsubscribe requests by a third-party on behalf of email
addresses that they have somehow obtained. This is a secret associated directly
with the person rather than with a user so that it can be used in those
scenarios where it can't be guaranteed that the person has registered a user
account.
                  """,
    )

    class Meta:
        db_table = 'person'
        managed = True
        ordering = [ 'surname', 'first_name' ]

################################################################################

class PersonInOrganisation(models.Model):

    """
An association between a person and an organisation, with several details that
pertain to that assocation.
    """

    def __str__ ( self ) :
        return ''

    rowid = models.IntegerField(
        editable=False,
        primary_key=True,
   )

    person_rowid = models.ForeignKey (
        'Person',
        db_column='person_rowid',
        on_delete=models.PROTECT,
        verbose_name='Person',
    )

    organisation_rowid = models.ForeignKey (
        'Organisation',
        db_column='organisation_rowid',
        on_delete=models.PROTECT,
        verbose_name='Organisation'
    )

    role = models.CharField(
        blank=True,
        help_text="""
The role that the person has in the organisation; for example "Treasurer" of a
DATA member society.
                  """,
        max_length=20,
        null=True,
    )

    status = models.CharField(
        blank=True,
        help_text = \
            "The status of the association. I don't think we're using this." ,
        max_length=10,
    )

    PRIMARY_CONTACT_CHOICES = (
        ( 1, 'Yes' ) ,
        ( 0, 'No' ) ,
    )
    primary_contact = models.IntegerField(
        default=0,
        choices=PRIMARY_CONTACT_CHOICES,
        help_text = """
Indicates if somebody is the primary contact for their organisation.
        """ ,
    )

    class Meta:
        managed = True
        db_table = 'person_in_organisation'
        verbose_name_plural = 'Persons in organisation'

################################################################################

class User(models.Model):

    """
A user is an extension of a person, being somebody that is known to the DATA
Diary and has also registered a user account with us.

Currently we're not making full use of the Django authentication and
authorisation system. Only superuser access is managed through Django. So this
model contains all non-superuser users. That will change and we'll eventaully
manage all access via Django.

Users whose access is managed outside of Django are either admins (members of
the DATA commitee) or reps (the representatives of member societies).
    """

    def __str__ ( self ) :
        return self.userid

    userid = models.CharField(
        help_text="The user's userid that they've selected when registering.",
        max_length=20,
        primary_key=True,
        unique=True,
    )

    ROLE_CHOICES = (
        ( 'admin' , 'Admin' ) ,
        ( 'rep' , 'Rep' ) ,
    )
    role = models.CharField (
        choices=ROLE_CHOICES,
        help_text="""
The user's role. This can only be one of "Admin" or "Rep". It is determined at
the point that the user registers their user account.
                  """,
        max_length=5,
    )

    password = models.CharField(
        editable=False,
        help_text = """
A hash of the users' password. We do <b>not</b> store passwords in plain text.
                    """ ,
        max_length=20,
    )

    person_rowid = models.ForeignKey(
        'Person',
        db_column='person_rowid',
        help_text="The person that the userid is associated with.",
        on_delete=models.PROTECT,
        verbose_name='person',
    )

    STATUS_CHOICES = (
        ( 'CONFIRMED', 'Confirmed' ) ,
        ( 'UNCONFIRMED', 'Unconfirmed' ) ,
    )
    status = models.CharField(
        choices=STATUS_CHOICES,
        help_text="""
The staus of the user account. When user accounts are regsitered they are
initially in an "Unconfirmed" status. An email is sent to the email address
associated with the user account. That email contains a link to confirm the
user account. Clicking on that link changes the status of the user account to
"Confirmed".
                  """,
        max_length=12,
    )

    secret = models.TextField(
        blank=True,
        editable=False,
        help_text="""
Used to store a randomly generated secret for security purposes; for example
if an email is sent out with a link to confirm a user account, then a secret is
generated and stored and is also used in the URL of the link in the email. That
Way we know that it truly is the recipient of the email that is confirming the
account.
                  """,
    )

    datetime = models.DateTimeField(
        blank=True,
        null=True,
        editable=False,
        help_text="""
A datetime that can be set to limit the time that certain options are available;
for example to restrict a password reset to within a day following the time that
the password reset link was requested.
                  """,
    )

    class Meta:
        managed = True
        db_table = 'user'

################################################################################

class NewsItem ( models.Model ) :

    """
A news item published via the website.
    """

    rowid = models.IntegerField (
        primary_key = True
    )

    published_date = models.DateField (
        help_text="""
                  The publication date of the news item.
                  """
    )

    title = models.CharField (
        max_length=100 ,
        help_text="The title of the news item, limited to 100 characters."
    )

    image = models.TextField (
        blank=True ,
        help_text="""
The path relative to the site root of an image file associated with the news
item. This will be used to include the image in the news item card.
                  """
    )

    mailchimp_image = models.URLField (
        blank=True ,
        help_text="""
The full URL of the image for the news item that's been uploaded to the
Mailchimp content manager. This is so that it can be included in Mailchimp
mailshots.
                  """
    )

    precis = models.CharField (
        max_length=250 ,
        help_text="A one line precis of the news item."
    )

    item_text = models.TextField (
        help_text="""
Enter a free text description of the event in HTML.
                  """
    )

    class Meta:
        managed = True
        db_table = 'whatson_news_item'
        ordering = [ '-published_date' ]

################################################################################







class SocialMediaPlatform ( models.Model ):

    """
A social media platform, e.g. Facebook, Twitter, etc.
    """

    def __str__ ( self ) :
        return self.name

    name = models . CharField (
        help_text="""
The name of the social media platform, e.g. Facebook", "Twitter", etc.
                  """ ,
        max_length = 10 ,
        primary_key = True ,
        unique = True
    )

    icon = models . CharField (
        help_text = """
The name of the font-awesome icon that we use to represent this social media
platform.
        """ ,
        max_length = 10
    )

    class Meta :
        managed = True
        db_table = 'whatson_social_media_platform'

class SocialMediaHandle ( models . Model ) :

    """
A social media handle for an organisation.
    """

    organisation = models . ForeignKey (
        'Organisation' ,
        db_column = 'organisation_rowid' ,
        help_text = "The organisation that the handle is associated with." ,
        on_delete = models . PROTECT ,
        verbose_name = 'organisation' ,
    )

    platform = models . ForeignKey (
        'SocialMediaPlatform' ,
        db_column = 'platform_name' ,
        help_text = """
The social media platform that the handle is for e.g. 'Facebook', 'Twitter',
etc.
        """ ,
        on_delete = models . PROTECT ,
        verbose_name = 'platform name' ,
    )

    handle = models . URLField (
        help_text = """
The handle, e.g. '@AllestreeAmDram'. These can be entered with or without the
@ prefix.
        """
    )

    class Meta :
        managed = True
        db_table = 'whatson_social_media_handle'
        unique_together = ( ( 'organisation' , 'platform' ) , )
