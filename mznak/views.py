# -*- coding: utf-8 -*-

from django.core.context_processors import csrf
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib import messages
 

from order.forms import OrderForm
from order.models import Order
from review.models import Review
from slideshow.models import Slider
from textblock.models import TextBlock
from signs.models import Sign

import config
from django.conf import settings
from livesettings import config_value
import datetime

PAGINATION_COUNT = 5

def get_common_context(request):
    c = {}
    
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save(request.POST['action'])
            if request.POST['action'] == 'request':
                c['order_ok'] = True
            else: 
                c['feedback_ok'] = True
            form = OrderForm()
    c['form'] = form
    
    c['request_url'] = request.path
    c['is_debug'] = settings.DEBUG
    c['phone'] = config_value('MyApp', 'PHONE')
    ORDERS_COUNT = int(config_value('MyApp', 'ORDERS_COUNT'))
    c['oc_3'] = ORDERS_COUNT % 10
    ORDERS_COUNT = ORDERS_COUNT / 10
    c['oc_2'] = ORDERS_COUNT % 10
    c['oc_1'] = ORDERS_COUNT / 10
    c.update(csrf(request))
    return c

def separate(l):
    if len(l) <= 10:
        return [l]
    else:
        lenght = len(l)
        res = []
        for a in range(0, lenght / 10 +1):
            res.append(l[a*10: a*10 + 10])
        return res

def home(request):
    c = get_common_context(request)
    c['request_url'] = 'home'
    c['slider'] = Slider.objects.all()
    c['reviews'] = Review.objects.all()
    c['textblocks'] = TextBlock.objects.all()
    c['signs_registred'] = separate(Sign.objects.filter(designed=False))
    c['signs_designed'] = separate(Sign.objects.filter(designed=True))
    return render_to_response('index.html', c, context_instance=RequestContext(request))