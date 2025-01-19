from django.shortcuts import render, redirect         
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm    

#define a function view called login_view that takes a request from user
def login_view(request):                                
   error_message = None   
   #form object with username and password fields                             
   form = AuthenticationForm()                            

   #when user hits "login" button, then POST request is generated
   if request.method == 'POST':                     
       form =AuthenticationForm(data=request.POST)

       #check if form is valid
       if form.is_valid():                                
           username=form.cleaned_data.get('username')      
           password = form.cleaned_data.get('password')    

           #use Django authenticate function to validate the user
           user=authenticate(username=username, password=password)
           if user is not None:                   
          #then use pre-defined Django function to login if user authenticated
               login(request, user)                
               return redirect('recipes:list') 
       else:                                              
           error_message ='ooops.. something went wrong' 

   #prepare data to send from view to template
   context ={                                             
       'form': form,                                
       'error_message': error_message                     
   }
   #load the login page using "context" information
   return render(request, 'auth/login.html', context)   

#define a function view called logout_view that takes a request from user
def logout_view(request):                                  
   logout(request)             #pre-defined Django function to logout
   return render(request, 'auth/success.html')    