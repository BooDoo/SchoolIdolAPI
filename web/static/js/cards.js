
$(function () {
    $('[data-toggle="popover"]').popover();
})

$(".sidebar-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("active");
});

function addCardButtonHandler() {
    // ADD CARD
    $('a[href="#addCard"]').unbind('click');
    $('a[href="#addCard"]').click(function(e) {
	var addCardButton = $(this);
	var card = addCardButton.closest('.card');
	$('#id_card').val(card.prop('id')).change();
	addCardFormHandler(card.find('img.non_idolized').prop('src'),
			   card.find('img.idolized').prop('src'));

	$('#addCardModal form.add').unbind('submit');
	$('#addCardModal form.add').submit(function(e) {
	    e.preventDefault();
	    $(this).ajaxSubmit({
		success: function(data) {
		    addCardButton.before(data + '|');
		    $('#addCardModal').modal('hide');
		    editCardFormHandler();
		    $('[data-toggle="popover"]').popover();
		},
		error: function() {
		    onDone();
		    alert('Opps! Something bad happened. Try again.');
		}
	    });
	});
    });
}

function load_more_function() {
    var button = $("#load_more");
    var oldButtonContent = button.html();
    button.html('<div class="loader">Loading...</div>');
    var next_page = button.attr('data-next-page');
    $.get('/ajax/cards/' + location.search + (location.search == '' ? '?' : '&') + 'page=' + next_page, function(data) {
	button.replaceWith(data);
	pagination();
	addCardButtonHandler();
	editCardFormHandler();
	statistics_buttons();
	$('[data-toggle="popover"]').popover();
    });
}

function pagination() {
    var button = $("#load_more");
    $(window).scroll(
	function () {
	    if (button.length > 0
		&& button.find('.loader').length == 0
		&& ($(window).scrollTop() + $(window).height())
		>= ($(document).height() - button.height())) {
		load_more_function();
	    }
	});
}

function statistics_buttons() {
    $('.btn.minimum_statistics').unbind('click');
    $('.btn.minimum_statistics').click(function() {
	card = $(this).closest('.card')
	card.find('.statistics_minimum').show()
	card.find('.statistics_non_idolized_maximum').hide()
	card.find('.statistics_idolized_maximum').hide()
	card.find('.hp_non_idolized').show()
	card.find('.hp_idolized').hide()
    })
    $('.btn.non_idolized_statistics').unbind('click');
    $('.btn.non_idolized_statistics').click(function() {
	card = $(this).closest('.card')
	card.find('.statistics_minimum').hide()
	card.find('.statistics_non_idolized_maximum').show()
	card.find('.statistics_idolized_maximum').hide()
	card.find('.hp_non_idolized').show()
	card.find('.hp_idolized').hide()
    })
    $('.btn.idolized_statistics').unbind('click');
    $('.btn.idolized_statistics').click(function() {
	card = $(this).closest('.card')
	card.find('.statistics_minimum').hide()
	card.find('.statistics_non_idolized_maximum').hide()
	card.find('.statistics_idolized_maximum').show()
	card.find('.hp_non_idolized').hide()
	card.find('.hp_idolized').show()
    })
}

$(document).ready(function() {
    addCardButtonHandler();
    statistics_buttons();
    pagination();
});
