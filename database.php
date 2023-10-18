<?php
$servername = "34.133.205.100";
$username = "root";
$password = "AITteam@123";
//$database="point";

// Create connection
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>