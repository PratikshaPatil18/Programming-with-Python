<?php
//constructor
class constructor{
	public $name;
    public $age;
function __construct($n,$a){
	echo"from constructor block <br>";
	$this->name=$n;
	$this->age=$a;
}
function info()
{
	echo"Name :".$this->name."<br> Age :".$this->age;
}
}
$obj=new constructor("chetan",20);
$obj->info();

?>