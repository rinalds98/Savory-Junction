// This function provides a custom datepicker for reservations.
$( function() {
    $( "#datepicker" ).datepicker();
  } );

// This function sets a timer for alerts so they don't
// stay on the screen forever.
setTimeout(function(){
  let messages = document.getElementById("msg");
  let alert = new bootstrap.Alert(messages);
  alert.close();
},3000);
