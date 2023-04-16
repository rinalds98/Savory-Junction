// This function provides a custom datepicker for reservations.
// This function was taken from https://jqueryui.com/datepicker/
$( function() {
    $( "#datepicker" ).datepicker();
  } );

// This function sets a timer for alerts so they don't
// stay on the screen forever.
setTimeout(function(){
  let messages = document.getElementById("msg");
  console.log(messages)
  let alert = new bootstrap.Alert(messages);
  console.log(alert)
  alert.close();
},3000);