
import json
import os
from django.shortcuts import render

def default_map(request):
    cur_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(cur_dir, 'mapbox_token.json')) as token_file:
        data = json.load(token_file)
    return render(request, 'default.html',
                  { 'mapbox_access_token' : data['mapbox_access_token'] })
