$('.ui.dropdown').dropdown({
    clearable: true
});

$('#dropdownMenuAddCollege').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/college/list',
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuAddCollege input.search').val();
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

$('#dropdownMenuEditCollege').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/college/list',
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuEditCollege input.search').val();
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
})
.dropdown('set value', new URL(window.location.href).searchParams.get("college"))
.dropdown('set text', new URL(window.location.href).searchParams.get("college"));

$('#dropdownMenuAddCourse').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/course/list',
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuAddCourse input.search').val();
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

$('#dropdownMenuEditCourse').dropdown({
    clearable: true,
    apiSettings: {
        url: '/api/course/list',
        method: 'GET',
        cache: false,
        saveRemoteData: false,
        beforeSend: function(settings) {
            const query = $('#dropdownMenuEditCourse input.search').val();
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
})
.dropdown('set value', new URL(window.location.href).searchParams.get("course"))
.dropdown('set text', new URL(window.location.href).searchParams.get("course"));