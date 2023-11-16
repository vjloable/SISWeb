$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: '/api/college/list',
    beforeSend: function() {
      $('#collegeTab').html('<div class="ui indeterminate text loader">Fetching data</div>');
    },
    success: function (results) {
      $('#collegeTab').html(results.content);
      $('#collegeTabControls').html(results.buttons);
    },
    error: function (error) {
      console.log('Error:', error);
    }
  });
  
});


$('.menu .item').tab({
  onVisible: function() {
    var activeTab = $('.tab.segment.active');
    var activeTabName = activeTab.attr('data-tab');
    
    $.ajax({
      type: 'GET',
      url: '/api/'+activeTabName+'/list',
      beforeSend: function() {
        $('#'+activeTabName+'Tab').html('<div class="ui indeterminate text loader">Fetching data</div>');
      },
      success: function (results) {
        $('#'+activeTabName+'Tab').html(results.content);
        $('#'+activeTabName+'TabControls').html(results.buttons);
      },
      error: function (error) {
        console.log('Error:', error);
      }
    });
  },
});