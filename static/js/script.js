// This function provides a custom datepicker for reservations.
// This function was taken from https://jqueryui.com/datepicker/
$( function() {
  $( "#datepicker" ).datepicker();
} );

// This function sets a timer for alerts so they don't
// stay on the screen forever.
setTimeout(function(){
let messages = document.getElementById("msg");
let alert = new alert(messages);
alert.close();
},3000);