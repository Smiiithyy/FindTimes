from pyexpat import model
from rest_framework import serializers
from .models import Bar, Comment, Games


    

        

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
        fields = ('id', 'bar_id', 'bar','name', 'comment', 'image')
        
class GameSerializer(serializers.HyperlinkedModelSerializer):
    game= serializers.HyperlinkedRelatedField(
        view_name='game_detail',
        read_only= True
    )
    bar_id = serializers.PrimaryKeyRelatedField(
        queryset = Bar.objects.all(),
        source = 'bar'
        
    )
    
    class Meta:
        model = Games
        fields = ('id', 'bar_id', 'game', 'sport', 'gametime','teamOne','teamTwo','timeofpost')
    
        

class BarSerializer(serializers.HyperlinkedModelSerializer):
    # comment = serializers.HyperlinkedRelatedField(
    #     view_name='comment_detail',
    #     many = True,
    #     read_only = True
    # )     
    comment = CommentSerializer(many = True)
    game = GameSerializer(many=True)
    
    bar_url = serializers.ModelSerializer.serializer_url_field(
        view_name = 'bar_detail'
    )
    
    class Meta: 
        model = Bar
        # fields = ('id', 'bar_name', 'photo_url', 'address', 'city', 'state', 'comment')
        fields =('id', 'bar_name', 'photo_url','address', 'city', 'state','bar_url', 'comment','game')
        
        