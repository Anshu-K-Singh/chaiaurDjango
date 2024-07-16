from django.http import HttpResponse

def Home(request): #request will request a url 
    
    #Http Response will create response to the  
    return HttpResponse("hey You are at the home page ")

def About(request):
    return HttpResponse("hey You are at the About page ")

def Contact(request):
    return HttpResponse("hey You are at the Contact page ")

#these are all methods created for the pages


#go to create urls in the path function
#url me hi btana pdega ki konsi method to hit krna chahte h  (about or home or contact)
