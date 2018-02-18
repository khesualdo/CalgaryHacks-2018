<?php
include('config.php');

$username=$_POST['username'];
$password=$_POST['password'];
$username=mysqli_real_escape_string($con, $username);
$password=mysqli_real_escape_string($con, $password);

$error ='';
if (isset($_POST['submit'])) {
	$sql="select * from USER where username='$username'";
	$result = mysqli_query($con, $sql);
	$row = mysqli_fetch_array($result);
	$rows = mysqli_num_rows($result);
	if ($rows == 1){
		$salt = $row['salt'];
		$hashpassword = hash('sha256', $salt.$password);
		if ($hashpassword == $row['password']){
         	$_SESSION['login_user'] = $username;
			header( "Location: ./dashboard.php" );	
		}
		else{
			//header( "Location: ./index.html" ); die;
			$error = 'Wrong username or password';
		}
	}
	else{
		//header( "Location: ./index.html" ); die;
		$error = 'Wrong username or password';
	}
}
?>
