from django.shortcuts import render,HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm,AssetlayerForm,UserIntegrationLayerForm,UserCommunicationLayerForm,UserInformationLayerForm,UserFunctionalLayerForm,UserBusinessLayerForm
from .models import UserRegistrationModel,AssetLayerModel,UserIntegrationLayerModel,UserCommunicationLayerModel,UserInformationLayerModel,UserFunctionalLayerModel,UserBusinessLayerModel
from .algo.MyPCAAlgorithm import StartPCA
# Create your views here.
def UserRegisterActions(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'You have been successfully registered')
            form = UserRegistrationForm()
            return render(request, 'UserRegistrations.html', {'form': form})
        else:
            messages.success(request, 'Email or Mobile Already Existed')
            print("Invalid form")
    else:
        form = UserRegistrationForm()
    return render(request, 'UserRegistrations.html', {'form': form})
def UserLoginCheck(request):
    if request.method == "POST":
        loginid = request.POST.get('loginname')
        pswd = request.POST.get('pswd')
        print("Login ID = ", loginid, ' Password = ', pswd)
        try:
            check = UserRegistrationModel.objects.get(loginid=loginid, password=pswd)
            status = check.status
            print('Status is = ', status)
            if status == "activated":
                request.session['id'] = check.id
                request.session['loggeduser'] = check.name
                request.session['loginid'] = loginid
                request.session['email'] = check.email
                print("User id At", check.id, status)
                return render(request, 'users/UserHome.html', {})
            else:
                messages.success(request, 'Your Account Not at activated')
                return render(request, 'UserLogin.html')
        except Exception as e:
            print('Exception is ', str(e))
            pass
        messages.success(request, 'Invalid Login id and password')
    return render(request, 'UserLogin.html', {})
def UserHome(request):
    return render(request, 'users/UserHome.html', {})

def UserAssetLayer(request):
    if request.method == 'POST':
        form = AssetlayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Asset layer Information Added')
            form = AssetlayerForm()
            data = AssetLayerModel.objects.all()
            return render(request, 'users/UserAssetsForms.html', {'form': form,'data':data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")
    else:
        form = AssetlayerForm()
        data = AssetLayerModel.objects.all()
    return render(request, 'users/UserAssetsForms.html', {'form': form,'data':data})


def UserIntegrationLayer(request):
    if request.method == 'POST':
        form = UserIntegrationLayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Integration layer Information Added')
            form = UserIntegrationLayerForm()
            data = UserIntegrationLayerModel.objects.all()
            return render(request, 'users/UserIntegrationForms.html', {'form': form,'data':data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")
    else:
        form = UserIntegrationLayerForm()
    data = UserIntegrationLayerModel.objects.all()
    return render(request, 'users/UserIntegrationForms.html', {'form': form,'data':data})



def UserCommunicationLayer(request):
    if request.method == 'POST':
        form = UserCommunicationLayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Communication layer Information Added')
            form = UserCommunicationLayerForm()
            data = UserCommunicationLayerModel.objects.all()
            return render(request, 'users/UserCommunicationForms.html', {'form': form, 'data': data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")
    else:
        form = UserCommunicationLayerForm()
    data = UserCommunicationLayerModel.objects.all()
    return render(request, 'users/UserCommunicationForms.html', {'form': form, 'data': data})


def UserInformationLayer(request):
    if request.method == 'POST':
        form = UserInformationLayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Infomation layer Information Added')
            form = UserInformationLayerForm()
            data = UserInformationLayerModel.objects.all()
            return render(request, 'users/UserInformationForms.html', {'form': form, 'data': data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")
            data = UserInformationLayerModel.objects.all()
            return render(request, 'users/UserInformationForms.html', {'form': form, 'data': data})
    else:
        form = UserInformationLayerForm()
    data = UserInformationLayerModel.objects.all()
    return render(request, 'users/UserInformationForms.html', {'form': form, 'data': data})


def UserFunctionalLayer(request):
    if request.method == 'POST':
        form = UserFunctionalLayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Functional layer Information Added')
            form = UserFunctionalLayerForm()
            data = UserFunctionalLayerModel.objects.all()
            return render(request, 'users/UserFunctionalForms.html', {'form': form, 'data': data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")

    else:
        form = UserFunctionalLayerForm()
    data = UserFunctionalLayerModel.objects.all()
    return render(request, 'users/UserFunctionalForms.html', {'form': form, 'data': data})


def UserBusinesslayer(request):
    if request.method == 'POST':
        form = UserBusinessLayerForm(request.POST)
        if form.is_valid():
            print('Data is Valid')
            form.save()
            messages.success(request, 'Functional layer Information Added')
            form = UserBusinessLayerForm()
            data = UserBusinessLayerModel.objects.all()
            return render(request, 'users/UserBusinessForms.html', {'form': form, 'data': data})
        else:
            messages.success(request, 'Database error occured')
            print("Invalid form")

    else:
        form = UserBusinessLayerForm()
    data = UserBusinessLayerModel.objects.all()
    return render(request, 'users/UserBusinessForms.html', {'form': form, 'data': data})

def UserPcaAnalysis(request):
    obj = StartPCA()
    df = obj.preProcessPCA()
    df = df.fillna(df.mean())
    df = df.fillna(0)
    data = df.to_html()
    return render(request,"users/PCAResults.html",{'data':data})
def PCAScores(request):
    obj = StartPCA()
    variance, singular = obj.calculatePCAScores()
    return render(request, "users/PCAscores.html", {'variance': variance,'singular':singular})