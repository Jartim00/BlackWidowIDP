<?php
function news($uploaded, $news, $photos, $videos) {
	echo "<hr><h3>" . $uploaded . "</h3>";
	echo "<p>" . $news . "</p>";

	forEach($photos as $photo) {
		echo "<p><img src='images/" . $photo["name"] . "' style='height: 480px;' class='img-responsive'></p> ";
	} unset($photo);

	//forEach($videos as $video) { //need video player or youtube link
	//	echo "<p><img src='" . $video . "' width=''></p> ";
	//} unset($video);

}
?>
