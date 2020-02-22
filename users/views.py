from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,FeedbackForm

# Create your views here.

def register(request):
    context={}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request,'Account Created Successfully')
            return HttpResponseRedirect(reverse('users:login'))
    
    else :
        form = UserRegisterForm()

    context['form']=form

    

   
    return render(request,'users/register.html',context)


def feedback(request):
    context={}
    if request.method=='POST':
        form=FeedbackForm(request.POST)
        if form.is_valid():
            if form.is_unique(form['name'].value(),form['surname'].value(),form['country'].value(),form['number'].value()):
                if form.check_user(form['username'].value()):
                    form.save()
                    messages.success(request,'Thank You for your Valuable Feedback')
                    return HttpResponseRedirect(reverse('users:feedback'))
                else:
                    context['form']=form
                    messages.error(request,"Username doesn't exist",extra_tags='danger')
                    return render(request,'users/feedback.html',context)
            
            else:
                context['form']=form
                messages.error(request,'Cannot Submit Twice',extra_tags='danger')
                return HttpResponseRedirect(reverse('users:feedback'))

    
    else:
        form=FeedbackForm()
    
    context['form']=form

    return render(request,'users/feedback.html',context)