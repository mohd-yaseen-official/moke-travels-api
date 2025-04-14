from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.db.models import Q

from places.models import *
from .pagination import StandardResultSetPagination
from .serializer import *


@api_view(['GET'])
@permission_classes([AllowAny])
def places(request):

    places = Place.objects.all()

    query = request.GET.get('q')
    categories_query = request.GET.get('category')
    if query:
        places = places.filter(Q(name__icontains=query) | Q(location__icontains=query))

    if categories_query:
        pks = categories_query.split(',')
        places = places.filter(category__in=pks)
 

    paginator = StandardResultSetPagination()
    paginator_instance = paginator.paginate_queryset(places, request)

    serializer = PlaceSerializer(paginator_instance, many=True, context={"request": request})

    response_data = {
        "status": 2200,
        'count': paginator.page.paginator.count,
        'links': {
            'next': paginator.get_next_link(),
            'previous': paginator.get_previous_link(),
        },
        "data": serializer.data
    }
    return Response(response_data)


@api_view(['GET'])
def view_place(request, pk):

    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)

        serializer = PlaceDetailSerializer(place, context={"request": request})

        response_data = {
            "status": 2200,
            "data": serializer.data
        }
        return Response(response_data)
    
    else:
        response_data = {
            "status": 2404,
            "message": 'Place Not Found'
        }
        return Response(response_data)
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_protected_place(request, pk):

    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)

        serializer = PlaceDetailSerializer(place, context={"request": request})

        response_data = {
            "status": 2200,
            "data": serializer.data
        }
        return Response(response_data)
    
    else:
        response_data = {
            "status": 2404,
            "message": 'Place Not Found'
        }
        return Response(response_data)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def categories(request):
    categories = Category.objects.all()

    serializer = CategorySerializer(categories, many=True)

    response_data = {
        "status": 2200,
        "data": serializer.data
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_comments(request, pk):
    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)
        comments = Comment.objects.filter(place=place)

        serializer = CommentSerializer(comments, many=True, context={"request": request})

        response_data = {
            'status': 2200,
            'data': serializer.data
        }
    else:
        response_data = {
            "status": 2400,
            "message": 'Place Not Found'
        }

    return Response(response_data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_comment(request, pk):

    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, place=place)

            response_data = {
                "status": 2200,
                "message": 'Comment Added Successfully'
            }
            return Response(response_data)
        else:
            response_data = {
                "status": 2400,
                "message": 'Failed to Add Comment',
                "errors": serializer.errors
            }
            return Response(response_data)
    else:
        response_data = {
            "status": 2400,
            "message": 'Place Not Found'
        }
        return Response(response_data)
    

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_likes(request, pk):
    
    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)

        if place.likes.filter(id=request.user.id).exists():
            place.likes.remove(request.user)
            response_data = {
                "status": 2200,
                "message": 'Disliked Place'
            }
        else:
            place.likes.add(request.user)
            response_data = {
                "status": 2200,
                "message": 'Liked Place'
            }
    else:
        response_data = {
            "status": 2400,
            "message": 'Place Not Found'
        }
    
    return Response(response_data)


@api_view(['GET'])
@permission_classes([AllowAny])
def view_likes(request, pk):
    
    if Place.objects.filter(pk=pk).exists():
        place = Place.objects.get(pk=pk)
        
        likes_list = []
        for user in place.likes.all():
            likes_list.append(user.first_name)

        response_data = {
            "status": 2200,
            'total_likes': place.total_likes(),
            "data": likes_list
        }
    else:
        response_data = {
            "status": 2400,
            "message": 'Place Not Found'
        }
    
    return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_reply(request, pk):
    
    if Comment.objects.filter(pk=pk):
        comment = Comment.objects.get(pk=pk)
        reply = request.data.get('reply')
        Reply.objects.create(reply=reply, comment=comment, user=request.user)

        response_data = {
            'status': 2200,
            'message': 'Reply added'
        }
    else:
        response_data = {
            'status': 2400,
            'message': 'Comment not found'
        }
    return Response(response_data)