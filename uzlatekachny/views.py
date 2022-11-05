from django.shortcuts import render

# Create your views here.
async def index_cze(request):
    return render(request, 'index.html')
