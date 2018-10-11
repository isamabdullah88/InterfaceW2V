from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
from .models import *

# Create your views here.
def index(request):
	return render(request, 'Interface/base.html')

class ImageView(TemplateView):
	in_template = 'Interface/input.html'
	out_template = 'Interface/output.html'
	form = []

	def get(self, request):
		self.form = WordForm(initial={'words': Word.objects.first()})
		return render(request, self.in_template, {'form': self.form})

	def post(self, request):
		print('post recieved!')
		form_post = WordForm(request.POST)
		img_set = []
		if form_post.is_valid():
			print('yup!')
			print()
			form_data = form_post.save(commit=False)
			# form_data.save()
			file_name = form_data.words

			with open('./Interface/static/Results/'+file_name+'.txt', 'r') as f:
				for line in f:
					l = line.split(',')[0]
					img_set += [l]

		context = {'img_set': img_set, 'form': self.form, 'word': file_name}
		return render(request, self.out_template, context)
