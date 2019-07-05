from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render,redirect
import requests
from Allorder.models import Product,Customer
from Allorder .form import UpdateForm
from django.http import HttpResponseRedirect, HttpResponse
def cutomer_page(request):
	query_set=Customer.objects.all()
	context={
		'customer':query_set
	}
	from  django.db.utils import IntegrityError
	if request.method == 'GET':
		headers = {"Accept": "application/json", "Content-Type": "application/json"}
		r = requests.get("https://ed132262e67d426893252a6a25146285:e498ddfb0638a28216e60c34b90cffef@cab-store12.myshopify.com/admin/api/2019-04/orders.json")
		data=r.json()
		try : 
			# print("lenght : ",data["orders"][i]["customer"]["id"])
			for i in range(0,len(data["orders"])):
				email = data["orders"][i]["customer"]["email"]
				customer_id = data["orders"][i]["customer"]["id"]
				first_name = data["orders"][i]["customer"]["first_name"]
				last_name = data["orders"][i]["customer"]["last_name"]
				name = first_name + last_name
				contactno = data["orders"][i]["customer"]["phone"]
				Customer.objects.create(email=email,customer_id=customer_id,name=name,contactno=contactno)
			return render(request,"home_page.html",context)
		except IntegrityError :
			return render(request,"home_page.html",context)
	return render(request,"home_page.html",context)

def edit_customer(request,customer_id):
	customer_id = customer_id
	email = request.POST['email']
	contactno = request.POST['contactno']
	print("id: ",customer_id)
	abc = Customer.objects.filter(customer_id=customer_id).first()
	print("data : ",abc.email)
	Customer.objects.filter(customer_id=customer_id).update(email=email,contactno=contactno)
	return HttpResponseRedirect('/')


def edit_customer_page(request,customer_id):
	customer_id = customer_id
	form = UpdateForm(request.POST or None)
	context={
	'customer_id': customer_id,
	'form':form
	}
	return render(request,'updata_detail.html', context)