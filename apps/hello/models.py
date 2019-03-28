from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField('Date of birth', db_index=True)
    bio = models.TextField('Bio', blank=True)
    email = models.EmailField('Email')
    jabber = models.EmailField('Jabber ID')
    skype = models.CharField('Skype ID', max_length=50, blank=True)
    other_contacts = models.TextField('Other contacts', blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
