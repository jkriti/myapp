# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from django.http import Http404

from django.template.defaultfilters import slugify

from collection.forms import ThingForm
from collection.models import Thing
from django.forms import formset_factory
# the rewritten view!
def index(request):
    things = Thing.objects.all()

    return render(request, 'index.html', {
        'things': things,
    })

# our new view
def thing_detail(request, slug):
    # grab the object...
    thing = Thing.objects.get(slug=slug)

    # and pass to the template
    return render(request, 'things/thing_detail.html', {
        'thing': thing,
    })

def edit_thing(request, slug):
    # grab the object
    thing = Thing.objects.get(slug=slug)
    # set the form we're using
    form_class = ThingForm

    # if we're coming to this view from a submitted form
    if request.method == 'POST':
        # grab the data from the submitted form and apply to
        # the form
        form = form_class(data=request.POST, instance=thing)
        if form.is_valid():
            # save the new data
            form.save()
            return redirect('thing_detail', slug=thing.slug)
    # otherwise just create the form
    else:
        form = form_class(instance=thing)

    # and render the template
    return render(request, 'things/edit_thing.html', {
        'thing': thing,
        'form': form,
    })

def create_thing(request):
    form_class = ThingForm

    # if we're coming from a submitted form, do this
    if request.method == 'POST':
        # grab the data from the submitted form and
        # apply to the form
        form = form_class(request.POST)
        if form.is_valid():
            # create an instance but don't save yet
            thing = form.save(commit=False)

            # set the additional details
            thing.user = request.user
            thing.slug = slugify(thing.name)

            # save the object
            thing.save()

            # redirect to our newly created thing
            return redirect('thing_detail', slug=thing.slug)

    # otherwise just create the form
    else:
        form = form_class()

    return render(request, 'things/create_thing.html', {
        'form': form,
    })


  

def myview(request):

  if request.method == 'POST':

    form = MyForm(request.POST, extra=request.POST.get('total_input_fields'))

    if form.is_valid():
    	print "valid!"
    else:
        form = MyForm()
	
  return render(request, "template", { 'form': form })