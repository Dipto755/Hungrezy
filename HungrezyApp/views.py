from django.shortcuts import render
# from HungrezyApp.forms import customersignupform
# from HungrezyApp.models import customer
# from HungrezyApp.models import rider
from HungrezyApp.models import customer_account
from HungrezyApp.models import rider_account
from HungrezyApp.models import business_account
from django.contrib.auth.models import User


# Create your views here.

from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our homepage</h1>")


def restaurants(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our restatrants page</h1>")


def menu(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our menu page</h1>")


def homemadefoodoptions(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our home made food options page</h1>")


def category(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our category page</h1>")


def aboutus(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our about us page</h1>")


def contact(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our contact info page</h1>")


def login(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our login page</h1>")


def admin(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our admin page</h1>")


def updaterestaurant(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update restaurant page</h1>")


def updaterider(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider page</h1>")


def updatecustomer(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update customer page</h1>")


def updateriderstatus(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider status page</h1>")


def updateadminprifile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update admin profile page</h1>")


def rider(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider page</h1>")


def updateriderprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update rider profile page</h1>")


def ridersalary(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider salary</h1>")


def riderhistory(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rider history page</h1>")


def restaurantowner(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our restaurant owner page</h1>")


def updateownerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update owner profile page</h1>")


def ownerupdaterestaurant(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update restaurant as owner page</h1>")


def updateprice(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update price page</h1>")


def updatemenu(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our update menu page</h1>")


def customer(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our customer page</h1>")


def updatecustomerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update customer profile page</h1>")


def order(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our order page</h1>")


def rating(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our rating page</h1>")


def review(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our review page</h1>")


def homemadefoodsuppiler(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our homemade food supplier page</h1>")


def updatesuppilerprofile(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update supplier profile page</h1>")


def updatehomemadefoodprice(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update homemade food price page</h1>")


def updatehomemadefoodoptions(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our update homemade food options page</h1>")


def signup(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our signup page</h1>")


def signupas(request):
    return HttpResponse("<style>h1{text-align: center;}</style><h1>Welcome... This is our signup as page</h1>")


def customeraccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our customer account signup page</h1>")
    
    # if(request.method == 'POST'):
    #     form = customersignupform(request.POST)
    #     form.save()
        
    # form = customersignupform()
        
    # context = {
    #     'customer_signup_form' : form
    # }
    
    if(request.method == 'POST'):
        # cus_id = request.POST['cus_id']
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        password = request.POST['password']

        userT = User(username=name, email=email, password=password)
        userT.save()
        
        userObjs = User.objects.all()
        get_user = userObjs.get(username=name)
        
        # csu = customer(name=name, email=email, address = address, contact_number = contact_no, gender=gender, password=password, user=get_user)
        # csu.save()
        
        casu = customer_account(name=name, email=email, address=address,contact_number=contact_no, gender=gender, password=password, user = get_user)
        casu.save()
    
    
    
    return render(request, 'customer_acc_signup.html')


def businessaccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our business account signup page</h1>")
    
    if(request.method == 'POST'):
        name = request.POST['name']
        email = request.POST['email']
        restaurant_name = request.POST['restaurant_name']
        service = request.POST['service']
        food = request.POST['food']
        address = request.POST['address']
        # namdelivary_methode = request.POST['delivary_method']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        password = request.POST['password']
        
        userT = User(username=name, email=email, password=password)
        userT.save()
        
        userObjs = User.objects.all()
        get_user = userObjs.get(username=name)
        
        bsu = business_account(name=name, email=email, res_name = restaurant_name, service = service, food_type=food, address=address, contact_no=contact_no, gender=gender, password=password, user=get_user)
        bsu.save()
        
    
    return render(request, 'business_acc_signup.html')


def rideraccountsignup(request):
    # return HttpResponse(
    #     "<style>h1{text-align: center;}</style><h1>Welcome... This is our rider account signup page</h1>")
    
    if(request.method == 'POST'):
        name =  request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        delivary_method = request.POST['delivary_method']
        contact_no = request.POST['contact_no']
        gender = request.POST['gender']
        password = request.POST['password']
        
        userT = User(username=name, email=email, password=password)
        userT.save()
        
        userObjs = User.objects.all()
        get_user = userObjs.get(username=name)
        
        # rsu = rider(u_name=name, email=email, address=address, delivary_method=delivary_method, gender=gender, contact_number=contact_no, password=password, user=get_user)
        # rsu.save()
        
        rasu = rider_account(user_name = name, email = email, address = address, delivary_method = delivary_method, gender = gender, contact_number = contact_no, password = password, user = get_user)
        rasu.save()
        
        
    return render(request, 'rider_acc_signup.html')
