from urllib import request
from django.shortcuts import render,redirect
import requests

# Create your views here.
def codeforce_user_view(request):

    url="https://codeforces.com/api/user.info?handles={}"

    msg =''
    errmsg = ''
    msgclass = ''

    user=[]

    if 'handle' in request.POST:
       handle=request.POST['handle']
       r = requests.get(url.format(handle)).json()
       
       # errmsg="we dont find value"
       #print("the status is: ",r['status'])


     

       user=[]

       if r['status'] != "OK":
           # print("this is null")
            user =[]
            errmsg= "there are no handle name in this site."
            if errmsg:
                msg = errmsg
                msgclass = 'is-danger'
            else:
                msg = "successfully find this handle"
                msgclass = 'is-success'
            return render(request,'codeforce_user.html',{'user':user,'msg': msg,'msgclass': msgclass})

       else:
            r = requests.get(url.format(handle)).json()
            #msg="we find the value"
           # print(r)
            
            user_info={
                    'Handle': r['result'][0]['handle'],
                    'First': r['result'][0].get('firstName',''),
                    'Last': r['result'][0].get('lastName', ''),
                    'Country': r['result'][0].get('country',''),
                    'Rating': r['result'][0].get('rating',''),
                    'Rank': r['result'][0].get('rank', ''),
                    'Max': r['result'][0].get('maxRank', ''),
                    'Photo': r['result'][0]['titlePhoto']
             }
            

            #print("hi , i am here.. please look at")

            if errmsg:
                msg = errmsg
                msgclass = 'is-danger'
            else:
                msg = "successfully find this handle"
                msgclass = 'is-success'

            user.append(user_info)



            context={
                    'user' :user,
                    #'user_info' :user_info,
                    'msg': msg,
                    'msgclass': msgclass
        

               }
            return render(request,'codeforce_user.html',context)
    
    return render(request,'codeforce_user.html',{'user':user})
    
       
          





    #handle='stranger_boy'

   # r = requests.get(url.format(handle)).json()
   # msg="we find the value"
   # print(r)
 
