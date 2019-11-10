function ajax(method, url, data) {
    if (!data) data = [];

    var result = null;
    var request = $.ajax({
        type: method,
        url: url,
        data: data,
        async: false,
        success: function (response) {
            if (response.result !== 1) {
                new PNotify({
                    text: response.message,
                    type: 'error',
                    styling: 'bootstrap3',
                    delay: 2000
                });
            } else {
                new PNotify({
                    text: response.message,
                    type: 'success',
                    styling: 'bootstrap3',
                    delay: 2000
                });
            }
        },
        error: function (response) {
            new PNotify({
                text: response.message,
                type: 'error',
                styling: 'bootstrap3',
                delay: 2000
            });
        }
    });
    request.done(function (response) {
        result = response;
    });
    return result;
}

$('.delete-btn').each(function () {
    const button = $(this);

    button.click(function (e) {
        e.preventDefault();
        const name = button.data('name');
        const redirect = button.data('redirect');
        const csrf_token = button.data('csrf_token');
        if (window.confirm(`Are you sure you want to delete ${name}?`)) {
            const res = ajax('POST', button.data('url'), {csrfmiddlewaretoken: csrf_token});

            if (res.result > 0) {
                button.closest('tr').remove();

                if (redirect) {
                    setTimeout(() => {
                        window.location = redirect;
                    },1000);
                }
            }
        }
    });
});

$('.table-responsive-xl').doubleScroll({
    onlyIfScroll: true,
    resetOnWindowResize: true,
    timeToWaitForResize: 1000
});

function showFormErrors(form, response) {
    try {
        for (var err in response.errors) {
            addHasError(form, err, response.errors[err][0]);
        }

    } catch (err) {
        console.error(err.message);
    }
}

function addHasError(form, name, message) {
    var input = form.find('[name=' + name + ']');

    if (typeof (input) !== "undefined") {
        input.addClass('invalid');
    }
}

function removeErrors(form) {
    const inputs = form.find('input, textarea, select');
    inputs.each(function () {
        var el = $(this);
        el.removeClass('invalid');
    });
}