import requests
from .models import Passenger
from .forms import PassengerForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PassengerForm

import matplotlib.pyplot as plt
import io
import base64
import plotly
import plotly.graph_objs as go
import plotly.offline as pyo

import json
from django.utils.safestring import mark_safe

def dashboard(request):
    passengers = Passenger.objects.all()

    # 1. Survival Prediction Distribution
    survived_count = passengers.filter(prediction="Survived").count()
    not_survived_count = passengers.filter(prediction="Did Not Survive").count()
    survival_chart = go.Figure(
        data=[
            go.Pie(
                labels=["Survived", "Not Survived"],
                values=[survived_count, not_survived_count],
                hole=0.4,  # Donut chart
                marker=dict(colors=['#28a745', '#dc3545'])
            )
        ],
        layout=go.Layout(title="Survival Prediction Distribution")
    )

    # 2. Age Distribution (Histogram)
    ages = [p.Age for p in passengers if p.Age is not None]
    age_histogram = go.Figure(
        data=[
            go.Histogram(
                x=ages,
                nbinsx=20,
                marker_color='#007bff',
                opacity=0.7
            )
        ],
        layout=go.Layout(
            title="Age Distribution of Passengers",
            xaxis=dict(title="Age"),
            yaxis=dict(title="Count")
        )
    )

    # 3. Fare Comparison by Class (Box Plot)
    pclass_groups = {
        "1st Class": [p.Fare for p in passengers if p.Pclass == 1],
        "2nd Class": [p.Fare for p in passengers if p.Pclass == 2],
        "3rd Class": [p.Fare for p in passengers if p.Pclass == 3]
    }
    box_traces = [
        go.Box(
            y=fare_list,
            name=class_name,
            marker=dict(color=color)
        )
        for (class_name, fare_list), color in zip(pclass_groups.items(), ['#ff7f0e', '#2ca02c', '#1f77b4'])
    ]
    fare_boxplot = go.Figure(
        data=box_traces,
        layout=go.Layout(
            title="Fare Comparison by Passenger Class",
            yaxis=dict(title="Fare"),
            xaxis=dict(title="Passenger Class")
        )
    )

    # Convert graphs to JSON
    survival_chart_json = json.dumps(survival_chart, cls=plotly.utils.PlotlyJSONEncoder)
    age_histogram_json = json.dumps(age_histogram, cls=plotly.utils.PlotlyJSONEncoder)
    fare_boxplot_json = json.dumps(fare_boxplot, cls=plotly.utils.PlotlyJSONEncoder)

    return render(request, 'passengers/dashboard.html', {
        'survival_chart': mark_safe(survival_chart_json),
        'age_chart': mark_safe(age_histogram_json),
        'fare_chart': mark_safe(fare_boxplot_json)
    })

def passenger_list(request):
    passengers = Passenger.objects.all()

    # Preprocess gender and embarked data
    for passenger in passengers:
        passenger.gender = "Male" if passenger.Sex_male else "Female"
        passenger.embarked_q = "Yes" if passenger.Embarked_Q else "No"
        passenger.embarked_s = "Yes" if passenger.Embarked_S else "No"

    return render(request, 'passengers/passenger_list.html', {'passengers': passengers})

from django.shortcuts import render, redirect
from .forms import PassengerForm

def create_passenger(request):
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
def passenger_detail(request, pk):
    passenger = get_object_or_404(Passenger, id=pk)
    
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
def passenger_delete(request, pk):
    passenger = get_object_or_404(Passenger, id=pk)
    if request.method == "POST":
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'passengers/passenger_confirm_delete.html', {'passenger': passenger})