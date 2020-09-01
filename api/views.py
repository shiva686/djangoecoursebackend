from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from ecourse_admin.models import adminlogin as admin;
from ecourse_admin.models import websitedetails as websitedetail;
from ecourse_admin.models import addcourse as addcour;
from ecourse_admin.models import addcourse as readcour;
from ecourse_admin.models import addcourse as limitcourse;
from ecourse_admin.models import userlogin as user;
from ecourse_admin.models import userlogin as readuser;
from ecourse_admin.models import myvid as mycour;
from ecourse_admin.models import userprofilepic as userpic;
from ecourse_admin.models import websitedetails as website;
from rest_framework.response import Response;
from rest_framework.views import APIView;
from rest_framework import status
from rest_framework import status as stus
from ecourses.settings import SECRET_KEY 
from django.utils.deprecation import MiddlewareMixin
import jwt
import datetime
import base64
import uuid

refreshtoken = "refreshtoken"
class IndexView(APIView):
	def post(self, request):
		data = request.data,
		return Response(data)

class adminlogin(APIView):
	def post(self, request):
		email = request.data['email']
		password = request.data['password'] 
		if password != "":
			try:
				data = admin.objects.get(password=password , email=email)
				login= jwt.encode({'login':True ,'exp':  datetime.datetime.utcnow() + datetime.timedelta(seconds=86400)}, SECRET_KEY, algorithm='HS256')
				request.session['login']=True
				statu=status.HTTP_200_OK
			except:
				login = 'error'
				statu=status.HTTP_404_NOT_FOUND
		else:
			login = 'not found'
			statu=status.HTTP_404_NOT_FOUND
		return Response(login,status=statu)

class Adminchangepassword(APIView):
	def post(self,request):
		password = request.data['password']
		newpassword = request.data['newpassword']
		try:
			data=admin.objects.get(password=password)
			data.password = newpassword
			data.save()
			res="ok"
			statu=status.HTTP_200_OK
		except:
			 res="err"
			 statu=status.HTTP_404_NOT_FOUND
		return Response(res,status=statu)


class Adminwebsitedetails(APIView):
	def post(self,request):
		websitename = request.data['websitename']
		aboutwebsite = request.data['aboutwebsite']
		try:
			data=websitedetail.objects.get(websitename=websitename)
			data.websitename=websitename
			data.aboutwebsite=aboutwebsite
			data.save()
			res="ok"
			statu=status.HTTP_200_OK
		except:
			 res="err"
			 statu=status.HTTP_404_NOT_FOUND
		return Response(res,status=statu)


class Adminaddcourses(APIView):
	def post(self,request):
		title = request.data['title']
		shortdescription = request.data['shortdescription']
		description = request.data['description']
		status="publish"
		image = request.data['thumbail']
		try:
			data=readcour.objects.get(title=title)
			return Response('exits',status=stus.HTTP_404_NOT_FOUND)
		except:
			addcourse = addcour(title=title,shortdescription=shortdescription,description=description,status=status,image=image)
			addcourse.save()
			return Response(addcourse.id,status=stus.HTTP_200_OK)

class delcourse(APIView):
	def post(self,request):
		id=request
		j=0
		data=id.data['data']
		length =len(data)
		try:
			while j<length:
				ids = data[str(j)]['id']
				data=readcour.objects.get(id=ids)
				data.delete()
				j+=1
			return Response('deleted',status=stus.HTTP_200_OK)
		except:
			return Response('err',status=stus.HTTP_404_NOT_FOUND)
 

class courses(APIView):
	def get(seft,request):
		try:
			data=readcour.objects.all()
			res={}
			j=0
			for i in data:
				res[j]={
				"title":i.title,
				"shortdescription":i.shortdescription,
				"description":i.description,
				"id":i.id,
				"status":i.status,
				"image":i.image
				}
				j +=1
			if res != {}:
				return Response(res , status=status.HTTP_200_OK)
			else:
				return Response({'err':'err'},status=status.HTTP_204_NO_CONTENT)
		except:
			return Response({'err':'err'} , status.HTTP_204_NO_CONTENT)



class limitcourses(APIView):
	def get(seft,request):
		try:
			data=limitcourse.objects.all().order_by('-id')[:8]
			res={}
			j=0
			for i in data:
				res[j]={
				"title":i.title,
				"shortdescription":i.shortdescription,
				"description":i.description,
				"id":i.id,
				"status":i.status,
				"image":i.image
				}
				j +=1
			if res != {}:
				return Response(res , status=status.HTTP_200_OK)
			else:
				return Response({'err':'err'},status=status.HTTP_404_NOT_FOUND)
		except:
			return Response({'err':'err'} , status.HTTP_404_NOT_FOUND)



class logout(APIView):
	def get(self, request):
		del request.session['login']
		return Response('ok',status=status.HTTP_200_OK)


class auth(APIView):
	def post(self, request):
		print(request.data)
		try:
			login = request.session['login']
			if(login == True):
				return Response('ok',status=status.HTTP_200_OK)
			else:
				return Response('err',status=status.HTTP_204_NO_CONTENT)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)

class userSignup(APIView):
	def post(self, request):
		email = request.data['email']
		password=request.data['password']
		name=request.data['name']
		try:
			checkuser = user.objects.get(email=email)
			print(request.data)
			return Response('exits',status=status.HTTP_404_NOT_FOUND)
		except:
			print(request.data)
			userloindata = user(email=email,password=password,name=name)
			userloindata.save()
			login= jwt.encode({'id':str(userloindata.studentid) ,'exp':  datetime.datetime.utcnow() + datetime.timedelta(seconds=6048)}, SECRET_KEY, algorithm='HS256')
			return Response(login ,status=status.HTTP_200_OK)
		
class userSignin(APIView):
	def post(self, request):
		email = str(request.data['email'])
		password=str(request.data['password'])
		try:
			print(request.data)
			checkuser = user.objects.get(email=email,password=password)
			login=jwt.encode({'id':str(checkuser.studentid) ,'exp':  datetime.datetime.utcnow() + datetime.timedelta(seconds=6048)}, SECRET_KEY, algorithm='HS256')
			return Response(login,status=status.HTTP_200_OK)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)

class userAuth(APIView):
	def post(self, request):
		try:
			token = request.data['token']
			login=jwt.decode(token, SECRET_KEY, algorithm='HS256')
			checkuser = user.objects.get(studentid=login['id'])
			return Response('ok',status=status.HTTP_200_OK)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)

class mycourses(APIView):
	def post(self, request):
		try:
			token = request.data['token']
			login=jwt.decode(token, SECRET_KEY, algorithm='HS256')
			course_id = mycour.objects.filter(studentid=login['id'])
			res={}
			j=0
			for i in course_id:
				res[j]={
				"course_id":i.course_id
				}
				j +=1
			reslen = len(res)
			data=readcour.objects.all();
			for k , v in res.items():
				for i in data:
					if v['course_id']==str(i.id):
						res[k]={
						"title":i.title,
						"shortdescription":i.shortdescription,
						"description":i.description,
						"course_id":i.id,
						"status":i.status,
						"image":i.image
						}
			if res !={}:
				return Response(res , status=status.HTTP_200_OK)
			else:
				return Response('err',status=status.HTTP_204_NO_CONTENT)
		except:
		    return Response('err',status=status.HTTP_204_NO_CONTENT)
 

class selectedcourse(APIView):
	def post(self,request):
		print(request.data)
		token = request.data['token']
		course_id = request.data['courseid']
		studentid=jwt.decode(token, SECRET_KEY, algorithm='HS256')
		try:
			check = mycour.objects.get(studentid=studentid['id'],course_id=course_id)
			return Response('owned',status=status.HTTP_302_FOUND)
		except:
			print(request.data)
			insert = mycour(studentid=studentid['id'],course_id=course_id)
			insert.save()
			return Response('ok',status=status.HTTP_200_OK)


class userprofile(APIView):
	def post(self, request):
		try:
			data = request.data['token']
			token = jwt.decode(data , SECRET_KEY , algorithm='HS256')
			stu_id = token['id']
			use =user.objects.all()
			for i in use:
				if stu_id == str(i.studentid):
					res={
					"stu_id":i.studentid,
					"name":i.name,
					"email":i.email
					}
			return Response(res , status=status.HTTP_200_OK)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)


		
class userchangepassword(APIView):
	def post(self, request):
		data = request.data['token']
		password = request.data['password']
		token = jwt.decode(data , SECRET_KEY , algorithm='HS256')
		stu_id = token['id']
		use = user.objects.get(studentid=stu_id)
		try:
			use.password = password
			use.save()
			return Response('ok',status=status.HTTP_200_OK)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)

		
class profilepic(APIView):
	def post(self, request):
		data = request.data['token']
		pic = request.data['pic']
		token = jwt.decode(data , SECRET_KEY , algorithm='HS256')
		stu_id = token['id']
		useprofilepic = userpic.objects.get(studentid=stu_id)
		try:
			useprofilepic.profile_pic=pic
			useprofilepic.save()
		except:
			useprofilepic(studentid=stu_id,profile_pic=pic)
			useprofilepic.save()
		return Response('ok' , status=status.HTTP_200_OK)

	
	
class websitedetails(APIView):
    def get(self, request):
    	web = website.objects.all()
    	data ={
    	 "websitename":web[0].websitename,
    	 "aboutwebsite":web[0].aboutwebsite
    	}
    	return Response(data , status=status.HTTP_200_OK)


class admin_students_list(APIView):
	def get(self, request):
		try:
			login = request.session['login']
			j=0
			res={}
			if(login == True):
				stu_details = user.objects.all()
				for stu in stu_details:
					res[j]={
					"name":stu.name,
					"email":stu.email,
					"id":stu.studentid
					}
					j+=1
			return Response(res , status=status.HTTP_200_OK)
		except:
			return Response('err',status=status.HTTP_404_NOT_FOUND)
		

class deleteuser(APIView):
	def post(self, request):
		email=request.data['email']
		login = request.session['login']
		if login == True:
			stu_delete = user.objects.get(email=email)
			stu_delete.delete()
			return Response('ok' , status=status.HTTP_200_OK)
		else:
			return Response('err',status=status.HTTP_404_NOT_FOUND)
		
		
class addwebsitedetails(APIView):
	def post(self, request):
		websitename = request.data['websitename']
		aboutwebsite = request.data['aboutwebsite']
		login = request.session['login']
		if login == True:
			try:
				web = website.objects.get(websitename='E-Courses')
				web.websitename = websitename
				web.aboutwebsite = aboutwebsite
				web.save()
			except:
				web = website(websitename=websitename,aboutwebsite=aboutwebsite)
				web.save()
			return Response('ok',status=status.HTTP_200_OK)
		else:
			return Response('err',status=status.HTTP_404_NOT_FOUND)