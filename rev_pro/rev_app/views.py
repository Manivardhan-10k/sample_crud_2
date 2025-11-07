from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf  import csrf_exempt
from .models import UserDetails
import json
from .serializer   import UserDetailsSerializer

#cross site request forgery

# Create your views here.


def welcome(req):
    return HttpResponse ("server is working")


#data handling 

@csrf_exempt
def reg_user(request):
    # print(request.POST["name"])  #.get("name")
    # print(request.POST.get("nam"))
    # print("after the req")

    # user_name =request.POST.get("name")
    # user_email=request.POST.get("email")
    # user_mob=request.POST.get("mob") 
    # print(user_name,user_mob,user_email)


    # #ORM -> Object Relational Mapping
    # new_user=UserDetails.objects.create(name=user_name,email=user_email,mobile=user_mob)
    # return JsonResponse({"msg":"use created!!"})

    user_data={}
    for key in request.POST:
         user_data[key] = request.POST[key]
    serialized_Data=UserDetailsSerializer(data=user_data)
    if serialized_Data.is_valid():
         serialized_Data.save()
         return HttpResponse("user created")
    else:
         return HttpResponse("failed to register")

     




def users(request):
    # all_users=UserDetails.objects.all().values()
    # return JsonResponse({"data":list(all_users)})

    all_users=UserDetails.objects.all()  ##queryset
    serialized_data=UserDetailsSerializer(all_users,many=True)
    return JsonResponse({"all_users":serialized_data.data})



def delete_user(req,uid):
    user_to_be_deleted=UserDetails.objects.get(id=uid)
    user_to_be_deleted.delete()
    return HttpResponse ("user deleted!!")


@csrf_exempt
def update_user(req,uid):
    # print(json.loads(req.body)["name"])
    # print(type(req.body))
    # print(type(req.POST.get("name")))
    # user_to_be_updated=UserDetails.objects.get(id=uid)
    # if req.POST.get('name'):
    #     user_to_be_updated.name=req.POST.get('name')
    # if req.POST.get("email"):
    #     user_to_be_updated.email=req.POST.get("email")
    # if req.POST.get("mob"):
    #     user_to_be_updated.mobile=req.POST.get("mob")
    # user_to_be_updated.save()
    # return HttpResponse("user updated!!")
#   else:
#       return HttpResponse("invalid method!!")


       user_to_be_updated=UserDetails.objects.get(id=uid)
       user_data={}
    #    user_data["name"]
       for prop in req.POST: ## req.POST -> dict         prop->key       value->req.POST[prop]  
             user_data[prop]=req.POST[prop]
             print(user_data)
       serialized_data=UserDetailsSerializer(user_to_be_updated,data=user_data,partial=True)
       if serialized_data.is_valid():
            serialized_data.save()
            return HttpResponse("user updated!")
       




#serializers -> json data conversion -> sql 
#sql -> pyhton objects



#server -> render      +      localhost
#aiven  -> cloud database    + mysql
#media storage->cloudinary   + flolders/



