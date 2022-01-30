from flask import Flask, url_for, redirect, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":

        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={ENTER_API_KEY}&units=metric'
        city = request.form.get("city")

        r = requests.get(url.format(city)).json()
        # print(r)

        weather = {
            'city': city,
            'cur_temp':  r['main']['temp'],
            'feels_like': r['main']['feels_like'],
            'min_temp': r['main']['temp_min'],
            'max_temp': r['main']['temp_max'],

            'description':  r['weather'][0]['description'],
            'icon':  r['weather'][0]['icon'],

        }

        return render_template("result.html", weather=weather)

    elif request.method == "GET":

        return render_template("search.html")


if __name__ == "__main__":
    app.jinja_env.auto_reload = True

    app.config["TEMPLATES_AUTO_RELOAD"] = True

    app.run(debug=True)
