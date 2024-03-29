document.addEventListener('DOMContentLoaded', function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav); //initialise without defining a variable

  // date picker initialization
  let datepicker= document.querySelectorAll('.datepicker');
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: {done: "Select"} // allows you to change the text and localise the datepicker (see doc in materialize)
  });

  //select initialization
  let selects = document.querySelectorAll('select');
  M.FormSelect.init(selects);

  //collapsible initialization
  var collapsibles = document.querySelectorAll('.collapsible');
  M.Collapsible.init(collapsibles);
  });
 
