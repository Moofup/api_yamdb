from rest_framework import serializers

from posts.models import Post, Group, Comment, User


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(many=True,
                                         read_only=True,
                                         slug_field='posts')

    class Meta:
        model = User
        fields = ('id', 'username', 'posts')
        ref_name = 'ReadOnlyUsers'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = ('id', 'author', 'text', 'post', 'created')
        model = Comment
