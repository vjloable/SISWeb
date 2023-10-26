$(document).on('click', '#gotoAddCollege', function() {
  window.location.href = '/college/create';
});

$(document).on('click', '#gotoAddCourse', function() {
  window.location.href = '/course/create';
});

$(document).on('click', '#gotoAddStudent', function() {
  window.location.href = '/student/create';
});

$(document).on('click', '.cancel-button', function() {
  window.location.href = '/';
});