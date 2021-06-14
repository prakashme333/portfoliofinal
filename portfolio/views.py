from django.shortcuts import render
from portfolio.models import contact,about_service
from django.shortcuts import redirect

# Create your views here.
def homepage(request):

   if request.method=="GET":
      contain = about_service.objects.all()
      return render(request, 'index.html',{'contain':contain})
   else:
      newcontact = contact()
      newcontact.name = request.POST.get('name')
      newcontact.email = request.POST.get('email')
      newcontact.subject = request.POST.get('subject')
      newcontact.message = request.POST.get('message')
      newcontact.save()
      return redirect('homepage')

