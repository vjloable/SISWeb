$(document).on('click', '#gotoAddCollege', function() {
  window.location.href = '/college/create';
});

$(document).on('click', '#gotoAddCourse', function() {
  window.location.href = '/course/create';
});

$(document).on('click', '#gotoAddStudent', function() {
  window.location.href = '/student/create';
});

$(document).on('click', '#gotoDeleteCollege', function() {
  var buttonValue = $(this).attr('value');
  var data = {
    'code': buttonValue
  };
  $.ajax({
    type: 'POST',
    url: "/api/college/delete",
    type: "POST",
    data: JSON.stringify(data),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      window.location.reload();
    },
  });
});

$(document).on('click', '#gotoDeleteCourse', function() {
  var buttonValue = $(this).attr('value');
  var data = {
    'code': buttonValue
  };
  $.ajax({
    type: 'POST',
    url: "/api/course/delete",
    type: "POST",
    data: JSON.stringify(data),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      window.location.reload();
    },
  });
});

$(document).on('click', '#gotoDeleteStudent', function() {
  var buttonValue = $(this).attr('value');
  var data = {
    'student_id': buttonValue
  };
  $.ajax({
    type: 'POST',
    url: "/api/student/delete",
    type: "POST",
    data: JSON.stringify(data),
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      window.location.reload();
    },
  });
});

$(document).on('click', '.cancel-button', function() {
  window.location.href = '/';
});