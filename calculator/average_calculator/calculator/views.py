from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import NumberStore
from .utils import fetch_numbers, WINDOW_SIZE

def get_window_state():
    return list(NumberStore.objects.order_by('timestamp').values_list('value', flat=True))

@api_view(['GET'])
def fetch_and_calculate(request, numberid):
    previous_state = get_window_state()
    numbers = fetch_numbers(numberid)
    
    for num in numbers:
        if NumberStore.objects.count() >= WINDOW_SIZE:
            NumberStore.objects.order_by('timestamp').first().delete()
        NumberStore.objects.get_or_create(value=num)
    
    current_state = get_window_state()
    avg = round(sum(current_state) / len(current_state), 2) if current_state else 0
    
    return Response({
        "windowPrevState": previous_state,
        "windowCurrState": current_state,
        "numbers": numbers,
        "avg": avg
    })