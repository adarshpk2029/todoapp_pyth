from django.shortcuts import render,redirect
from django.views import View
from .forms import TodoForm
from .models import TodoModel
from django.contrib import messages

# Create your views here.
class TodoListView(View):
    def get(self,request):
        todo=TodoModel.objects.all()
        return render(request,"list.html",{"data":todo})
    

class TodoAddView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"add.html",{"form":form})
    def post(self,request):
        form_data=TodoForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Todo Added Successfully")
            return redirect('list')
        else:
            messages.error(request,"Todo Adding Failed")
            return render(request,"add.html",{"form":form_data})
        
class TododeleteView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid)
        todo.delete()
        messages.success(request,"Todo Deleted successfully")
        return redirect("list")
    
class TodoEditView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid)
        form=TodoForm(instance=todo)
        return render(request,"edit.html",{"form":form})
    def post(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=TodoModel.objects.get(id=tid)
        form_data=TodoForm(data=request.POST,files=request.FILES,instance=todo)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Todo Updated")
            return redirect('list')
        else:
            return render(request,'edit.html',{"form":form_data})    
