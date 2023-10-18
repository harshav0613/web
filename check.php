<?php
require "db.php";
$tag_num = isset($_GET['tag']) ? $_GET['tag'] : 0;
$status="";
$sql="SELECT * FROM tags WHERE tag_num=$tag_num;";
$result = $conn->query($sql);
$names=array();
if ($result->num_rows > 0) {

 $status="sucess";
 echo json_encode(['status'=>$status]);
}
else
{
    $status="invalid";
    echo json_encode(['status'=>$status]);
}
?>