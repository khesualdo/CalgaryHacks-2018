<?php
include('config.php');

$myfirstname=$_POST['myfirstname'];
$mylastname=$_POST['mylastname'];
$myusername=$_POST['myusername'];
$mypassword=$_POST['mypassword'];
$mypasswordconfirm=$_POST['mypasswordconfirm'];
$salt='';
$hashpassword='';

$error='';
if (isset($_POST['submit'])) {
	if ($mypassword!=$mypasswordconfirm){
		$error = "Password does not match.";
	}
	else{
	//$myusername=mysqli_real_escape_string($con, $myusername);
	//$mypassword=mysqli_real_escape_string($con, $myusername);
	$sql="SELECT * FROM USER WHERE username='$myusername'";
	$result = mysqli_query($con, $sql);
	$rows = mysqli_num_rows($result);
	if ($rows != 0){
		$error = "Username already taken.";
	}
	else{
		$salt = substr(md5(mt_rand() . microtime()), mt_rand(0,35), 5);
		$hashpassword = hash('sha256', $salt.$mypassword);
		$sql="INSERT INTO USER (username, password, salt, firstname, lastname) VALUES ('$myusername', '$hashpassword', '$salt', '$myfirstname', '$mylastname')";
		if ($con->query($sql) === TRUE){
			header( "Location: ./index.php" );
		}
		else {
			$error = "SQL error..";
		}
	}

	}
}
?>
