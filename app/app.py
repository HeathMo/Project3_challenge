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
    all_db = get_all_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(all_db)

@app.route("/raw-us-web-api")
def us_scrape():
    us_db = get_us_data_from_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(us_db)

@app.route("/raw-g-web-api")
def other_scrape():
    all_countries_db = get_all_country_data_from_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(all_countries_db)

########################################################
# These 2 API routes made up to test queries  
@app.route("/raw-d-web-api")
def decade_scrape():
    decades_db = get_decade_data_from_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(decades_db)

@app.route("/raw-s-web-api")
def shapes_scrape():
    shapes_db = get_shapes_data_from_db()
    print("responding to chart-data route: ", datetime.datetime.now())

    return jsonify(shapes_db)   
########################################################   




def get_all_db():
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
 
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/UFO_Project_db")
    
    # All countries and the number of sightings for each
    cursor = con.cursor()
    cursor.execute("""SELECT DISTINCT(UPPER(country)), COUNT(country) FROM ufo_sightings GROUP BY country ORDER BY COUNT(country) DESC""")
    
    results = cursor.fetchall()
    results_dict1 = [{"country": result[0], "country_sightings": result[1]} for result in results]
   
    con.close()

    return results_dict1

def get_us_data_from_db():
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/UFO_Project_db")
   
    # Get the top 20 US states with the most sightings
    cursor = con.cursor()
    cursor.execute("""SELECT UPPER(state), COUNT(state) FROM ufo_sightings WHERE country = 'us' GROUP BY state ORDER BY COUNT(state) DESC FETCH FIRST 20 ROWS ONLY""")
    
    results = cursor.fetchall()
    results_dict2 = [{"US_states": result[0], "count_sightings": result[1]} for result in results]
   
    con.close()

    return results_dict2

def get_all_country_data_from_db():
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
    
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/UFO_Project_db")
   
    # Get the top 20 states not in the US with the most sightings
    cursor = con.cursor()
    cursor.execute("""SELECT UPPER(state), COUNT(state) FROM ufo_sightings WHERE country != 'us' GROUP BY state ORDER BY COUNT(state) DESC FETCH FIRST 20 ROWS ONLY""")
    
    results = cursor.fetchall()
    results_dict3 = [{"Non_US_states": result[0], "count_sightings": result[1]} for result in results]
   
    con.close()

    return results_dict3

    ##########################################################################

    #   Where do these next 2 additional queries go?
    # Query 4

def get_decade_data_from_db():
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
    
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/UFO_Project_db")
   
    # Uses 0-to-9 decade the most widely used method for denominating decades. 
    # This query goes from 1940s to roughly mid-2014 (the latest data).

    cursor = con.cursor()
    cursor.execute("""SELECT 'Decade: 1940 - 1949' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1940' AND '1949' UNION ALL SELECT 'Decade: 1950 - 1959' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1950' AND '1959' UNION ALL SELECT 'Decade: 1960 - 1969' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1960' AND '1969' UNION ALL SELECT 'Decade: 1970 - 1979' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1970' AND '1979' UNION ALL SELECT 'Decade: 1980 - 1989' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1980' AND '1989' UNION ALL SELECT 'Decade: 1990 - 1999' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '1990' AND '1999' UNION ALL SELECT 'Decade: 2000 - 2014' AS "Decade", COUNT(*) AS "# of Sightings" FROM ufo_sightings WHERE TO_CHAR(datetime,'YYYY') BETWEEN '2000' AND '2014' ORDER BY 1""")
    
    results = cursor.fetchall()
    results_dict4 = [{"Decade": result[0], "count_sightings": result[1]} for result in results]
   
    con.close()

    return results_dict4

    # Query 5

def get_shapes_data_from_db():
    #table_name = UNLESS WE ARE RUNNING ONE TABLE, THIS IS NEED IF NOT THEN JUST RUN THE QUERY BELOW IN EXECUTE
    
    con = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/UFO_Project_db")
   
    # Uses 0-to-9 decade the most widely used method for denominating decades. 
    # This query goes from 1940s to roughly mid-2014 (the latest data).

    cursor = con.cursor()
    cursor.execute("""SELECT * FROM (SELECT UPPER(country), shape, COUNT(shape) FROM ufo_sightings WHERE country = 'us' GROUP BY country, shape ORDER BY COUNT(shape) DESC FETCH FIRST 5 ROWS ONLY) usa UNION ALL SELECT * FROM (SELECT UPPER(country), shape, COUNT(shape) FROM ufo_sightings WHERE country = 'ca' GROUP BY country, shape ORDER BY COUNT(shape) DESC FETCH FIRST 5 ROWS ONLY) can UNION ALL SELECT * FROM (SELECT UPPER(country), shape, COUNT(shape) FROM ufo_sightings WHERE country = 'gb' GROUP BY country, shape ORDER BY COUNT(shape) DESC FETCH FIRST 5 ROWS ONLY) gbr UNION ALL SELECT * FROM (SELECT UPPER(country), shape, COUNT(shape) FROM ufo_sightings WHERE country = 'au' GROUP BY country, shape ORDER BY COUNT(shape) DESC FETCH FIRST 5 ROWS ONLY) aus""")
    
    results = cursor.fetchall()
    results_dict5 = [{"country": result[0], "shape": result[1], "count_sightings": result[2]} for result in results]
   
    con.close()

    return results_dict5

    ##########################################################################


@app.route("/index.html")
def index():
    print("responding to home route: ", datetime.datetime.now())

    return render_template("index.html")

@app.route("/united_states.html")
def united_states():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("united_states.html")

@app.route("/global.html")
def canada():
    print ("responding to charts route: ", datetime.datetime.now())
    return render_template("global.html")

@app.route("/markermap.html")
def markermap():
    print("responding to home route: ", datetime.datetime.now())
    return render_template("markermap.html")


@app.route("/global_heatmap.html")
def heatmap():
    print("responding to home route: ", datetime.datetime.now())
    return render_template("global_heatmap.html")

@app.route("/misc.html")
def miscellaneous():
    print ("responding to charts route: ", datetime.datetime.now())

    return render_template("misc.html")

if __name__ == "__main__":
    app.run(debug=True)

print("finished running app.py")