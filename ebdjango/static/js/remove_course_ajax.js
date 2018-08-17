// //removing course form database
// function add_remove_course_event_listener(id, data, request_path){
// 	$("#"+id).submit(function(e){
// 		alert("clicked")
// 		e.preventDefault();
// 		//getting course id to remove it from database
// 		var course_id = $("input[name=courseId]").val();
// 		alert(course_id);
// 		window.parent_element = $(this).parent().parent().parent();
// 		M.toast({html: 'Course succesfully removed!'})
// 		$.ajax({
// 		    method: "POST",
// 		    data: $(this).serialize(),
// 		    url: "{{request.path}}"
// 		});
// 		//removing entire div of the course
// 		window.parent_element.hide();
		
// 	});
// }
//removing course form database
function add_remove_course_event_listener(id, data, request_path){
	$(".remove_course").submit(function(){
		
		
	});
}