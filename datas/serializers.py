
from rest_framework_mongoengine import serializers
from . import models
 
class roomSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.room
        fields = '__all__' #这个是将所有的字段都序列化
 

 
class postSerializer(serializers.DocumentSerializer):
    # user = serializers.ObjectIdField(source = "")
    class Meta:
        model = models.post
        fields = '__all__' #这个是将所有的字段都序列化
 

class userSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.user
        fields = '__all__' #这个是将所有的字段都序列化


class followingSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.following
        fields = '__all__' #这个是将所有的字段都序列化



class userSerializer(serializers.DocumentSerializer):
    class Meta:
        model = models.user
        fields = '__all__' #这个是将所有的字段都序列化




class data2Serializer(serializers.DocumentSerializer):
    class Meta:
        model = models.data2
        fields = '__all__' #这个是将所有的字段都序列化