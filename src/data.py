
# GOOGLE MAPS API KEY
apikey = ""

# DATABASE LOGIN
host = "localhost"
user = "root"
pwd = ""
database = "SOLMAPS"

# KML FILE PATH
kml_fpath = "MyMap.kml"

# HTML CODE
head = """<!DOCTYPE html>
			<html>
			  <head>
			    <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
			    <meta charset="utf-8">
			    <title>Simple Polygon</title>
			    <style>
			      /* Always set the map height explicitly to define the size of the div
			       * element that contains the map. */
			      #map {
			        height: 100%;
			      }
			      /* Optional: Makes the sample page fill the window. */
			      html, body {
			        height: 100%;
			        margin: 0;
			        padding: 0;
			      }
			    </style>
			  </head>
			  <body>
			    <div id="map"></div>
			    <script>

			      

			      function initMap() {
			        var map = new google.maps.Map(document.getElementById('map'), {
			          zoom: 18,
			          center: """

middle = """,
          mapTypeId: 'terrain'
        });

        // Define the LatLng coordinates for the polygon's path.
        var polygonCoords = ["""

tail = """	    ];
        

        // Construct the polygon.
        var polygonField = new google.maps.Polygon({
          paths: polygonCoords,
          strokeColor: '#FF0000',
          strokeOpacity: 0.8,
          strokeWeight: 2,
          fillColor: '#FF0000',
          fillOpacity: 0.35
        });
        polygonField.setMap(map);
      }
			</script>
		    <script async defer
		    src="https://maps.googleapis.com/maps/api/js?key=%s&callback=initMap">
		    </script>
		  </body>
		</html>""" % (apikey)