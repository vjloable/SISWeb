$(document).on('click', '#gotoAddCollege', function() {
  window.location.href = '/college/create';
});

$(document).on('click', '#gotoAddCourse', function() {
  window.location.href = '/course/create';
});

$(document).on('click', '#gotoAddStudent', function() {
  window.location.href = '/student/create';
});

$(document).on('click', '.gotoDeleteCollege', function() {
  var buttonValue = $(this).val();
  let action = 'delete';
  $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a college code of '+buttonValue+'?');
  $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
  $('#iconConfirmationModal').toggleClass('trash alternative');
  $('#confirmationModal')
  .modal({
    closable  : false,
    onDeny    : function(){},
    onApprove : function() {
      var data = {
        'code': buttonValue
      };
      $.ajax({
        type: 'POST',
        url: "/api/college/delete",
        data: JSON.stringify(data),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(response) {
          let content = '';
          let status = '';
          let icon = '';
          if(response.success === false){
            content = response.results;
            status = 'Error!';
            icon = 'times circle outline error red'
          }else{
            content = "Successfully "+action+"d a College named "+buttonValue+".";
            status = 'Success!';
            icon = 'check circle outline green'
          }
          $('#statusAlertModal').text(status);
          $('#contentAlertModal').text(content);
          $("#iconAlertModal").toggleClass(icon);
          $('#row'+buttonValue).remove();
          $('#alertModal')
          .modal({
            closable  : false,
            onDeny    : function(){},
            onApprove : function() {
              var count = $(".cards .card").length;
              console.log(count);
              if(count <= 1){
                window.location.reload();
              }
            }
          })
          .modal('show');
        },
      });
    }
  })
  .modal('show');
});

$(document).on('click', '.gotoDeleteCourse', function() {
  var buttonValue = $(this).val();
  let action = 'delete';
  $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a course code of '+buttonValue+'?');
  $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
  $('#confirmationModal')
  $('#confirmationModal')
  .modal({
    closable  : false,
    onDeny    : function(){},
    onApprove : function() {
      var data = {
        'code': buttonValue
      };
      $.ajax({
        type: 'POST',
        url: "/api/course/delete",
        data: JSON.stringify(data),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(response) {
          let content = '';
          let status = '';
          let icon = '';
          if(response.success === false){
            content = response.results;
            status = 'Error!';
            icon = 'times circle outline error red'
          }else{
            content = "Successfully "+action+"d a Course named "+buttonValue+".";
            status = 'Success!';
            icon = 'check circle outline green'
          }
          $('#statusAlertModal').text(status);
          $('#contentAlertModal').text(content);
          $("#iconAlertModal").toggleClass(icon);
          $('#row'+buttonValue).remove();
          $('#alertModal')
          .modal({
            closable  : false,
            onDeny    : function(){},
            onApprove : function() {
              var count = $(".cards .card").length;
              console.log(count);
              if(count <= 1){
                window.location.reload();
              }
            }
          })
          .modal('show');
        },
      });
    }
  })
  .modal('show');
});

$(document).on('click', '.gotoDeleteStudent', function() {
  var buttonValue = $(this).val();
  let action = 'delete';
  $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a student id of '+buttonValue+'?');
  $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
  $('#iconConfirmationModal').toggleClass('trash alternative');
  $('#confirmationModal')
  .modal({
    closable  : false,
    onDeny    : function(){},
    onApprove : function() {
      var data = {
        'student_id': buttonValue
      };
      $.ajax({
        type: 'POST',
        url: "/api/student/delete",
        data: JSON.stringify(data),
        contentType:"application/json; charset=utf-8",
        dataType:"json",
        success: function(response) {
          let content = '';
          let status = '';
          let icon = '';
          if(response.success === false){
            content = response.results;
            status = 'Error!';
            icon = 'times circle outline error red'
          }else{
            content = "Successfully "+action+"d a Student named "+buttonValue+".";
            status = 'Success!';
            icon = 'check circle outline green'
          }
          $('#statusAlertModal').text(status);
          $('#contentAlertModal').text(content);
          $("#iconAlertModal").toggleClass(icon);
          $('#row'+buttonValue).remove();
          $('#alertModal')
          .modal({
            closable  : false,
            onDeny    : function(){},
            onApprove : function() {
              var count = $(".cards .card").length;
              console.log(count);
              if(count <= 1){
                window.location.reload();
              }
            }
          })
          .modal('show');
        },
      });
    }
  })
  .modal('show');
});

$(document).on('click', '.gotoEditCollege', function() {
  var buttonValue = $(this).val();
  var data = {
    'code': buttonValue
  };
  $.ajax({
    type: 'GET',
    url: "/api/college/read",
    data: data,
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      results = (response.results+"").split(",");
      college_code = results[0];
      college_name = results[1];
      window.location.href = "/college/update?code="+college_code+"&name="+college_name;
    },
  });
});

$(document).on('click', '.gotoEditCourse', function() {
  var buttonValue = $(this).val();
  var data = {
    'code': buttonValue
  };
  $.ajax({
    type: 'GET',
    url: "/api/course/read",
    data: data,
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      results = (response.results+"").split(",");
      course_code = results[0];
      course_name = results[1];
      college_code = results[2];
      window.location.href = "/course/update?code="+course_code+"&name="+course_name+"&college="+college_code;
    },
  });
});

$(document).on('click', '.gotoEditStudent', function() {
  var buttonValue = $(this).val();
  var data = {
    'student_id': buttonValue
  };
  $.ajax({
    type: 'GET',
    url: "/api/student/read",
    data: data,
    contentType:"application/json; charset=utf-8",
    dataType:"json",
    success: function(response) {
      results = (response.results+"").split(",");
      student_id = results[0]; 
      firstname = results[1];
      lastname = results[2];
      course = results[3];
      year = results[4];
      gender = results[5];
      window.location.href = "/student/update?student_id="+student_id+"&firstname="+firstname+"&lastname="+lastname+"&course="+course+"&year="+year+"&gender="+gender;
    },
  });
});

$(document).on('click', '.cancel-button', function() {
  window.location.href = '/';
});