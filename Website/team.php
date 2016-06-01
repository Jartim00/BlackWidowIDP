<?php
	include_once("errors.php");
	$page="team";
	include_once("login.php"); //method to check if logged in.

	$members = array(
		"Mariska Buursma", "Kevin Nauta", "Jaron Timmerman", "Melvin Kool", "Jurjen Hazenberg", "Sylvius Roeles", 
		"Jouke Smitstra", "Dirk de Vries", 
		"Peter Oldenkamp", "Thomas Jongsma", "Amar Borovac",
		"Nynke van der Wijk", "Jop Wielens");
	$studie = array(
		"I", "I", "I", "I", "I", "I",
		"E", "E",
		"W", "W", "W",
		"Tutor", "Tutor");
	$fotos = array("
		mariska.jpg","kevin.jpg","jaron.jpg","melvin.jpeg","jurjen.jpg","sylvius.jpg",
		"jouke.jpg","dirk.jpg",
		"peter.jpg", "thomas.jpg", "amar.jpg",
		"nynke.jpeg","jop.jpg");
?>

<!doctype html>
<html>
<head>
	<meta charset='utf-8'>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="/style/menubar.css"/>
	<link rel="stylesheet" type="text/css" href="/style/gototop.css"/>
	<link rel="stylesheet" type="text/css" href="/style/team.css"/>
	<link rel="shortcut icon" type="image/png" href="images/favico.png" />
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<link rel="stylesheet" type="text/css" href="/style/bootstrap.min.css" />
	<script src="/js/jquery-1.12.3.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
	<script src="/js/gototop.js"></script>
	<title>TEAM | BLACK WIDOW | IDP 8</title>
</head>

<body>
<?php include_once("menu.php"); ?>
<a href="#" id="back-to-top" title="Back to top"><span class="glyphicon glyphicon-arrow-up"></span></a>
<center>
<h1>The Team</h1><hr>
<p><img src="/images/groepsfoto.jpg" style='height:480px'></p><br>
<div class="row">
	<?php
	for($i=0; $i<sizeof($members); $i++) {
		echo("<div class='col=sm-12 col-md-4' >
				<div class='tile'>
				<img src='images/" . $fotos[$i] . "' class='img-responsive'>");
		echo("<span class='tile-caption' style=''>" . $members[$i] . " (");
		if($studie[$i] == "I") {
			echo "Informatica";
		} else if ($studie[$i] == "E") {
			echo "Elektrotechniek";
		} else if ($studie[$i] == "W") {
			echo "Werktuigbouwkunde";
		} else {
			echo $studie[$i];
		}
		echo (")</span></div></div>");
	}
	?>
</div>

<?php include_once("foot.php"); ?>
</center>
</body>
</html>
