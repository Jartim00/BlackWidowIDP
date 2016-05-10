<?php
	include_once("errors.php");
	$page="progress";
	include_once("login.php"); //method to check if logged in.
	include_once("database.php"); //configs for querying to database
	include_once("newsitem.php"); //makeup for newsitem
?>

<!doctype html>
<html>
<head>
	<meta charset='utf-8'>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="shortcut icon" type="image/png" href="images/favico.png" />
	<link rel="stylesheet" type="text/css" href="/style/menubar.css"/>
	<link rel="stylesheet" type="text/css" href="/style/bootstrap.min.css" />
	<link rel="stylesheet" type="text/css" href="/style/gototop.css"/>
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<script src="/js/jquery-1.12.3.min.js"></script>
	<script src="/js/gototop.js"></script>
	<script src="/js/bootstrap.min.js"></script>
	<title>OUR PROGRESS | BLACK WIDOW | IDP 8</title>
</head>

<body>
<?php include_once("menu.php"); ?>
<a href="#" id="back-to-top" title="Back to top"><span class="glyphicon glyphicon-arrow-up"></span></a>
<center>
<h1>Our Progress</h1>
<?php
//here come the news messages
$query = "SELECT messageID, uploaded, message FROM Messages ORDER BY uploaded DESC"; //no LIMIT x
$result = query($query);

while ($row = mysqli_fetch_assoc($result)) {
	$photoQuery = "SELECT name FROM Photos WHERE messageID = '" . $row['messageID'] . "'";
	$photos = query($photoQuery);

	$videoQuery = "SELECT name FROM Videos WHERE messageID = '" . $row['messageID'] . "' ";
	$videos = query($videoQuery);

	news($row['uploaded'], $row['message'], $photos, $videos);
}
?>

<?php include_once("foot.php"); ?>
</center>
</body>
</html>
