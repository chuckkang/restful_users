from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from models import User, UserManager
def index(request):
	# display all of the user
	# create inital group of uses:
		# user_data = User.objects.create(first_name="Chuck", last_name="Kang", email="asdf@asdf.com".lower())
		# user_data = User.objects.create(first_name="Michelle", last_name="Kang", email="qwer@qwer.com".lower())
		# user_data = User.objects.create(first_name="Thomas", last_name="Kang", email="zxcv@zxcv.com".lower())

	context = {
		'user_data': User.objects.all()
	}
	return render(request, "restful_user/index.html", context)

def create(request):
	#  create a NEW user
	if request.method=="GET":	
		return render(request, "restful_user/create.html")
	else:
		return redirect("/restful_user") #send user to the index.page

def show(request, id):
	# if id = get information from the first user id
	context = { 'user': User.objects.get(id=id) }
	
	return render(request, "restful_user/show.html", context)

def edit(request, id):
	
	if request.method=="POST":
		# do error validation
		errors = (User.objects.basic_validator(request.POST))

		if len(errors)>0:
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return redirect("/users/" + id + "/edit")
	
		else:
			# do the update
			user = User.objects.get(id=id)
			user.first_name = request.POST['first_name'].strip()
			user.last_name = request.POST['last_name'].strip()
			user.email = request.POST['email'].strip().lower()
			user.save()
			messages.add_message(request, messages.INFO, "User has beeen updated.")
			return redirect ("/users/"+str(user.id))
	else:
		context = {
			'user': User.objects.get(id=id)
		}
		return render(request, "restful_user/edit.html", context)
	

def delete(request, id):
	if (request.method=="GET"):
		user = { 'user': User.objects.get(id=id)}
		return render(request, "restful_user/delete.html", user)
	else:
		id = request.POST['id']
		try:
			x = User.objects.get(id=id)
			if (x):
				deleted = User.objects.get(id=id).delete()
				errMessage = "User has been deleted"
		except:
			errMessage = "User does not exist"
			messages.add_message(request,  messages.INFO, errMessage)
		return redirect("/")

def new_user(request):
	
	if request.method=="GET":
		return render(request, "restful_user/create.html")
	else:
		# make sure all the fields are done.
		errors = User.objects.basic_validator(request.POST)

		if len(errors)>0:
			for tag, error in errors.iteritems():
				messages.error(request, error, extra_tags=tag)
			return render(request, "restful_user/create.html")
		else:

			User.objects.create(first_name=request.POST['first_name'].strip(), last_name=request.POST['last_name'].strip(), email= request.POST['email'].strip().lower())
			messages.add_message(request, messages.INFO, "User has been added")
			return redirect("/")
			

