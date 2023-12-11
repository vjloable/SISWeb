$(document).ready(function () {
  $.ajax({
    type: 'GET',
    url: '/last_tab',
    success: function (results) {
      return results;
    },
    error: function (error) {
      console.log('Error:', error);
    }
  }).done((result) => {
    activeTabName = result.toLowerCase();
    console.log(result);
    $.ajax({
      type: 'GET',
      url: '/api/' + activeTabName + '/list',
      success: function (results) {
        $('#' + activeTabName + 'Tab').html(results.content);
        $('#' + activeTabName + 'TabControls').html(results.buttons);
        $.tab('change tab', activeTabName);
      },
      error: function (error) {
        console.log('Error:', error);
      }
    });
  });
});


$('.menu .item').tab({
  onVisible: function() {
    console.log("visible");
    var activeTab = $('.tab.segment.active');
    var activeTabName = activeTab.attr('data-tab');
    $.ajax({
      type: 'GET',
      url: '/api/'+activeTabName+'/list',
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