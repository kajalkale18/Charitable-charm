from django.shortcuts import render
import razorpay
# Create your views here.
def index(request):
    return render(request,'index.html')
def pay_now(request):
    if request.method == "POST":
        amount = request.POST.get('amount')
        email = request.POST.get('email')
        amount = int(amount)
        c = razorpay.Client(auth=('rzp_test_hiic6D1AgJcwTl', 'SEOJWm7zRXO7jpZbczbHUN5T'))
        payment = c.order.create({'amount': amount*100, 'currency': 'INR', 'payment_capture': '1'})
        return render(request,'donte_now.html',{'payment':payment,'email':email})
    return render(request, 'donte_now.html')
def success(request):
    return render(request,'donate_succss.html')
def about(request):
    return render(request,'about.html')