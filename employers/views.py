#from ipaddress import summarize_address_range
from django import views
from django.db.models import Sum
#from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              render, redirect,
                              HttpResponseRedirect)
from django.urls import reverse
#from matplotlib.pyplot import summer
from qr_code.qrcode.utils import QRCodeOptions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# import orange sms
#from python_orange_sms import utils
#import employers
from .models import *
from .forms import *
#from .models import Employers
from .serializers import *

#-----------Integration Orange Sms----------#
# SENDER_NAME = 'Innov'  # Name of your app in dev console
# AUTH_TOKEN = 'Authorization header'  # Authorization header from dev console

# message = "The sms message you want to send to the recipient"  # Your message
# recipient_phone_number = '243xxxxxxxxx'  # a Receiver phone number
# dev_phone_number = '243xxxxxxxxx'  # Sender (your phone number)
# recipient_phone_number and dev_phone_number are international phone numbers without + or leading zeros:  format regex('^[1-9][\d]{10,14}$')

#sms = utils.SMS(AUTH_TOKEN=AUTH_TOKEN, )
# res = sms.send_sms(message=message,
# dev_phone_number=dev_phone_number,       recipient_phone_number=recipient_phone_number)
#--------end integration Orange Sms---------#


# ------section homePage -------------------#

def index(request):
    return render(request, "index.html")

# ------endSection homePage ----------------#


def home(request):
    return render(request, "home.html")
# ------section dashboard -------------------#


def dashboard(request):
    User = get_user_model()
    users = User.objects.all().order_by("username")
    count = users.count()
    employers = Employers.objects.all().order_by("nom")
    count1 = employers.count()
    #context = {}
    #context1 = {}
    #n1 = Employers.objects.filter(status='1')
    #n2 = Employers.objects.filter(status='2')
    # add the dictionary during initialization
    #context["data"] = Employers.objects.all()
    # context["total"] = Traitement.objects.all().aggregate(
    # Sum('montant_total')) or 0
    # context["depense20"] = Traitement.objects.all().aggregate(
    # Sum('montant_a_payer')) or 0
    return render(request, "dashboard.html", {'count': count,
                                              'count1': count1,
                                              })


# ------endSection dashboard ----------------#

# ------section forms -------------------#


def EmployerList(request):
    employers = Employers.objects.all().order_by("nom")
    count = employers.count()
    # Build context for rendering QR codes.
    # 3 is the number of page that coul be apply
    paginator = Paginator(employers, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "employers-list.html", {'employers': employers,
                                                   'count': count,
                                                   'page_obj': page_obj
                                                   })


def EmployerSearch(request):
    search_post = request.GET.get('search')

    if search_post:
        employers = Employers.objects.filter(
            Q(pk=search_post))
    else:
        employers = Employers.objects.all().order_by("nom")

    return render(request, "employers-search.html", {'employers': employers,
                                                     })


def EmployerCreate(request):
    if request.method == "POST":
        form = EmployerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('employers-list')
            except:
                pass
    else:
        form = EmployerForm()
    return render(request, 'employer-create.html', {'form': form})

# after updating it will redirect to detail_View


def detail_view(request, person):
    # dictionary for initial data with
    # field names as keys
    context = {}
    #context1 = {}
    #n1 = Employers.objects.filter(status='1')
    #n2 = Employers.objects.filter(status='2')
    # add the dictionary during initialization
    context["data"] = Employers.objects.get(pk=person)
    context["data1"] = Traitement.objects.filter(person=person)
    context["total"] = Traitement.objects.filter(person=person).aggregate(
        Sum('montant_total')) or 0
    context["depense20"] = Traitement.objects.filter(person=person).aggregate(
        Sum('montant_a_payer')) or 0
    return render(request, "employer-detail.html", context)
    # {'n1': n1,
    # 'n2': n2})


def EmployerUpdate(request, pk):
    employers = Employers.objects.get(pk=pk)
    form = EmployerForm(initial={'nom': employers.nom, 'prenom': employers.prenom,
                                 'email': employers.email, 'status': employers.status, 'matricule': employers.matricule, 'phone': employers.phone, 'image': employers.image})
    if request.method == "POST":
        form = EmployerForm(request.POST, request.FILES, instance=employers)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('/employers-list')
            except Exception as e:
                pass
    return render(request, 'employer-update.html', {'form': form})


def EmployerDelete(request, pk):
    employers = Employers.objects.get(pk=pk)
    try:
        employers.delete()
    except:
        pass
    return redirect('employers-list')


def TraitementCreate(request, person):

    id_person = Employers.objects.get(pk=person)
    #traitement = Traitement.objects.get(person=id_person)
    form = TraitementForm(
        initial={'person': id_person, 'partenaire': request.user})
    if request.method == "POST":
        form = TraitementForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                #model = form.instance
                return redirect('employer-detail', person=person)
            except Exception as e:
                pass
    return render(request, 'traitement-create.html', {'form': form})


def TraitementDelete(request, pk):
    traitement = Traitement.objects.get(pk=pk)
    #id_person = Employers.objects.get(pk=traitement.person)
    try:
        traitement.delete()
        # return redirect('employer-detail', person=20)
    except:
        pass
    return redirect('employers-list')


def PartenaireList(request):
    User = get_user_model()
    users = User.objects.all().order_by("username")
    count = users.count()
# Build context for rendering QR codes.
# 3 is the number of page that coul be apply
    paginator = Paginator(users, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "employers-list.html", {'users': users,
                                                   'count': count,
                                                   'page_obj': page_obj
                                                   })


#-------fin section forms ---------------#

# ------section api ---------------------#


class EmployerView(viewsets.ModelViewSet):
    serializer_class = EmployerSerializer
    queryset = Employers.objects.all()


'''
@api_view(['GET', 'POST'])
def employers_list(request):
    if request.method == 'GET':
        data = Employers.objects.all()

        serializer = EmployerSerializer(
            data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = EmployerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def employers_detail(request, pk):
    try:
        employers = Employers.objects.get(pk=pk)
    except Employers.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = EmployerSerializer(
            employers, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
'''

#------------fin section api ------------#
