# from django.shortcuts import render
# from django.http import JsonResponse
#
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import RestaurantSerializer
#
# from .models import Restaurant
# # Create your views here.
#
# @api_view(['GET'])
# def apiOverview(request):
# 	api_urls = {
# 		'List':'/task-list/',
# 		'Detail View':'/task-detail/<str:pk>/',
# 		'Create':'/task-create/',
# 		'Update':'/task-update/<str:pk>/',
# 		'Delete':'/task-delete/<str:pk>/',
# 		}
#
# 	return Response(api_urls)
#
# @api_view(['GET'])
# def taskList(request):
# 	tasks = Restaurant.objects.all().order_by('-id')
# 	serializer = RestaurantSerializer(tasks, many=True)
# 	return Response(serializer.data)
#
# @api_view(['GET'])
# def taskDetail(request, pk):
# 	tasks = Restaurant.objects.get(id=pk)
# 	serializer = RestaurantSerializer(tasks, many=False)
# 	return Response(serializer.data)
#
#
# @api_view(['POST'])
# def taskCreate(request):
# 	serializer = RestaurantSerializer(data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
# @api_view(['POST'])
# def taskUpdate(request, pk):
# 	task = Restaurant.objects.get(id=pk)
# 	serializer = RestaurantSerializer(instance=task, data=request.data)
#
# 	if serializer.is_valid():
# 		serializer.save()
#
# 	return Response(serializer.data)
#
#
# @api_view(['DELETE'])
# def taskDelete(request, pk):
# 	task = Restaurant.objects.get(id=pk)
# 	task.delete()
#
# 	return Response('Item succsesfully delete!')
#
#
#
