from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

import urllib
import requests


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'App/index.html')

    def post(self, request):
        tes = False
        key = ''


        if request.method == "POST":
            original_url = request.POST['original_url']
            url = urllib.parse.quote(original_url)
            tes = True

            r = request.get(f'http://cutt.ly/api/api.php?key={key}&short={url}&userDomain=1')
            return render(request, 'App/index.html', {
                'tes': tes,
                'original_url': original_url
            })
