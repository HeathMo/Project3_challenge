from flask import Flask, jsonify, render_template, redirect, flash
import datetime

import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    print("responding to home route: ", datetime.datetime.now())

    return render_template("index.html")

@app.route("/raw-web-api")
def scrape():
    dog_db = get_dog_data_from_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(dog_db)

# @app.route("/raw-us-web-api")
# def scrape():
#     dog_db = get_dog_data_from_db()
#     new_name = new_functiondb()
#     print("responding to chart-data route: ", datetime.datetime.now())

#     return jsonify(us_db)

# @app.route("/raw-g-web-api")
# def scrape():
#     dog_db = get_dog_data_from_db()
#     print("responding to chart-data route: ", datetime.datetime.now())

#     return jsonify(g_db)

@app.route("/templates/global_heatmap.html")
def graphs_api():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("global_heatmap.html")


def get_dog_data_from_db():
    table_name = "breeds"
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
 
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/TheWoofTeam")
    # con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/NAMEOFDATABASE")

    cursor = con.cursor()
    cursor.execute(f'SELECT breed_name, animal_type FROM {table_name}')
    #cursor.execute(f'paste query here')

    results = cursor.fetchall()
    results_dict = [{"dogs": results[0], "type": results[1]} for result in results]
    #results_dict = [{"first_item": results[0], "second_item": results[1]} for result in results]

    con.close()

    return results_dict

@app.route("/templates/index.html")
def index():
    print("responding to home route: ", datetime.datetime.now())

    return render_template("index.html")

@app.route("/templates/united_states.html")
def united_states():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("united_states.html")

@app.route("/templates/global.html")
def canada():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("global.html")

@app.route("/templates/misc.html")
def miscellaneous():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("misc.html")

if __name__ == "__main__":
    app.run(debug=True)

print("finished running app.py")