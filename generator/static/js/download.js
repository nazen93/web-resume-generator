var button = document.getElementById('resume-download');

button.addEventListener('click', glyphicon_swap)

function glyphicon_swap(){
	var glyphicon_class = document.getElementsByClassName('glyphicon')[0];
	var text = document.getElementById('downloaded');
	glyphicon_class.className = 'glyphicon glyphicon-ok';
	text.innerHTML = 'Thank you for using my website!'
}