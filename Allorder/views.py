from django.shortcuts import render
import requests
import os
import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from . models import Product,Customer
from . form import UpdateForm
def create_product(request):
	if request.method == 'GET':
		headers = {"Accept": "application/json", "Content-Type": "application/json"}
		r = requests.get("https://ed132262e67d426893252a6a25146285:e498ddfb0638a28216e60c34b90cffef@cab-store12.myshopify.com/admin/api/2019-04/products.json")
		#data = serializers.serialize('json', r)
		data=r.json()
		print("length : ",)
		for i in range(0,len(data["products"])):
			title = data["products"][i]["title"]
			Product.objects.create(title=title)
		products = json.loads(r.text)
        
		# print("length : ",data["orders"][0]["default_address"])
		context={
		 "products":products.get("products")
		}

		return render(request,'Allorder/all_order.html',context)



