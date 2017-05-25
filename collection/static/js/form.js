// check how many times elements with this name attribute exist: extra_field_*
form_count = $('input[name*="extra_field_*"]').length;

// when the button 'add another' is clicked then create a new input element
$(document.body).on("click", "#add-another",function(e) {
  new_attribute = $('<input type="text"/>');
  // add a name attribute with a corresponding number (form_count)
  new_attribute.attr('name', 'extra_field_' + form_count);
  // append the new element in your html
  $("#form_empty_layer").append(new_attribute);
  // increment the form_count variable
  form_count ++;
  // save the form_count to another input element (you can set this to invisible. This is what you will pass to the form in order to create the django form fields
  $("[name=total_input_fields]").val(form_count);

})