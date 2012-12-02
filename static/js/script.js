(function($){

    $('input, textarea').placeholder();

    $.fn.disableButton = function(options){
        var settings = $.extend( {
            'text': 'Working...',
            'class': 'disabled'
        }, options);
        return this.each(function(){
            var $button = $(this);
            $button.attr('disabled', 'disabled');
            $button.addClass(settings['class']);
            $button.width($button.width());
            $button.data({
                '_oldtext': $button.text(),
                '_settings': settings
            });
            $button.text(settings['text']);
        });
    };

    $.fn.enableButton = function(options){
        return this.each(function(){
            var $button = $(this),
                settings = $button.data('_settings');
            $button.removeAttr('disabled');
            $button.removeClass(settings['class']);
            $button.text($button.data('_oldtext'));
            $button.css('width', 'auto');
        });
    };

    $(function(){

        $('.modal .close').click(function(evt){
            evt.preventDefault();
            $(this).closest('.modal').hide();
        });
        $(document).keyup(function(evt){
            if(evt.keyCode == 27){
                $('.modal').hide();
            }
        });

        $(document).delegate('#action', 'submit', function(evt){
            evt.preventDefault();
        });

        $(document).delegate('#button_email', 'click', function(evt){
            evt.preventDefault();
            var $button = $(this),
                $email = $('#id_email'),
                hasError = false;

            if($button.is(':disabled')){
                return;
            }

            $button.disableButton();

            // Require email address
            if(!$email.val()){
                $email.addClass('error');
                hasError = true;
            }else{
                $email.removeClass('error');
            }

            if(!hasError){
                var responder = $('[name="Country"]').find('option:selected').attr('data-response') || 219;
                $.get('https://nt.salsalabs.com/save', {
                    'object': $('[name="object"]').val(),
                    'tag': $('[name="tag"]').val(),
                    'ip': $('[name="ip"]').val(),
                    'user_agent': $('[user_agent="object"]').val(),
                    'email_trigger_KEYS': responder,
                    'organization_KEY': $('[name="organization_KEY"]').val(),
                    'redirect': $('[name="redirect"]').val(),
                    'Email': $('[name="Email"]').val(),
                    'Phone': $('[name="Phone"]').val(),
                    'Country': $('[name="Country"]').val(),
                    'organizer': $('[name="organizer"]').val()
                });
                $button.text('Thanks!');
            }else{
                $button.enableButton();
            }


        });

        $('#button_call').show();
        $(document).delegate('#button_call', 'click', function(evt){
            evt.preventDefault();
            var $button = $(this),
                $phone = $('#id_phone'),
                $country = $('#country'),
                hasError = false;

            if($button.is(':disabled')){
                return;
            }

            $button.disableButton();

            // Require phone number
            if(!$phone.val()){
                $phone.addClass('error');
                hasError = true;
            }else{
                $phone.removeClass('error');
            }

            // Require country
            if(!$country.val()){
                $country.closest('.fauxselect').addClass('error');
                hasError = true;
            }else{
                $country.closest('.fauxselect').removeClass('error');
            }

            if(!hasError){
                $.post(CALL_TOOL_URL, {
                    'number': $('[name="Phone"]').val(),
                    'country': $('[name="Country"]').val()
                });
                $button.text('Thanks!');
                $('#call_modal').show();
            }else{
                $button.enableButton();
            }
        });

        if(window.location.search.indexOf('email_action') >= 0){
            $('#email_modal').show();
        }

        if(window.location.search.indexOf('call_action') >= 0){
            $('#call_modal').show();
        }

    });

})(jQuery);
