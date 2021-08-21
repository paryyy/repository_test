from django.shortcuts import render
from .models import ExplainModel
from .forms import GiveNumber_form
from django.http import HttpResponseRedirect

# Create your views here.
#create app sub
def sayhello(request):
    if request.method == "POST":
        form = GiveNumber_form(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            resultt = num1 * num2
            #return HttpResponseRedirect('/Home/')
            return render(request, 'result.html', {'resultt': resultt})
            return HttpResponseRedirect('/Home/')
        #for save gitttt

    else:
        form = GiveNumber_form()

    return render(request, 'hello.html', {'form': form})
            #return render(request, 'explain.html', ans_dic)
        #return render(request, 'hello.html')


def explain(request):
    if request.method == "POST":
        data = request.POST
        a = data['multi']
        b = data['divi']
        ans = data['multi'] + data['divi']
        ans_dic = {'ans': ans}
        return render(request, 'explain.html', ans_dic)
    explains = ExplainModel.objects.all()
    context = {'explains': explains}
    return render(request, 'explain.html', context)

def detail(request, explainid):
    det_detail = ExplainModel.objects.get(id=explainid)
    context = {'det_detail': det_detail}
    return render(request, 'detail.html', context)



def Multiplication(request):
    return render(request, 'Multiplication'),




def division(request):
    return render(request, 'division.html'),


def GiveNumber_view(request):
    form = GiveNumber_form()
    if request.method == "POST":
        form = GiveNumber_form(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 * num2
            context = {'res': res, 'form':form}
            return render(request, 'hello.html', context)
    else:
        form = GiveNumber_form()



