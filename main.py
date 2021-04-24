from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def index():
    return """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <title>Hackathon Project</title>
    <link href="index.css" rel="stylesheet" type="text/css" />

    <script>
    function displayScore() {
      var earthHour = document.forms["data"]["hourParticipation"].value;
      var charity = document.forms["data"]["charityIncentives"].value;
      var rooftop = document.forms["data"]["rooftopGardens"].value;
      var solar = document.forms["data"]["solarPanels"].value;

      var score = 0

      if (earthHour == "yes") {
        score ++;
      }
      if (charity == "yes") {
        score ++;
      }
      if (rooftop == "yes") {
        score ++;
      }
      if (solar == "yes") {
        score ++;
      }

      alert(score);

    }
    </script>
  </head>
  <body>
    <h1>Hackathon Project</h1>
    <form id="data" onsubmit="return displayScore()">
      <b> Environmental Participation </b> <br>
      Have you participated in Earth Hour? <input type="text" name="hourParticipation"><br>
      Have you partaken in environmental charity incentives? <input type="text" name="charityIncentives"><br>
      <hr>
      <b> Sustainability </b> <br>
      Do you have rooftop gardens? <input type="text" name="rooftopGardens"></input><br>
      Do you have solar panels? <input type="text" name="solarPanels"></input><br>
      <input type="submit" value="Submit">
    </form>

  </body>
</html>
"""

def run():
  app.run(host='0.0.0.0', port=8080)

def keep():
  t = Thread(target=run)
  t.start()

keep()

