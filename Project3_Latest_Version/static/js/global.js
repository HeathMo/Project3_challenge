// //Plotly code here
// function buildChart() {
//     d3.json("static/json/GLOBAL.json",(data) => {
//         console.log(data);
//         // resultArray = data.sightings_by_decade;
//         // var result = resultArray[0];
//         // var decade = result.Decade;
//         var decade = data.sightings_by_decade.Decade;
//         var count = data.sightings_by_decade.count_sightings;
//         // var count = result.count_sightings;
//         console.log(decade);
//         console.log(count);
//         console.log(data.sightings_by_decade);
//         var label = data.sightings_by_decade[0];
//         // var decades = result.decade;
//         // var counts = result.count;

//         // Build a Bubble Chart

//         var barLayout = {
//             title: "Global Sightings Count",
//             // margin: { t: 50 },
//             xaxis: { title: "Decades" },
//             yaxis: { title: "Count" },
//             // margin: { t: 30 },
//         };
//         var barData = [
//             {
//                 x: decade,
//                 y: count,
//                 text: label,
//                 // mode: "markers",
//             }

//         ];

//         Plotly.newPlot("bar", barData, barLayout);
//     })
// }

// buildChart()
var bar_data = [
  {
    x: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    y: [4596, 3817, 4482, 4509, 4346, 6607, 7972, 7152, 6360, 6321, 5702, 4652],
    type: "bar",
  },
];
var bar_layout = {
  title: "Global UFO Sightings by Month",
  bargap: 0.05,
 
};
Plotly.newPlot("bar", bar_data, bar_layout);

// var bars_data = [
//   {
//     x: ["US", "CA", "GB", "AU"],
//     y: [63553, 2942, 11, 10],
//     type: "bar",
//   },
// ];
// var bars_layout = {
//   title: "UFO Sightings Per Country",
//   bargap: 0.05,
// };
// Plotly.newPlot("bar", bars_data, bars_layout);
