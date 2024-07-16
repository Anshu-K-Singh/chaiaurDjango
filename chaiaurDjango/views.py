from django.http import HttpResponse
from django.shortcuts import render

def Home(request): #request will request a url 
    
    #Http Response will create response to the
    # return HttpResponse("hey You are at the home page ")
    return render(request, 'website/index.html')

def About(request):
    return render(request, 'website/About.html')
    

def Contact(request):
    return render(request, 'website/contact.html')

#these are all methods created for the pages


#go to create urls in the path function
#url me hi btana pdega ki konsi method to hit krna chahte h  (about or home or contact)
