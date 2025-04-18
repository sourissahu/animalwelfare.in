<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
  $name = $_POST["name"];
  $email = $_POST["email"];
  $message = $_POST["message"];

  $to = "animalwelfare4iith@gmail.com";
  $subject = "New Contact Form Message";
  $body = "From: $name\nEmail: $email\n\n$message";

  mail($to, $subject, $body);
  header("Location: thankyou.html");
}
echo "PHP is working!";
?>
