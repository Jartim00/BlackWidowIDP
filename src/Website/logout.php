<?php
	include_once("errors.php");

	session_start();
	$_SESSION['username'] = "";
	session_unset();
	session_destroy();
	
	header("Location: http://www.black-widow.nl/".$_GET['page'].".php");
?>