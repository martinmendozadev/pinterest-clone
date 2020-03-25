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
    """Using method GET and response with a JSON"""

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
        content_type='application/json'
    )

    return response

def check_point(response, name, age):
    """Return a greeting"""
    if age < 14:
        message = 'Sorry {}, you aren\'t allowed here'.format(name)
    else:
        message = 'Hello, {} welcome to marttGram'.format(name)

    return HttpResponse(message)
    
