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

$('#signup-form').submit(function(e){
  e.preventDefault();
  var data = $(this).serialize();
  $.ajax({
    type: "POST",
    url: "{% url 'userSignUpAPI' %}",
    data: data,
    dataType: "json",
    success: function(data) {
      $("#new-registrated-user").val(data.email);
      $("#signup-form").hide();
      $("#successfull-signup").show();
    },
    error: function() {
        alert('ERR By SUBMITTING signup');
    }
  });
})

$('#pwforgotten-form').submit(function(e){
  e.preventDefault();
  var data = $(this).serialize();
  $.ajax({
    type: "POST",
    url: "{% url 'userKeysCreateKeyAPI' %}",
    data: data,
    dataType: "json",
    success: function(data) {
      $('#pw-reset-sended').show()
      $('#pwforgotten-form').hide()
    },
    error: function() {
        alert('ERR By SUBMITTING signup');
    }
  });
})

$('#resend-activation').click(function(){
  var data = $('#resend-key-form').serialize();
  $.ajax({
    type: "POST",
    url: "{% url 'userKeysCreateKeyAPI' %}",
    data: data,
    dataType: "json",
    success: function(data) {},
    error: function() {
        alert('ERR By SUBMITTING signup');
    }
  });
})

$('#signup-email').blur(function(){
  if (validateEmail($(this).val())){
    var url = `{% url 'userUserIsTakenAPI' %}?email=${$(this).val()}`
    $.ajax({
      type: "GET",
      url: url,
      success: function(data) {
        if (data.user_is_taken) $('#signup-email-warning').text('Email is already taken.');
        else $('#signup-email-warning').text('');
      },
      error: function() {
          alert('ERR By SUBMITTING RETRIEVE USER');
      }
    });
  }
  else {
    $('#signup-email-warning').text('Please use a valid Email.');
  }
})

$('#pwforgotten-email').blur(function(){
  if (validateEmail($(this).val())){
    $('#pwforgotten-email-warning').text('');
  }
  else {
    $('#pwforgotten-email-warning').text('Please use a valid Email.');
  }
})
