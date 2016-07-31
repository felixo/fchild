from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'getbills.views.index', name='index'),
    url(r'^addAplication/', 'getbills.views.addAplication', name='addAplication'),
    url(r'^thankyou/', 'getbills.views.thankyou', name='thankyou'),
]