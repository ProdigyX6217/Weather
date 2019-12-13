from flask import Flask, render_template, request
import requests
import pprint
import os

from dotenv import load_dotenv
load_dotenv()

TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)


@app.route('/')
def index():
    """Renders the Index Route."""

    # Render Template
    return render_template('index.html')


@app.route('/weather')
def weather_page():
    """Renders the Weather Route."""

    # Render Template
    return render_template('weather_form.html')


@app.route('/weather_results')
def weather_results_page():
    users_city = request.args.get('city')
    print(users_city)
    
    pp = pprint.PrettyPrinter(indent=4)

    weather_url = "http://api.openweathermap.org/data/2.5/weather?q="+users_city+"&appid=2608f679d4594364525f6c6cc2246c79"

    response = requests.get(weather_url)
    response_json = response.json()
    pp.pprint(response_json)

    main_data = response_json["main"]
    temp_in_kelvin = main_data["temp"]

    print("It is now " + str(temp_in_kelvin) + "degrees kelvin")

    # Render Template
    return render_template('weather_results.html', temp=temp_in_kelvin)
    

if __name__ == "__main__":
    app.run()