from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
import speech_recognition as sr
# Create your views here.
import datetime
from django.core.files.storage import FileSystemStorage
class IndexView(View):

	def get(self, request):
		context = {}
		return render(request, 'index.html', context)
	
	def post(self, request):
		context = {}
		return render(request, 'index.html', context)

class UploadView(View):

	def get(self, request):
		context = {}
		return HttpResponse("Working")
	
	def post(self, request):
		myfile = request.FILES['audio_data']
		fs = FileSystemStorage()
		fname = str(datetime.datetime.now()).replace(":", "")
		filename = fs.save("audiofile/"+fname.replace(".", "")+".wav", myfile)
		r = sr.Recognizer()
		hellow=sr.AudioFile("audiofile/"+fname.replace(".", "")+".wav")
		with hellow as source:
			audio = r.record(source)
		try:
			s = r.recognize_google(audio)
			print("Text: "+s)
		except Exception as e:
			print("Exception: "+str(e))
		return HttpResponse("OK")
