from django.shortcuts import render
from. forms import *
from. models import *

# Create your views here.
def index(request):
    enq=Contact_us.objects.all()
    card_model=Card.objects.all()
    test_model=Testimonials.objects.all()
    form_obj=Contact_form()
    if request.method == 'POST':
        if 'save' in request.POST:
            form=Contact_form(request.POST)
            form.save()
    context=[]
    context={
        "form_obj":form_obj,
        "enq":enq,
        "card_model":card_model,
        "test_model":test_model
    }        
    return render(request,'index.html',context)
