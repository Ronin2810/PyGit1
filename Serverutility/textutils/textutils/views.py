from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    return render(request,'home.html')
    # from django.http import HttpResponse
    # Passing variables in a Websites as a parameter inside render()
    # Mention the variables inside the html file
    # Instead of using httpresponse we can use rendering and create a template of html files where you can do front end coding.(home.html)
def gotoport(request):
    return render(request,'gotoport.html')
def about(request):
    return render(request,'about.html')
def cp1(request):
    return render(request,'cp1.html')
def txtanalyze(request):
    a = request.POST.get('text','default')
    rmvpnc = request.POST.get('rmvpnc','off')
    rmvspchar = request.POST.get('rmvspchar','off')
    rmvextsp = request.POST.get('rmvextsp', 'off')
    if rmvpnc=="on":
        puncs = '''!()-[]{};:'"\,<>./~_'''
        analyzed1 = ""
        for i in a:
            if i not in puncs:
                analyzed1+=i

        lst1 = {'a1':'Task Completed','a2':analyzed1}
        a = analyzed1

    if rmvspchar=="on":
        spchar1 = '''#$%^&*@+*'''
        analyzed1 = ""
        for j in a:
            if j not in spchar1:
                analyzed1+=j
        a = analyzed1
        lst1 = {'a1':'Task Completed','a2':analyzed1}

    if rmvextsp=="on":
        analyzed1 = ""
        for j,i in enumerate(a):
            if a[j]==" " and a[j+1]==" ":
                pass
            else:
                analyzed1+=i
        lst1 = {'a1':'Task Completed','a2':analyzed1}

    if rmvpnc!="on" and rmvspchar!="on" and rmvextsp!="on":
        return HttpResponse("Error")


    return render(request,'analyze.html',lst1)

