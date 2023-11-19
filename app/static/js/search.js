$('#collegeSearch').search({
  apiSettings: {
    url: '/api/college/list',
    method: 'POST',
    cache: false,
    saveRemoteData: false,
    beforeSend: function(settings) {
      var query = $("#collegeInputSearch").val();
      if(query.length > 0){
        console.log(">0");
        settings.data = JSON.stringify({ query: query });
      }else{
        console.log("==0");
        settings.data = JSON.stringify({ query: "" });
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      console.log('response=> '+response);
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
    method: 'POST',
    cache: false,
    saveRemoteData: false,
    beforeSend: function(settings) {
      var query = $("#courseInputSearch").val();
      if(query.length > 0){
        settings.data = JSON.stringify({ query: query });
      }else{
        settings.data = JSON.stringify({ query: "" });
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      console.log('response=> '+response);
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
    method: 'POST',
    cache: false,
    saveRemoteData: false,
    beforeSend: function(settings) {
      var query = $("#studentInputSearch").val();
      if(query.length > 0){
        settings.data = JSON.stringify({ query: query });
      }else{
        settings.data = JSON.stringify({ query: "" });
      }
      settings.contentType = 'application/json';
      return settings;
    },
    onResponse(response) {
      console.log('response=> '+response);
      $('#studentTab').html(response.content);
      $('#studentTabControls').html(response.buttons);
    }
  },
  showNoResults: false,
  searchDelay: 400,
  minCharacters: 0,
});