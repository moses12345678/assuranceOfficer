from django import views
#from django.shortcuts import render, redirect
from django.shortcuts import (get_object_or_404,
                              render, redirect,
                              HttpResponseRedirect)
from qr_code.qrcode.utils import QRCodeOptions
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# import orange sms
#from python_orange_sms import utils
#import employers
from .models import Employers
from .forms import EmployerForm
from .models import Employers
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

# ------section forms -------------------#


def EmployerList(request):
    employers = Employers.objects.all().order_by("firstname")
    count = employers.count()
    # Build context for rendering QR codes.
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
        employers = Employers.objects.all().order_by("firstname")

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


def detail_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}
    #n1 = Employers.objects.filter(status='1')
    #n2 = Employers.objects.filter(status='2')
    # add the dictionary during initialization
    context["data"] = Employers.objects.get(pk=pk)

    return render(request, "employer-detail.html", context)
    # {'n1': n1,
    # 'n2': n2})


def EmployerUpdate(request, pk):
    employers = Employers.objects.get(pk=pk)
    form = EmployerForm(initial={'firstname': employers.firstname, 'lastname': employers.lastname,
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
