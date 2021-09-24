//Plotly code here
var us_data = [
    {
        x: [8683, 3754, 3707, 3398, 2915, 2447, 2362, 2319, 2251, 1781, 1722, 
            1667, 1431, 1385, 1268, 1248, 1238, 1236, 1235, 1205],
        y: ['CA', 'FL', 'WA', 'TX', 'NY', 'IL', 'AZ', 'PA', 'OH', 'MI', 'NC',
            'OR', 'MO', 'CO', 'IN', 'VA', 'MA', 'NJ', 'GA', 'WI'],
        orientation: 'h'
    }
];

Plotly.newPlot("bar", us_data);