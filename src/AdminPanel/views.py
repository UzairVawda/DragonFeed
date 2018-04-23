from __future__ import unicode_literals
from django.shortcuts import render

#adminpanel.html - admin panel where the user can edit certain features
def AdminPanel(request):
    return render(request, 'adminpanel.html')
