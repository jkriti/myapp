# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib import admin
# import your model
from collection.models import Thing

# set up automated slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'branch','rollno','year','description',)
    prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Thing, ThingAdmin)