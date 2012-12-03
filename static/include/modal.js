(function(){

    var cookie = {

        'write': function(name, value, length) {
            var date = new Date();
            date.setTime(date.getTime() + length);
            document.cookie = name + '=' + value + '; expires=' + date.toGMTString() + '; path=/';
        },

        'read': function(name) {
            var nameEq = name + '=';
            var ca = document.cookie.split(';');
            for(var i=0; i < ca.length; i++) {
                var c = ca[i];
                while(c.charAt(0) == ' '){
                    c = c.substring(1, c.length);
                }
                if(c.indexOf(nameEq) === 0){
                    return c.substring(nameEq.length, c.length);
                }
            }
            return null;
        },

        'delete': function(name){
            this.write(name, '', -1);
        }

    };

    var querystring = {

        encode: function(obj){
            var bits = [];
            for(var bit in obj) {
                if(obj.hasOwnProperty(bit)) {
                    var key = encodeURIComponent(bit),
                        value = encodeURIComponent(obj[bit]);
                    bits.push(key + '=' + value);
                }
            }
            return bits.join("&");
        },

        decode: function(){
            var urlParams = {},
                plusToSpace = /\+/g,
                search = /([^&=]+)=?([^&]*)/g,
                decode = function(s){
                    return decodeURIComponent(s.replace(plusToSpace, ' '));
                },
                query  = window.location.search.substring(1);
            while(match = search.exec(query)){
                urlParams[decode(match[1])] = decode(match[2]);
            }
            return urlParams;
        }

    };

    var addEvent = function(elem, type, eventHandle) {
        if(elem === null || elem === undefined){
            return;
        }
        if(elem.addEventListener){
            elem.addEventListener(type, eventHandle, false);
        }else if(elem.attachEvent){
            elem.attachEvent('on' + type, eventHandle);
        }else{
            elem['on' + type] = eventHandle;
        }
    };

    var className = {

        'regex': function(className){
            return new RegExp('(\\s|^)' + className + '(\\s|$)', 'gi');
        },

        'add': function(elem, className){
            if(!elem.className.match(this.regex(className))){
                elem.className = elem.className + ' ' + className;
            }
        },

        'remove': function(elem, className){
            elem.className = elem.className.replace(this.regex(className), ' ');
        }

    };

    // Default settings
    var qs = querystring.decode(),
        canPostMessage = !!window.postMessage,
        defaults = {
            'variant': 'modal',
            'campaign': 'itu',
            'url': null,
            'cookieLength': 24 * 60 * 60 * 1000,
            'test': false
        },
        ieQuirks = (document.compatMode != 'CSS1Compat') && (navigator.appVersion.indexOf("MSIE") != -1);

    // Ensure that user hasn't opted out
    var cookieName = '_idl_opt_out_itu',
        opted_out = cookie.read(cookieName) == 'true';
    if(!opted_out || defaults.test){

        // Caches settings serialization and fetch of body element
        var settings = querystring.encode(defaults),
            head = document.getElementsByTagName('head')[0],
            body = document.getElementsByTagName('body')[0],
            html = document.getElementsByTagName('html')[0],
            ifr, ifr_src;

        if(ieQuirks){
            className.add(html, 'idl_ie_quirks');
        }

        // Sets frame URL
        ifr_src = 'https://members.internetdefenseleague.org/campaign/?campaign=itu&variant=modal';


        // Creates and appends iframe element containing content
        ifr = document.createElement('iframe');
        ifr.type = 'text/javascript';
        ifr.async = true;
        ifr.scrolling = 'no';
        ifr.frameBorder = 0;
        ifr.id = 'idl_alert';
        ifr.src = ifr_src;
        className.add(html, 'idl_' + defaults.variant);
        body.appendChild(ifr);

        var metatags = document.getElementsByTagName('meta'),
            oldViewport = null,
            newViewport;

        // Creates and appends iframe element containing content
        var backdrop = document.createElement('div');
        backdrop.id = 'idl_backdrop';
        body.appendChild(backdrop);

        // Creates and appends close bytton
        var closeBtn = document.createElement('a');
        closeBtn.id = 'idl_close';
        closeBtn.href = '#';
        closeBtn.innerHTML = 'x';
        body.appendChild(closeBtn);

        // Close modal and set opt-out cookie on click of close button,
        // backdrop, or <esc> press.
        var closeModal = function(evt){
            className.remove(html, 'idl_' + defaults.variant);
            if(!defaults.test){
                cookie.write(cookieName, 'true', defaults.cookieLength);
            }
            ifr.parentNode.removeChild(ifr);
            backdrop.parentNode.removeChild(backdrop);
            closeBtn.parentNode.removeChild(closeBtn);
            if(oldViewport){
                head.appendChild(oldViewport);
            }
            if(newViewport){
                newViewport.parentNode.removeChild(newViewport);
            }
        };
        addEvent(closeBtn, 'click', closeModal);
        addEvent(backdrop, 'click', closeModal);
        addEvent(document, 'keyup', function(evt){
            if(evt.keyCode == 27){
                closeModal(evt);
            }
        });

        // Send messages to set a class on the <html> tag of the included page
        if(canPostMessage){
            try{
                var checkMobile = function(){
                    var message = '';
                    if(window.innerWidth <= 800 && window.innerHeight <= 800){
                        message = 'idl_mobile';
                        if(window.innerWidth > window.innerHeight){
                            message = message + ':idl_landscape';
                        }
                    }
                    ifr.contentWindow.postMessage(message, '*');
                };
                addEvent(window, 'resize', checkMobile);
                addEvent(window, 'load', function(){
                    checkMobile();
                });
                checkMobile();
            }catch(err){}
        }

        // Find and store old viewport. If there is no old viewport, let's
        // create one with defaults to force iOS to redraw appropriately.
        // We'll update with our own, but restore the old one on close.
        try{
            for(var i in metatags){
                var tag = metatags[i];
                if(metatags.hasOwnProperty(i) && !!tag.nodeName && tag.name == 'viewport'){
                    oldViewport = tag;
                    oldViewport.parentNode.removeChild(oldViewport);
                    break;
                }
            }
            if(!oldViewport){
                oldViewport = document.createElement('meta');
                oldViewport.name = 'viewport';
                oldViewport.content = 'width=980, user-scalable=1';
            }
            newViewport = document.createElement('meta');
            newViewport.name = 'viewport';
            newViewport.content = 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0';
            head.appendChild(newViewport);
        }catch(err){}


        // Add CSS string
        var style = document.createElement('style'),
            rules = "#idl_alert{border:0;position:fixed;text-decoration:none}.idl_ie_quirks #idl_alert{position:absolute}html.idl_banner{padding-top:90px}html.idl_banner #idl_alert{width:100%;height:90px;top:0;left:0;-webkit-box-shadow:0 -1px 4px 0 #000;box-shadow:0 -1px 4px 0 #000}html.idl_banner #idl_close{display:none}html.idl_modal #idl_alert{width:600px;height:400px;top:50%;left:50%;margin:-200px 0 0 -300px;z-index:2147483647;background:#FFF;border-radius:5px;-webkit-box-shadow:0 0 30px 0 rgba(0,0,0,0.75);box-shadow:0 0 30px 0 rgba(0,0,0,0.75)}#idl_backdrop{position:fixed;width:100%;height:100%;top:0;left:0;z-index:2147483646;background:#000;opacity:0.75;filter:alpha(opacity=75)}.idl_ie_quirks #idl_backdrop{position:absolute}html.idl_banner #idl_backdrop{display:none}#idl_close{position:fixed;top:50%;left:50%;margin:-190px 0 0 269px;z-index:2147483647;width:20px;height:20px;display:block;font:bold 20px/1 'Helvetica Neue','Helvetica',sans-serif;overflow:hidden;text-align:center;color:#FFF;text-decoration:none}.idl_ie_quirks #idl_close{zoom:1;position:absolute}";
        style.type = 'text/css';
        head.appendChild(style);
        if(style.styleSheet){
            style.styleSheet.cssText = rules;
        }else{
            style.innerHTML = rules;
        }


    }

})();