from django.views import View
from django.shortcuts import render
from django.utils.translation import gettext as _


class IndexView(View):
    def get(self, request, *args, **kwargs):
        a = None
        a.hello()
        return render(request, 'index.html', context={'text': _('Some text to test translations')})
