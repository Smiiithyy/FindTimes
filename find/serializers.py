from pyexpat import model
from rest_framework import serializers
from .models import Bar, Comment


    
class BarSerializer(serializers.HyperlinkedModelSerializer):
    comment = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many = True,
        read_only = True
    )     
    
    bar_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'bar_detail'
    )
    
    class Meta: 
        model = Bar
        # fields = ('id', 'bar_name', 'photo_url', 'address', 'city', 'state', 'comment')
        fields =('id', 'bar_url', 'comment')
        

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    bar = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        read_only = True
    )     
    
    bar_id = serializers.PrimaryKeyRelatedField(
        queryset=Bar.objects.all(),
        source = 'bar'
    )
    
    class Meta: 
        model = Comment
        # fields = ('id', 'bar', 'name', 'comment')
        fields = ('id', 'bar_id', 'bar','name', 'comment')