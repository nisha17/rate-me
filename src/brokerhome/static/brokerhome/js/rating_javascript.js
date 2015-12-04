
function prepareEventHandlers(){
	var frm = document.getElementById('rate_form')
	
	frm.onsubmit = function(){
		if (true){

			$('#myModal').modal('show');
			// alert("you submitted rating");
			 return false
		}

		else{
			alert('login')
			return true
		}
	}
}


window.onload = function() {
	prepareEventHandlers();
}









// $('#go').click(function() {
//   if (test1 === "") {
//     alert("Please enter all values in the fields");
//     $('#myModal').modal('show');
//   }

// });