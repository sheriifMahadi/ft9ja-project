function loadJson(selector) {
    if(document.querySelector(selector)){
        return JSON.parse(document.querySelector(selector).getAttribute('data-json'));

    }
  }

function createTradeChart(jsonData, timestamps){
    new Chart(
        document.getElementById("chart"), 
        { 
            type: 'line', 
            data: { 
                labels:timestamps,
                datasets: [{ 
                    label: 'Profit $', 
                    data: jsonData[0], 
                    borderColor: 'green', 
                    fill: false, 
                    tension: 0.1 
                },
                {
                    label: "Loss $",
                    data: jsonData[1],
                    borderColor: 'red',
                    fill: "false",
                    tension: 0.1
                } 
            ]// End datasets 
            }// End data             
        }); 
}

function createHomeChart(){
    if (document.getElementById("traded")){
        new Chart(
            document.getElementById("traded"), 
            { 
                type: 'pie', 
                data: { 
                    labels : [],
                        datasets : [ {
                            backgroundColor : [ "#51EAEA", "#FCDDB0",
                                    "#FF9D76", "#FB3569", "#82CD47" ],
                            data : [100, 300, 400, 300, 69,
                            120, 30, 50, 80, 10]
                        } ]
                    },
                                
            }); 
    }
}

function createHomeLineChart(){
    if(document.getElementById("home-line")){
        new Chart(
            document.getElementById("home-line"), 
            { 
                type: 'line', 
                data: { 
                    labels:["", "", "", "", "", "", "", "", "", ""],
                    datasets: [{ 
                        label: 'Profit $', 
                        data: [3, 5.7, 40, 50, 80.7, 50.1, 70.7, 70.4, 90, 90.5], 
                        borderColor: 'green', 
                        fill: false, 
                        tension: 0.1 
                    },
                    {
                        label: "Loss $",
                        data: [20, 60, 40, 10, 0.5, 6.5, 2.5, 10, 1, 4],
                        borderColor: 'red',
                        fill: "false",
                        tension: 0.1
                    } 
                ]// End datasets 
                }// End data             
            }); 
    }
}
window.onload = function(){
    const jsonData = loadJson("#hidden-div");

    const now = new Date();
    const hours = now.getHours();
    const minutes = now.getMinutes();

    let timestamps = []
    for (i = 0; i < 10; i++){
        timestamps.push(`${hours}:${minutes + i}`)
    }
    if (jsonData){
        createTradeChart(jsonData, timestamps)

    }
    createHomeChart()
    createHomeLineChart()
}
