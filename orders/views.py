from django.shortcuts import render
from django.http import HttpResponse
from random import randint as rand
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def orders(request):
    order_list = [{'name': f'order{i}', 'ordered_warranty': rand(0,1)} for i in range(1,15)]
    return render(request, 'order.html', {'orders': order_list})


def pages(request):
    int_list = [num for num in range(1, 1001)]
    paginator = Paginator(int_list, 100)
    page = request.GET.get('page', 1)
    
    try:
        nums = paginator.page(page)
    except PageNotAnInteger:
        nums = paginator.page(1)
    except EmptyPage:
        nums = paginator.page(paginator.num_pages)
    
    print(nums.has_other_pages())

    return render(request, 'pages.html', {'nums': nums})


