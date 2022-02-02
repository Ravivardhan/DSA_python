<?php
    $name="Name: Ravi vardhan <br>";
    $register_number="Register number: 1910162"."<br>";
    $age="age :20"."<br>";
    $gender="gender : Male <br>";
    $branch="branch : CSE <br>";
    $year="year : 3"."<br>";
    $semester="semester : 2"."<br>";
    $marks=array("sub1_theory"=>47,"sub2_theory"=>92,"sub3_theory"=>45,"sub4_theory"=>45,"sub5_theory"=>45,"sub6_theory"=>45,"sub7_practical"=>45,"sub8_practical"=>45);

    echo "<h3 style=margin-left:14%;font-size:27px;text-align:left>".$name.$register_number.$age.$gender.$branch.$year.$semester."</h3>";
    

    echo "<table style=width:70%;margin-left:14%; border=\"1\">
    <th height=50px; style=text-align:center;font-size:200%;>Subject</th><th style=text-align:center;font-size:200%;height=50px;>Marks</th>";

    $pass=TRUE;
    $total_marks=0;
    while($element=each($marks))
    {
        $total_marks=$total_marks+$element['value'];

        if($element['value']<35)
        {
            $element['value']='fail';
            $pass=FALSE;
        }
        /*echo $element['key'].'&nbsp&nbsp&nbsp&nbsp'.$element['value']."<br>";*/
        echo "<tr height=50px; ><td style=text-align:center;font-size:200%;>".$element['key']."</td>"."<td style=text-align:center;font-size:200%;>".$element['value']."</td></tr>";
        
    }
    echo "</table>";
    $percentage=($total_marks/800)*100;
    
    if($pass)
    {
        echo "<h1 style=text-align:right;margin-right:20%>"."Total Marks :".$total_marks."</h1>";

        echo "<h1 style=text-align:right;margin-right:18%>"."Percentage :".$percentage."%"."</h1>";

    }
    else{
        echo "<h1 style=text-align:right;margin-right:20%>status :FAIL</h1>";
    }



?>

