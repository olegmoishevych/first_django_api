from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer


def index(request):
  return HttpResponse("Privet!")


@api_view(['GET', 'POST'])
def blog_posts(request):
  if request.method == 'GET':
    posts = BlogPost.objects.all()
    serializer = BlogPostSerializer(posts, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    serializer = BlogPostSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_blog_post(request, post_id):
  try:
    post = BlogPost.objects.get(id=post_id)
  except BlogPost.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  post.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def update_blog_post(request, post_id):
  try:
    post = BlogPost.objects.get(id=post_id)
  except BlogPost.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  serializer = BlogPostSerializer(post, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
