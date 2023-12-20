from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser 
from django.shortcuts import render, get_object_or_404
from rest_framework import status, viewsets

import json
class EmployeeViewSet(viewsets.ModelViewSet):
	queryset = Employee.objects.all()
	serializer_class = EmployeeSerializer

	def retrieve(self, request, pk=0): #Retrieve Single Record based on primary key
		Emp = get_object_or_404(Employee, pk=pk)
		return JsonResponse({
	            "employee_regNo": Emp.employee_regNo,
	            "emplyee_name": Emp.employee_name,
	            "employee_email": Emp.employee_email,
	            "employee_mobile": Emp.employee_mobile
	        })

	def list(self,request): #Retrieving all Objects
		print("--------------------------")
		print("Inside List()")
		print("--------------------------")
		try:
			Emp = Employee.objects.all()
			data_list = []
			for i in Emp:
				print(i.__dict__)
				data_list.append({
	            "employee_regNo": i.employee_regNo,
	            "emplyee_name": i.employee_name,
	            "employee_email": i.employee_email,
	            "employee_mobile": i.employee_mobile
				})
			print(data_list)
			return JsonResponse({
				"Status": data_list
				})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Fail to Retrieve Entire DB!"
				})

	def create(self, request): #POST request for creating a new record
		print("------------------")
		print("Inside POST()")
		print("------------------")
		try:
			print(request)
			print(request.method)
			print(request.__dict__)
			data = json.loads(request.body.decode())
			obj = Employee()
			obj.employee_regNo = data.get('employee_regNo',id)
			obj.employee_name = data.get('emplyee_name',id)
			obj.employee_email = data.get('employee_email',id)
			obj.employee_mobile = data.get('employee_mobile',id)
			obj.save()
			return JsonResponse({
				"Status": "Successfully Inserted"
			})
		except Exception as e:
			print(e)
			return JsonResponse({
                "Status": "Record Already Exists!"
            })

	def update(self, request, pk=None): #Update request for updating a record or Modifying Record
		print("---------------------")
		print("Inside Update()")
		print("---------------------")
		try:
			data = json.loads(request.body.decode())
			obj = Employee.objects.get(id=pk)  
			obj.employee_regNo = data.get('employee_regNo',id)
			obj.employee_name = data.get('emplyee_name',id)
			obj.employee_email = data.get('employee_email',id)
			obj.employee_mobile = data.get('employee_mobile',id)
			obj.save()
			return JsonResponse({
			"Status": "Successfully Updated"
		})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Updating Data"
		})

	def destroy(self, request, pk=None): #Delete request for deleting a certain record by the PK
		print("--------------------")
		print("Inside Destroy()")
		print("--------------------")
		print(pk)
		try:
			Emp = Employee.objects.all()
			Emp.delete()
			return JsonResponse({
				"Status" : "Successfully Deleted"
				})
		except Exception as e:
			print(e)
			return JsonResponse({
				"Status": "Error While Deleting data from db",
			})
		
