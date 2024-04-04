from django.views import View
from django.shortcuts import render
from django.utils.translation import gettext as _


class IndexView(View):
    a = None
    a.hello()
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', context={'text': _('Some text to test translations')})
