from django.http import JsonResponse
from requests import request
from . import models
from datas.serializers import *
from bson import json_util
from rest_framework_mongoengine import generics
from django.http import HttpResponse
# class ListView(generics.ListCreateAPIView):
#     queryset = models.data1.objects.all()
#     serializer_class = serializers.data1Serializer



def getRooms(request):
    if request.method=='GET':
        queryset = models.room.objects.all().order_by('_id')
        serializer_class = roomSerializer(queryset, many=True)
        return JsonResponse({'data':serializer_class.data, 'safe':False})
       
def getPosts(request):
    if request.method=='GET':
        queryset = models.post.objects.all_fields().order_by('_id')
        postSerial = postSerializer(queryset, many=True)
        data = postSerial.data
        # user => user
        for i, query in enumerate(queryset):
            # print(query.user)
            userSerial = userSerializer(query.user)
            data[i]["user"] = userSerial.data
        # whoLikes => List(user)
        for i, query1 in enumerate(queryset):
            for j, query2 in enumerate(query1.whoLikes):
                # print(query2)
                userSerial = userSerializer(query2)
                data[i]["whoLikes"][j] = userSerial.data

        data = json_util.dumps(data)
        return HttpResponse({data }, content_type='application/json')
    
# def getLikes(request):
#     if request.method=='GET':
#         queryset = models.like.objects.all().order_by('_id')
#         serializer_class = likeSerializer(queryset, many=True)
#         return JsonResponse({'data':serializer_class.data, 'safe':False})
    



def getUsers(request):
    if request.method=='GET':
        queryset = models.user.objects.all_fields().order_by('_id')

        serializer_class = userSerializer(queryset, many=True)
        dataDump = json_util.dumps(serializer_class.data)
        data = dataDump.replace('\\"', '')
        # print( json_util.loads(data))

        print(json_util.dumps(models.user.objects.first()))

        # queryset1 = models.user.objects.first()
        # serializer1 = userSerializer(queryset1, many = True)
        # print(queryset1.likePosts)
        # queryset1 = models.user.objects.only('username', 'likePosts').get()
        # queryset1 = models.user.objects.filter(name ='FrankSaSa_').first()
        # print(queryset1.likePosts)
        # serializer1_class = userSerializer(queryset1)
        # dataDump1 = json_util.dumps(serializer1_class.data)
        # print(dataDump1)

        # return JsonResponse({'data':data, 'safe':False}, mimetype='application/json')
        return HttpResponse({data}, content_type='application/json')




def getFollowings(request):
    if request.method=='GET':
        queryset = models.following.objects.all_fields()#.order_by('_id')
        followingSerial = followingSerializer(queryset, many=True)
        data = followingSerial.data
        # user => user
        # whoFollow => user
        for i, query in enumerate(queryset):
            userSerial1 = userSerializer(query.user)
            userSerial2 = userSerializer(query.whoFollow)
            data[i]["user"] = userSerial1.data
            data[i]["whoFollow"] = userSerial2.data
        # userSerial1 = userSerializer(queryset.user)
        # userSerial2 = userSerializer(queryset.whoFollow)
        # data["user"] = userSerial1.data
        # data["whoFollow"] = userSerial2.data
        # data[i]["user"] = userSerial1.data
        # data[i]["whoFollow"] = userSerial2.data
        
        
        data = json_util.dumps(data)

        return HttpResponse({data}, content_type='application/json')




def getData2(request):
    if request.method=='GET':
        queryset = models.data2.objects.all().order_by('_id')
        print(queryset)
        serializer_class = data2Serializer(queryset, many=True)
        return JsonResponse({'data':serializer_class.data, 'safe':False})
        # return JsonResponse(serializer_class.data, safe=False)


        # elif request.method=='POST':
        #     queryset = models.data1.objects.all().order_by('_id')
        #     serializer_class = data1Serializer
        #     return JsonResponse(serializer_class.data, safe=FALSE)


class data1View(generics.ListCreateAPIView):
    queryset = models.room.objects.all().order_by('_id')
    serializer_class = roomSerializer

class data2View(generics.ListCreateAPIView):
    queryset = models.data2.objects.all().order_by('_id')
    serializer_class = data2Serializer
