<?php
	include_once("errors.php");
	$page="index";
	include_once("login.php"); //method to check if logged in.
	include_once("database.php"); //configs for querying to database
	include_once("newsitem.php"); //makeup for a news message
?>

<!doctype html>
<html>
<head>
	<meta charset='utf-8'>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<link rel="shortcut icon" type="image/png" href="images/favico.png" />
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="/style/menubar.css"/>
	<link rel="stylesheet" type="text/css" href="/style/gototop.css"/>
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<link rel="stylesheet" type="text/css" href="/style/bootstrap.min.css" />
	<script src="/js/jquery-1.12.3.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
	<script src="/js/carousel.js"></script>
	<script src="/js/gototop.js"></script>
	<title>BLACK WIDOW | IDP 8</title>
</head>

<body>
<a href="#" id="back-to-top" title="Back to top"><span class="glyphicon glyphicon-arrow-up"></span></a>
<?php
include_once("menu.php");
echo"<center>";

//carousel
$fotoArray = array();
$message = array();
$fotoQuery = "SELECT name, messageID FROM Photos ORDER BY RAND() LIMIT 5";
$fotos = query($fotoQuery);
while($foto = mysqli_fetch_assoc($fotos)){
	array_push($fotoArray, $foto['name']);
	$messageQuery = "SELECT message FROM Messages WHERE messageID = '".$foto['messageID']."'";
	array_push($message, mysqli_fetch_assoc(query($messageQuery))['message'] );
}

echo "<div id='carousel-blackwidow' class='carousel slide' data-ride='carousel'>
	<!-- Indicators -->
	<ol class='carousel-indicators'>";

for($i=0; $i < count($fotoArray); $i++){
	echo" <li data-target='#carousel-blackwidow' data-slide-to='".$i."' ".($i==0 ? "class='active'" : "")."></li>";
}

echo "</ol>
	<!-- Wrapper for slides -->
	<div class='carousel-inner' role='listbox'>";

for($i=0; $i < sizeof($fotoArray); $i++){	
	echo "
	<div class='item" . ($i == 0 ? " active" : "") . "'>
		<picture class='img-responsive'>
			<!--[if IE 9]><video style='display: none;'><![endif]-->

			<source srcset='/images/".$fotoArray[$i]."'></source>

			<!--[if IE 9]></video><![endif]-->
			<img alt='".$fotoArray[$i]."' srcset='/images/".$fotoArray[$i]."' style='height: 480px' class='img-responsive'>
		</picture>
		<div class='carousel-caption'>
			<p>".$message[$i]."</p>
		</div>		
	</div>";
}

echo "</div><!-- Controls -->
	<a class='left carousel-control' href='#carousel-blackwidow' role='button' data-slide='prev'>
		<span class='glyphicon glyphicon-chevron-left' aria-hidden='true'></span>
		<span class='sr-only'>Previous</span>
	</a>
	<a class='right carousel-control' href='#carousel-blackwidow' role='button' data-slide='next'>
		<span class='glyphicon glyphicon-chevron-right' aria-hidden='true'></span>
		<span class='sr-only'>Next</span>
	</a>
</div>";

//here come the news messages
$query = "SELECT messageID, uploaded, message FROM Messages ORDER BY messageID DESC LIMIT 5";
$result = query($query);

while ($row = mysqli_fetch_assoc($result)) {
	$photoQuery = "SELECT name FROM Photos WHERE messageID = '" . $row['messageID'] . "'";
	$photos = query($photoQuery);

	$videoQuery = "SELECT name FROM Videos WHERE messageID = '" . $row['messageID'] . "' ";
	$videos = query($videoQuery);

	news($row['uploaded'], $row['message'], $photos, $videos);
}
echo "</center>";

include_once("foot.php");
?>
</body>
</html>
