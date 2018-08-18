$(window).on('load',function() {
    console.log("initializing");
    console.log(events_array);
    var today = moment();  //get todays date
    $('#calendar').fullCalendar({
        header: {
          left: '',
          center: '',
          right: ''
        },
        allDaySlot: false,
        minTime: "08:00:00",
        columnFormat: 'ddd',
        contentHeight: 'auto',
        // this is a monday, where our calendar will start
        // so: sunday = 12-31-2000, tuesday = 01-02-2001 etc.
        defaultDate: '2012-01-01',
        defaultView: 'agendaWeek',
        editable: false,
        eventLimit: true, // allow "more" link when too many events
        eventSources: [

            // your event source
            // {
            //   events: [ // put the array in the `events` property
            //     {
            //       title  : 'Event',
            //       start  : '2012-01-01T10:30:00',
            //       end   : '2012-01-01T13:30:00'
            //     }
                
            //   ],

            // }
            {
                events: events_array,
            }
            // any other event sources...

          ]
        

    });
});