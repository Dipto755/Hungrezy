from django.shortcuts import render

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
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our customer account signup page</h1>")


def businessaccountsignup(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our business account signup page</h1>")


def rideraccountsignup(request):
    return HttpResponse(
        "<style>h1{text-align: center;}</style><h1>Welcome... This is our rider account signup page</h1>")
