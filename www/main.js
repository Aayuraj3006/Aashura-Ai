$(document).ready(function () {
	$('.text').textillate({
		loop: true,
		sync: true,
		in: {
			effect: 'bounceIn',
		},
		out: {
			effect: 'bounceOut',
		}
	});

	//siri wave
	var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
	style : 'ios9',
	amplitude: "1",
	speed :0.35,
	autostart: true
  });

  //siri wave animation
  $('.siri-message').textillate({
		loop: true,
		sync: true,
		in: {
			effect: 'fadeIn',
			sync: true,
		},
		out: {
			effect: 'fadeOut',
			sync: true,
		} 
	});

// Mic button click event
$("#Micbtn").click(function () {
	eel.playAssistantSound();

    $("#oval").attr("hidden", true);

    $("#SiriWave").attr("hidden", false);

	eel.takeCommand()()

});
});



