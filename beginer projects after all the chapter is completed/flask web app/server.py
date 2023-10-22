from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import pandas
from addinfo import CafeForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd5a9532cd23a20dc7713665f'
bootstrap = Bootstrap5(app)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/cafe")
def cafe():
    global cafe_lists
    data = pandas.read_csv("cafe-data.csv")
    data_dict = data.to_dict()
    cafe_lists = []
    for i in data_dict["Cafe Name"]:
        cafe_lists.append({"Cafe Name": data_dict["Cafe Name"][i],
        "Location": data_dict["Location"][i],
        "Open": data_dict["Open"][i],
        "Close": data_dict["Close"][i],
        "Coffee": data_dict["Coffee"][i],
        "Wifi": data_dict["Wifi"][i],
        "Power": data_dict["Power"][i],
        })
    return render_template("cafe.html", lists=cafe_lists)

# @app.route("/cafe")
# def delete():
    
    

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafe'))
    return render_template("add.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)