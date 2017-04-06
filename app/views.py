from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .sentiment import main
from urllib.parse import urlparse, parse_qs
from operator import itemgetter
import json
from django.http import HttpResponse
# Create your views here.

def YoutubeRequestView(request):


    if request.method == 'POST':


        url = parse_qs(urlparse(request.POST['youtube_url']).query)
        print(str(url['v'][0]))
        l = main(str(url['v'][0]))

        return HttpResponse(l)

    context_dict = {'sentiment': 'sentiment'}
    return render(request, 'app/youtube_request.html', context_dict)
