$('#addCollegeForm').form({
  fields: {
    code: {
      identifier: 'code',
      rules: [
        {
          type: 'empty',
          prompt: 'Please enter the college code'
        }
      ]
    },
    name: {
      identifier: 'name',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter a college name'
        }
      ]
    },
  },
  onSuccess: function () {
    var allFields = $('#addCollegeForm').form('get values');
    var data = {
        "code": allFields['code'], 
        "name": allFields['name']
      }
    $.ajax({
      url: "/api/college/create",
      type: "POST",
      data: JSON.stringify(data),
      contentType:"application/json; charset=utf-8",
      dataType:"json",
      success: function(){
        window.location.href = '/';
      }
    })

    return false;
  }
});

$('#addCourseForm').form({
  fields: {
    code: {
      identifier: 'code',
      rules: [
        {
          type: 'empty',
          prompt: 'Please enter the course code'
        }
      ]
    },
    name: {
      identifier: 'name',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter a course name'
        }
      ]
    },
    college: {
      identifier: 'college',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter the college for this course'
        }
      ]
    },
  },
  onSuccess: function () {
    var allFields = $('#addCourseForm').form('get values');
    var data = {
        "code": allFields['code'], 
        "name": allFields['name'],
        "college": allFields['college'],
      }
    $.ajax({
      url: "/api/course/create",
      type: "POST",
      data: JSON.stringify(data),
      contentType:"application/json; charset=utf-8",
      dataType:"json",
      success: function(){
        window.location.href = '/';
      }
    })

    return false;
  }
});

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
    course: {
      identifier: 'course',
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
    var allFields = $('#addStudentForm').form('get values');
    var data = {
        "student_id": (allFields['student_id']), 
        "firstname": allFields['firstname'],
        "lastname": allFields['lastname'],
        "course": allFields['course'], 
        "year": allFields['year'],
        "gender": allFields['gender']
      };
    $.ajax({
      url: "/api/student/create",
      type: "POST",
      data: JSON.stringify(data),
      contentType:"application/json; charset=utf-8",
      dataType:"json",
      success: function(){
        window.location.href = '/';
      }
    })

    return false;
  }
});