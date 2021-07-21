import json

from django.http import JsonResponse
from django.views import View
from dog.models import Dog
from owner.models import Owner

# Create your views here.
class DogView(View):
    def post(self, request):
        data = json.loads(request.body)
        
        if not Owner.objects.filter(id=data["owner_id"]).exists():
            return JsonResponse({"MESSAGE" : "OWNER_DOES_NOT_EXISTS"}, status=404)

        Dog.objects.create(
            name = data["name"],
            age = data["age"],
            owner_id = data["owner_id"]
        )
        return JsonResponse({"MESSAGE" : "SUCCESS"}, status=201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []
        for dog in dogs:
            results.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner' : Owner.objects.get(id=(dog.owner_id)).name  
                }
            )
        return JsonResponse({"results" : results}, status=200)
            

