import requests
import matplotlib.pyplot as plt
import seaborn as sns

# -------- Configuration --------
API_KEY = '6c4e4e48d4683b9b7aa6d9d90e543d28'  
CITY = 'canada'  
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# -------- Fetch Weather Data --------
response = requests.get(URL)
data = response.json()

# -------- Parse Data --------
dates = []
temperatures = []

for forecast in data['list']:
    dates.append(forecast['dt_txt'])
    temperatures.append(forecast['main']['temp'])

# -------- Visualization --------
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temperatures, marker='o', color='blue')
plt.xticks(rotation=45)
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.grid(True)
plt.show()
