from django.shortcuts import render, redirect

# Create your views here.
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from django.contrib.postgres.search import TrigramSimilarity
import itertools
import functools

from .forms import loginForm, RevealedSearchForm, RevealedForm, StoreForm, StoreSearchForm
from .models import Revealed, Total, Store


def logen(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request.POST)
            if form.is_valid():
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('add')
                else:
                    messages.error(request, "تاكد من اسم المستخدم وكلمة السر")
                    return redirect(request.META['HTTP_REFERER'])
        else:
            form = loginForm()
        context = {
            'form': form,
        }
        return render(request, 'login.html', context)
    else:
        return redirect('add')


def logoout(request):
    logout(request)
    return redirect('login')


def relSearch(request):
    if request.user.is_authenticated:
        form2 = ''
        if request.method == 'POST':
            form = RevealedSearchForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                search = Revealed.objects.all()
                paginator = Paginator(search, 50)
                page = request.GET.get('page', 1)
                try:
                    form2 = paginator.page(page)
                except PageNotAnInteger:
                    form2 = paginator.page(1)
                except EmptyPage:
                    form2 = paginator.page(paginator.num_pages)
                if name != '':
                    search = search.annotate(similarity=TrigramSimilarity('paName', name), ).filter(similarity__gt=0.8)
                    paginator = Paginator(search, 50)
                    page = request.GET.get('page', 1)
                    try:
                        form2 = paginator.page(page)
                    except PageNotAnInteger:
                        form2 = paginator.page(1)
                    except EmptyPage:
                        form2 = paginator.page(paginator.num_pages)

        else:
            form = RevealedSearchForm()
        context = {
            'form': form,
            'search': form2,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'relsearch.html', context)

    else:
        return redirect('login')
    

def add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RevealedForm(request.POST)
            if form.is_valid():
                oldTotal = Total.objects.get(id=1).total
                newTotal = float(form.cleaned_data['given']) + float(oldTotal)
                Total.objects.filter(id=1).update(total=newTotal)
                form.save()
                form = RevealedForm()
                return redirect('add')
        else:
            form = RevealedForm()
        context = {
            'form': form,
        }
        return render(request, 'index.html', context)
    else:
        return redirect('login')


def all(request):
    if request.user.is_authenticated:
        if request.method == 'POST' and request.POST.get('form_type') == 'formOne':
            statid = request.POST.get('statid')
            stat = Revealed.objects.get(id=statid).status
            if stat is False:
                Revealed.objects.filter(id=statid).update(status=True)
            elif stat is True:
                Revealed.objects.filter(id=statid).update(status=False)
            return redirect('all')

        elif request.method == 'POST' and request.POST.get('form_type') == 'formThree':
            delstatid = request.POST.get('delstatid')
            delstat = Revealed.objects.get(id=delstatid).delStatus
            statid = Revealed.objects.get(id=delstatid).status
            if delstat is False:
                if statid is True:
                    oldTotal = Total.objects.get(id=1).total
                    newTotal = float(Revealed.objects.get(id=delstatid).reminder) + float(oldTotal)
                    Total.objects.filter(id=1).update(total=newTotal)
                    Revealed.objects.filter(id=delstatid).update(delStatus=True)
                elif statid is False:
                    oldTotal = Total.objects.get(id=1).total
                    newTotal = float(oldTotal) - float(Revealed.objects.get(id=delstatid).given)
                    Total.objects.filter(id=1).update(total=newTotal)
                    Revealed.objects.filter(id=delstatid).delete()
            elif delstat is True:
                Revealed.objects.filter(id=delstatid).update(delStatus=False)
            return redirect('all')

        else:
            form = Revealed.objects.all().order_by('-time')
            paginator = Paginator(form, 50)
            page = request.GET.get('page', 1)
            try:
                form2 = paginator.page(page)
            except PageNotAnInteger:
                form2 = paginator.page(1)
            except EmptyPage:
                form2 = paginator.page(paginator.num_pages)

        context = {
            'form2': form2,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'all.html', context)
    else:
        return redirect('login')


def edit(request, id):
    if request.user.is_authenticated:
        if Revealed.objects.get(id=id).status is True:
            return redirect(request.META['HTTP_REFERER'])
        else:
            if request.method == 'POST':
                form2 = Revealed.objects.get(id=id)
                form3 = RevealedForm(request.POST, instance=form2)
                if form3.is_valid():
                    oldTotal = Total.objects.get(id=1).total
                    oldgiven = Revealed.objects.get(id=id).given
                    outTotal = float(oldTotal) - float(oldgiven)
                    newTotal = float(outTotal) + float(form3.cleaned_data['given'])
                    Total.objects.filter(id=1).update(total=newTotal)
                    form3.save()
                    return redirect('all')
            else:
                form = RevealedForm()
                form2 = Revealed.objects.get(id=id)

            context = {
                'form': form,
                'form2': form2,
            }
            return render(request, 'edit.html', context)
    else:
        return redirect('login')


def dliverd(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            Total.objects.filter(id=1).update(total=0)
            Revealed.objects.filter(delStatus=True).update(ann=True)
            return redirect('del')

        else:
            form = Revealed.objects.all().order_by('-time')
            paginator = Paginator(form, 50)
            page = request.GET.get('page', 1)
            try:
                form2 = paginator.page(page)
            except PageNotAnInteger:
                form2 = paginator.page(1)
            except EmptyPage:
                form2 = paginator.page(paginator.num_pages)
            form3 = Total.objects.get(id=1)

        context = {
            'form2': form2,
            'form3': form3,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'dliverd.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')

def alll(request):
    if request.user.is_superuser:
        form = Revealed.objects.all().order_by('-time')
        paginator = Paginator(form, 50)
        page = request.GET.get('page', 1)
        try:
            form2 = paginator.page(page)
        except PageNotAnInteger:
            form2 = paginator.page(1)
        except EmptyPage:
            form2 = paginator.page(paginator.num_pages)
        form3 = Total.objects.get(id=1)

        context = {
            'form2': form2,
            'form3': form3,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'alln.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')


def storeAdd(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = StoreForm(request.POST)
            if form.is_valid():
                form.save()

            return redirect('storeadd')
        else:
            form = StoreForm()
        context = {
            'form': form,
        }
        return render(request, 'storeadd.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')


def storeShow(request):
    if request.user.is_superuser:
        if request.method == 'POST' and request.POST.get('form_type') == 'formOne':
            storeid = request.POST.get('storeid')
            Store.objects.filter(id=storeid).delete()
            form = Store.objects.all().order_by('-time')
            paginator = Paginator(form, 50)
            page = request.GET.get('page', 1)
            try:
                form2 = paginator.page(page)
            except PageNotAnInteger:
                form2 = paginator.page(1)
            except EmptyPage:
                form2 = paginator.page(paginator.num_pages)

        else:
            form = Store.objects.all().order_by('-time')
            paginator = Paginator(form, 50)
            page = request.GET.get('page', 1)
            try:
                form2 = paginator.page(page)
            except PageNotAnInteger:
                form2 = paginator.page(1)
            except EmptyPage:
                form2 = paginator.page(paginator.num_pages)

        context = {
            'form2': form2,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'storeshow.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')


def storeEdit(request, id):
    if request.user.is_superuser:
        if request.method == 'POST':
            form2 = Store.objects.get(id=id)
            form3 = StoreForm(request.POST, instance=form2)
            if form3.is_valid():
                form3.save()
                return redirect('storeshow')
        else:
            form = StoreForm()
            form2 = Store.objects.get(id=id)

        context = {
            'form': form,
            'form2': form2,
        }
        return render(request, 'storeedit.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')


def storeSearch(request):
    if request.user.is_superuser:
        form2 = ''
        if request.method == 'POST':
            form = StoreSearchForm(request.POST)
            if request.POST['code'] != '':
                search = Store.objects.filter(code=request.POST['code'])
                paginator = Paginator(search, 50)
                page = request.GET.get('page', 1)
                try:
                    form2 = paginator.page(page)
                except PageNotAnInteger:
                    form2 = paginator.page(1)
                except EmptyPage:
                    form2 = paginator.page(paginator.num_pages)
            elif request.POST['name'] != '':
                search = Store.objects.annotate(similarity=TrigramSimilarity('name', request.POST['name']), ).filter(similarity__gt=0.8)
                paginator = Paginator(search, 50)
                page = request.GET.get('page', 1)
                try:
                    form2 = paginator.page(page)
                except PageNotAnInteger:
                    form2 = paginator.page(1)
                except EmptyPage:
                    form2 = paginator.page(paginator.num_pages)
        else:
            form = StoreSearchForm()
        context = {
            'form': form,
            'search': form2,
            'counter': functools.partial(next, itertools.count(1)),
        }
        return render(request, 'storesearch.html', context)
    elif request.user.is_authenticated:
        return redirect('add')
    else:
        return redirect('login')
