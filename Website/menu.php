<?php
echo "<center><a href='index.php'><div id='logo'>
	<img src='images/blackwidowlogo.png' class='img-responsive'>
	</div></a></center>

	<div id='cssmenu'>
	<ul>
	   <li " . ($page == "index" ? "class='active'" : "" ) . "><a href='index.php'><span>Home</span></a></li>
	   <li " . ($page == "progress" ? "class='active'" : "" ) . "><a href='progress.php'><span>Our Progress</span></a></li>
	   <li " . ($page == "team" ? "class='active'" : "" ) . "><a href='team.php'><span>The Team</span></a></li>
	   <li " . ($page == "project" ? "class='active'" : "" ) . ( (!isset($_SESSION['username'])) || ( $_SESSION['username'] == "") ? " class='last'" : "") . "><a href='project.php'><span>The Project</span></a></li>
	" . (isset($_SESSION['username']) && $_SESSION['username'] != "" ? "<li ".($page == "submit" ? "class='active'" : "" )."><a href='submit.php'><span>Submit a News!</span></a></li>" : "")
//	  . (isset($_SESSION['username']) && $_SESSION['username'] != "" ? "<li ".($page == "images" ? "class='active'" : "" )."><a href='images.php'><span>Images (DEV)</span></a></li>" : "")
	  . (isset($_SESSION['username']) && $_SESSION['username'] != "" ? "<li class='last'><a href='logout.php?page=".$page."'><span>Log Out</span></a></li>" : "")
	. "</ul>
	</div>";

?>
