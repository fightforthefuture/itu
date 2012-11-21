function getip(json){
    $('#signup_ip').val(json.ip);
}

$(function() {
	$('input, textarea').placeholder();
				
	$("#user_agent").val(navigator.userAgent);
	$('#country').change(function(){
		if ($(this).find('option:selected').data('response')) {
			$('#trigger').val($(this).find('option:selected').data('response'));
		} else {
			$('#trigger').val("209");
		}
	});
});
		