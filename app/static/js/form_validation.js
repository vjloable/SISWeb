$('.coupled.modal')
  .modal({
    allowMultiple: false
  })
;


function previewImage(event, category) {
  var output = document.getElementById('imagePreview' + category);
  const ALLOWED_EXTENSIONS = ["image/jpg", "image/jpeg", "image/png", "image/gif"];
  const ALLOWED_SIZE = 1000000;
  try {
    var file = event.target.files[0];
    if (ALLOWED_EXTENSIONS.includes(file.type)) {
      if (ALLOWED_SIZE >= file.size) {
        output.src = URL.createObjectURL(file);
        output.onload = function () {
          URL.revokeObjectURL(output.src);
          $('#imagePreview' + category).removeClass('hidden');
        }
      } else {
        var status = "Warning!";
        var content = "The submitted image exceeds 1MB file size limit. Please select another image.";
        var icon = "exclamation triangle yellow";
        $('#statusAlertModal').text(status);
        $('#contentAlertModal').text(content);
        $("#iconAlertModal").toggleClass(icon);
        $('#alertModal').modal({
          closable: false,
          onDeny: function () { },
          onApprove: function () { }
        }).modal('show');  
      }
    } else {
      var status = "Warning!";
      var content = "The file input is not supported, please provide images with jpg, jpeg, png, and gif extensions only.";
      var icon = "exclamation triangle yellow";
      $('#statusAlertModal').text(status);
      $('#contentAlertModal').text(content);
      $("#iconAlertModal").toggleClass(icon);
      $('#alertModal').modal({
        closable: false,
        onDeny: function () { },
        onApprove: function () { }
      }).modal('show');
    }
  }
  catch (err) {
    console.log("No image selected.");
  }

};

function removeImage(category) {
  var output = document.getElementById('imagePreview' + category);
  output.src = "";
};

function uploadImage(action, category) {
  var formData = new FormData($('#' + action + category + 'Form')[0]);
  try {
    return $.ajax({
      type: "POST",
      url: '../api/' + String(category).toLowerCase() + '/image_upload',
      data: formData,
      processData: false,
      contentType: false,
      cache: false,
      beforeSend: function () {
        $("#yesConfirmButton").toggleClass("loading disabled");
        $("#noConfirmButton").toggleClass("disabled");
      },
      success: function (response) {
        console.log("success");
        return { "loading": false, "url": response.url };
      },
      complete: function () {
        $("#yesConfirmButton").toggleClass("loading disabled");
        $("#noConfirmButton").toggleClass("disabled");
      }
    });
  }
  catch (err) {
    console.log("No image selected.");
  }
}

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
    let action = 'add';
    var allFields = $('#addCollegeForm').form('get values');
    $('#headerConfirmationModal').text('Are you sure you want to ' + action + ' a record with a college code of ' + allFields['code'] + '?');
    $('#contentConfirmationModal').text('By confirming to ' + action + ', any changes made are permanent and irreversible. Hit Yes if you are sure to ' + action + ' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable: false,
      onDeny: function () { },
      onApprove: function () {
        var data = {
          "code": allFields['code'],
          "name": allFields['name'],
        };
        $.ajax({
          url: "/api/college/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The college code '" + data['code'] + "' is already taken. \nTry another college code again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              content = "Successfully created a College named " + data["name"] + ".";
              status = 'Success!';
              icon = 'check circle outline green'
              uploadImage(action, "College")
                .then((uploadResponse) => {
                  var data = {
                    "code": allFields['code'],
                    "url": uploadResponse.url
                  }
                  
                  if (uploadResponse.url == "") {
                    content += "\nWith no image was uploaded.";
                  } else {
                    $.ajax({
                      type: "POST",
                      url: '../api/college/image_url_set',
                      data: JSON.stringify(data),
                      contentType: "application/json; charset=utf-8",
                      dataType: "json"
                    });
                    content += "\nWhile successfully uploaded the image.";
                  }

                  $('#statusAlertModal').text(status);
                  $('#contentAlertModal').text(content);
                  $("#iconAlertModal").toggleClass(icon);
                  $('#alertModal').modal({
                    closable: false,
                    onDeny: function () { },
                    onApprove: function () {
                      window.location.href = '/';
                    }
                  }).modal('show');
                  return false;
                });
            }
          }
        })
        return false;
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
    let action = 'add';
    var allFields = $('#addCourseForm').form('get values'); 
    $('#headerConfirmationModal').text('Are you sure you want to ' + action + ' a record with a course code of ' + allFields['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        var data = {
          "code": allFields['code'],
          "name": allFields['name'],
          "college": allFields['college'],
        }
        $.ajax({
          url: "/api/course/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The course code '" + data['code'] + "' is already taken. \nTry another course code again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              content = "Successfully created a Course named " + data["name"] + ".";
              status = 'Success!';
              icon = 'check circle outline green'
              uploadImage(action, "Course")
                .then((uploadResponse) => {
                  var data = {
                    "code": allFields['code'],
                    "url": uploadResponse.url
                  }

                  if (uploadResponse.url == "") {
                    content += "\nWith no image was uploaded.";
                  } else {
                    $.ajax({
                      type: "POST",
                      url: '../api/course/image_url_set',
                      data: JSON.stringify(data),
                      contentType: "application/json; charset=utf-8",
                      dataType: "json"
                    });
                    content += "\nWhile successfully uploaded the image.";
                  }

                  $('#statusAlertModal').text(status);
                  $('#contentAlertModal').text(content);
                  $("#iconAlertModal").toggleClass(icon);
                  $('#alertModal').modal({
                    closable: false,
                    onDeny: function () { },
                    onApprove: function () {
                      window.location.href = '/';
                    }
                  }).modal('show');
                  return false;
                });
            }
          }
        })
        return false;
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
    let action = 'add';
    var allFields = $('#addStudentForm').form('get values');
    $('#headerConfirmationModal').text('Are you sure you want to ' + action + ' a record with a student id of ' + allFields['student_id']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove: function () {
        var data = {
          "student_id": (allFields['student_id']),
          "firstname": allFields['firstname'],
          "lastname": allFields['lastname'],
          "course": allFields['course'],
          "year": allFields['year'],
          "gender": allFields['gender'],
          "img_url": ""
        };
        $.ajax({
          url: "/api/student/create",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The student code '" + data['student_id'] + "' is already taken. \nTry another student id again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              content = "Successfully created a Student named " + data["firstname"] + " " + data["lastname"] + ".";
              status = 'Success!';
              icon = 'check circle outline green'
              uploadImage(action, "Student")
                .then((uploadResponse) => {
                  var data = {
                    "student_id": allFields['student_id'],
                    "url": uploadResponse.url
                  }

                  if (uploadResponse.url == "") {
                    content += "\nWith no image was uploaded.";
                  } else {
                    $.ajax({
                      type: "POST",
                      url: '../api/student/image_url_set',
                      data: JSON.stringify(data),
                      contentType: "application/json; charset=utf-8",
                      dataType: "json"
                    });
                    content += "\nWhile successfully uploaded the image.";
                  }

                  $('#statusAlertModal').text(status);
                  $('#contentAlertModal').text(content);
                  $("#iconAlertModal").toggleClass(icon);
                  $('#alertModal').modal({
                    closable: false,
                    onDeny: function () { },
                    onApprove: function () {
                      window.location.href = '/';
                    }
                  }).modal('show');
                  return false;
                });
            }
          }
        })
        return false;
      }
    })
    .modal('show');
    return false;
  }
});

$('#editCollegeForm').form('set values', {
  code: new URL(window.location.href).searchParams.get("code"),
  name: new URL(window.location.href).searchParams.get("name"),
  // img_url: new URL(window.location.href).searchParams.get("img_url"),  
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
    let action = 'edit';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a college code of '+ allFields['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        var data = {
          "code": new URL(window.location.href).searchParams.get("code"),
          "new_code": allFields['code'],
          "new_name": allFields['name'],
        };
        $("#yesConfirmButton").toggleClass("loading disabled");
        $("#noConfirmButton").toggleClass("disabled");
        $.ajax({
          url: "/api/college/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The college code '" + data['code'] + "' is already taken. \nTry another college code again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              var previousImage = $('#imagePreviewCollege').attr('src');
              content = "Successfully " + action + "ed a College named " + allFields['name'] + ".";
              status = 'Success!';
              icon = 'check circle outline green';
              if (previousImage.slice(0, 4) == "blob") {
                // - delete the original
                var data = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/college/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                // - upload new image
                  $("#yesConfirmButton").toggleClass("loading disabled");
                  $("#noConfirmButton").toggleClass("disabled");
                  uploadImage(action, "College")
                    .then((uploadResponse) => {
                      var data = {
                        "code": allFields['code'],
                        "url": uploadResponse.url
                      }
                      // - set the new image url
                      $.ajax({
                        type: "POST",
                        url: '../api/college/image_url_set',
                        data: JSON.stringify(data),
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        complete: function () {
                          $("#yesConfirmButton").toggleClass("loading disabled");
                          $("#noConfirmButton").toggleClass("disabled");
                          $('#statusAlertModal').text(status);
                          $('#contentAlertModal').text(content);
                          $("#iconAlertModal").toggleClass(icon);
                          $('#alertModal').modal({
                            closable: false,
                            onDeny: function () { },
                            onApprove: function () {
                              window.location.href = '/';
                            }
                          }).modal('show');
                          return false;
                        }
                      });
                    });
                }); 
              } else if (previousImage == "") {
                content = "Successfully " + action + "ed a College named " + allFields['name'] + ".";
                status = 'Success!';
                icon = 'check circle outline green'
                // - delete the original
                var data = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/college/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                  // - set the new image url
                  var data = {
                    "code": allFields['code'],
                    "url": ""
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/college/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              } else {
                var data_rename = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                  "new_code": allFields['code'],
                }
                $.ajax({
                  type: "POST",
                  url: '../api/college/image_rename',
                  data: JSON.stringify(data_rename),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json"
                }).done((response) => {
                  var data = {
                    "code": allFields['code'],
                    "url": response.url
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/college/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              }
            }
          }
        })
        return false;
      }
    })
    .modal('show');
    return false;
  }
});

$('#editCourseForm').form('set values', {
  code: new URL(window.location.href).searchParams.get("code"),
  name: new URL(window.location.href).searchParams.get("name")
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
    let action = 'edit';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a course code of '+ allFields['code']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        var data = {
          "code": new URL(window.location.href).searchParams.get("code"),
          "new_code": allFields['code'],
          "new_name": allFields['name'],
          "new_college": allFields['college'],
        };
        $("#yesConfirmButton").toggleClass("loading disabled");
        $("#noConfirmButton").toggleClass("disabled");
        $.ajax({
          url: "/api/course/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The course code '" + data['code'] + "' is already taken. \nTry another course code again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              var previousImage = $('#imagePreviewCourse').attr('src');
              content = "Successfully " + action + "ed a Course named " + allFields['name'] + ".";
              status = 'Success!';
              icon = 'check circle outline green';
              if (previousImage.slice(0, 4) == "blob") {
                // - delete the original
                var data = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/course/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                  // - upload new image
                  $("#yesConfirmButton").toggleClass("loading disabled");
                  $("#noConfirmButton").toggleClass("disabled");
                  uploadImage(action, "Course")
                    .then((uploadResponse) => {
                      var data = {
                        "code": allFields['code'],
                        "url": uploadResponse.url
                      }
                      // - set the new image url
                      $.ajax({
                        type: "POST",
                        url: '../api/course/image_url_set',
                        data: JSON.stringify(data),
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        complete: function () {
                          $("#yesConfirmButton").toggleClass("loading disabled");
                          $("#noConfirmButton").toggleClass("disabled");
                          $('#statusAlertModal').text(status);
                          $('#contentAlertModal').text(content);
                          $("#iconAlertModal").toggleClass(icon);
                          $('#alertModal').modal({
                            closable: false,
                            onDeny: function () { },
                            onApprove: function () {
                              window.location.href = '/';
                            }
                          }).modal('show');
                          return false;
                        }
                      });
                    });
                });
              } else if (previousImage == "") {
                content = "Successfully " + action + "ed a Course named " + allFields['name'] + ".";
                status = 'Success!';
                icon = 'check circle outline green'
                // - delete the original
                var data = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/course/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                  // - set the new image url
                  var data = {
                    "code": allFields['code'],
                    "url": ""
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/course/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              } else {
                var data_rename = {
                  "code": new URL(window.location.href).searchParams.get("code"),
                  "new_code": allFields['code'],
                }
                $.ajax({
                  type: "POST",
                  url: '../api/course/image_rename',
                  data: JSON.stringify(data_rename),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json"
                }).done((response) => {
                  var data = {
                    "code": allFields['code'],
                    "url": response.url
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/course/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              }
            }
          }
        })
        return false;
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
  // img_url: new URL(window.location.href).searchParams.get("img_url")
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
    let action = 'edit';
    $('#headerConfirmationModal').text('Are you sure you want to '+action+' a record with a student id of '+allFields['student_id']+'?');
    $('#contentConfirmationModal').text('By confirming to '+action+', any changes made are permanent and irreversible. Hit Yes if you are sure to '+action+' and No if not.');
    $('#iconConfirmationModal').toggleClass('question circle outline');
    $('#confirmationModal')
    .modal({
      closable  : false,
      onDeny    : function(){},
      onApprove : function() {
        var data = {
          "student_id": new URL(window.location.href).searchParams.get("student_id"),
          "new_student_id": (allFields['student_id']),
          "new_firstname": allFields['firstname'],
          "new_lastname": allFields['lastname'],
          "new_course": allFields['course'],
          "new_year": allFields['year'],
          "new_gender": allFields['gender']
        };
        $("#yesConfirmButton").toggleClass("loading disabled");
        $("#noConfirmButton").toggleClass("disabled");
        $.ajax({
          url: "/api/student/update",
          type: "POST",
          data: JSON.stringify(data),
          contentType: "application/json; charset=utf-8",
          dataType: "json",
          success: function (response) {
            let content = '';
            let status = '';
            let icon = '';
            if (response.success === false) {
              var results = response.results;
              content = "There is something wrong with the input data in the form.";
              if (results.indexOf("Duplicate") !== -1) {
                content = "The student id '" + data['student_id'] + "' is already taken. \nTry another student id again.";
              }
              status = 'Error!';
              icon = 'times circle outline error red'
              $('#statusAlertModal').text(status);
              $('#contentAlertModal').text(content);
              $("#iconAlertModal").toggleClass(icon);
              $('#alertModal').modal({
                closable: false,
                onDeny: function () { },
                onApprove: function () {
                  window.location.href = '/';
                }
              }).modal('show');
              return false;
            } else {
              var previousImage = $('#imagePreviewStudent').attr('src');
              content = "Successfully " + action + "ed a Student named " + allFields["firstname"] + " " + allFields["lastname"] + ".";
              status = 'Success!';
              icon = 'check circle outline green';
              if (previousImage.slice(0, 4) == "blob") {
                // - delete the original
                var data = {
                  "student_id": new URL(window.location.href).searchParams.get("student_id"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/student/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                  // - upload new image
                  $("#yesConfirmButton").toggleClass("loading disabled");
                  $("#noConfirmButton").toggleClass("disabled");
                  uploadImage(action, "Student")
                    .then((uploadResponse) => {
                      var data = {
                        "student_id": allFields['student_id'],
                        "url": uploadResponse.url
                      }
                      // - set the new image url
                      $.ajax({
                        type: "POST",
                        url: '../api/student/image_url_set',
                        data: JSON.stringify(data),
                        contentType: "application/json; charset=utf-8",
                        dataType: "json",
                        complete: function () {
                          $("#yesConfirmButton").toggleClass("loading disabled");
                          $("#noConfirmButton").toggleClass("disabled");
                          $('#statusAlertModal').text(status);
                          $('#contentAlertModal').text(content);
                          $("#iconAlertModal").toggleClass(icon);
                          $('#alertModal').modal({
                            closable: false,
                            onDeny: function () { },
                            onApprove: function () {
                              window.location.href = '/';
                            }
                          }).modal('show');
                          return false;
                        }
                      });
                    });
                });
              } else if (previousImage == "") {
                content = "Successfully " + action + "ed a Student named " + allFields["firstname"] + " " + allFields["lastname"] + ".";
                status = 'Success!';
                icon = 'check circle outline green'
                // - delete the original
                var data = {
                  "student_id": new URL(window.location.href).searchParams.get("student_id"),
                }
                $.ajax({
                  type: 'POST',
                  url: "/api/student/image_destroy",
                  data: JSON.stringify(data),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json",
                }).done(() => {
                  // - set the new image url
                  var data = {
                    "student_id": allFields['student_id'],
                    "url": ""
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/student/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              } else {
                var data_rename = {
                  "new_student_id": allFields['student_id'],
                  "student_id": new URL(window.location.href).searchParams.get("student_id")
                }
                $.ajax({
                  type: "POST",
                  url: '../api/student/image_rename',
                  data: JSON.stringify(data_rename),
                  contentType: "application/json; charset=utf-8",
                  dataType: "json"
                }).done((response) => {
                  var data = {
                    "student_id": allFields['student_id'],
                    "url": response.url
                  }
                  $.ajax({
                    type: "POST",
                    url: '../api/student/image_url_set',
                    data: JSON.stringify(data),
                    contentType: "application/json; charset=utf-8",
                    dataType: "json",
                    complete: function () {
                      $("#yesConfirmButton").toggleClass("loading disabled");
                      $("#noConfirmButton").toggleClass("disabled");
                      $('#statusAlertModal').text(status);
                      $('#contentAlertModal').text(content);
                      $("#iconAlertModal").toggleClass(icon);
                      $('#alertModal').modal({
                        closable: false,
                        onDeny: function () { },
                        onApprove: function () {
                          window.location.href = '/';
                        }
                      }).modal('show');
                      return false;
                    }
                  });
                });
              }
            }
          }
        })
        return false;
      }
    })
    .modal('show');
    return false;
  }
});

$('#mockFileCollegeButton').on('click', function () {
  $('#realInputCollegeButton').trigger('click');
});

$('#mockFileCourseButton').on('click', function () {
  $('#realInputCourseButton').trigger('click');
});

$('#mockFileStudentButton').on('click', function () {
  $('#realInputStudentButton').trigger('click');
});