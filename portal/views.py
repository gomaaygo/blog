from django.shortcuts import render
from .models import Area, Noticia
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AreaForm, NoticiaForm

def index(request):
	areas = Area.objects.all()
	return render(request, 'portal/index.html', {'areas': areas})

def lista_area(request):
	areas = Area.objects.all()
	return render(request, 'portal/area.html', {'areas': areas})

def detalhes_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	return render(request, 'portal/area_detail.html', {'area': area})

def adicionar_area(request):
	if request.method == "POST":
		form = AreaForm(request.POST)

		if form.is_valid():
			area = form.save(commit=False)
			area.author = request.user
			area.save()

			return redirect('detalhes_area', pk=area.pk)
	else:
		form = AreaForm()	
	return render(request, 'portal/area_edit.html', {'form' : form})

def alterar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)

	if request.method == "POST":
		form = AreaForm(request.POST, instance=area)

		if form.is_valid():
			area = form.save(commit=False)
			area.save()

			return redirect('detalhes_area', pk=area.pk)
	else:
		form = AreaForm(instance=area)	
	return render(request, 'portal/area_edit.html', {'form' : form})

def excluir_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.delete()

	return redirect('lista_area')

def ativar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.ativar()

	return redirect('lista_area')

def desativar_area(request, pk):
	area = get_object_or_404(Area, pk=pk)
	area.desativar()

	return redirect('lista_area')



#-------------------------------------------------------------------------

#VIEW NOTÍCIA

def lista_noticia(request):
	noticias = Noticia.objects.all()
	return render(request, 'portal/noticia.html', {'noticias': noticias})

def detalhes_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	return render(request, 'portal/noticia_detail.html', {'noticia': noticia})

def adicionar_noticia(request):
	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES)

		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.autor = request.user
			noticia.save()

			return redirect('detalhes_noticia', pk=noticia.pk)
	else:
		form = NoticiaForm()	
	return render(request, 'portal/noticia_edit.html', {'form' : form})


def alterar_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)

	if request.method == "POST":
		form = NoticiaForm(request.POST, request.FILES, instance=noticia)

		if form.is_valid():
			noticia = form.save(commit=False)
			noticia.save()

			return redirect('detalhes_noticia', pk=noticia.pk)
	else:
		form = NoticiaForm(instance=noticia)	
	return render(request, 'portal/noticia_edit.html', {'form' : form})

def excluir_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.delete()

	return redirect('lista_noticia')

def publicar_noticia(request, pk):
	noticia = get_object_or_404(Noticia, pk=pk)
	noticia.publicar()

	return redirect('lista_noticia')



