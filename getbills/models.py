# ! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

Status = (
    ('Unseen', 'На рассмотрении'),
    ('Approved', 'Утверждено'),
    ('Denide', 'Отклонено'),
)

class Application(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    docfile = models.FileField(upload_to='bills')
    status = models.CharField(max_length=200, choices=Status)
    data = models.DateTimeField('date published',auto_now_add=True)

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.name) or u''

class Winners(models.Model):
    number = models.IntegerField()
    winner = models.ForeignKey(Application, related_name='Winner')
    date_begin = models.DateTimeField('date of begin')
    date_end = models.DateTimeField('date of end')

    def __unicode__(self):  # __unicode__ on Python 2
        return unicode(self.number) or u''