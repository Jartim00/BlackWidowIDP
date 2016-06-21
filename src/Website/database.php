<?php
function db_escape($string) {
	return mysqli_real_escape_string(connect(), $_POST['message']);
}

function query($query) {
	if($query == "") {
		echo("<p>Error: query is empty.</p>");
		return FALSE;
	}
	
	$mysqli = connect();
	if($mysqli == FALSE) {
		echo("<p>Error: could not connect.</p>");
		return FALSE;
	}
	
	$result = mysqli_query($mysqli, $query);
	if($result === FALSE) {
		echo("<p>Error: query didn't work: ". mysqli_error($mysqli) ."</p>");
		return FALSE;
	}
	
	mysqli_close($mysqli);
	return $result;	
}

function connect() {
	$hostname = "localhost";
	$username = "DEPRECATED";
	$password = "DEPRECATED";
	$database = "DEPRECATED";
	$mysqli = mysqli_connect($hostname, $username, $password, $database);
	if (mysqli_connect_errno($mysqli)) {
		echo "<p>Could not login to database: " . mysqli_connect_error() . "</p>";
		return FALSE;
	} else {
		return $mysqli;
	}
}
?>