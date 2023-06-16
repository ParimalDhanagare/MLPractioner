from django.shortcuts import render

from joblib import load
model = load('C:/Users/parim/OneDrive/Desktop/RandomForestDeployment/RandomForest.pkl')

def predictor(request):
    if request.method == 'POST':
        pH = request.POST['pH']
        Hardness = request.POST['Hardness']
        Solids = request.POST['Solids']
        Chloramines = request.POST['Chloramines']
        Sulfate = request.POST['Sulfate']
        Conductivity = request.POST['Conductivity']
        Organic_carbon= request.POST['Organic_carbon']
        Trihalomethanes = request.POST['Trihalomethanes']
        Turbidity = request.POST['Turbidity']
        y_pred = model.predict([[pH, Hardness, Solids,Chloramines,Sulfate,Conductivity,Organic_carbon,Trihalomethanes,Turbidity]])
        if y_pred[0] == 0:
            y_pred = 'Not Potable'
        elif y_pred[0] == 1:
            y_pred = 'Potable'
        return render(request, 'main.html', {'result' : y_pred})
    return render(request, 'main.html')