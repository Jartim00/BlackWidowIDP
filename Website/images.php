<?php
	include_once("errors.php");
	$page="images";
	include_once("login.php"); //method to check if logged in.
	if($_SESSION['username'] != "DEPRECATED" ) {
		header("Location: ../");
	}
?>

<!doctype html>
<html>
<head>
	<meta charset='utf-8'>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" type="text/css" href="/style/menubar.css"/>
	<link rel="shortcut icon" type="image/png" href="images/favico.png" />
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<link rel="stylesheet" type="text/css" href="/style/bootstrap.min.css" />	
	<link rel="stylesheet" type="text/css" href="/style/gototop.css"/>
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<script src="/js/jquery-1.12.3.min.js"></script>
	<script src="/js/gototop.js"></script>
	<script src="/js/bootstrap.min.js"></script>
	<title>BLACK WIDOW | IDP 8</title>
</head>

<body>
<?php include_once("menu.php"); ?>
<a href="#" id="back-to-top" title="Back to top"><span class="glyphicon glyphicon-arrow-up"></span></a>
<center>
<h1>Images</h1><hr>
<?
$files = scandir("images/");

for($i=0; $i < count($files); $i++) {
	if(substr($files[$i], 0, 5) == "2016-") { //only photos that have been uploaded as part of a news 
		echo '<img src="images/'.$files[$i].'" style="width: 720px"><br><br>';
	}
}
?>

</center>
<?php include_once("foot.php"); ?>
</body>
</html>
