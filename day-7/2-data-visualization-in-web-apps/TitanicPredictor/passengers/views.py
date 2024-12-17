import requests
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64
from django.shortcuts import render, redirect, get_object_or_404
from .models import Passenger
from .forms import PassengerForm

# Helper function to generate image and return its URL
def get_graph():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')  # Save the plot to the buffer
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')  # Encode as base64
    buffer.close()
    print(f"Graph data: {graph[:100]}...")  # Print the first 100 characters of the graph data for debugging
    return f"data:image/png;base64,{graph}"  # Return as a base64 URL

# Passenger List View with Visualization
def passenger_list(request):
    passengers = Passenger.objects.all()

    # Add computed fields for display
    for passenger in passengers:
        passenger.gender = "Male" if passenger.Sex_male else "Female"
        passenger.embarked_q_status = "Yes" if passenger.Embarked_Q else "No"
        passenger.embarked_s_status = "Yes" if passenger.Embarked_S else "No"

    # Visualization: Survival Distribution
    survived = passengers.filter(prediction="Survived").count()
    not_survived = passengers.filter(prediction="Did Not Survive").count()

    # Debugging: Print the counts to verify data
    print(f"Survived count: {survived}, Not survived count: {not_survived}")

    plt.clf()  # Clear the current figure
    plt.figure(figsize=(6, 4))
    plt.bar(["Survived", "Did Not Survive"], [survived, not_survived], color=["green", "red"])
    plt.title("Survival Prediction Distribution")
    plt.xlabel("Prediction")
    plt.ylabel("Count")
    plt.tight_layout()
    graph = get_graph()

    print(f"Graph URL: {graph[:100]}...")  # Print the first 100 characters of the graph URL for debugging

    return render(
        request,
        'passengers/passenger_list.html',
        {'passengers': passengers, 'graph': graph}
    )


# Passenger Create View
def passenger_create(request):
    if request.method == "POST":
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save(commit=False)
            # Call Flask API
            api_url = "http://127.0.0.1:5000/predict"
            response = requests.post(api_url, json=form.cleaned_data)
            print("response.json: ", response.json())
            if response.status_code == 200:
                passenger.prediction = response.json()['prediction']
                passenger.save()
                return redirect('passenger_list')
    else:
        form = PassengerForm()
    return render(request, 'passengers/passenger_form.html', {'form': form})

import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import io, base64
from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from .models import Passenger

# Helper function to convert Matplotlib plots to base64
def get_graph():
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png).decode('utf-8')
    buffer.close()
    return f"data:image/png;base64,{graph}"

# Passenger Detail View with Record-Specific Visualization
def passenger_detail(request, id):
    passenger = get_object_or_404(Passenger, id=id)

    # Derived fields for display
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
        "prediction": "Survived" if passenger.prediction == 1 else "Did Not Survive",
    }

    # Fare Comparison: Compare this passenger's fare with average fare by class
    avg_fares = [
        Passenger.objects.filter(Pclass=1).aggregate(avg_fare=Avg('Fare'))['avg_fare'] or 0,
        Passenger.objects.filter(Pclass=2).aggregate(avg_fare=Avg('Fare'))['avg_fare'] or 0,
        Passenger.objects.filter(Pclass=3).aggregate(avg_fare=Avg('Fare'))['avg_fare'] or 0,
    ]
    passenger_fare = passenger.Fare

    print("avg_fares: ", avg_fares)
    print("passenger_fare: ", passenger_fare)

    plt.clf()  # Clear the current figure
    plt.figure(figsize=(6, 4))
    sns.barplot(x=["1st Class", "2nd Class", "3rd Class"], y=avg_fares, palette="muted")
    plt.axhline(y=passenger_fare, color='red', linestyle='--', label="Passenger Fare")
    plt.title("Passenger Fare vs Average Fare by Class")
    plt.ylabel("Fare")
    plt.legend()
    plt.tight_layout()
    fare_graph = get_graph()

    # Debugging statement to verify the graph variable
    print(f"Fare Graph variable: {fare_graph[:100]}...")

    # Pass context to template
    return render(
        request,
        'passengers/passenger_detail.html',
        {
            'passenger': passenger_data,
            'fare_graph': fare_graph,
        }
    )



# Passenger Delete View
def passenger_delete(request, id):
    passenger = get_object_or_404(Passenger, id=id)
    if request.method == "POST":
        passenger.delete()
        return redirect('passenger_list')
    return render(request, 'passengers/passenger_confirm_delete.html', {'passenger': passenger})
