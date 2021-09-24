//Plotly code here
function buildChart() {
    d3.json("static/json/GLOBAL.json",(data) => {
        console.log(data);
        // resultArray = data.sightings_by_decade;
        // var result = resultArray[0];
        // var decade = result.Decade;
        var decade = data.sightings_by_decade.Decade;
        var count = data.sightings_by_decade.count_sightings;
        // var count = result.count_sightings;
        console.log(decade);
        console.log(count);
        console.log(data.sightings_by_decade);
        var label = data.sightings_by_decade[0];
        // var decades = result.decade;
        // var counts = result.count;

        // Build a Bubble Chart

        var barLayout = {
            title: "Global Sightings Count",
            // margin: { t: 50 },
            xaxis: { title: "Decades" },
            yaxis: { title: "Count" },
            // margin: { t: 30 },
        };
        var barData = [
            {
                x: decade,
                y: count,
                text: label,
                // mode: "markers",
            }

        ];

        Plotly.newPlot("bar", barData, barLayout);
    })
}

buildChart()