$('.ui.dropdown').dropdown({
    clearable: true
});

$('#dropdownMenuCollege').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/college/list',
        method: 'POST',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuCollege input.search').val().trim();
            settings.data = JSON.stringify({ query: query });
            settings.contentType = 'application/json';
            return settings;
        },
        onResponse: function(response) {
            return { success: response.success, results: response.results};
        },
        onFailure: function (response) {
            console.log("fail");
        },
        onError: function (response) {
            console.log("error");
        },
    },
});

$('#dropdownMenuCourse').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/course/list',
        method: 'POST',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuCourse input.search').val().trim();
            settings.data = JSON.stringify({ query: query });
            settings.contentType = 'application/json';
            return settings;
        },
        onResponse: function(response) {
            return { success: response.success, results: response.results};
        },
        onFailure: function (response) {
            console.log("fail");
        },
        onError: function (response) {
            console.log("error");
        },
    },
});
