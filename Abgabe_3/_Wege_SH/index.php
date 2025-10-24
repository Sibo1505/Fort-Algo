<?php
$towns = array(array("name" => "Niebüll", "x"=>"475", "y"=>"187"),
array("name" => "Flensburg", "x"=>"881", "y"=>"194"),
array("name" => "Tarp", "x"=>"894", "y"=>"342"),
array("name" => "Bredstedt", "x"=>"567", "y"=>"398"),
array("name" => "Schleswig", "x"=>"986", "y"=>"526"),
array("name" => "Husum", "x"=>"638", "y"=>"572"),
array("name" => "Kiel", "x"=>"1424", "y"=>"784"),
array("name" => "Neumünster", "x"=>"1309", "y"=>"1077"),
array("name" => "Hamburg", "x"=>"1269", "y"=>"1679"),
array("name" => "Lübeck", "x"=>"1833", "y"=>"1341"),
array("name" => "Heiligenhafen", "x"=>"2070", "y"=>"711"),
array("name" => "Lütjenburg", "x"=>"1763", "y"=>"811"),
array("name" => "Plön", "x"=>"1628", "y"=>"976"),
array("name" => "Hohenweststedt", "x"=>"1071", "y"=>"1062"),
array("name" => "Brunsbüttel", "x"=>"725", "y"=>"1272"),
array("name" => "Itzehoe", "x"=>"969", "y"=>"1284"),
array("name" => "Heide", "x"=>"673", "y"=>"935"),
array("name" => "Büdelsdorf", "x"=>"1091", "y"=>"784"),
array("name" => "Wahlstedt", "x"=>"1524", "y"=>"1240"),
array("name" => "Neustadt", "x"=>"1894", "y"=>"1051"),
array("name" => "Wismar", "x"=>"2392", "y"=>"1312"),
array("name" => "Bad Oldesloe", "x"=>"1595", "y"=>"1413"),
array("name" => "Elmshorn", "x"=>"1075", "y"=>"1468"),
array("name" => "Bad Bramstedt", "x"=>"1272", "y"=>"1277"),
array("name" => "Kappeln", "x"=>"1287", "y"=>"343"),
array("name" => "Büsum", "x"=>"494", "y"=>"1006"),
array("name" => "Süderbrarup", "x"=>"1153", "y"=>"373"),
array("name" => "Eckernförde", "x"=>"1202", "y"=>"580"),
array("name" => "Gettorf", "x"=>"1313", "y"=>"666"),
array("name" => "Schönberg", "x"=>"1615", "y"=>"683"),
array("name" => "Preetz", "x"=>"1528", "y"=>"882"),
array("name" => "Nortorf", "x"=>"1217", "y"=>"960"),
array("name" => "Melsdorf", "x"=>"654", "y"=>"1064"),
array("name" => "Marne", "x"=>"603", "y"=>"1230"),
array("name" => "Bargteheide", "x"=>"1519", "y"=>"1510"),
array("name" => "Ahrensburg", "x"=>"1502", "y"=>"1576"),
array("name" => "Ratzeburg", "x"=>"1864", "y"=>"1542"),
array("name" => "Mölln", "x"=>"1818", "y"=>"1629"),
array("name" => "Ahrensbök", "x"=>"1734", "y"=>"1157"),
array("name" => "Husby", "x"=>"1019", "y"=>"216"),
array("name" => "Sörup", "x"=>"1077", "y"=>"275"),
array("name" => "Böklund", "x"=>"1017", "y"=>"425"),
array("name" => "Friedrichstadt", "x"=>"652", "y"=>"706"),
array("name" => "Tönning", "x"=>"548", "y"=>"772"),
array("name" => "Wesselburen", "x"=>"543", "y"=>"910"),
array("name" => "Hanerau-Hademarschen", "x"=>"814", "y"=>"1015"),
array("name" => "Burg (Dithmarschen)", "x"=>"699", "y"=>"1177"),
array("name" => "Kellinghusen", "x"=>"1111", "y"=>"1234"),
array("name" => "Krempe", "x"=>"948", "y"=>"1372"),
array("name" => "Glückstadt", "x"=>"891", "y"=>"1429"),
array("name" => "Wedel", "x"=>"1112", "y"=>"1688"),
array("name" => "Pinneberg", "x"=>"1157", "y"=>"1582"),
array("name" => "Kaltenkirchen", "x"=>"1294", "y"=>"1373"),
);

$roads = array(
array("from" => "Flensburg", "to" => "Tarp", "type" => "autobahn"),
array("from" => "Tarp", "to" => "Schleswig", "type" => "autobahn"),
array("from" => "Schleswig", "to" => "Büdelsdorf", "type" => "autobahn"),
array("from" => "Büdelsdorf", "to" => "Nortorf", "type" => "autobahn"),
array("from" => "Nortorf", "to" => "Neumünster", "type" => "autobahn"),
array("from" => "Neumünster", "to" => "Bad Bramstedt", "type" => "autobahn"),
array("from" => "Kaltenkirchen", "to" => "Bad Bramstedt", "type" => "autobahn"),
array("from" => "Kaltenkirchen", "to" => "Hamburg", "type" => "autobahn"),

array("from" => "Büdelsdorf", "to" => "Kiel", "type" => "autobahn"),

array("from" => "Kiel", "to" => "Neumünster", "type" => "autobahn"),

array("from" => "Hamburg", "to" => "Pinneberg", "type" => "autobahn"),
array("from" => "Elmshorn", "to" => "Pinneberg", "type" => "autobahn"),
array("from" => "Elmshorn", "to" => "Itzehoe", "type" => "autobahn"),
array("from" => "Itzehoe", "to" => "Hanerau-Hademarschen", "type" => "autobahn"),
array("from" => "Heide", "to" => "Hanerau-Hademarschen", "type" => "autobahn"),


array("from" => "Hamburg", "to" => "Ahrensburg", "type" => "autobahn"),
array("from" => "Bargteheide", "to" => "Ahrensburg", "type" => "autobahn"),
array("from" => "Bargteheide", "to" => "Bad Oldesloe", "type" => "autobahn"),
array("from" => "Lübeck", "to" => "Bad Oldesloe", "type" => "autobahn"),
array("from" => "Bargteheide", "to" => "Wahlstedt", "type" => "autobahn"),
array("from" => "Lübeck", "to" => "Wahlstedt", "type" => "autobahn"),

array("from" => "Lübeck", "to" => "Wismar", "type" => "autobahn"),
array("from" => "Lübeck", "to" => "Neustadt", "type" => "autobahn"),
array("from" => "Heiligenhafen", "to" => "Neustadt", "type" => "autobahn"),

//normal roads
array("from" => "Kiel", "to" => "Schönberg", "type" => "normal"),
array("from" => "Niebüll", "to" => "Flensburg", "type" => "normal"),
array("from" => "Kappeln", "to" => "Süderbrarup", "type" => "normal"),
array("from" => "Böklund", "to" => "Süderbrarup", "type" => "normal"),
array("from" => "Böklund", "to" => "Schleswig", "type" => "normal"),
array("from" => "Schleswig", "to" => "Husum", "type" => "normal"),
array("from" => "Bredstedt", "to" => "Husum", "type" => "normal"),
array("from" => "Bredstedt", "to" => "Niebüll", "type" => "normal"),
array("from" => "Friedrichstadt", "to" => "Husum", "type" => "normal"),
array("from" => "Friedrichstadt", "to" => "Tönning", "type" => "normal"),
array("from" => "Wesselburen", "to" => "Tönning", "type" => "normal"),
array("from" => "Wesselburen", "to" => "Heide", "type" => "normal"),
array("from" => "Büsum", "to" => "Heide", "type" => "normal"),
array("from" => "Melsdorf", "to" => "Heide", "type" => "normal"),
array("from" => "Melsdorf", "to" => "Marne", "type" => "normal"),
array("from" => "Brunsbüttel", "to" => "Marne", "type" => "normal"),
array("from" => "Brunsbüttel", "to" => "Glückstadt", "type" => "normal"),
array("from" => "Husum", "to" => "Flensburg", "type" => "normal"),
array("from" => "Schleswig", "to" => "Eckernförde", "type" => "normal"),
array("from" => "Friedrichstadt", "to" => "Büdelsdorf", "type" => "normal"),
array("from" => "Heide", "to" => "Büdelsdorf", "type" => "normal"),
array("from" => "Hanerau-Hademarschen", "to" => "Hohenweststedt", "type" => "normal"),
array("from" => "Neumünster", "to" => "Hohenweststedt", "type" => "normal"),
array("from" => "Itzehoe", "to" => "Kellinghusen", "type" => "normal"),
array("from" => "Bad Bramstedt", "to" => "Kellinghusen", "type" => "normal"),
array("from" => "Bad Bramstedt", "to" => "Wahlstedt", "type" => "normal"),
array("from" => "Ahrensbök", "to" => "Wahlstedt", "type" => "normal"),
array("from" => "Ahrensbök", "to" => "Neustadt", "type" => "normal"),
array("from" => "Plön", "to" => "Neustadt", "type" => "normal"),
array("from" => "Plön", "to" => "Preetz", "type" => "normal"),
array("from" => "Kiel", "to" => "Preetz", "type" => "normal"),
array("from" => "Kiel", "to" => "Lütjenburg", "type" => "normal"),
array("from" => "Schönberg", "to" => "Lütjenburg", "type" => "normal"),
array("from" => "Plön", "to" => "Neumünster", "type" => "normal"),
array("from" => "Kappeln", "to" => "Eckernförde", "type" => "normal"),
array("from" => "Gettorf", "to" => "Eckernförde", "type" => "normal"),
array("from" => "Gettorf", "to" => "Kiel", "type" => "normal"),
array("from" => "Büdelsdorf", "to" => "Hohenweststedt", "type" => "normal"),
array("from" => "Glückstadt", "to" => "Elmshorn", "type" => "normal"),
array("from" => "Wedel", "to" => "Elmshorn", "type" => "normal"),
array("from" => "Hamburg", "to" => "Wahlstedt", "type" => "normal"),
array("from" => "Neumünster", "to" => "Plön", "type" => "normal"),
array("from" => "Lütjenburg", "to" => "Plön", "type" => "normal"),
array("from" => "Bad Oldesloe", "to" => "Ratzeburg", "type" => "normal"),
array("from" => "Heiligenhafen", "to" => "Lütjenburg", "type" => "normal"),
array("from" => "Lübeck", "to" => "Ratzeburg", "type" => "normal"),
array("from" => "Itzehoe", "to" => "Hohenweststedt", "type" => "normal"),
array("from" => "Wahlstedt", "to" => "Kiel", "type" => "normal"),
array("from" => "Schleswig", "to" => "Tarp", "type" => "normal"),
array("from" => "Tarp", "to" => "Flensburg", "type" => "normal"),
array("from" => "Schleswig", "to" => "Büdelsdorf", "type" => "normal"),
array("from" => "Eckernförde", "to" => "Büdelsdorf", "type" => "normal"),
array("from" => "Melsdorf", "to" => "Hanerau-Hademarschen", "type" => "normal"),
array("from" => "Bad Bramstedt", "to" => "Hamburg", "type" => "normal"),
array("from" => "Bargteheide", "to" => "Hamburg", "type" => "normal"),
array("from" => "Bargteheide", "to" => "Bad Oldesloe", "type" => "normal"),
array("from" => "Lübeck", "to" => "Bad Oldesloe", "type" => "normal"),
array("from" => "Lübeck", "to" => "Neustadt", "type" => "normal"),
array("from" => "Heiligenhafen", "to" => "Neustadt", "type" => "normal"),
array("from" => "Husby", "to" => "Flensburg", "type" => "normal"),
array("from" => "Sörup", "to" => "Flensburg", "type" => "normal"),
array("from" => "Sörup", "to" => "Kappeln", "type" => "normal"),
array("from" => "Mölln", "to" => "Ratzeburg", "type" => "normal"),
);



?>
<html>

<body>

    <div style="position:relative;width:100%; height:100%;">
		<canvas id="myCanvas" width="3000" height="2000" style="border:1px solid #d3d3d3;z-index:1;position:absolute;">
		Your browser does not support the HTML5 canvas tag.</canvas>
		<script>
		window.onload = function() {
		  var canvas = document.getElementById("myCanvas");
		  var ctx = canvas.getContext("2d");
		  var img = document.getElementById("map");
		  ctx.drawImage(img, 0, 0);
		  
		  <?php
		  foreach ($roads as $road)
		  {
			  $from = $road['from'];
			  $to =  $road['to'];
			  $type =  $road['type'];
			  
			  foreach ($towns as $town)
			  {
				  if ($from == $town['name'])
				  {
					  $from_x = $town['x'];
					  $from_y = $town['y'];
				  }
				  if ($to == $town['name'])
				  {
					  $to_x = $town['x'];
					  $to_y = $town['y'];
				  }
			  }
			  
			  if ($type == "autobahn")
			  {
				  ?>
				  ctx.lineWidth = 10;
				  ctx.strokeStyle = '#0000ff';
				  <?php
			  }
			  if ($type == "normal")
			  {
				  ?>
					  ctx.lineWidth = 5;
				      ctx.strokeStyle = '#ffd900';
				  <?php
			  }
			  
			  
			  echo "ctx.beginPath();
ctx.moveTo($from_x, $from_y);
ctx.lineTo($to_x, $to_y);
ctx.stroke();";
		  }
		  
		  ?>
		};
		</script>
		
        <img src="sh.png" id="map" style="position: absolute;display:none;">
        <div id="naming" style="position: absolute;z-index:2;">
            <input type="text" id="name">
            <input type="submit" value="add" id="add">
        </div>
        <div id="coord"  style="position: absolute;background-color: white;z-index:10;">Koordinaten<br></div>
		<div id="coord"  style="position: absolute;background-color: white;">Strassen<br>
			<?php
			foreach ($towns as $town)
			{
				$name = $town['name'];
				$x = $town['x'];
				$y = $town['y'];
				echo "<div style='position:absolute;z-index:1;top:$y;left:$x;background-color:white;'>".$name."</div>";
			}
			 
			?>
		</div>
    </div>
  <div style="margin-top:1300px">  
 <!-- 		Strasse hinzufügen<br>
		<select  name=from>
		<?php
		foreach ($towns as $id => $town)
		{
			$name = $town['name'];
			$x = $town['x'];
			$y = $town['y'];
			echo "<option value=$id>$name,$x,$y</option>\n";
		} 
		?></select> 
		<select  name=to>
		<?php
		foreach ($towns as $id => $town)
		{
			$name = $town['name'];
			$x = $town['x'];
			$y = $town['y'];
			echo "<option value=$id>$name,$x,$y</option>\n";
		} 
		?></select> 		
		-->
		<h1>Orte</h1>
		<pre>
<?php
		foreach ($towns as $town)
		{
			$name = $town['name'];
			$x = $town['x'];
			$y = $town['y'];
			echo "$name,$x,$y\n";
		}
		
		?>
		</pre>
		
		
				<h1>Strassen</h1>
				<pre>
<?php
	  foreach ($roads as $road)
	  {
		  $from = $road['from'];
		  $to =  $road['to'];
		  $type =  $road['type'];
		  echo "$from,$to,$type\n";
	  }
		
				?>
				</pre>
		
		Korrekturen bitte der Form:
		<pre>Strassen
array("from" => "Kiel", "to" => "Schönberg", "type" => "normal"),

Orten
array("name" => "Pinneberg", "x"=>"1157", "y"=>"1582"),
</pre>

		
		<br>
		
    </div>
	


    <script>

    let map = document.querySelector("#myCanvas");

    map.addEventListener("click", function (event){
        let x = event.pageX - event.currentTarget.offsetLeft; 
        let y = event.pageY - event.currentTarget.offsetTop;

        let name = document.querySelector("#naming");
        name.style.top = y;
        name.style.left = x;


    }
    
    );

    let add = document.querySelector("#add");

    add.addEventListener("click", function (event){
        event.preventDefault();
        let name = document.querySelector("#naming");

        let x = name.offsetLeft;
        let y = name.offsetTop;

        let nametext = document.querySelector("#name");


        let coord = document.querySelector("#coord");
        coord.innerHTML += '("name" => "' + nametext.value 
							+ '", "x"=>"' + x
		                    + '", "y"=>"' + y + '"),<br>';
        console.log(nametext.value + "x:"+x + "y:"+y);
    }
    
    );



    </script>
</body>
</html>