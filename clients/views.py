from django.shortcuts import render, redirect  
from clients.forms import ClientForm  
from clients.models import Client  
from django.db.models import Q

# Create your views here.  
def clients(request):
    
    orderby = request.GET.get("orderby")
    direction = request.GET.get("direction")
    direction_dict = {"asc":"","desc":"-"}
    direction_reverse = {"asc":"desc","desc":"asc"}

    orderbyclause = "cusername"
   
    try:
        if request.GET.get("orderby") is not None and request.GET.get("direction") is not None:
            if request.GET.get("direction") is not None:
                orderbyclause = direction_dict[direction]+request.GET.get("orderby")
                direction = direction_reverse[direction]
        else:
            orderby = "cusername"
            direction = "desc"
    except:
        pass
     

    if request.GET.get("search") is not None:
        search = request.GET.get("search")
        clients = Client.objects.filter(Q(cusername__icontains=search)|
                Q(cemail__icontains=search)|Q(cphone__icontains=search)|Q(csuburb__icontains=search)).order_by(orderbyclause)
    else:
        clients = Client.objects.all().order_by(orderbyclause)
    return render(request,"show.html",{'clients':clients,"direction":direction,"orderby":orderby})

def add(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save(commit=True)  
                return redirect('/clients')
            except:
                print(form.errors)
                pass
        else:
        	print(form.errors)
    else:  
        form = ClientForm()  
    return render(request,'index.html',{'form':form}) 
    

def edit(request, id):  
    client = Client.objects.get(id=id)  
    form = ClientForm(instance = client)  
    return render(request,'edit.html', {'form':form,'clientid':client.id})  

def update(request, id):  
    client = Client.objects.get(id=id)  
    form = ClientForm(request.POST, instance = client)  
    if form.is_valid():  
        form.save(commit=True) 
        return redirect("/clients")  
    return render(request,'edit.html', {'form':form,'clientid':client.id})
