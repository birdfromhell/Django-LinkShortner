from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

import pyshorteners


# Create your views here.
class IndexView(View):

    def get(self, request):
        return render(request, 'App/index.html')

    def post(self, request):
        tes = False

        if request.method == "POST":
            tes = True
            original_url = request.POST['original_url']
            bitly = pyshorteners.Shortener(api_key="4874bb7031c647ccd574370236bca9c602c19fb7")
            result_url = bitly.bitly.short(original_url)

            return render(request, 'App/index.html', {
                'tes': tes,
                'original_url': original_url,
                'result_url': result_url
            })


class Login(TemplateView):
    template_name = 'App/login.html'
