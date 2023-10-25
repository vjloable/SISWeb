// Form Validator Script
$('#addStudentForm').form({
  fields: {
    student_id: {
      identifier: 'student_id',
      rules: [
        {
          type: 'regExp[/^[0-9]{4}-[0-9]{4}$/]',
          prompt: 'Please enter your student ID (ex: 2020-1234)'
        }
      ]
    },
    firstname: {
      identifier: 'firstname',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your first name'
        }
      ]
    },
    lastname: {
      identifier: 'lastname',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your last name'
        }
      ]
    },
    course_id: {
      identifier: 'course_id',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your course ID (ex: BSCS)'
        }
      ]
    },
    year: {
      identifier: 'year',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your current year level'
        }
      ]
    },
    gender: {
      identifier: 'gender',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your gender'
        }
      ]
    },
  },
  onSuccess: function () {
    // Handle form submission if the input is valid.
    $(this).closest('.ui.modal').modal('hide');
    return false;
  }
});