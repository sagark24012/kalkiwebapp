from django.shortcuts import render
from app.models import Genpntdatatable
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    genPointCount = Genpntdatatable.objects.all().count()
    genPointDataListgenPointDataList = Genpntdatatable.objects.all()

    
    context = {
    	'genPointCount': genPointCount,
        'genPointDataList': genPointDataListgenPointDataList,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)