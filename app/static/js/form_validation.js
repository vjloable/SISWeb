$('.coupled.modal')
  .modal({
    allowMultiple: false
  })
;

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
    let action = 'add';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/college/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully created a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
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
    let action = 'add';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/course/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully created a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
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
    let action = 'add';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data['student_id']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/student/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully created a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
    return false;
  }
});

$('#editCollegeForm').form('set values', {
  code: new URL(window.location.href).searchParams.get("code"),
  name: new URL(window.location.href).searchParams.get("name")
})

$('#editCollegeForm').form({
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
    var allFields = $('#editCollegeForm').form('get values');
    var data = {
      "code": new URL(window.location.href).searchParams.get("code"), 
      "new_code": allFields['code'], 
      "new_name": allFields['name']
    }
    let action = 'edit';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/college/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully created a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
    return false;
  }
});

$('#editCourseForm').form('set values', {
  code: new URL(window.location.href).searchParams.get("code"),
  name: new URL(window.location.href).searchParams.get("name"),
})

$('#editCourseForm').form({
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
    var allFields = $('#editCourseForm').form('get values');
    var data = {
      "code": new URL(window.location.href).searchParams.get("code"), 
      "new_code": allFields['code'], 
      "new_name": allFields['name'],
      "new_college": allFields['college'],
    }
    let action = 'edit';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data["new_code"]+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/course/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully "+action+"ed a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
    return false;
  }
});

$('#editStudentForm').form('set values', {
  student_id: new URL(window.location.href).searchParams.get("student_id"),
  firstname: new URL(window.location.href).searchParams.get("firstname"),
  lastname: new URL(window.location.href).searchParams.get("lastname"),
  course: new URL(window.location.href).searchParams.get("course"),
  year: new URL(window.location.href).searchParams.get("year"),
  gender: new URL(window.location.href).searchParams.get("gender"),
})

$('#editStudentForm').form({
  fields: {
    student_id: {
      identifier: 'student_id',
      rules: [
        {
          type: 'regExp[/^[0-9]{4}-[0-9]{4}$/]',
          prompt: 'Please enter your new student ID (ex: 2020-1234)'
        }
      ]
    },
    firstname: {
      identifier: 'firstname',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your new first name'
        }
      ]
    },
    lastname: {
      identifier: 'lastname',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your new last name'
        }
      ]
    },
    course: {
      identifier: 'course',
      rules: [
        {
          type   : 'empty',
          prompt : 'Please enter your new course ID (ex: BSCS)'
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
    var allFields = $('#editStudentForm').form('get values');
    var data = {
      "student_id": new URL(window.location.href).searchParams.get("student_id"),  
      "new_student_id": (allFields['student_id']), 
      "new_firstname": allFields['firstname'],
      "new_lastname": allFields['lastname'],
      "new_course": allFields['course'], 
      "new_year": allFields['year'],
      "new_gender": allFields['gender']
    };
    let action = 'add';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+'name a record with a college code of '+data['student_id']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        $.ajax({
          url: "/api/student/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType:"application/json; charset=utf-8",
          dataType:"json",
          success: function(response){
            let content = '';
            let status = '';
            let icon = '';
            if(response.success === false){
              content = response.results;
              status = 'Error!';
              icon = 'times circle outline error red'
            }else{
              content = "Successfully created a College named "+data["name"]+".";
              status = 'Success!';
              icon = 'check circle outline green'
            }
            $('#statusAlertModal').text(status);
            $('#contentAlertModal').text(content);
            $("#iconAlertModal").toggleClass(icon);
            $('#alertModal')
            .modal({
              closable  : false,
              onDeny    : function(){},
              onApprove : function() {
                window.location.href = '/';
              }
            })
            .modal('show');
          }
        })
      }
    })
    .modal('show');
    return false;
  }
});

function uploadImage() {
  var formData = new FormData($('#uploadForm')[0]);

  $.ajax({
    url: '/upload',
    type: 'POST',
    data: formData,
    contentType: false,
    processData: false,
    beforeSend: function() {
      $("#loadingText").text("Loading");
    },
    success: function(response) {
      $("#loadingText").text("Succes");
      alert(response);
    },
    error: function(error) {
      console.error('Error uploading image:', error);
    }
  });
}