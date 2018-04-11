# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
from app.forms import MomentForm
from django.core.urlresolvers import reverse
def welcome(request):
	return HttpResponse("hello world")

def moments_input(request):
	if request=='POST':
		form=MomentForm(request.POST)
		if form.is_valid():
			moment=form.save()
			moment.save()
			return HttpResponseRedirect(reverse('app.views.welcome'))
	else:
		form=MomentForm()
		PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		return render(request,os.path.join(PROJECT_ROOT,'app/templates',
	'moments_input.html'),{'form':form})

