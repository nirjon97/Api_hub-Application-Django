from multiprocessing import context
from django.shortcuts import render
import requests


# Create your views here.

def github_Profile_view(request):

    user=[]
    msg =''
    errmsg = ''
    msgclass = ''

    if 'user_name' in request.POST:

        user_nam= request.POST['user_name']
       #print("the user name is : ",user_nam)
        url =f"https://api.github.com/users/{user_nam}"
        
        r = requests.get(url.format(user_nam)).json()

        #if we don't find any data in this list
        check =r.get('login','')
        if check =='':
           # print("the value of r is :  ",r)
           # print("this is error,you have to resolve it")
            user=[]
            errmsg= "there are no handle name in this site."

            
            if errmsg:
                msg = errmsg
                msgclass = 'is-danger'

            else:
                msg = "successfully find this handle"
                msgclass = 'is-success'


        else:
          #  print(" lets do it... that not so easy")
            user_info={
                    'Login_name': r['login'],
                    'Name': r['name'],
                    'Email': r['email'],
                    'Public_repos': r['public_repos'],
                    'Followers': r['followers'],
                    'Following': r['following'],
                    'Created_at': r['created_at'],
                    'Avatar_url': r['avatar_url']
             } 

            user.append(user_info)
           # print(r)

            if errmsg:
                msg = errmsg
                msgclass = 'is-danger'

            else:
                msg = "successfully find this handle"
                msgclass = 'is-success'
            
            
        

    context={
        'user': user,
        'msg': msg,
        'msgclass': msgclass

    }
    return render(request,'github.html',context)
