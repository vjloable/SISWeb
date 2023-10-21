$('.menu .item')
    .tab({
      onVisible: function() {
        var activeTab = $('.tab.segment.active');
        var activeTabName = activeTab.attr('data-tab');
        $.ajax({
            type: 'GET',
            url: '/api/'+activeTabName,
            success: function (response) {
                $('#'+activeTabName).html(response.content);
            },
            error: function (error) {
                console.log('Error:', error);
            }
        });
      }
    });