$(function() {
	$('#power').on('click', function(){
		$(this).toggleClass('on');
	});

	$('input[type="range"]').rangeslider({
		
	});

	var $document   = $(document),
		selector    = '[data-rangeslider]',
		$element    = $(selector);

    // Example functionality to demonstrate a value feedback
    function valueOutput(element) {
    	var value = element.value,
    	output = element.parentNode.getElementsByTagName('output')[0];
    	output.innerHTML = value;
    }
    
    for (var i = $element.length - 1; i >= 0; i--) {
    	valueOutput($element[i]);
    };

    $document.on('change', 'input[type="range"]', function(e) {
    	valueOutput(e.target);
    });

    // Basic rangeslider initialization
    $element.rangeslider({

        // Deactivate the feature detection
        polyfill: false,

        // Callback function
        onInit: function() {},

        // Callback function
        onSlide: function(position, value) {
        	console.log('onSlide');
        	console.log('position: ' + position, 'value: ' + value);
        },

        // Callback function
        onSlideEnd: function(position, value) {
        	console.log('onSlideEnd');
        	console.log('position: ' + position, 'value: ' + value);
        }
    });
});