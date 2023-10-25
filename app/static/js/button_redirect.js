$(document).on('click', '#showAddCollegeModal', function() {
  window.location.href = '/college/create';
});

$(document).on('click', '#showAddCourseModal', function() {
  window.location.href = '/course/create';
});

$(document).on('click', '#showAddStudentModal', function() {
  window.location.href = '/student/create';
});

$(document).on('click', '.cancel-button', function() {
  window.location.href = '/';
});