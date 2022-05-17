var team1_points = 0
var team2_points = 0

function addTeam1() {
    team1_points += 1;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
}

function subtractTeam1() {
    team1_points -= 1;
    document.getElementById('team1_points').innerHTML = team1_points + ' points'
}

function addTeam2() {
    team2_points += 1;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
}

function subtractTeam2() {
    team2_points -= 1;
    document.getElementById('team2_points').innerHTML = team2_points + ' points'
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
