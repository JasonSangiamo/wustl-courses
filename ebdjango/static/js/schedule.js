var events_array = [];


function convertClassSchedule (daysString, start_time, end_time, course_name,section_id){
    //converting pm times to military times
    if(start_time.substring(start_time.length -1) == 'P'){
        hours = parseInt(start_time.substring(0, start_time.indexOf(":")));
        hours = hours + 12;
        start_time = hours + start_time.substring(start_time.indexOf(":"),start_time.length-1);

        // start_time = parseInt(start_time.substr(0,start_time.length-1)) + 12
    }
    else{
        start_time = parseInt(start_time.substring(0,start_time.length-1)) 
    }
    if(end_time.substring(end_time.length -1) == 'P'){
        hours = parseInt(end_time.substring(0, end_time.indexOf(":")));
        hours = hours + 12;
        end_time = hours + end_time.substring(end_time.indexOf(":"),end_time.length-1);
    }
    else{
        end_time = parseInt(end_time.substring(0,end_time.length-1)) 
    }


    //converting MTWTFSS form to corrospodning dates they will have in calendar
    var days_of_week = new Set([]);
    if (daysString.substring(0,1) == "M"){
        days_of_week.add("2012-01-02");
    }if (daysString.substring(1,2) == "T"){
        days_of_week.add("2012-01-03");}
    if (daysString.substring(2,3) == "W"){
        days_of_week.add("2012-01-04");
    }
    if (daysString.substring(3,4) == "R"){
        days_of_week.add("2012-01-05");
    }
    if (daysString.substring(4,5) == "F"){
        days_of_week.add("2012-01-06");
    }if (daysString.substring(5,6) == "S"){
        days_of_week.add("2012-01-07");
    }if (daysString.substring(6,7) == "S"){
        days_of_week.add("2012-01-01");
    }

    //creating event objects by iterating through days to add
    days_of_week.forEach(function(value){
        events_array.push({
            title: course_name+"BAH",
            id: "Zzzzzzzzz",
            className: "course_name:" + course_name + " schedule_object_for" +section_id,
            id: "Zzzzzzzzzzzzz",
            start: value + "T" + start_time,
            end: value + "T" + end_time,
        })
    })
}

