from django.shortcuts import render
from rest_framework.decorators import api_view
from pymongo import MongoClient
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

client=MongoClient()
db= client['peoples']

@api_view(['GET'])
def get_all(request):
    collection=db['people']
    cursor=collection.find_one({})
    return JsonResponse(cursor,safe=False)



@api_view(['GET'])
def get_name(request):
    collection=db['people']
    cursor=collection.aggregate([{"$count":"name"}])
    cursor=list(cursor)
    return JsonResponse(cursor,safe=False)


@api_view(['GET'])
def get_sample(request):
    collection=db['people']
    cursor =collection.aggregate([{ "$group" :{ '_id': "$name","rating":{"$max":"$points"}}},{"$sort":{"rating":-1}},{"$limit":4}])
    cursor=list(cursor)
    return JsonResponse(cursor,safe=False)


@api_view(['POST'])
def post_fav(request):
    print(request.data)
    collection = db['people']
    # data= []
    cursor=collection.insert(request.data)
    
    return JsonResponse({"data":"success"},safe=False)  






    