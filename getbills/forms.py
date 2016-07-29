#! /usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Application
from django import forms
from django.utils.translation import ugettext_lazy as _



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ('name', 'mail', 'city', 'docfile')
        labels = {
            'name': _('ФИО'),
            'city': _('Город'),
            'mail': _('E-mail'),
            'docfile': _('Загрузить файл (jpg, png, tiff)'),
        }
