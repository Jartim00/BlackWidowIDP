<?php
	include_once("errors.php");
	$page="submit";
	include_once("login.php");

	if($_SESSION['username'] != "DEPRECATED" ) {
		header("Location: index.php");
	}

	if(isset($_POST['check']) && $_POST['check'] == "TRUE") {
		include_once("database.php"); //configs for querying to database

		$target_file = date("Y-m-d_H:i:s") ."_". str_replace(" ", "+", basename($_FILES["imgs"]["name"]));
		echo "<p>: File ".$target_file."</p>";

		$uploadOk = 0;
		$imageFileType = pathinfo(strtolower($target_file),PATHINFO_EXTENSION);

		// Check if image file is a actual image or fake image
		if(isset($_POST["submit"])) {
			$check = getimagesize($_FILES["imgs"]["tmp_name"]);
			if($check !== FALSE) {
				echo "<p>: File is an image - " . $check["mime"] . ".</p>";
				$uploadOk = 1;
			} else {
				echo "<p>: File is not an image.</p>";
				$uploadOk = 0;
			}
		}

		// Check file size
		if ($_FILES["imgs"]["size"] > 50000000) { //50000000 = 50.000.000 B = 50.000 KB = 50 MB
			echo "<p>: Sorry, your file is too large.</p>";
			$uploadOk = 0;
		}

		// Check if file already exists
		if (file_exists("images/".$target_file)) {
			echo "<p>: Sorry, file already exists.</p>";
			$uploadOk = 0;
		}

		// Allow certain file formats
		if($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif" ) {
			echo "<p>: Sorry, only JPG, JPEG, PNG & GIF files are allowed.</p>";
			$uploadOk = 0;
		}

		// Check if $uploadOk is set to 0 by an error
		if ($uploadOk == 0) {
			echo "<p>: Sorry, your file was not uploaded.</p>";
		// if everything is ok, database the queries and try to upload file
		} else {
			$maxID = "SELECT MAX(messageID) FROM Messages";
			$num = mysqli_fetch_assoc(query($maxID));
			$messageID = $num["MAX(messageID)"] + 1;
			
			$maxID = "SELECT MAX(id) FROM Photos";
			$num = mysqli_fetch_assoc(query($maxID));
			$photoID = $num["MAX(id)"] + 1;

			$message = db_escape($_POST['message']);
			$message = str_replace('\r\n', "<br>", $message); //remove all extra spaces and tabs (indents and stuffs)
			$messageQuery = ("INSERT INTO Messages (messageID, uploaded, message) VALUES (" . $messageID . ", '". date("Y-m-d H:i:s") ."', '" . $message . "')");

			$imageQuery = "INSERT INTO Photos (id, name, messageID) VALUES (".$photoID.", '".$target_file."', ".$messageID.")";

			if(FALSE === query($messageQuery)) {
				echo 'Message query did not work.<br>';
				break;
			} else {
				if(FALSE === query($imageQuery)) {
					echo 'Photo query did not work.<br>';
					break;
				} else {
					if (move_uploaded_file($_FILES["imgs"]["tmp_name"], "images/".$target_file)) {
						echo "<p>: The file ". basename( $_FILES["imgs"]["name"]). " has been uploaded.</p>";
						include_once("email.php"); 
						email($target_file, $message);
					} else {
						echo "<p>: Sorry, there was an error uploading your file ".basename($_FILES["imgs"]["name"]).".</p>";
						
						//remove the database queries linked to the failed upload
						$removeMessage = "DELETE FROM Messages WHERE messageID = " . $messageID;
						$removePhoto = "DELETE FROM Photos WHERE messageID = " . $messageID;
						
						query($removeMessage);
						query($removePhoto);
					}
				}
			}
		}
		
		if($uploadOk == 1) {
			header("Location: index.php"); //after submitting a story, go to the front page to check it out.
		}
	}
?>

<!doctype html>
<html>
<head>
	<meta charset='utf-8'>
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="shortcut icon" type="image/png" href="images/favico.png" />
	<link rel="stylesheet" type="text/css" href="/style/menubar.css"/>
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<link rel="stylesheet" type="text/css" href="/style/bootstrap.min.css" />
	<link rel="stylesheet" type="text/css" href="/style/gototop.css"/>
	<link rel="stylesheet" type="text/css" href="/style/glyphicons.css"/>
	<script src="/js/gototop.js"></script>
	<script src="/js/jquery-1.12.3.min.js"></script>
	<script src="/js/bootstrap.min.js"></script>
	<title>BLACK WIDOW | IDP 8</title>
</head>

<?php include_once("menu.php"); ?>
<a href="#" id="back-to-top" title="Back to top"><span class="glyphicon glyphicon-arrow-up"></span></a>
<center>
<h1>Submit a new story</h1><hr>

<form id="newMsg" action="" method="post" enctype="multipart/form-data">
<input type="hidden" name="check" value="TRUE">
<p><textarea name="message" form="newMsg" rows=7 cols=50>News message...</textarea></p>
<p>Photo's: <input type="file" name="imgs" id="imgs" accept="image/*"></p>
<p><input type="submit" name="submit" value="Send!"></p>
</form>
</center>
<?php include_once("foot.php"); ?>
</body>
</html>
