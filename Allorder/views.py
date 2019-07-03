from django.shortcuts import render
import requests
import os
import json
from django.http import HttpResponse
from django.http import JsonResponse
SHOPIFY_API_KEY = os.environ.get('ed132262e67d426893252a6a25146285')
SHOPIFY_API_SECRET = os.environ.get('e498ddfb0638a28216e60c34b90cffef')
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

		




def customer_detail(request):
	if request.method == 'GET':
		headers = {"Accept": "application/json", "Content-Type": "application/json"}
		r = requests.get("https://ed132262e67d426893252a6a25146285:e498ddfb0638a28216e60c34b90cffef@cab-store12.myshopify.com/admin/api/2019-04/orders.json")
		data=r.json()

		for i in range(0,len(data["orders"])):
			email = data["orders"][i]["customer"]["email"]
			customer_id = data["orders"][i]["customer"]["id"]
			first_name = data["orders"][i]["customer"]["first_name"]
			last_name = data["orders"][i]["customer"]["last_name"]
			name = first_name + last_name
			contactno = data["orders"][i]["customer"]["phone"]
			allCustomer = Customer.objects.values('customer_id')
			if allCustomer:
				for a in allCustomer:
					if str(customer_id) not in a["customer_id"]:
						print("true")
						Customer.objects.create(email=email,customer_id=customer_id,name=name,contactno=contactno)
			else:
				Customer.objects.create(email=email,customer_id=customer_id,name=name,contactno=contactno)
		return JsonResponse(data)
		


def cutomer_page(request):
	query_set=Customer.objects.all()
	context={
	'customer':query_set
	}
	return render(request,'Allorder/customer_detail.html', context)

def edit_customer(request,customer_id):
	customer_id = customer_id
	email = request.POST['email']
	contactno = request.POST['contactno']
	print("id: ",customer_id)
	abc = Customer.objects.filter(customer_id=customer_id).first()
	print("data : ",abc.email)
	Customer.objects.filter(customer_id=customer_id).update(email=email,contactno=contactno)
	query_set=Customer.objects.all()
	context={
	'customer':query_set
	}
	return render(request,'Allorder/customer_detail.html', context)


def edit_customer_page(request,customer_id):
	customer_id = customer_id
	form = UpdateForm(request.POST or None)
	context={
	'customer_id': customer_id,
	'form':form
	}
	return render(request,'Allorder/updata_detail.html', context)

def webhook_call(request):
	r=requests.get("https://ed132262e67d426893252a6a25146285:e498ddfb0638a28216e60c34b90cffef@cab-store12.myshopify.com/admin/api/2019-04/webhooks.json")
	data=r.json()
	return JsonResponse(data)