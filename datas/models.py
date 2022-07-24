# Create your models here.
from __future__ import unicode_literals
from django.db import models
# from datas.models import following as following_, post as post_
from mongoengine import *

class room(Document):
    _id = ObjectIdField(max_length=45)
    rating = DecimalField(max_length=45)
    price = IntField(max_length=45)
    name = StringField(max_length=45)
    payment = ListField(max_length=45)

    # 指明连接的数据表名
    meta = {'collection': 'rooms'}

    def __unicode__(self):
        return self.name
   


class user(Document):
    _id = ObjectIdField(primary_key=True, max_length=45)
    name = StringField(max_length=45)
    username = StringField(max_length=45)
    password = StringField(max_length=45)
    role = StringField(max_length=45)
    sex = StringField(max_length=45)
    photo = StringField(max_length=45)
    tokens = ListField(max_length=45)
    createdAt = DateTimeField(max_length=45)
    updatedAt = DateTimeField(max_length=45)
    # followings = ListField(ReferenceField('following'))
    # followings = ListField(ReferenceField('following'))
    followings = ListField(ReferenceField('following',  bref=False))


    # followings = ListField(ReferenceField('self'))
    # followings = ListField(ObjectIdField())

    # followings = models.ForeignKey('following', blank=True, on_delete=models.CASCADE)
    likePosts = ListField(ReferenceField('post', bref=False))
    # likePosts = ListField(models.ForeignKey('post', blank=True, on_delete=models.CASCADE))


    # 指明连接的数据表名
    meta = {'collection': 'users'}

    # def __unicode__(self):
    #     return self.name
        # return self.tags




class following(Document):
    _id = ObjectIdField(primary_key = True, max_length=45)
    # user = StringField(ReferenceField(user))
    # user = StringField(ReferenceField(user))
    user = ReferenceField('user', bref=False)
    # whoFollow = ListField(ReferenceField(user))
    # whoFollow = ListField(models.ForeignKey(user, on_delete=models.CASCADE))
    whoFollow = ReferenceField('user',  bref=False)
    createdAt = DateTimeField(max_length=45)
    updatedAt = DateTimeField(max_length=45)

    # 指明连接的数据表名
    meta = {'collection': 'followings'}
    # def __unicode__(self):
    #     return self.name


# following.register_delete_rule(user, 'followings', PULL)


class comment_detail(Document):
    _id = ObjectIdField(max_length=45)
    user = ReferenceField(user)
    content = StringField(max_length=45)
    likes = IntField(max_length=45)
    whoLikes = ListField(ReferenceField('user'))
    createdAt = DateTimeField(max_length=45)
    updatedAt = DateTimeField(max_length=45)

    # 指明连接的数据表名
    meta = {'collection': 'comment_details'}
    # def __unicode__(self):
    #     return self.name


class post(Document):
    _id = ObjectIdField(primary_key=True,max_length=45)
    user = ReferenceField('user')
    tags = ListField(max_length=45)
    type = StringField(max_length=45)
    image = StringField(max_length=45)
    content = StringField(max_length=45)
    likes = IntField(max_length=45)
    whoLikes = ListField(ReferenceField('user'))
    comments = IntField(max_length=45)
    commentDetail = ListField(ReferenceField('comment_detail'))
    createdAt = DateTimeField(max_length=45)
    updatedAt = DateTimeField(max_length=45)

    # 指明连接的数据表名
    meta = {'collection': 'posts'}
    # def __unicode__(self):
    #     return self.name


# class like(Document):
#     _id = ObjectIdField(max_length=45)
#     createdAt = DateTimeField(max_length=45)
#     updatedAt = DateTimeField(max_length=45)

#     # 指明连接的数据表名
#     meta = {'collection': 'likes'}

#     def __unicode__(self):
#         return self.name





class data2(Document):
    _id = ObjectIdField(max_length=45)
    rating = DecimalField(max_length=45)
    price = IntField(max_length=45)
    name = StringField(max_length=45)
    payment = ListField(max_length=45)


    # 指明连接的数据表名
    meta = {'collection': 'rooms'}
    def __unicode__(self):
        return self.name

    # _id = ObjectIdField(max_length=45)
    # user = StringField(max_length=45)
    # tags = StringField(max_length=45)
    # type = StringField(max_length=45)
    # image = StringField(max_length=45)
    # content = Int32Field(max_length=45)
    # likes = StringField(max_length=45)
    # whoLikes = ObjectIdField(max_length=45)
    # comments = Int32Field(max_length=45)
    # commentDetail = StringField(max_length=45)
    # createdAt = DateTimeField(max_length=45)
    # updatedAt = DateTimeField(max_length=45)

    # # 指明连接的数据表名
    # meta = {'collection':'posts'}
    # def __unicode__(self):
    #     return self.name
