import json
from django.http.response import JsonResponse
from django.views         import View
from .models              import Owner
from dog.models           import Dog

# Create your views here.

class OwnerView(View):
    def post(self, request):
        data = json.loads(request.body)
    
        Owner.objects.create(
            name =  data["name"],
            age =   data["age"],
            email = data["email"],
        )
        return JsonResponse({"MESSAGE":"CREATED"}, status=201)

    def get(self, request):
        owners = Owner.objects.all()
        results = []
        for owner in owners:
            dogs = Dog.objects.all()
            dog_list = []
            for dog in dogs:
                dog_list.append(
                    {
                        "dog_name" : dog.name,
                        "dog_age" : dog.age
                    }
                )
            results.append(
                {
                    "name" : owner.name,
                    "age" : owner.age,
                    "email" : owner.email,
                    "dog_info" : dog_list
                }
            )
        return JsonResponse({'results':results}, status=200)




