<?php
include('config.php');

$username=$_POST['username'];
$password=$_POST['password'];
$username=mysqli_real_escape_string($con, $username);
$password=mysqli_real_escape_string($con, $password);

$error ='';
$sql="select * from GUNSHOT";
$result = mysqli_query($con, $sql);
$latarr = array();
$longarr = array();
while ($row = mysqli_fetch_array($result)){
	array_push($latarr, $row['LAT']);
	array_push($longarr, $row['LONG']);
}

$latlongArray = array();
array_push($latlongArray, $latarr);
array_push($latlongArray, $longarr);

echo json_encode($latlongArray);

?>
