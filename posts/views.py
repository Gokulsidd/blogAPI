from django.shortcuts import render , get_object_or_404
from rest_framework import generics , status
from rest_framework.response import Response
from .permissions import IsAuthorOrReadonly 
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.urls import reverse
from django.http import HttpResponseRedirect


from .models import Post , Comment ,Vote
from .serializers import PostSerializer , CommentSerializer , VoteSerializer
# Create your views here.

class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadonly ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadonly ,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class CommentCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = CommentSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class VoteCreate(generics.CreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = VoteSerializer

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                vote = Vote.objects.get(user=self.request.user, post=post)
                vote.value = serializer.validated_data['value']
                vote.save()
            except Vote.DoesNotExist:
                serializer.save(user=self.request.user, post=post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    


