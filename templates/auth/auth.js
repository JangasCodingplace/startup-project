$('#auth').click(function(){
  $( "#auth-sidebar").toggle("slow", function(){});

  $('#main').removeClass(['col-md-12', 'col-xl-12']);
  $('#main').addClass(['col-md-8', 'col-xl-8']);
});

$('a[name="signup-switch"]').click(function(){
  $( "#signin-form").hide();
  $("#pwforgotten-form").hide();
  $( "#signup-form").show();
})
$('a[name="signin-switch"]').click(function(){
  $("#signup-form").hide();
  $("#pwforgotten-form").hide();
  $("#signin-form").show();
})
$('a[name="pwforgotten-switch"]').click(function(){
  $( "#signup-form").hide();
  $( "#signin-form").hide();
  $("#pwforgotten-form").show();
})

$('h3[name="close-auth"]').click(function(){
  $( "#auth-sidebar").toggle("slow", function(){
    $('#main').removeClass(['col-md-8', 'col-xl-8']);
    $('#main').addClass(['col-md-12', 'col-xl-12']);
  });
})