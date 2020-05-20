# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from models_univers import *
from models_object import *
from models_process import *



class AuthMessage(models.Model):
    user_id = models.IntegerField()
    message = models.TextField()

    class Meta:
        db_table = 'auth_message'







class BaseAccounts(models.Model):
    login = models.CharField(max_length=256, blank=True, null=True)
    validation_code = models.CharField(max_length=256, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    auth_status = models.IntegerField()
    nickname = models.CharField(max_length=100, blank=True, null=True)
    fullname = models.CharField(max_length=100, blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    avatar = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_accounts'


class BaseAction(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'base_action'


class BaseActionslog(models.Model):
    dtime = models.DateTimeField()
    profile_id = models.IntegerField()
    object = models.CharField(max_length=2)
    object_id = models.IntegerField()
    action = models.CharField(max_length=1)
    attributes = models.CharField(max_length=256, blank=True, null=True)
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_actionslog'


class BaseActionspricelist(models.Model):
    title = models.CharField(max_length=128)
    price = models.FloatField()
    price_edit = models.FloatField(blank=True, null=True)
    price_delete = models.FloatField(blank=True, null=True)
    allow = models.IntegerField()
    group = models.CharField(max_length=2)
    project_id = models.IntegerField()
    user_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_actionspricelist'


class BaseAfishacinemarate(models.Model):
    rate1 = models.IntegerField()
    rate2 = models.IntegerField()
    rate3 = models.IntegerField()
    rate = models.FloatField()
    vnum = models.IntegerField()
    organization_id = models.IntegerField()

    class Meta:
        db_table = 'base_afishacinemarate'


class BaseAlterstreettype(models.Model):
    value_id = models.IntegerField()
    name = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_alterstreettype'


class BaseApilogger(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()
    details = models.CharField(max_length=256)
    ip = models.CharField(max_length=15)
    method = models.CharField(max_length=32)
    event = models.IntegerField()

    class Meta:
        db_table = 'base_apilogger'


class BaseArea(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_area'


class BaseArticles(models.Model):
    title = models.CharField(max_length=128)
    pub_date = models.DateTimeField()
    text = models.TextField()
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_articles'


class BaseAwards(models.Model):
    awards_id = models.IntegerField()
    year = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=1)
    fest_id = models.IntegerField()

    class Meta:
        db_table = 'base_awards'


class BaseAwardsnames(models.Model):
    name_en = models.CharField(max_length=256, blank=True, null=True)
    name_ru = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_awardsnames'


class BaseAwardsrelations(models.Model):
    kid = models.IntegerField()

    class Meta:
        db_table = 'base_awardsrelations'


class BaseAwardsrelationsAwards(models.Model):
    awardsrelations_id = models.IntegerField()
    awards_id = models.IntegerField()

    class Meta:
        db_table = 'base_awardsrelations_awards'
        unique_together = (('awardsrelations_id', 'awards_id'),)


class BaseBackground(models.Model):
    image = models.CharField(max_length=100)
    url = models.CharField(max_length=256)
    country_id = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)
    date_adding = models.DateTimeField()
    site_id = models.IntegerField()
    subdomain = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_background'


class BaseBannedusersandips(models.Model):
    profile_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=15, blank=True, null=True)
    dtime = models.DateTimeField()
    who_id = models.IntegerField()

    class Meta:
        db_table = 'base_bannedusersandips'


class BaseBookercinemas(models.Model):
    cinema_id = models.IntegerField()
    settings_id = models.IntegerField()
    permission = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_bookercinemas'


class BaseBookingschedules(models.Model):
    unique = models.CharField(max_length=64)
    hall_id = models.IntegerField()
    dtime = models.DateTimeField()
    temp = models.IntegerField()

    class Meta:
        db_table = 'base_bookingschedules'


class BaseBookingschedulesFilms(models.Model):
    bookingschedules_id = models.IntegerField()
    sourcefilms_id = models.IntegerField()

    class Meta:
        db_table = 'base_bookingschedules_films'
        unique_together = (('bookingschedules_id', 'sourcefilms_id'),)


class BaseBookingsettings(models.Model):
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_bookingsettings'


class BaseBoxoffice(models.Model):
    bx_id = models.CharField(max_length=256)
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    name = models.CharField(max_length=256)
    kid = models.IntegerField()
    screens = models.IntegerField(blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    week_sum = models.IntegerField(blank=True, null=True)
    all_sum = models.IntegerField(blank=True, null=True)
    week_audience = models.IntegerField(blank=True, null=True)
    all_audience = models.IntegerField(blank=True, null=True)
    country_id = models.IntegerField()
    days = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_boxoffice'


class BaseBoxofficeDistributor(models.Model):
    boxoffice_id = models.IntegerField()
    distributors_id = models.IntegerField()

    class Meta:
        db_table = 'base_boxoffice_distributor'
        unique_together = (('boxoffice_id', 'distributors_id'),)


class BaseBudget(models.Model):
    budget = models.BigIntegerField()
    currency = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_budget'


class BaseBuilding(models.Model):
    city_id = models.IntegerField()
    street_id = models.IntegerField(blank=True, null=True)
    number = models.CharField(max_length=8, blank=True, null=True)
    path = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'base_building'


class BaseBuyticketstatistic(models.Model):
    dtime = models.DateTimeField()
    profile_id = models.IntegerField()
    session_id = models.IntegerField()
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_buyticketstatistic'


class BaseCarrierlayer(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_carrierlayer'


class BaseCarrierriptype(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_carrierriptype'


class BaseCarriertapecategorie(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_carriertapecategorie'


class BaseCarriertype(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_carriertype'


class BaseCinema(models.Model):
    city_id = models.IntegerField()
    cinema_circuit_id = models.IntegerField(blank=True, null=True)
    street_type_id = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=64, blank=True, null=True)
    number_housing = models.IntegerField(blank=True, null=True)
    number_hous = models.CharField(max_length=16, blank=True, null=True)
    letter_housing = models.CharField(max_length=1, blank=True, null=True)
    zip = models.CharField(max_length=6, blank=True, null=True)
    opening = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    code = models.IntegerField()

    class Meta:
        db_table = 'base_cinema'


class BaseCinemaMetro(models.Model):
    cinema_id = models.IntegerField()
    metro_id = models.IntegerField()

    class Meta:
        db_table = 'base_cinema_metro'
        unique_together = (('cinema_id', 'metro_id'),)


class BaseCinemaName(models.Model):
    cinema_id = models.IntegerField()
    namecinema_id = models.IntegerField()

    class Meta:
        db_table = 'base_cinema_name'
        unique_together = (('cinema_id', 'namecinema_id'),)


class BaseCinemaPhone(models.Model):
    cinema_id = models.IntegerField()
    phone_id = models.IntegerField()

    class Meta:
        db_table = 'base_cinema_phone'
        unique_together = (('cinema_id', 'phone_id'),)


class BaseCinemaSite(models.Model):
    cinema_id = models.IntegerField()
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_cinema_site'
        unique_together = (('cinema_id', 'site_id'),)


class BaseCinemacircuit(models.Model):
    name = models.CharField(max_length=64)
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_cinemacircuit'


class BaseCity(models.Model):
    phone_code = models.IntegerField(blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_city'


class BaseCityName(models.Model):
    city_id = models.IntegerField()
    namecity_id = models.IntegerField()

    class Meta:
        db_table = 'base_city_name'
        unique_together = (('city_id', 'namecity_id'),)


class BaseComposition(models.Model):
    runtime = models.CharField(max_length=16, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tablature = models.TextField(blank=True, null=True)
    source_id = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_composition'


class BaseCompositionCountry(models.Model):
    composition_id = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        db_table = 'base_composition_country'
        unique_together = (('composition_id', 'country_id'),)


class BaseCompositionMedia(models.Model):
    composition_id = models.IntegerField()
    mediafiles_id = models.IntegerField()

    class Meta:
        db_table = 'base_composition_media'


class BaseCompositionName(models.Model):
    composition_id = models.IntegerField()
    compositionname_id = models.IntegerField()

    class Meta:
        db_table = 'base_composition_name'
        unique_together = (('composition_id', 'compositionname_id'),)


class BaseCompositionTags(models.Model):
    composition_id = models.IntegerField()
    newstags_id = models.IntegerField()

    class Meta:
        db_table = 'base_composition_tags'
        unique_together = (('composition_id', 'newstags_id'),)


class BaseCompositionText(models.Model):
    composition_id = models.IntegerField()
    news_id = models.IntegerField()

    class Meta:
        db_table = 'base_composition_text'
        unique_together = (('composition_id', 'news_id'),)


#class BaseCompositionname(models.Model):
#    status = models.IntegerField()
#    name = models.CharField(max_length=256)
#
#    class Meta:
#     
#        db_table = 'base_compositionname'


class BaseCompositionpersonrel(models.Model):
    person_id = models.IntegerField()
    composition_id = models.IntegerField()

    class Meta:
        db_table = 'base_compositionpersonrel'


class BaseCompositionpersonrelType(models.Model):
    compositionpersonrel_id = models.IntegerField()
    compositionpersontype_id = models.IntegerField()

    class Meta:
        db_table = 'base_compositionpersonrel_type'
        unique_together = (('compositionpersonrel_id', 'compositionpersontype_id'),)


class BaseCompositionpersontype(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_compositionpersontype'


class BaseCompositiontracktmp(models.Model):
    url = models.CharField(max_length=256)
    error = models.IntegerField()

    class Meta:
        db_table = 'base_compositiontracktmp'


class BaseCopyfilmaddvalue(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'base_copyfilmaddvalue'


class BaseCopyfilmformat(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'base_copyfilmformat'


class BaseCopyfilmtype(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'base_copyfilmtype'


class BaseCountry(models.Model):
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_country'


class BaseCurrencyrate(models.Model):
    currency = models.CharField(max_length=1)
    country_id = models.IntegerField()
    value = models.FloatField()
    by_currency = models.CharField(max_length=1)
    date = models.DateField()

    class Meta:
        db_table = 'base_currencyrate'


class BaseDemonstration(models.Model):
    name = models.CharField(max_length=256)
    time = models.DateTimeField()
    place_id = models.IntegerField()

    class Meta:
        db_table = 'base_demonstration'


class BaseDialogmessages(models.Model):

    class Meta:
        db_table = 'base_dialogmessages'


class BaseDialogmessagesReaders(models.Model):
    dialogmessages_id = models.IntegerField()
    newsreaders_id = models.IntegerField()

    class Meta:
        db_table = 'base_dialogmessages_readers'
        unique_together = (('dialogmessages_id', 'newsreaders_id'),)


class BaseDistributors(models.Model):
    iid = models.BigIntegerField(blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    usa = models.IntegerField()

    class Meta:
        db_table = 'base_distributors'


class BaseDistributorsFilm(models.Model):
    distributors_id = models.IntegerField()
    film_id = models.IntegerField()

    class Meta:
        db_table = 'base_distributors_film'
        unique_together = (('distributors_id', 'film_id'),)


class BaseDistributorsName(models.Model):
    distributors_id = models.IntegerField()
    namedistributors_id = models.IntegerField()

    class Meta:
        db_table = 'base_distributors_name'
        unique_together = (('distributors_id', 'namedistributors_id'),)


class BaseEmailnotice(models.Model):
    email = models.CharField(max_length=256)
    count = models.IntegerField()
    dtime = models.DateTimeField()
    type = models.IntegerField()

    class Meta:
        db_table = 'base_emailnotice'


class BaseFestcompetition(models.Model):
    name_en = models.CharField(max_length=256)
    name_ru = models.CharField(max_length=256)
    type = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_festcompetition'


class BaseFilms(models.Model):
    year = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)
    rated = models.IntegerField(blank=True, null=True)
    budget_id = models.IntegerField(blank=True, null=True)
    imdb_id = models.IntegerField(blank=True, null=True)
    imdb_rate = models.FloatField(blank=True, null=True)
    imdb_votes = models.IntegerField(blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    generated = models.IntegerField()
    generated_dtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'base_films'


class BaseFilmsCountry(models.Model):
    films_id = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_country'
        unique_together = (('films_id', 'country_id'),)


class BaseFilmsDistributor(models.Model):
    films_id = models.IntegerField()
    distributors_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_distributor'


class BaseFilmsGenre(models.Model):
    films_id = models.IntegerField()
    genre_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_genre'
        unique_together = (('films_id', 'genre_id'),)


class BaseFilmsImages(models.Model):
    films_id = models.IntegerField()
    images_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_images'


class BaseFilmsName(models.Model):
    films_id = models.IntegerField()
    namefilms_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_name'
        unique_together = (('films_id', 'namefilms_id'),)


class BaseFilmsProduction(models.Model):
    films_id = models.IntegerField()
    productionsco_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_production'
        unique_together = (('films_id', 'productionsco_id'),)


class BaseFilmsRelease(models.Model):
    films_id = models.IntegerField()
    filmsreleasedate_id = models.IntegerField()

    class Meta:
        db_table = 'base_films_release'
        unique_together = (('films_id', 'filmsreleasedate_id'),)


class BaseFilmsbudget(models.Model):
    kid = models.IntegerField()
    budget = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_filmsbudget'


class BaseFilmsreleasedate(models.Model):
    release = models.DateField()
    note = models.CharField(max_length=256, blank=True, null=True)
    format = models.CharField(max_length=1)
    country_id = models.IntegerField()

    class Meta:
        db_table = 'base_filmsreleasedate'


class BaseFilmssources(models.Model):
    id_films_id = models.IntegerField()
    source_id = models.IntegerField()
    id_films_sources = models.BigIntegerField()

    class Meta:
        db_table = 'base_filmssources'


class BaseFilmsvotes(models.Model):
    kid = models.IntegerField()
    user_id = models.IntegerField()
    rate_1 = models.IntegerField()
    rate_2 = models.IntegerField()
    rate_3 = models.IntegerField()

    class Meta:
        db_table = 'base_filmsvotes'


class BaseForumgeneral(models.Model):
    name = models.CharField(max_length=64)
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_forumgeneral'


class BaseForumgeneralTopics(models.Model):
    forumgeneral_id = models.IntegerField()
    news_id = models.IntegerField()

    class Meta:
        db_table = 'base_forumgeneral_topics'
        unique_together = (('forumgeneral_id', 'news_id'),)


class BaseGenre(models.Model):
    name = models.CharField(max_length=64)
    name_en = models.CharField(max_length=64, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_genre'


class BaseHall(models.Model):
    number = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    screen_size_w = models.IntegerField(blank=True, null=True)
    screen_size_h = models.IntegerField(blank=True, null=True)
    image_format = models.CharField(max_length=1)
    sound_format = models.CharField(max_length=1)
    cinema_id = models.IntegerField()
    max_price = models.IntegerField(blank=True, null=True)
    min_price = models.IntegerField(blank=True, null=True)
    kid = models.IntegerField()

    class Meta:
        db_table = 'base_hall'


class BaseHallName(models.Model):
    hall_id = models.IntegerField()
    namehall_id = models.IntegerField()

    class Meta:
        db_table = 'base_hall_name'
        unique_together = (('hall_id', 'namehall_id'),)


class BaseHallssources(models.Model):
    id_hall_id = models.IntegerField()
    source_id = models.IntegerField()
    url_hall_sources = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_hallssources'


class BaseImageparameter(models.Model):
    dimension = models.CharField(max_length=1)
    color = models.CharField(max_length=1)
    aspect_ratio = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_imageparameter'


class BaseImages(models.Model):
    file = models.CharField(max_length=256)
    status = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_images'


class BaseImdb(models.Model):
    id_imdb = models.BigIntegerField()
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'base_imdb'


class BaseImportsources(models.Model):
    url = models.CharField(max_length=256)
    source = models.CharField(max_length=64)
    code = models.IntegerField(blank=True, null=True)
    dump = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'base_importsources'


class BaseIntegralrating(models.Model):
    afisha_id = models.IntegerField(blank=True, null=True)
    i_rate = models.FloatField(blank=True, null=True)
    trouble = models.CharField(max_length=50, blank=True, null=True)
    imdb = models.FloatField(blank=True, null=True)
    reviews = models.FloatField(blank=True, null=True)
    rotten = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'base_integralrating'


class BaseInterface(models.Model):
    ip_address = models.CharField(max_length=15, blank=True, null=True)
    platform = models.CharField(max_length=64, blank=True, null=True)
    browser = models.CharField(max_length=64, blank=True, null=True)
    display = models.CharField(max_length=12, blank=True, null=True)
    timezone = models.CharField(max_length=64, blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_interface'


class BaseKifilmrelations(models.Model):
    kid = models.BigIntegerField()

    class Meta:
        db_table = 'base_kifilmrelations'


class BaseKifilmrelationsName(models.Model):
    kifilmrelations_id = models.IntegerField()
    namefilms_id = models.IntegerField()

    class Meta:
        db_table = 'base_kifilmrelations_name'
        unique_together = (('kifilmrelations_id', 'namefilms_id'),)


class BaseLanguage(models.Model):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        db_table = 'base_language'


class BaseLanguagecountry(models.Model):
    language_id = models.IntegerField()
    country_id = models.IntegerField()

    class Meta:
        db_table = 'base_languagecountry'


class BaseLetsgetbank(models.Model):
    name = models.CharField(max_length=128)
    account = models.CharField(max_length=64)
    site_id = models.IntegerField(blank=True, null=True)
    subdomain = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_letsgetbank'


class BaseLetsgetcalendar(models.Model):
    event_name = models.CharField(max_length=256, blank=True, null=True)
    event_place = models.CharField(max_length=256, blank=True, null=True)
    dtime = models.DateTimeField(unique=True)
    sms = models.IntegerField()
    email = models.IntegerField()
    start_notify_sms = models.CharField(max_length=2)
    start_notify_email = models.CharField(max_length=2)
    start_notify_sms_dtime = models.DateTimeField(blank=True, null=True)
    start_notify_email_dtime = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=1)
    price = models.CharField(max_length=16, blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    client_id = models.IntegerField()
    bank_id = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    pdf = models.CharField(max_length=64, blank=True, null=True)
    paid = models.IntegerField()
    bcr = models.IntegerField(blank=True, null=True)
    bcr_code = models.CharField(max_length=128, blank=True, null=True)
    num_sessions = models.IntegerField()
    invoice_template_id = models.IntegerField(blank=True, null=True)
    auto = models.IntegerField()
    subdomain = models.CharField(max_length=128, blank=True, null=True)
    report_id = models.IntegerField(blank=True, null=True)
    report_send = models.IntegerField()

    class Meta:
        db_table = 'base_letsgetcalendar'


class BaseLetsgetcalendarClients(models.Model):
    letsgetcalendar_id = models.IntegerField()
    letsgetclients_id = models.IntegerField()

    class Meta:
        db_table = 'base_letsgetcalendar_clients'


class BaseLetsgetcalendarclientnotified(models.Model):
    client_id = models.IntegerField()
    invite_notified = models.IntegerField()
    invite_status = models.CharField(max_length=128, blank=True, null=True)
    invite_dtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'base_letsgetcalendarclientnotified'


class BaseLetsgetcalendarnotified(models.Model):
    event_id = models.IntegerField()
    profile_id = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    sms_notified = models.IntegerField()
    sms_status = models.CharField(max_length=128, blank=True, null=True)
    sms_id = models.CharField(max_length=64, blank=True, null=True)
    email_notified = models.IntegerField()
    email_status = models.CharField(max_length=128, blank=True, null=True)
    invite_notified = models.IntegerField()
    invite_status = models.CharField(max_length=128, blank=True, null=True)
    invoice_notified = models.IntegerField()
    invoice_status = models.CharField(max_length=128, blank=True, null=True)
    sms_dtime = models.DateTimeField(blank=True, null=True)
    email_dtime = models.DateTimeField(blank=True, null=True)
    invite_dtime = models.DateTimeField(blank=True, null=True)
    invoice_dtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'base_letsgetcalendarnotified'


class BaseLetsgetclients(models.Model):
    profile_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField(blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    tag = models.CharField(max_length=128, blank=True, null=True)
    subdomain = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_letsgetclients'


class BaseLikes(models.Model):
    evaluation = models.IntegerField()
    film = models.IntegerField()
    dtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'base_likes'


class BaseLogger(models.Model):
    text = models.CharField(max_length=256)
    url = models.CharField(max_length=256, blank=True, null=True)
    obj_name = models.CharField(max_length=256, blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)
    event = models.IntegerField()
    code = models.IntegerField()

    class Meta:
        db_table = 'base_logger'


class BaseMediafiles(models.Model):
    sign = models.CharField(max_length=256)
    path = models.CharField(max_length=256)
    profile_id = models.IntegerField()
    dtime = models.DateTimeField()
    tmp = models.IntegerField()
    size = models.CharField(max_length=32, blank=True, null=True)
    bitrate = models.CharField(max_length=32, blank=True, null=True)
    runtime = models.CharField(max_length=16, blank=True, null=True)
    original_file_name = models.CharField(max_length=256, blank=True, null=True)
    original_artist = models.CharField(max_length=128, blank=True, null=True)
    original_album = models.CharField(max_length=128, blank=True, null=True)
    original_title = models.CharField(max_length=128, blank=True, null=True)
    mtype = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_mediafiles'


class BaseMediafilesTags(models.Model):
    mediafiles_id = models.IntegerField()
    newstags_id = models.IntegerField()

    class Meta:
        db_table = 'base_mediafiles_tags'


class BaseMegamag(models.Model):
    megamag_id = models.CharField(max_length=64)
    city_id = models.IntegerField()
    cinema_id = models.IntegerField()
    film_kid = models.IntegerField()
    film_name = models.CharField(max_length=128)
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_megamag'


class BaseMetro(models.Model):
    name = models.CharField(max_length=64)
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_metro'


class BaseMoviemegogo(models.Model):
    afisha_id = models.IntegerField(blank=True, null=True)
    megogo_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    title_en = models.CharField(max_length=128, blank=True, null=True)
    genres = models.CharField(max_length=256, blank=True, null=True)
    serial = models.IntegerField()
    page = models.CharField(max_length=256, blank=True, null=True)
    type_f = models.CharField(max_length=10, blank=True, null=True)
    kinopoisk_id = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=128, blank=True, null=True)
    budget = models.CharField(max_length=20, blank=True, null=True)
    premiere = models.CharField(max_length=20, blank=True, null=True)
    dvd = models.CharField(max_length=20, blank=True, null=True)
    duration = models.CharField(max_length=20, blank=True, null=True)
    kinopoisk = models.FloatField(blank=True, null=True)
    imdb = models.FloatField(blank=True, null=True)
    story = models.TextField(blank=True, null=True)
    poster_url = models.CharField(max_length=256, blank=True, null=True)
    poster_thumbnail = models.CharField(max_length=256, blank=True, null=True)
    rel_ignore = models.IntegerField()

    class Meta:
        db_table = 'base_moviemegogo'


class BaseNamecinema(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namecinema'


class BaseNamecity(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namecity'


class BaseNamedistributors(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namedistributors'


class BaseNamefilms(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namefilms'


class BaseNamehall(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_namehall'


class BaseNameperson(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_nameperson'


class BaseNameproduct(models.Model):
    status = models.IntegerField()
    language_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_nameproduct'


class BaseNews(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    dtime = models.DateTimeField()
    visible = models.IntegerField()
    img = models.CharField(max_length=256, blank=True, null=True)
    video = models.CharField(max_length=256, blank=True, null=True)
    autor_id = models.IntegerField(blank=True, null=True)
    site_id = models.IntegerField()
    subdomain = models.CharField(max_length=128)
    world_pub = models.IntegerField()
    reader_type = models.CharField(max_length=2, blank=True, null=True)
    autor_status = models.IntegerField()
    autor_nick = models.IntegerField()
    extra = models.CharField(max_length=256, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    language_id = models.IntegerField(blank=True, null=True)
    views = models.IntegerField()
    parent_id = models.IntegerField(blank=True, null=True)
    branch_id = models.IntegerField(blank=True, null=True)
    translation_for_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_news'


class BaseNewsReaders(models.Model):
    news_id = models.IntegerField()
    newsreaders_id = models.IntegerField()

    class Meta:
        db_table = 'base_news_readers'


class BaseNewsTags(models.Model):
    news_id = models.IntegerField()
    newstags_id = models.IntegerField()

    class Meta:
        db_table = 'base_news_tags'
        unique_together = (('news_id', 'newstags_id'),)


class BaseNewsaltertranslation(models.Model):
    news_id = models.IntegerField()
    title = models.CharField(max_length=128)
    text = models.TextField()
    language_id = models.IntegerField()

    class Meta:
        db_table = 'base_newsaltertranslation'


class BaseNewsaltertranslationTags(models.Model):
    newsaltertranslation_id = models.IntegerField()
    newstags_id = models.IntegerField()

    class Meta:
        db_table = 'base_newsaltertranslation_tags'
        unique_together = (('newsaltertranslation_id', 'newstags_id'),)


class BaseNewsfilms(models.Model):
    kid = models.IntegerField()
    message_id = models.IntegerField()
    source_id = models.CharField(max_length=128, blank=True, null=True)
    source_obj_id = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    rate_1 = models.IntegerField(blank=True, null=True)
    rate_2 = models.IntegerField(blank=True, null=True)
    rate_3 = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_newsfilms'


#class BaseNewsreaders(models.Model):
#    user_id = models.IntegerField()
#    status = models.CharField(max_length=1)
#    message_id = models.IntegerField()
#
#    class Meta:
#     
#        db_table = 'base_newsreaders'


#class BaseNewstags(models.Model):
#
#    class Meta:
#     
#        db_table = 'base_newstags'


class BaseNotfoundcinemasrelations(models.Model):
    name = models.CharField(max_length=128)
    kid = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_notfoundcinemasrelations'


class BaseNotfoundfilmsrelations(models.Model):
    name = models.CharField(max_length=128)
    kid = models.IntegerField()
    source_obj_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_notfoundfilmsrelations'


class BaseNotfoundpersonsrelations(models.Model):
    name = models.CharField(max_length=128)
    kid = models.IntegerField()

    class Meta:
        db_table = 'base_notfoundpersonsrelations'


class BaseNowru(models.Model):
    nowru_id = models.IntegerField()
    idec = models.IntegerField()
    kinopoisk_id = models.IntegerField(blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    regions = models.CharField(max_length=256)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    player_code = models.CharField(max_length=256)
    url_api = models.CharField(max_length=256)
    url_web = models.CharField(max_length=256)
    url_poster = models.CharField(max_length=256, blank=True, null=True)
    url_image = models.CharField(max_length=256, blank=True, null=True)
    url_player = models.CharField(max_length=256, blank=True, null=True)
    rel_ignore = models.IntegerField()

    class Meta:
        db_table = 'base_nowru'


class BaseOkinoua(models.Model):
    imdb = models.IntegerField(blank=True, null=True)
    kid = models.IntegerField()
    url = models.CharField(max_length=256)
    name_ru = models.CharField(max_length=128)
    name_ua = models.CharField(max_length=128, blank=True, null=True)
    release = models.DateField()
    distributor = models.CharField(max_length=256)

    class Meta:
        db_table = 'base_okinoua'


class BaseOrganization(models.Model):
    name = models.CharField(max_length=256)
    uni_slug = models.CharField(max_length=256)
    slug = models.CharField(max_length=256)
    ownership = models.CharField(max_length=1, blank=True, null=True)
    room_num = models.IntegerField(blank=True, null=True)
    room_type = models.CharField(max_length=1, blank=True, null=True)
    site = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=256, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    source_obj_id = models.IntegerField(blank=True, null=True)
    source_id = models.CharField(max_length=256, blank=True, null=True)
    edited = models.DateTimeField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    trailer = models.CharField(max_length=256, blank=True, null=True)
    creator_id = models.IntegerField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    note_accept = models.IntegerField()
    visible = models.IntegerField()
    owner = models.CharField(max_length=128, blank=True, null=True)
    alter_name = models.CharField(max_length=256, blank=True, null=True)
    branding = models.CharField(max_length=256, blank=True, null=True)
    domain_id = models.IntegerField(blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    circuit_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_organization'


class BaseOrganizationBuildings(models.Model):
    organization_id = models.IntegerField()
    building_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_buildings'
        unique_together = (('organization_id', 'building_id'),)


class BaseOrganizationEditors(models.Model):
    organization_id = models.IntegerField()
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_editors'


class BaseOrganizationImages(models.Model):
    organization_id = models.IntegerField()
    organizationimages_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_images'


class BaseOrganizationPhones(models.Model):
    organization_id = models.IntegerField()
    organizationphones_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_phones'
        unique_together = (('organization_id', 'organizationphones_id'),)


class BaseOrganizationRelations(models.Model):
    organization_id = models.IntegerField()
    organizationrelations_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_relations'


class BaseOrganizationStaff(models.Model):
    organization_id = models.IntegerField()
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_staff'


class BaseOrganizationTags(models.Model):
    organization_id = models.IntegerField()
    organizationtags_id = models.IntegerField()

    class Meta:
        db_table = 'base_organization_tags'
        unique_together = (('organization_id', 'organizationtags_id'),)


#class BaseOrganizationimages(models.Model):
#    img = models.CharField(max_length=256)
#    status = models.IntegerField()
#
#    class Meta:
#     
#        db_table = 'base_organizationimages'


class BaseOrganizationlang(models.Model):
    organization_id = models.IntegerField()
    name = models.CharField(max_length=256)
    note = models.TextField(blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)
    language_id = models.IntegerField()

    class Meta:
        db_table = 'base_organizationlang'


class BaseOrganizationlangBuildings(models.Model):
    organizationlang_id = models.IntegerField()
    building_id = models.IntegerField()

    class Meta:
        db_table = 'base_organizationlang_buildings'
        unique_together = (('organizationlang_id', 'building_id'),)


class BaseOrganizationmenu(models.Model):
    tag_id = models.IntegerField()

    class Meta:
        db_table = 'base_organizationmenu'


class BaseOrganizationnews(models.Model):
    news_id = models.IntegerField()
    organization_id = models.IntegerField()
    tag_id = models.IntegerField(blank=True, null=True)
    group_flag = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_organizationnews'


#class BaseOrganizationphones(models.Model):
#    phone = models.CharField(max_length=64)
#    note = models.CharField(max_length=128, blank=True, null=True)
#
#    class Meta:
#     
#        db_table = 'base_organizationphones'


#class BaseOrganizationrelations(models.Model):
#    name = models.CharField(max_length=128)
#    link = models.CharField(max_length=256)

#    class Meta:
#     
#        db_table = 'base_organizationrelations'


#class BaseOrganizationtags(models.Model):
#    name = models.CharField(max_length=128)
#    alter_name = models.CharField(max_length=128, blank=True, null=True)
#    group_flag = models.CharField(max_length=128, blank=True, null=True)
#
#    class Meta:
#     
#        db_table = 'base_organizationtags'


class BaseOrgmenu(models.Model):
    organization_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=256)
    profile_id = models.IntegerField(blank=True, null=True)
    private = models.IntegerField()

    class Meta:
        db_table = 'base_orgmenu'


class BaseOrgmenuSubmenu(models.Model):
    orgmenu_id = models.IntegerField()
    orgsubmenu_id = models.IntegerField()

    class Meta:
        db_table = 'base_orgmenu_submenu'
        unique_together = (('orgmenu_id', 'orgsubmenu_id'),)


class BaseOrgmenulang(models.Model):
    orgmenu_id = models.IntegerField()
    name = models.CharField(max_length=256)
    language_id = models.IntegerField()

    class Meta:
        db_table = 'base_orgmenulang'


class BaseOrgsubmenu(models.Model):
    name = models.CharField(max_length=256)
    page_type = models.CharField(max_length=1, blank=True, null=True)
    url = models.CharField(max_length=64, blank=True, null=True)
    booker_profile_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_orgsubmenu'


class BaseOrgsubmenuGallery(models.Model):
    orgsubmenu_id = models.IntegerField()
    projectsgallery_id = models.IntegerField()

    class Meta:
        db_table = 'base_orgsubmenu_gallery'


class BaseOrgsubmenuNews(models.Model):
    orgsubmenu_id = models.IntegerField()
    news_id = models.IntegerField()

    class Meta:
        db_table = 'base_orgsubmenu_news'
        unique_together = (('orgsubmenu_id', 'news_id'),)


class BaseOrgsubmenulang(models.Model):
    orgsubmenu_id = models.IntegerField()
    name = models.CharField(max_length=256)
    language_id = models.IntegerField()

    class Meta:
        db_table = 'base_orgsubmenulang'


class BasePaidactions(models.Model):
    profile_id = models.IntegerField()
    action_id = models.IntegerField()
    object = models.CharField(max_length=256, blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    dtime = models.DateTimeField()
    allow = models.IntegerField()
    ignore = models.IntegerField()
    number = models.IntegerField()
    act = models.CharField(max_length=1, blank=True, null=True)
    future = models.IntegerField()
    director_id = models.IntegerField(blank=True, null=True)
    stage_id = models.IntegerField(blank=True, null=True)
    is_accepted = models.IntegerField()

    class Meta:
        db_table = 'base_paidactions'


class BasePerson(models.Model):
    iid = models.BigIntegerField(blank=True, null=True)
    kid = models.BigIntegerField(blank=True, null=True)
    male = models.IntegerField(blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    city_id = models.IntegerField(blank=True, null=True)
    artist = models.IntegerField()
    is_group = models.IntegerField()
    text = models.TextField(blank=True, null=True)
    video = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_person'


class BasePersonMusician(models.Model):
    from_person_id = models.IntegerField()
    to_person_id = models.IntegerField()

    class Meta:
        db_table = 'base_person_musician'


class BasePersonName(models.Model):
    person_id = models.IntegerField()
    nameperson_id = models.IntegerField()

    class Meta:
        db_table = 'base_person_name'
        unique_together = (('person_id', 'nameperson_id'),)


class BasePersonPoster(models.Model):
    person_id = models.IntegerField()
    images_id = models.IntegerField()

    class Meta:
        db_table = 'base_person_poster'


class BasePersoninterface(models.Model):
    option1 = models.IntegerField()
    option2 = models.IntegerField()
    option3 = models.IntegerField()
    option4 = models.IntegerField()
    first_change = models.IntegerField()
    changed = models.IntegerField()
    temp_subscription = models.IntegerField(blank=True, null=True)
    temp_subscription_topics = models.IntegerField(blank=True, null=True)
    money = models.FloatField()
    wf_topic = models.IntegerField(blank=True, null=True)
    wf_last = models.IntegerField(blank=True, null=True)
    wf_style = models.CharField(max_length=7, blank=True, null=True)
    wf_msg_open = models.IntegerField()

    class Meta:
        db_table = 'base_personinterface'


class BasePersoninterfaceLikes(models.Model):
    personinterface_id = models.IntegerField()
    likes_id = models.IntegerField()

    class Meta:
        db_table = 'base_personinterface_likes'


class BasePhone(models.Model):
    phone = models.CharField(max_length=64)
    phone_type = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_phone'


class BasePost(models.Model):
    title = models.CharField(max_length=128, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    dtime = models.DateTimeField()
    visible = models.IntegerField()

    class Meta:
        db_table = 'base_post'


class BaseProductionsco(models.Model):
    name = models.CharField(max_length=256)
    imdb_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_productionsco'


class BaseProfile(models.Model):
    user_id = models.IntegerField(unique=True)
    person_id = models.IntegerField(blank=True, null=True)
    personinterface_id = models.IntegerField(blank=True, null=True)
    login_counter = models.IntegerField(blank=True, null=True)
    auth_status = models.IntegerField()
    folder = models.CharField(max_length=128)
    site_id = models.IntegerField()
    show_profile = models.CharField(max_length=1)
    path = models.CharField(max_length=256, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    phone_visible = models.IntegerField()
    kid = models.IntegerField(blank=True, null=True)
    bg = models.CharField(max_length=64, blank=True, null=True)
    bg_url = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_profile'


class BaseProfileAccounts(models.Model):
    profile_id = models.IntegerField()
    accounts_id = models.IntegerField()

    class Meta:
        db_table = 'base_profile_accounts'
        unique_together = (('profile_id', 'accounts_id'),)


class BaseProfileInterface(models.Model):
    profile_id = models.IntegerField()
    interface_id = models.IntegerField()

    class Meta:
        db_table = 'base_profile_interface'
        unique_together = (('profile_id', 'interface_id'),)


class BaseProfileSiteAdmin(models.Model):
    profile_id = models.IntegerField()
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_profile_site_admin'


class BaseProjects(models.Model):
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
    director_id = models.IntegerField(blank=True, null=True)
    email = models.IntegerField()
    sms = models.IntegerField()
    budget = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=1, blank=True, null=True)
    is_public = models.IntegerField()

    class Meta:
        db_table = 'base_projects'


class BaseProjectsDirectors(models.Model):
    projects_id = models.IntegerField()
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_projects_directors'


class BaseProjectsMembers(models.Model):
    projects_id = models.IntegerField()
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_projects_members'


class BaseProjectsStages(models.Model):
    projects_id = models.IntegerField()
    projectstages_id = models.IntegerField()

    class Meta:
        db_table = 'base_projects_stages'


class BaseProjectsgallery(models.Model):
    photo_id = models.IntegerField()
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'base_projectsgallery'


class BaseProjectsgallerylang(models.Model):
    gallery_id = models.IntegerField()
    name = models.CharField(max_length=256)
    title = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    language_id = models.IntegerField()

    class Meta:
        db_table = 'base_projectsgallerylang'


class BaseProjectstages(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()

    class Meta:
        db_table = 'base_projectstages'


class BaseQanswers(models.Model):

    class Meta:
        db_table = 'base_qanswers'


class BaseQanswersItem(models.Model):
    qanswers_id = models.IntegerField()
    news_id = models.IntegerField()

    class Meta:
        db_table = 'base_qanswers_item'
        unique_together = (('qanswers_id', 'news_id'),)


class BaseQuestionanswer(models.Model):

    class Meta:
        db_table = 'base_questionanswer'


class BaseQuestionanswerItem(models.Model):
    questionanswer_id = models.IntegerField()
    news_id = models.IntegerField()

    class Meta:
        db_table = 'base_questionanswer_item'
        unique_together = (('questionanswer_id', 'news_id'),)


class BaseRaspishirelations(models.Model):
    rid = models.IntegerField()
    kid = models.IntegerField(blank=True, null=True)
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_raspishirelations'


class BaseRelationfp(models.Model):
    person_id = models.IntegerField()
    status_act_id = models.IntegerField()
    action_id = models.IntegerField()
    films_id = models.IntegerField()

    class Meta:
        db_table = 'base_relationfp'


class BaseReleases(models.Model):
    name_ru = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    details = models.CharField(max_length=128, blank=True, null=True)
    film_id = models.IntegerField()
    url = models.CharField(max_length=256)
    release_date = models.DateField()
    distributor1 = models.CharField(max_length=128, blank=True, null=True)
    distributor1_id = models.CharField(max_length=24, blank=True, null=True)
    distributor2 = models.CharField(max_length=128, blank=True, null=True)
    distributor2_id = models.CharField(max_length=24, blank=True, null=True)
    copies = models.IntegerField(blank=True, null=True)
    runtime = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_releases'


class BaseReleasesrelations(models.Model):
    film_kid = models.IntegerField()
    distributor_kid = models.IntegerField()
    release_id = models.IntegerField()
    rel_profile_id = models.IntegerField(blank=True, null=True)
    rel_dtime = models.DateTimeField(blank=True, null=True)
    rel_double = models.IntegerField()
    rel_ignore = models.IntegerField()

    class Meta:
        db_table = 'base_releasesrelations'


class BaseRuntime(models.Model):
    runtime = models.IntegerField()
    runtime_note = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'base_runtime'


class BaseSchedulerelations(models.Model):
    name = models.CharField(max_length=128)
    kid = models.IntegerField()
    hall_id = models.IntegerField()
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_schedulerelations'


class BaseSession(models.Model):
    demonstration_id = models.IntegerField()
    number = models.PositiveIntegerField()
    average_price = models.IntegerField(blank=True, null=True)
    number_people = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_session'


class BaseSessionFilm(models.Model):
    session_id = models.IntegerField()
    nameproduct_id = models.IntegerField()

    class Meta:
        db_table = 'base_session_film'
        unique_together = (('session_id', 'nameproduct_id'),)


class BaseSessionsafisharelations(models.Model):
    kid = models.IntegerField()
    source_id = models.IntegerField()
    schedule_id = models.IntegerField()

    class Meta:
        db_table = 'base_sessionsafisharelations'


class BaseSite(models.Model):
    url = models.CharField(max_length=200)
    site_type = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_site'


class BaseSitebanners(models.Model):
    file = models.CharField(max_length=256)
    name = models.CharField(max_length=128)
    url = models.CharField(max_length=256, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    budget = models.IntegerField()
    city_id = models.IntegerField(blank=True, null=True)
    btype = models.CharField(max_length=1)
    views = models.IntegerField()
    profile_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    style = models.CharField(max_length=32, blank=True, null=True)
    balance = models.FloatField()
    bg_disable_dtime_to = models.DateTimeField(blank=True, null=True)
    spent = models.FloatField()
    deleted = models.IntegerField()
    dtime = models.DateTimeField()
    last_show = models.DateField(blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_sitebanners'


class BaseSitebannersCities(models.Model):
    sitebanners_id = models.IntegerField()
    city_id = models.IntegerField()

    class Meta:
        db_table = 'base_sitebanners_cities'


class BaseSitebannersSites(models.Model):
    sitebanners_id = models.IntegerField()
    site_id = models.IntegerField()

    class Meta:
        db_table = 'base_sitebanners_sites'
        unique_together = (('sitebanners_id', 'site_id'),)


class BaseSitebannersclicks(models.Model):
    banner_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_sitebannersclicks'


class BaseSitebannersviews(models.Model):
    banner_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateField()

    class Meta:
        db_table = 'base_sitebannersviews'


class BaseSoundparameter(models.Model):
    sound = models.CharField(max_length=1)
    soundsystem = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_soundparameter'


class BaseSourcecinemas(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    city_id = models.IntegerField()
    cinema_id = models.IntegerField()
    name = models.CharField(max_length=256)
    name_alter = models.CharField(max_length=256, blank=True, null=True)
    address = models.CharField(max_length=256, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'base_sourcecinemas'


class BaseSourcecities(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    city_id = models.IntegerField()
    name = models.CharField(max_length=256)
    name_alter = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_sourcecities'


class BaseSourcefilms(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    name = models.CharField(max_length=256)
    name_alter = models.CharField(max_length=256, blank=True, null=True)
    kid = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    imdb = models.CharField(max_length=64, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)
    rel_profile_id = models.IntegerField(blank=True, null=True)
    rel_dtime = models.DateTimeField(blank=True, null=True)
    rel_double = models.IntegerField()
    rel_ignore = models.IntegerField()

    class Meta:
        db_table = 'base_sourcefilms'


class BaseSourcehalls(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    cinema_id = models.IntegerField()
    name = models.CharField(max_length=256)
    name_alter = models.CharField(max_length=256, blank=True, null=True)
    kid = models.IntegerField()

    class Meta:
        db_table = 'base_sourcehalls'


class BaseSourcereleases(models.Model):
    source_obj_id = models.IntegerField()
    film_id = models.IntegerField()
    release = models.DateField()
    distributor = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_sourcereleases'


class BaseSourceschedules(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    film_id = models.IntegerField()
    cinema_id = models.IntegerField()
    dtime = models.DateTimeField()
    hall = models.IntegerField(blank=True, null=True)
    sale = models.IntegerField()
    price = models.CharField(max_length=64, blank=True, null=True)
    extra = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_sourceschedules'


class BaseSourceusers(models.Model):
    source_id = models.CharField(max_length=256)
    source_obj_id = models.IntegerField()
    profile_id = models.IntegerField()

    class Meta:
        db_table = 'base_sourceusers'


class BaseStatistics(models.Model):
    name = models.CharField(max_length=128)
    sessions = models.IntegerField()
    sessions_sale = models.IntegerField()
    cinemas = models.IntegerField()
    cinemas_sale = models.IntegerField()
    films = models.IntegerField()
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_statistics'


class BaseStatisticsDetails(models.Model):
    statistics_id = models.IntegerField()
    statisticsdetails_id = models.IntegerField()

    class Meta:
        db_table = 'base_statistics_details'
        unique_together = (('statistics_id', 'statisticsdetails_id'),)


#class BaseStatisticsdetails(models.Model):
#    source = models.IntegerField()
#    cinemas = models.IntegerField()
#    cinemas_sale = models.IntegerField()
#    films = models.IntegerField()
#    sessions_sale = models.IntegerField()

#    class Meta:
#     
#        db_table = 'base_statisticsdetails'


class BaseStatusact(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'base_statusact'


class BaseStreet(models.Model):
    name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64)
    type = models.CharField(max_length=2)
    area_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_street'


class BaseStreettype(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_streettype'


class BaseSubscriberlog(models.Model):
    user_id = models.IntegerField()
    obj_id = models.IntegerField()
    notified = models.IntegerField()
    dtime = models.DateTimeField()
    error = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'base_subscriberlog'


class BaseSubscriberobjects(models.Model):
    type = models.CharField(max_length=2)
    obj = models.IntegerField()
    end_obj = models.IntegerField()
    in_work = models.IntegerField()

    class Meta:
        db_table = 'base_subscriberobjects'


class BaseSubscriberuser(models.Model):
    type = models.CharField(max_length=2)
    obj = models.IntegerField()
    profile_id = models.IntegerField()
    dtime = models.DateTimeField()
    unsubscribe = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_subscriberuser'


class BaseSubscriptionfeeds(models.Model):
    dtime = models.DateTimeField()
    profile_id = models.IntegerField()
    type = models.CharField(max_length=1)

    class Meta:
        db_table = 'base_subscriptionfeeds'


class BaseSubscriptionrelease(models.Model):
    profile_id = models.IntegerField()
    release_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField(blank=True, null=True)
    notified = models.IntegerField()
    kid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'base_subscriptionrelease'


class BaseSubscriptiontopics(models.Model):
    profile_id = models.IntegerField()
    kid = models.IntegerField()
    dtime = models.DateTimeField(blank=True, null=True)
    notified = models.IntegerField()
    quality = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        db_table = 'base_subscriptiontopics'


class BaseTop250(models.Model):
    key = models.CharField(max_length=256)
    date_upd = models.DateField()
    film_id = models.IntegerField()
    position = models.IntegerField()
    change = models.IntegerField()
    change_val = models.IntegerField(blank=True, null=True)
    rating = models.FloatField()
    votes = models.IntegerField()

    class Meta:
        db_table = 'base_top250'


class BaseTorrents(models.Model):
    film = models.IntegerField()
    source_obj_id = models.IntegerField(blank=True, null=True)
    go_link_id = models.CharField(max_length=32, blank=True, null=True)
    link = models.CharField(max_length=256, blank=True, null=True)
    tracker = models.CharField(max_length=64, blank=True, null=True)
    quality = models.CharField(max_length=32, blank=True, null=True)
    quality_avg = models.CharField(max_length=1, blank=True, null=True)
    file_size = models.CharField(max_length=32, blank=True, null=True)
    path = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        db_table = 'base_torrents'


class BaseTorrentsusers(models.Model):
    torrent_id = models.IntegerField()
    profile_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField()
    got = models.IntegerField()

    class Meta:
        db_table = 'base_torrentsusers'


class BaseUkrainefilms(models.Model):
    source_id = models.CharField(max_length=128)
    source_obj_id = models.IntegerField()
    kid = models.IntegerField()
    name = models.CharField(max_length=128)
    text = models.TextField()

    class Meta:
        db_table = 'base_ukrainefilms'


class BaseUkraineposters(models.Model):
    source_id = models.CharField(max_length=128)
    source_obj_id = models.IntegerField()
    poster = models.CharField(max_length=100)
    kid = models.IntegerField()

    class Meta:
        db_table = 'base_ukraineposters'


class BaseUkrainianreleases(models.Model):
    kid = models.IntegerField()
    release = models.DateField()

    class Meta:
        db_table = 'base_ukrainianreleases'


class BaseUserdeposit(models.Model):
    summa = models.FloatField()
    profile_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_userdeposit'


class BaseVersion(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'base_version'


class BaseWithdrawmoney(models.Model):
    summa = models.FloatField()
    who_id = models.IntegerField(blank=True, null=True)
    profile_id = models.IntegerField(blank=True, null=True)
    dtime = models.DateTimeField()

    class Meta:
        db_table = 'base_withdrawmoney'


class BaseWomenforumignored(models.Model):
    type = models.IntegerField()
    msg = models.IntegerField(blank=True, null=True)
    branch = models.IntegerField(blank=True, null=True)
    author = models.IntegerField(blank=True, null=True)
    user = models.IntegerField()

    class Meta:
        db_table = 'base_womenforumignored'


class BaseWomenforumignorelevel(models.Model):
    user = models.IntegerField()
    dtime = models.DateTimeField()
    type = models.IntegerField()

    class Meta:
        db_table = 'base_womenforumignorelevel'


class BaseWomenforumlikes(models.Model):
    profile_id = models.IntegerField()
    msg = models.IntegerField()
    like_type = models.IntegerField()

    class Meta:
        db_table = 'base_womenforumlikes'


class CacheTbl(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        db_table = 'cache_tbl'


class ColumnStats(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    column_name = models.CharField(max_length=64)
    min_value = models.CharField(max_length=255, blank=True, null=True)
    max_value = models.CharField(max_length=255, blank=True, null=True)
    nulls_ratio = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    avg_length = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    avg_frequency = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)
    hist_size = models.PositiveIntegerField(blank=True, null=True)
    hist_type = models.CharField(max_length=14, blank=True, null=True)
    histogram = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'column_stats'
        unique_together = (('db_name', 'table_name', 'column_name'),)


class ColumnsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    column_name = models.CharField(db_column='Column_name', max_length=64)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31)  # Field name made lowercase.

    class Meta:
        db_table = 'columns_priv'
        unique_together = (('host', 'db', 'user', 'table_name', 'column_name'),)


class Db(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.
    delete_history_priv = models.CharField(db_column='Delete_history_priv', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'db'
        unique_together = (('host', 'db', 'user'),)





class DjangoOpenidConsumerAssociation(models.Model):
    server_url = models.TextField()
    handle = models.CharField(max_length=255)
    secret = models.TextField()
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.TextField()

    class Meta:
        db_table = 'django_openid_consumer_association'


class DjangoOpenidConsumerNonce(models.Model):
    server_url = models.CharField(max_length=200)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=50)

    class Meta:
        db_table = 'django_openid_consumer_nonce'




class DjangoSite(models.Model):
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'django_site'


class Event(models.Model):
    db = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    body = models.TextField()
    definer = models.CharField(max_length=141)
    execute_at = models.DateTimeField(blank=True, null=True)
    interval_value = models.IntegerField(blank=True, null=True)
    interval_field = models.CharField(max_length=18, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    last_executed = models.DateTimeField(blank=True, null=True)
    starts = models.DateTimeField(blank=True, null=True)
    ends = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=18)
    on_completion = models.CharField(max_length=8)
    sql_mode = models.CharField(max_length=539)
    comment = models.CharField(max_length=64)
    originator = models.PositiveIntegerField()
    time_zone = models.CharField(max_length=64)
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'event'
        unique_together = (('db', 'name'),)


class Func(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    ret = models.IntegerField()
    dl = models.CharField(max_length=128)
    type = models.CharField(max_length=9)

    class Meta:
        db_table = 'func'


class GeneralLog(models.Model):
    event_time = models.DateTimeField()
    user_host = models.TextField()
    thread_id = models.BigIntegerField()
    server_id = models.PositiveIntegerField()
    command_type = models.CharField(max_length=64)
    argument = models.TextField()

    class Meta:
        db_table = 'general_log'


class GtidSlavePos(models.Model):
    domain_id = models.PositiveIntegerField(primary_key=True)
    sub_id = models.BigIntegerField()
    server_id = models.PositiveIntegerField()
    seq_no = models.BigIntegerField()

    class Meta:
        db_table = 'gtid_slave_pos'
        unique_together = (('domain_id', 'sub_id'),)


class HelpCategory(models.Model):
    help_category_id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    parent_category_id = models.PositiveSmallIntegerField(blank=True, null=True)
    url = models.TextField()

    class Meta:
        db_table = 'help_category'


class HelpKeyword(models.Model):
    help_keyword_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)

    class Meta:
        db_table = 'help_keyword'


class HelpRelation(models.Model):
    help_topic_id = models.PositiveIntegerField()
    help_keyword_id = models.PositiveIntegerField(primary_key=True)

    class Meta:
        db_table = 'help_relation'
        unique_together = (('help_keyword_id', 'help_topic_id'),)


class HelpTopic(models.Model):
    help_topic_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=64)
    help_category_id = models.PositiveSmallIntegerField()
    description = models.TextField()
    example = models.TextField()
    url = models.TextField()

    class Meta:
        db_table = 'help_topic'


class Host(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'host'
        unique_together = (('host', 'db'),)


class IndexStats(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    index_name = models.CharField(max_length=64)
    prefix_arity = models.PositiveIntegerField()
    avg_frequency = models.DecimalField(max_digits=12, decimal_places=4, blank=True, null=True)

    class Meta:
        db_table = 'index_stats'
        unique_together = (('db_name', 'table_name', 'index_name', 'prefix_arity'),)


class InnodbIndexStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=199)
    index_name = models.CharField(max_length=64)
    last_update = models.DateTimeField()
    stat_name = models.CharField(max_length=64)
    stat_value = models.BigIntegerField()
    sample_size = models.BigIntegerField(blank=True, null=True)
    stat_description = models.CharField(max_length=1024)

    class Meta:
        db_table = 'innodb_index_stats'
        unique_together = (('database_name', 'table_name', 'index_name', 'stat_name'),)


class InnodbTableStats(models.Model):
    database_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=199)
    last_update = models.DateTimeField()
    n_rows = models.BigIntegerField()
    clustered_index_size = models.BigIntegerField()
    sum_of_other_index_sizes = models.BigIntegerField()

    class Meta:
        db_table = 'innodb_table_stats'
        unique_together = (('database_name', 'table_name'),)


class LinkexchangeDjangoDbhash(models.Model):
    dbname = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    mtime = models.DateTimeField()

    class Meta:
        db_table = 'linkexchange_django_dbhash'
        unique_together = (('dbname', 'key'),)


class LinkexchangeDjangoDbhashitem(models.Model):
    hash_id = models.IntegerField()
    key = models.CharField(max_length=332)
    value = models.TextField()

    class Meta:
        db_table = 'linkexchange_django_dbhashitem'
        unique_together = (('hash_id', 'key'),)


class Plugin(models.Model):
    name = models.CharField(primary_key=True, max_length=64)
    dl = models.CharField(max_length=128)

    class Meta:
        db_table = 'plugin'


class Proc(models.Model):
    db = models.CharField(primary_key=True, max_length=64)
    name = models.CharField(max_length=64)
    type = models.CharField(max_length=12)
    specific_name = models.CharField(max_length=64)
    language = models.CharField(max_length=3)
    sql_data_access = models.CharField(max_length=17)
    is_deterministic = models.CharField(max_length=3)
    security_type = models.CharField(max_length=7)
    param_list = models.TextField()
    returns = models.TextField()
    body = models.TextField()
    definer = models.CharField(max_length=141)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    sql_mode = models.CharField(max_length=539)
    comment = models.TextField()
    character_set_client = models.CharField(max_length=32, blank=True, null=True)
    collation_connection = models.CharField(max_length=32, blank=True, null=True)
    db_collation = models.CharField(max_length=32, blank=True, null=True)
    body_utf8 = models.TextField(blank=True, null=True)
    aggregate = models.CharField(max_length=5)

    class Meta:
        db_table = 'proc'
        unique_together = (('db', 'name', 'type'),)


class ProcsPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    routine_name = models.CharField(db_column='Routine_name', max_length=64)  # Field name made lowercase.
    routine_type = models.CharField(db_column='Routine_type', max_length=12)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=141)  # Field name made lowercase.
    proc_priv = models.CharField(db_column='Proc_priv', max_length=27)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        db_table = 'procs_priv'
        unique_together = (('host', 'db', 'user', 'routine_name', 'routine_type'),)


class ProxiesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    proxied_host = models.CharField(db_column='Proxied_host', max_length=60)  # Field name made lowercase.
    proxied_user = models.CharField(db_column='Proxied_user', max_length=80)  # Field name made lowercase.
    with_grant = models.IntegerField(db_column='With_grant')  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=141)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.

    class Meta:
        db_table = 'proxies_priv'
        unique_together = (('host', 'user', 'proxied_host', 'proxied_user'),)


class RegistrationRegistrationprofile(models.Model):
    user_id = models.IntegerField(unique=True)
    activation_key = models.CharField(max_length=40)

    class Meta:
        db_table = 'registration_registrationprofile'


class RolesMapping(models.Model):
    host = models.CharField(db_column='Host', max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    role = models.CharField(db_column='Role', max_length=80)  # Field name made lowercase.
    admin_option = models.CharField(db_column='Admin_option', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'roles_mapping'
        unique_together = (('host', 'user', 'role'),)


class Servers(models.Model):
    server_name = models.CharField(db_column='Server_name', primary_key=True, max_length=64)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=2048)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=80)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=64)  # Field name made lowercase.
    port = models.IntegerField(db_column='Port')  # Field name made lowercase.
    socket = models.CharField(db_column='Socket', max_length=64)  # Field name made lowercase.
    wrapper = models.CharField(db_column='Wrapper', max_length=64)  # Field name made lowercase.
    owner = models.CharField(db_column='Owner', max_length=512)  # Field name made lowercase.

    class Meta:
        db_table = 'servers'


class SlowLog(models.Model):
    start_time = models.DateTimeField()
    user_host = models.TextField()
    query_time = models.TimeField()
    lock_time = models.TimeField()
    rows_sent = models.IntegerField()
    rows_examined = models.IntegerField()
    db = models.CharField(max_length=512)
    last_insert_id = models.IntegerField()
    insert_id = models.IntegerField()
    server_id = models.PositiveIntegerField()
    sql_text = models.TextField()
    thread_id = models.BigIntegerField()
    rows_affected = models.IntegerField()

    class Meta:
        db_table = 'slow_log'


class TableStats(models.Model):
    db_name = models.CharField(primary_key=True, max_length=64)
    table_name = models.CharField(max_length=64)
    cardinality = models.BigIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'table_stats'
        unique_together = (('db_name', 'table_name'),)


class TablesPriv(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    db = models.CharField(db_column='Db', max_length=64)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    table_name = models.CharField(db_column='Table_name', max_length=64)  # Field name made lowercase.
    grantor = models.CharField(db_column='Grantor', max_length=141)  # Field name made lowercase.
    timestamp = models.DateTimeField(db_column='Timestamp')  # Field name made lowercase.
    table_priv = models.CharField(db_column='Table_priv', max_length=121)  # Field name made lowercase.
    column_priv = models.CharField(db_column='Column_priv', max_length=31)  # Field name made lowercase.

    class Meta:
        db_table = 'tables_priv'
        unique_together = (('host', 'db', 'user', 'table_name'),)


class TimeZone(models.Model):
    time_zone_id = models.AutoField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    use_leap_seconds = models.CharField(db_column='Use_leap_seconds', max_length=1)  # Field name made lowercase.

    class Meta:
        db_table = 'time_zone'


class TimeZoneLeapSecond(models.Model):
    transition_time = models.BigIntegerField(db_column='Transition_time', primary_key=True)  # Field name made lowercase.
    correction = models.IntegerField(db_column='Correction')  # Field name made lowercase.

    class Meta:
        db_table = 'time_zone_leap_second'


class TimeZoneName(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=64)  # Field name made lowercase.
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id')  # Field name made lowercase.

    class Meta:
        db_table = 'time_zone_name'


class TimeZoneTransition(models.Model):
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_time = models.BigIntegerField(db_column='Transition_time')  # Field name made lowercase.
    transition_type_id = models.PositiveIntegerField(db_column='Transition_type_id')  # Field name made lowercase.

    class Meta:
        db_table = 'time_zone_transition'
        unique_together = (('time_zone_id', 'transition_time'),)


class TimeZoneTransitionType(models.Model):
    time_zone_id = models.PositiveIntegerField(db_column='Time_zone_id', primary_key=True)  # Field name made lowercase.
    transition_type_id = models.PositiveIntegerField(db_column='Transition_type_id')  # Field name made lowercase.
    offset = models.IntegerField(db_column='Offset')  # Field name made lowercase.
    is_dst = models.PositiveIntegerField(db_column='Is_DST')  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=8)  # Field name made lowercase.

    class Meta:
        db_table = 'time_zone_transition_type'
        unique_together = (('time_zone_id', 'transition_type_id'),)


class TransactionRegistry(models.Model):
    transaction_id = models.BigIntegerField(primary_key=True)
    commit_id = models.BigIntegerField(unique=True)
    begin_timestamp = models.DateTimeField()
    commit_timestamp = models.DateTimeField()
    isolation_level = models.CharField(max_length=16)

    class Meta:
        db_table = 'transaction_registry'


class User(models.Model):
    host = models.CharField(db_column='Host', primary_key=True, max_length=60)  # Field name made lowercase.
    user = models.CharField(db_column='User', max_length=80)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=41)  # Field name made lowercase.
    select_priv = models.CharField(db_column='Select_priv', max_length=1)  # Field name made lowercase.
    insert_priv = models.CharField(db_column='Insert_priv', max_length=1)  # Field name made lowercase.
    update_priv = models.CharField(db_column='Update_priv', max_length=1)  # Field name made lowercase.
    delete_priv = models.CharField(db_column='Delete_priv', max_length=1)  # Field name made lowercase.
    create_priv = models.CharField(db_column='Create_priv', max_length=1)  # Field name made lowercase.
    drop_priv = models.CharField(db_column='Drop_priv', max_length=1)  # Field name made lowercase.
    reload_priv = models.CharField(db_column='Reload_priv', max_length=1)  # Field name made lowercase.
    shutdown_priv = models.CharField(db_column='Shutdown_priv', max_length=1)  # Field name made lowercase.
    process_priv = models.CharField(db_column='Process_priv', max_length=1)  # Field name made lowercase.
    file_priv = models.CharField(db_column='File_priv', max_length=1)  # Field name made lowercase.
    grant_priv = models.CharField(db_column='Grant_priv', max_length=1)  # Field name made lowercase.
    references_priv = models.CharField(db_column='References_priv', max_length=1)  # Field name made lowercase.
    index_priv = models.CharField(db_column='Index_priv', max_length=1)  # Field name made lowercase.
    alter_priv = models.CharField(db_column='Alter_priv', max_length=1)  # Field name made lowercase.
    show_db_priv = models.CharField(db_column='Show_db_priv', max_length=1)  # Field name made lowercase.
    super_priv = models.CharField(db_column='Super_priv', max_length=1)  # Field name made lowercase.
    create_tmp_table_priv = models.CharField(db_column='Create_tmp_table_priv', max_length=1)  # Field name made lowercase.
    lock_tables_priv = models.CharField(db_column='Lock_tables_priv', max_length=1)  # Field name made lowercase.
    execute_priv = models.CharField(db_column='Execute_priv', max_length=1)  # Field name made lowercase.
    repl_slave_priv = models.CharField(db_column='Repl_slave_priv', max_length=1)  # Field name made lowercase.
    repl_client_priv = models.CharField(db_column='Repl_client_priv', max_length=1)  # Field name made lowercase.
    create_view_priv = models.CharField(db_column='Create_view_priv', max_length=1)  # Field name made lowercase.
    show_view_priv = models.CharField(db_column='Show_view_priv', max_length=1)  # Field name made lowercase.
    create_routine_priv = models.CharField(db_column='Create_routine_priv', max_length=1)  # Field name made lowercase.
    alter_routine_priv = models.CharField(db_column='Alter_routine_priv', max_length=1)  # Field name made lowercase.
    create_user_priv = models.CharField(db_column='Create_user_priv', max_length=1)  # Field name made lowercase.
    event_priv = models.CharField(db_column='Event_priv', max_length=1)  # Field name made lowercase.
    trigger_priv = models.CharField(db_column='Trigger_priv', max_length=1)  # Field name made lowercase.
    create_tablespace_priv = models.CharField(db_column='Create_tablespace_priv', max_length=1)  # Field name made lowercase.
    delete_history_priv = models.CharField(db_column='Delete_history_priv', max_length=1)  # Field name made lowercase.
    ssl_type = models.CharField(max_length=9)
    ssl_cipher = models.TextField()
    x509_issuer = models.TextField()
    x509_subject = models.TextField()
    max_questions = models.PositiveIntegerField()
    max_updates = models.PositiveIntegerField()
    max_connections = models.PositiveIntegerField()
    max_user_connections = models.IntegerField()
    plugin = models.CharField(max_length=64)
    authentication_string = models.TextField()
    password_expired = models.CharField(max_length=1)
    is_role = models.CharField(max_length=1)
    default_role = models.CharField(max_length=80)
    max_statement_time = models.DecimalField(max_digits=12, decimal_places=6)

    class Meta:
        db_table = 'user'
        unique_together = (('host', 'user'),)
