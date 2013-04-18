# Create your views here.
from django.http import HttpResponse
from django.conf import settings

from django.views.generic import TemplateView

class TokenMixin(object):

    def get_context_data(self, **kwargs):
        context = super(TokenMixin, self).get_context_data(**kwargs)
        context['MIXIN_SECRET'] = settings.MIXIN_SECRET
        context['MIXIN_APP_ID'] = settings.MIXIN_APP_ID

        return context


class HomeView(TokenMixin, TemplateView):
    template_name = 'home.html'


class NoMixinView(TemplateView):
    template_name = 'home.html'

