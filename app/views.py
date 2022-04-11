from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.

def home(request):
	return render(request,'index.html')

def signup(request):
	if request.method == "POST":
		fn = request.POST['fname']
		ln = request.POST['lname']
		ec = request.POST['empcode']
		em = request.POST['email']
		pwd = request.POST['pass']
		try:
			user = User.objects.create_user(first_name=fn,last_name=ln,username=em,password=pwd)
			EmployeeDetail.objects.create(user=user,empcode=ec)
			EmployeeExperience.objects.create(user=user)
			EmployeeEducation.objects.create(user=user)
			error="no"
		except:
			error="yes"

	return render(request,'signup.html',locals())

def emplogin(request):
	if request.method == "POST":
		e = request.POST['mail']
		p = request.POST['emppass']
		user=authenticate(username=e,password=p)
		if user:
			login(request,user)
			error="no"
		else:
			error="yes"

	return render(request,'emplogin.html',locals())

def emphome(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	return render(request,'emphome.html')

def emprofile(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	employee = EmployeeDetail.objects.get(user=user)
	if request.method == "POST":
		fn = request.POST['fname']
		ln = request.POST['lname']
		ec = request.POST['empcode']
		dp = request.POST['department']
		ds = request.POST['designation']
		c = request.POST['contact']
		jd = request.POST['jdate']
		g = request.POST['gender']

		employee.user.first_name = fn
		employee.user.last_name = ln
		employee.empcode = ec
		employee.empdept = dp
		employee.designation = ds		
		employee.contact= c
		employee.gender = g
		if jd:
			employee.joiningdate = jd
		try:
			employee.save()
			employee.user.save()
			error="no"
		except:
			error="yes"
	return render(request,'emprofile.html',locals())

def Logout(request):
	logout(request)
	return redirect('home')

	
def myexperience(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	experience = EmployeeExperience.objects.get(user=user)
	
	return render(request,'myexperience.html',locals())

def editexperience(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	experience = EmployeeExperience.objects.get(user=user)
	if request.method == "POST":
		c1n = request.POST['company1name']
		c1des = request.POST['company1desig']
		c1s = request.POST['company1salary']
		c1dur = request.POST['company1duration']
		c2n = request.POST['company2name']
		c2des = request.POST['company2desig']
		c2s = request.POST['company2salary']
		c2dur = request.POST['company2duration']
		c3n = request.POST['company3name']
		c3des = request.POST['company3desig']
		c3s = request.POST['company3salary']
		c3dur = request.POST['company3duration']

		experience.company1name = c1n
		experience.company1desig = c1des
		experience.company1salary = c1s
		experience.company1duration = c1dur
		experience.company2name = c2n
		experience.company2desig = c2des
		experience.company2salary = c2s
		experience.company2duration = c2dur
		experience.company3name = c3n
		experience.company3desig = c3des
		experience.company3salary = c3s
		experience.company3duration = c3dur

		try:
			experience.save()
			error="no"
		except:
			error="yes"
	
	return render(request,'editexperience.html',locals())

def myeducation(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	education = EmployeeEducation.objects.get(user=user)
	
	return render(request,'myeducation.html',locals())

def editeducation(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	education = EmployeeEducation.objects.get(user=user)
	if request.method == "POST":

		corsepg = request.POST['corsepg']
		schoolclgpg = request.POST['schoolclgpg']
		yearofpassingpg = request.POST['yearofpassingpg']
		percentagepg= request.POST['percentagepg']

		corsegra = request.POST['corsegra']
		schoolclggra = request.POST['schoolclggra']
		yearofpassinggra = request.POST['yearofpassinggra']
		percentagegra= request.POST['percentagegra']

		corsessc = request.POST['corsessc']
		schoolclgssc = request.POST['schoolclgssc']
		yearofpassingssc = request.POST['yearofpassingssc']
		percentagessc= request.POST['percentagessc']

		corsehsc = request.POST['corsehsc']
		schoolclghsc = request.POST['schoolclghsc']
		yearofpassinghsc = request.POST['yearofpassinghsc']
		percentagehsc= request.POST['percentagehsc']

		education.corsepg = corsepg
		education.schoolclgpg = schoolclgpg
		education.yearofpassingpg = yearofpassingpg
		education.percentagepg = percentagepg
		education.corsegra = corsegra
		education.schoolclggra = schoolclggra
		education.yearofpassinggra = yearofpassinggra
		education.percentagegra = percentagegra
		education.corsessc = corsessc
		education.schoolclgssc = schoolclgssc
		education.yearofpassingssc = yearofpassingssc
		education.percentagessc = percentagessc
		education.corsehsc = corsehsc
		education.schoolclghsc = schoolclghsc
		education.yearofpassinghsc = yearofpassinghsc
		education.percentagehsc = percentagehsc


		try:
			education.save()
			error="no"
		except:
			error="yes"
	
	return render(request,'editeducation.html',locals())

def changepass(request):
	if not request.user.is_authenticated:
		return redirect('emplogin')
	user=request.user
	if request.method == "POST":
		c = request.POST['curpass']
		n = request.POST['npass']

		if user.check_password(c):
			user.set_password(n)
			user.save()
			error="no"
		else:
			error="not"

	return	render(request,'changepass.html',locals())


def admlogin(request):
	if request.method == "POST":
		u = request.POST['username']
		p = request.POST['pass']
		user=authenticate(username=u,password=p)
		try:
			if user.is_staff:
				login(request,user)
				error="no"
			else:
				error="yes"
		except:
			error="yes"

	return render(request,'admlogin.html',locals())


def adminhome (request):
	if not request.user.is_authenticated:
		return redirect	('admlogin')
	return	render(request,'adminhome.html')

def changepassadmin(request):
	if not request.user.is_authenticated:
		return redirect('admlogin')
	user=request.user
	if request.method == "POST":
		c = request.POST['curpass']
		n = request.POST['npass']

		if user.check_password(c):
			user.set_password(n)
			user.save()
			error="no"
		else:
			error="not"

	return	render(request,'changepassadmin.html',locals())

def allemployee (request):
	if not request.user.is_authenticated:
		return redirect	('admlogin')
	employee =  EmployeeDetail.objects.all()
	return	render(request,'allemployee.html',locals())

def deleteemp (request,pid):
	if not request.user.is_authenticated:
		return redirect	('admlogin')
	user =  EmployeeDetail.objects.get(id=pid)
	user.delete()
	return	redirect('allemployee')

def editprofileadm (request,pid):
	if not request.user.is_authenticated:
		return redirect('admlogin')
	employee = EmployeeDetail.objects.get(id=pid)
	if request.method == "POST":
		fn = request.POST['fname']
		ln = request.POST['lname']
		ec = request.POST['empcode']
		dp = request.POST['department']
		ds = request.POST['designation']
		c = request.POST['contact']
		jd = request.POST['jdate']
		g = request.POST['gender']

		employee.user.first_name = fn
		employee.user.last_name = ln
		employee.empcode = ec
		employee.empdept = dp
		employee.designation = ds		
		employee.contact= c
		employee.gender = g
		if jd:
			employee.joiningdate = jd
		try:
			employee.save()
			employee.user.save()
			error="no"
		except:
			error="yes"
	return render(request,'editprofileadm.html',locals())


def editeducationadm(request,pid):
	if not request.user.is_authenticated:
		return redirect('admlogin')

	user = User.objects.get(id=pid)
	education = EmployeeEducation.objects.get(user=user)


	if request.method == "POST":

		corsepg = request.POST['corsepg']
		schoolclgpg = request.POST['schoolclgpg']
		yearofpassingpg = request.POST['yearofpassingpg']
		percentagepg= request.POST['percentagepg']

		corsegra = request.POST['corsegra']
		schoolclggra = request.POST['schoolclggra']
		yearofpassinggra = request.POST['yearofpassinggra']
		percentagegra= request.POST['percentagegra']

		corsessc = request.POST['corsessc']
		schoolclgssc = request.POST['schoolclgssc']
		yearofpassingssc = request.POST['yearofpassingssc']
		percentagessc= request.POST['percentagessc']

		corsehsc = request.POST['corsehsc']
		schoolclghsc = request.POST['schoolclghsc']
		yearofpassinghsc = request.POST['yearofpassinghsc']
		percentagehsc= request.POST['percentagehsc']

		education.corsepg = corsepg
		education.schoolclgpg = schoolclgpg
		education.yearofpassingpg = yearofpassingpg
		education.percentagepg = percentagepg
		education.corsegra = corsegra
		education.schoolclggra = schoolclggra
		education.yearofpassinggra = yearofpassinggra
		education.percentagegra = percentagegra
		education.corsessc = corsessc
		education.schoolclgssc = schoolclgssc
		education.yearofpassingssc = yearofpassingssc
		education.percentagessc = percentagessc
		education.corsehsc = corsehsc
		education.schoolclghsc = schoolclghsc
		education.yearofpassinghsc = yearofpassinghsc
		education.percentagehsc = percentagehsc


		try:
			education.save()
			error="no"
		except:
			error="yes"
	
	return render(request,'editeducationadm.html',locals())

def editexperienceadm(request,pid):
	if not request.user.is_authenticated:
		return redirect('admlogin')

	user = User.objects.get(id=pid)
	experience = EmployeeExperience.objects.get(user=user)
	if request.method == "POST":
		c1n = request.POST['company1name']
		c1des = request.POST['company1desig']
		c1s = request.POST['company1salary']
		c1dur = request.POST['company1duration']
		c2n = request.POST['company2name']
		c2des = request.POST['company2desig']
		c2s = request.POST['company2salary']
		c2dur = request.POST['company2duration']
		c3n = request.POST['company3name']
		c3des = request.POST['company3desig']
		c3s = request.POST['company3salary']
		c3dur = request.POST['company3duration']

		experience.company1name = c1n
		experience.company1desig = c1des
		experience.company1salary = c1s
		experience.company1duration = c1dur
		experience.company2name = c2n
		experience.company2desig = c2des
		experience.company2salary = c2s
		experience.company2duration = c2dur
		experience.company3name = c3n
		experience.company3desig = c3des
		experience.company3salary = c3s
		experience.company3duration = c3dur

		try:
			experience.save()
			error="no"
		except:
			error="yes"
	
	return render(request,'editexperienceadm.html',locals())