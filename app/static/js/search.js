$('#collegeSearch').search({
  apiSettings: {
    url: '/api/college/list',
    method: 'GET',
    cache: false,
    saveRemoteData: false,
    beforeSend: function(settings) {
      var query = $("#collegeInputSearch").val();
      if(query.length > 0){
        settings.data = { query: query, page: 1 };
      }else{
        settings.data = { query: "", page: 1 };
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      $('#collegeTab').html(response.content);
      $('#collegeTabControls').html(response.buttons);  
    }
  },
  showNoResults: false,
  searchDelay: 400,
  minCharacters: 0,
});

$('#courseSearch').search({
  apiSettings: {
    url: '/api/course/list',
    method: 'GET',
    cache: false,
    saveRemoteData: false,
    beforeSend: function(settings) {
      var query = $("#courseInputSearch").val();
      if(query.length > 0){
        settings.data = { query: query, page: 1 };
      }else{
        settings.data = { query: "", page: 1 };
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      $('#courseTab').html(response.content);
      $('#courseTabControls').html(response.buttons);
    }
  },
  showNoResults: false,
  searchDelay: 400,
  minCharacters: 0,
});

$('#studentSearch').search({
  apiSettings: {
    url: '/api/student/list',
    method: 'GET',
    cache: false,
    saveRemoteData: false,
    beforeSend: function (settings) {
      var query = $("#studentInputSearch").val();
      if (query.length > 0) {
        settings.data = { query: query, page: 1 };
      } else {
        settings.data = { query: "", page: 1 };
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      $('#studentTab').html(response.content);
      $('#studentTabControls').html(response.buttons);
    }
  },
  showNoResults: false,
  searchDelay: 400,
  minCharacters: 0,
});