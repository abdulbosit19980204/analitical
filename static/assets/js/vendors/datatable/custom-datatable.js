$(document).ready(function() {

  //Local Datatable JS
  $('#basicdata-tbl').DataTable({
    "scrollX": true,
  });


  //Advance Datatable
  $('#datatbl-advance').DataTable({    
    "scrollX": true,    
    stateSave: false,
    dom: 'Bfrtip',    
    buttons: [
      'print','excel','pdf', 'csv', 'copy',
    ] 
  });

  //Ajax Datatable JS
  $('#datatbl-ajax').DataTable( {
    "scrollX": true,  
    "ajax": '../assets/js/vendors/datatable/ajax-data/datatable-ajax.txt',
    scrollCollapse: true,
  });
  
});