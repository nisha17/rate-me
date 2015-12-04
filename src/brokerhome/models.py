from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    city_name = models.CharField(max_length=255)  # Field name made lowercase.
    slug = models.SlugField(unique=True, max_length=31, help_text='A label for url config')

    def __str__(self):
        return self.city_name

    def get_absolute_url(self):
        return reverse('brokerhome:city_details', kwargs={'pk': self.city_id})

    class Meta:
        db_table = 'city'
        verbose_name = 'cities'
        ordering = ['city_name']


class Locality(models.Model):
    locale_id = models.AutoField(primary_key=True)  # Field name made lowercase.
    city_id = models.ForeignKey(City, db_column="city_id", related_name="city_locality")  # Field name made lowercase.
    locale = models.CharField(max_length=255)

    def __str__(self):
        return self.locale

    class Meta:
        db_table = 'locality'
        unique_together = (('city_id', 'locale'),)
        verbose_name = 'localities'


class BrokerDetails(models.Model):
    broker_id = models.IntegerField(primary_key=True)  # Field name made lowercase.
    broker_name = models.CharField(max_length=255)
    firm_name = models.CharField(max_length=255, blank=True, null=True)  # Field name made lowercase.
    website = models.URLField(max_length=1000, blank=True, null=True)
    slug = models.SlugField(max_length=31, help_text='A label for url config', blank=True, null=True)

    def __str__(self):
        return self.broker_name

    class Meta:
        db_table = 'broker_details'
        verbose_name = 'brokers'


class BrokerLocale(models.Model):
    broker_loc_id = models.AutoField(primary_key=True)
    broker_id = models.ForeignKey('BrokerDetails', db_column="broker_id",
                                  related_name="locale_broker")  # Field name made lowercase.
    locale_id = models.ForeignKey('Locality', db_column="locale_id",
                                  related_name="broker_locale")  # Field name made lowercase.
    city_id = models.ForeignKey('City', db_column="city_id", related_name="broker_city")  # Field name made lowercase.

    class Meta:
        db_table = 'broker_locale'
        unique_together = (('broker_id', 'locale_id'),)


# class Users(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=255)

#     class Meta:
#         db_table = 'user'

#     def __str__(self):
#         return self.username


class BrokerRating(models.Model):
    rate_id = models.AutoField(primary_key=True)
    broker_id = models.ForeignKey(BrokerDetails, db_column="broker_id", related_name="broker_rate")
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL)
    rating = models.DecimalField(decimal_places=2, max_digits=10,blank=True, null=True)
    review = models.CharField(max_length=1000, blank=True, null=True)
    #slug = models.SlugField(unique=True, max_length=31, help_text='A label for url config')

    class Meta:
        db_table = 'broker_rating'


    # def get_absolute_url(self):
    #     return reverse('brokerhome:city_details', kwargs={'pk': '96'})