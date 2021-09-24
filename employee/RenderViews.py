from django.shortcuts import render, redirect
from .models import Employee
from .serializer import EmployeeSerializer


# from rest_framework.decorators import action, api_view
from django.http import JsonResponse
# from .views import HttpResponse
# from rest_framework.parsers import JSONParser 
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets

import json

class listViewSet(viewsets.ModelViewSet):
	def index(request):
		return render(request,'employee/index.html')
	

	def retrieve(self, request, pk=0):
		print("-----------------------------")
		print("Inside Render Get()")
		print("-----------------------------")
		try:
			Emp = get_object_or_404(Employee, pk=pk)
			return JsonResponse({
				"employee_regNo": Emp.employee_regNo,
				"emplyee_name": Emp.employee_name,
				"employee_email": Emp.employee_email,
				"employee_mobile": Emp.employee_mobile
			})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Record Doesn't exists"
			})

	#Retrieving all Objects
	def list(request):
		# print("--------------------------")
		# print("Inside Render List()")
		# print("--------------------------")
		try:
			Emp = Employee.objects.all()
			data_list = []
			for i in Emp:
				# print(i.__dict__)
				data_list.append({
				"employee_id": i.employee_id,
				"employee_regNo": i.employee_regNo,
				"emplyee_name": i.employee_name,
				"employee_email":i.employee_email,
				"employee_mobile": i.employee_mobile
				})
			# print(data_list)
			return render(request ,'employee/get.html' , {'data': data_list})
			# return JsonResponse({
			# 	"Status": data_list
			# 	})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	#POST request for creating a new record
	def create(request):
		print("------------------",request._post['employee_regNo'])
		
		print("------------------")
		try:
			# print(request)
			# print(request._post)
			# print(request.__dict__)
			print("Start of Try Block")				
			# print("request",request.__dict__)
			print("Middle of Try Block")
			obj = Employee()
			obj.employee_regNo = request._post['employee_regNo']
			obj.employee_name = request._post['username']
			obj.employee_email = request._post['email']
			obj.employee_mobile = request._post['number']
			obj.save()
			return redirect('get-employee')
			return JsonResponse({
				"Status": "Successfully Inserted"
			})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "OOPS! Records Already Exists!"
			})


	def update(request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print(request.method)
		print("---------------------")
		try:
			print("Start of Update")
			print("--------------------------------")
			print(pk)
			obj = Employee.objects.get(employee_id=pk)
			print("--------------------------------")
			print(request.method)
			if(request.method == 'POST'):	
				print("Inside Post Request()")
				obj.employee_regNo = request._post['employee_regNo']
				obj.employee_name = request._post['username']
				obj.employee_email = request._post['email']
				obj.employee_mobile = request._post['number']
				obj.save()
				return redirect('get-employee')
			else:
				return render(request,'employee/update.html', {'data': obj, 'pk':pk})

		# 	return JsonResponse({
		# 	"Status": "Successfully Updated"
		# })
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	#Delete request for deleting a certain record by the PK
	def destroy(request, pk=None):
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			# Emp = Employee.objects.all()
			obj = Employee.objects.get(employee_id=pk)
			obj.delete()
			return redirect('get-employee')
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})