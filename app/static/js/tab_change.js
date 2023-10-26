$(document).ready(function () {
  var activeTabName = 'tabColleges';
  $.ajax({
    type: 'GET',
    url: '/api/'+activeTabName,
    beforeSend: function() {
      $('#'+activeTabName).html('<div class="ui indeterminate text loader">Fetching data</div>');
    },
    success: function (response) {
      $('#'+activeTabName).html(response.content);
      $('#'+activeTabName+'Controls').html(response.buttons);
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
      url: '/api/'+activeTabName,
      beforeSend: function() {
        $('#'+activeTabName).html('<div class="ui indeterminate text loader">Fetching data</div>');
      },
      success: function (response) {
        $('#'+activeTabName).html(response.content);
        $('#'+activeTabName+'Controls').html(response.buttons);
      },
      error: function (error) {
        console.log('Error:', error);
      }
    });
  },

});