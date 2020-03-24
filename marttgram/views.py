"""MarttGram views"""

# Django
from django.http import HttpResponse, JsonResponse

# Utilities
from datetime import datetime
import json


def hello_word(request):
    """Return a greeting"""
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')

    return HttpResponse('Current server time is: {now}'.format(
        now=now))


def get(request):
    """Using method GET"""

    import pdb #Debuger
    #pdb.set_trace() # Ieractua con la cosola

    numbers = [int(number) for number in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)

    data = {
        'status' : 'ok',
        'numbers' : sorted_numbers,
        'message' : 'Integers sorted successfully',
    }

    response = HttpResponse(
        json.dumps(data, indent=4),
        content_type='aplication/json'
    )

    return response
    
