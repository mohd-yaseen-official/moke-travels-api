from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from places.models import *


class PlaceSerializer(ModelSerializer):

    is_liked = serializers.SerializerMethodField() # It can be used to show solid heart image when the place is liked by the user

    class Meta:
        model = Place
        fields = ('id', 'name', 'featured_image', 'location', 'category', 'total_likes')

    def get_is_liked(self, place):
        current_user = self.context.get('request').user
        return place.likes.filter(id=current_user.id).exists()


class GallerySerializer(ModelSerializer):

    class Meta:
        model = Gallery
        fields = ('id', 'image')


class CommentSerializer(ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'user', 'created_at')

    def get_user(self, comment):
        return comment.user.first_name


class PlaceDetailSerializer(ModelSerializer):

    category = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField() # It can be used to show solid heart image when the place is liked by the user

    class Meta:
        model = Place
        fields = ('id', 'name', 'description', 'featured_image', 'location', 'category', 'gallery', 'total_likes', 'is_liked')

    def get_category(self, place):
        return place.category.name
    
    def get_gallery(self, place):
        images = Gallery.objects.filter(place=place)
        serializer = GallerySerializer(images, many=True, context={"request": self.context.get('request')})
        return serializer.data
        
    def get_is_liked(self, place):
        current_user = self.context.get('request').user
        return place.likes.filter(id=current_user.id).exists()


class CategorySerializer(ModelSerializer):
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'image')


class ReplySerializer(ModelSerializer):
     
    user = serializers.SerializerMethodField()

    class Meta:
        model = Reply
        fields = ('id', 'reply', 'user', 'created_at')
    
    def get_user(self, reply):
        return reply.user.first_name
    

class CommentSerializer(ModelSerializer):

    user = serializers.SerializerMethodField()
    reply = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('id','comment', 'user', 'created_at', 'reply')

    def get_user(self, comment):
        return comment.user.first_name
    
    def get_reply(self, comment):
        replies = Reply.objects.filter(comment=comment)

        serializer = ReplySerializer(replies, many=True, context={"request": self.context.get('request')})

        return serializer.data