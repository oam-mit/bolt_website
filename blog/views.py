from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm,UserUpdateForm
from django.contrib import messages as mess
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import reverse
import json
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from .Custom_classes import bolt_custom
from boltiot import Bolt


b=None

# Create your views here.
def index(request):
   return render(request,'blog/index.html')


@login_required
def profile(request):
   if request.method=='POST':
      try:
         print("Hi,Hello")
      except Exception as e:
         print(e)
      profile_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
      user_form=UserUpdateForm(request.POST,instance=request.user)
      if profile_form.is_valid() and user_form.is_valid():
         mess.success(request,'Successfully changed your Profile')
         profile_form.save()
         user_form.save()
         return HttpResponseRedirect(reverse('blog:profile'))
         
   
   else:
      profile_form=ProfileUpdateForm(instance=request.user.profile)
      user_form=UserUpdateForm(instance=request.user)
   
   context={
      'user_form':user_form,
      'profile_form':profile_form,

   }
   return (render(request,'blog/profile.html',context))


@login_required
def action(request,action):
   response=b.b.isOnline()
   r=json.loads(response)
   if r['value']=='online':
      if action==1:
         try:
            suc=b.b.digitalWrite('1','HIGH')
            s =json.loads(suc)
            if s['success']==1:
               return HttpResponse('Turned On')
            else:
               return HttpResponse('Error Processing the Request')

         except Exception as e:
            mess.error(request,e,extra_tags='danger')
         
      else:
         suc=b.b.digitalWrite('1','LOW')
         s=json.loads(suc)
         if s['success']==1:
            return HttpResponse('Turned off')
         else:
            return HttpResponse('Error Processing the Request')

   else:
      return HttpResponse('Device is Offline')

@receiver(user_logged_in)
def do(sender,request,user,**kwargs):
   global b
   if b is None:
      print("It is none")
      b=bolt_custom(api_key=user.profile.api_key,device_key=user.profile.device_name)
   

def bulb_status(request):
   global b
   if b is None:
      b = bolt_custom(api_key=request.user.profile.api_key,device_key=request.user.profile.device_name)
   
   res=b.b.digitalRead('1')
   r = json.loads(res)
   if r['value']=='1':
      return HttpResponse("high")
   else:
      return HttpResponse("low")




def status(request):
   if b is None:
      return HttpResponse("Please Log In again")

   # bolt=Bolt(request.user.profile.api_key,request.user.profile.device_name)
   elif b.b is None and (request.user.profile.api_key is not None and request.user.profile.device_name is not None):
      b.b = Bolt(request.user.profile.api_key,request.user.profile.device_name)
   elif b.b is not None and (not request.user.profile.api_key  or not request.user.profile.device_name): 
      b.b = None
      return HttpResponse('No Registered Device')


   try:
      response=b.b.isOnline()
      r=json.loads(response)

   

      if r['value']=='online':
         return HttpResponse('Device is Online')
      else:
         return HttpResponse('Device is Offline')
   except:
      return HttpResponse("No Registered Device")


