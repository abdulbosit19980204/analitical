
  document.addEventListener('DOMContentLoaded', function() {
   

    /* initialize the external events
    -----------------------------------------------------------------*/
    var containerEl = document.getElementById('codex-events-list');
    var t = document.getElementById("e-title")
      , form_eve = document.getElementById("form-event")
      , d = null
      , r = document.getElementsByClassName("needs-validation")
      , d = null      
    new FullCalendar.Draggable(containerEl, {
      itemSelector: '.fc-event',
      eventData: function(getEvntList) {
        return {
          title: getEvntList.innerText.trim(),
          className: getEvntList.className 
        }
      },     
    });

    /* initialize the calendar
    ----------------------------------------------------------------*/
    var codexcalendarEvntlist = document.getElementById('codex-calendar');
    var calendar = new FullCalendar.Calendar(codexcalendarEvntlist, {
      codexEvntFilter: {
        left: 'prev,next today',
        center: 'title',
        right: 'dayGridMonth,timeGridWeek,timeGridDay,listYear'
      },

      initialDate: '2022-01-12',
      navLinks: true,           
      editable: true,
      droppable: true, 
      selectable: true,
      selectMirror: true,
      nowIndicator: true,
      dayMaxEvents: true, 


      
      drop: function(arg) {
        // is the "remove after drop" checkbox checked?
        if (document.getElementById('drop-remove').checked) {
          // if so, remove the element from the "Draggable Events" list
          arg.draggedEl.parentNode.removeChild(arg.draggedEl);
        }
      },
      select: function(arg) {

        d = null;
        $('#e-title').val('');
        var start=arg.start;
        var allDay=arg.allDay;
        $('#startdate').val(start);
        $('#allDay').val(allDay);
        $('#btn-delete-event').hide();              
        calendar.unselect()
      },
        eventClick: function(event) { 
           document.getElementById("e-title").value[0] = "",
            d = event.event,
                document.getElementById("e-title").value = d.title,           
            $('#modal-title').html('Edit Event')                      
        },
        events: [
            {
              title: 'All Day Event',
              start: '2022-02-01'
            },
            {
              title: 'Long Event',
              start: '2022-03-07',
              end: '2022-03-10'
            },
            {
              groupId: 999,
              title: 'metting',
              start: '2022-01-09T16:00:00'
            }
        ]
    });
           

    calendar.render();
    
});

    