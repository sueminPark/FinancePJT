from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content')


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    # class ArticleSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Article
    #         fields = ('title',)

    # override
    # article = ArticleSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        # read_only_fields = ('article','user',)
