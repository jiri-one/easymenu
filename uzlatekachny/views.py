from django.views.generic.list import ListView
from django.http import HttpResponse
from uzlatekachny.models import Food, Category

class FoodListView(ListView):
    """Main class to show food list."""
    model = Food
    template_name = 'index.html'
    
    # async def get(self, request, *args, **kwargs):
    #     return HttpResponse("Hello async world!")
