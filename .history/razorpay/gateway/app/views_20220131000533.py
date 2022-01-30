

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        amount=20000
        client=razorpay.Client(auth=('rzp_test_nwuQfgwlD5GMOG','bHlxwnN5qGKUWD0EHhJaYwuV'))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
                                       'payment_capture': '1'})
    return render(request,'app/index.html')


@csrf_exempt
def success(request):
    return render(request,'app/success.html')   


