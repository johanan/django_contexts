from django.conf import settings

def google_ua(request):
    my_context = {
        'GOOGLE_UA': settings.GOOGLE_UA,
        }

    return my_context