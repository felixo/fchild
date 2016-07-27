from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'getbills.views.index', name='index'),
]