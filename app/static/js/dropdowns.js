$('.ui.dropdown').dropdown({
    clearable: true
});

$('#dropdownMenuCollege').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/college/list',
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuCollege input.search').val().trim();
            settings.data = {query: query, page: -1};
            settings.contentType = 'application/json';
            return settings;
        },
        onResponse: function(response) {
            results = response.results
            var raw_response = []
            for (let i = 0; i < (results).length; i++) {
                raw_response.push({
                    "name": (results)[i][1],
                    "value": (results)[i][0]
                });
            }
            return { success: response.success, results: raw_response};
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
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuCourse input.search').val().trim();
            settings.data = { query: query, page: -1 };
            settings.contentType = 'application/json';
            return settings;
        },
        onResponse: function(response) {
            results = response.results
            var raw_response = []
            for (let i = 0; i < (results).length; i++) {
                raw_response.push({
                    "name": (results)[i][1],
                    "value": (results)[i][0]
                });
            }
            return { success: response.success, results: raw_response};
        },
        onFailure: function (response) {
            console.log("fail");
        },
        onError: function (response) {
            console.log("error");
        },
    },
});
