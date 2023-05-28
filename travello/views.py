from .models import Places, signup, News, PropertyImage,HomeSlide
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from .forms import RegistrationForm, SearchPlace
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import PropertyImage, SlideImage


def Home(request):
    return render(request,'Home.html')

def Add(request):
    san1=int(request.POST['num1'])
    san2=int(request.POST['num2'])
    res=san1+san2
    return render(request,'result.html',{'result':res})


def Index(request):
    dests=Places.objects.all()
    image=SlideImage.objects.all()
    return render(request,'index.html',{'dests':dests,'image_list':image})


def Registiration(request):
    context={
        'form':RegistrationForm,
    }
    return render(request,'register.html',context)

def All_Place(request):
    countries=Places.objects.all()
    context={
        'form':SearchPlace,
        'countries':countries,
    }
    return render(request,'Places.html',context)

def gorod(request): 
    context={}
    form=SearchPlace(request.POST)
    if form.is_valid():
        gozleg=form.cleaned_data['Name']
        if Places.objects.filter(country__startswith=gozleg):
            country=Places.objects.filter(country__startswith=gozleg)
            context['country']=country

        if Places.objects.filter(capital__startswith=gozleg):
            capital=Places.objects.filter(capital__startswith=gozleg)
            context['capital']=capital
        elif not Places.objects.filter(country__startswith=gozleg) and not Places.objects.filter(capital__startswith=gozleg):
            messages.add_message(request,messages.SUCCESS,'NOT FOUND')
        context['form']=SearchPlace
        context['gozleg']=gozleg
        return render(request,'Places.html',context)

    return redirect('allplace')
    


def addUser(request):
    form=RegistrationForm(request.POST)

    if form.is_valid():
        
        myregister=signup(Username=form.cleaned_data['Username'],
                                        Phone=form.cleaned_data['Phone'],
                                        Email=form.cleaned_data['Email']
                                        )
                        
        myregister.save()
        messages.add_message(request,messages.SUCCESS,'You have sign-up successfully')

        return redirect('/')
    messages.add_message(request,messages.SUCCESS,'Correct your email !!!')
    return redirect('registiration')

# const cars = ["🚗", "🚙", "🚕"];
def infocountry(request, country_id):
    products=Places.objects.all()
    post=get_object_or_404(Places, id=country_id)
    image_list=PropertyImage.objects.filter(property=post)
    return render(request,'infocountry.html',
    {
        'post':post,
        'image_list':image_list,
        'products':products
    })

def Newss(request):
    news=News.objects.all()
    return render(request,'news.html',{'news':news})

def eachnews(request, news_id):
    hertazelik=News.objects.get(id=news_id)
    return render(request,'eachnews.html',{'hertazelik':hertazelik})