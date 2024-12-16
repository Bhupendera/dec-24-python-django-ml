import requests
from django.shortcuts import render, redirect
from .models import Passenger
from .forms import PassengerForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Passenger
from .forms import PassengerForm


def passenger_list(request):
    passengers = Passenger.objects.all()
    # Add computed fields for display
    for passenger in passengers:
        passenger.gender = "Male" if passenger.Sex_male else "Female"
        passenger.embarked_q_status = "Yes" if passenger.Embarked_Q else "No"
        passenger.embarked_s_status = "Yes" if passenger.Embarked_S else "No"

    return render(request, 'passengers/passenger_list.html', {'passengers': passengers})

def passenger_create(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save(commit=False)
            # Call Flask API
            api_url = "http://127.0.0.1:5000/predict"
            response = requests.post(api_url, json=form.cleaned_data)
            if response.status_code == 200:
                passenger.prediction = response.json()['prediction']
                passenger.save()
                return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'passengers/passenger_form.html', {'form': form})

# New: View details of a passenger
def passenger_detail(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    
    # Add derived fields for display
    passenger_data = {
        "id": passenger.id,
        "Pclass": passenger.Pclass,
        "Age": passenger.Age,
        "SibSp": passenger.SibSp,
        "Parch": passenger.Parch,
        "Fare": passenger.Fare,
        "Sex": "Male" if passenger.Sex_male else "Female",
        "Embarked_Q": "Yes" if passenger.Embarked_Q else "No",
        "Embarked_S": "Yes" if passenger.Embarked_S else "No",
        "prediction": passenger.prediction,
    }
    
    return render(request, 'passengers/passenger_detail.html', {'passenger': passenger_data})

# New: Delete a passenger
def passenger_delete(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    if request.method == "POST":
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'passengers/passenger_confirm_delete.html', {'passenger': passenger})