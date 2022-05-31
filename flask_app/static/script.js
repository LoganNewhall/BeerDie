var team1_points = 0
var team2_points = 0

function addTeam1() {
    team1_points += 1;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function subtractTeam1() {
    team1_points -= 1;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
}

function sinkTeam1() {
    team1_points +=3;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function cupHitTeam1() {
    team1_points += 2;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function selfSinkTeam1() {
    alert('How embarrassing to sink your own team :( The sunked teammate must finish their drink!')
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}


function addTeam2() {
    team2_points += 1;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
    // console.log(user_id);
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function subtractTeam2() {
    team2_points -= 1;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
}

function sinkTeam2() {
    team2_points +=3;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function cupHitTeam2() {
    team2_points += 2;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function selfSinkTeam2() {
    alert('How embarrassing to sink your own team :( The sunked teammate must finish their drink!')
    // $.ajax({
    //     type: "POST",
    //     url: "/...",
    //     contentType: "application/json",
    //     data: JSON.stringify({user_id: user_id}),
    //     dataType: "json"
    // });
}

function endGame() {
    $.ajax({
        type: "POST",
        url: "/end",
        contentType: "application/json",
        data: JSON.stringify({team_1_score: team1_points, team_2_score: team2_points}),
        dataType: "json",
        success: function(response) {
            window.location.pathname = '/dashboard'
        }
    });
}
