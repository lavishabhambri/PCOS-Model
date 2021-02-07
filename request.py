import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':22.0, 'armsHair':2.0, 'Overweight':1, 'Periods':0, 'AcneOrskinTag':1,'HairThinning':1})
print(r.json())
