"""MarttGram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime


def hello_word(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')

    return HttpResponse('Current server time is: {now}'.format(
        now=now))


def get(request):
    """Using method GET"""

    import pdb #Debuger
    #pdb.set_trace() # Ieractua con la cosola

    numbers = sorted(request.GET['numbers'].split(','))
    response = JsonResponse([numbers], safe=False)

    return response
    
