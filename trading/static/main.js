function loadJson(selector) {
    // return document.querySelector(selector).getAttribute('data-json')
    return JSON.parse(document.querySelector(selector).getAttribute('data-json'));
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
                    label: "Loss",
                    data: jsonData[1],
                    borderColor: 'red',
                    fill: "false",
                    tension: 0.1
                } 
            ]// End datasets 
            }// End data             
        }); 
        new Chart(
            document.getElementById("traded"), 
            { 
                type: 'pie', 
                data: { 
                    labels : [ "Lion", "Horse", "Elephant", "Tiger",
        				"Jaguar" ],
                        datasets : [ {
                            backgroundColor : [ "#51EAEA", "#FCDDB0",
                                    "#FF9D76", "#FB3569", "#82CD47" ],
                            data : [ 418, 263, 434, 586, 332 ]
                        } ]
                    },
                                
            }); 
}
