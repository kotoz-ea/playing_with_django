from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# 
def fetch_data_from_ras() -> list:
    # get data from device connedted to port /dev/tty01
    return [
    {'id': 1, 'name': 'Any thing to be shown 1'},
    {'id': 2, 'name': 'Any thing to be shown 2'},
    {'id': 3, 'name': 'Any thing to be shown 3'},
    {'id': 4, 'name': 'Any thing to be shown 4'},
]

def home(request) -> 'HttpResponse':
    data_set = fetch_data_from_ras()
    data = {'data': data_set}
    return render(request, 'base/home.html', data)


def telemetry(request, pk) -> 'HttpResponse':
    data = None
    data_set = fetch_data_from_ras()
    for i in data_set:
        if i['id'] == int(pk):
            data = i
    context = {'data': data}
    return render(request, 'base/telemetry.html', context)
