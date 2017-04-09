/* Project specific Javascript goes here. */

/*
Formatting hack to get around crispy-forms unfortunate hardcoding
in helpers.FormHelper:

    if template_pack == 'bootstrap4':
        grid_colum_matcher = re.compile('\w*col-(xs|sm|md|lg|xl)-\d+\w*')
        using_grid_layout = (grid_colum_matcher.match(self.label_class) or
                             grid_colum_matcher.match(self.field_class))
        if using_grid_layout:
            items['using_grid_layout'] = True

Issues with the above approach:

1. Fragile: Assumes Bootstrap 4's API doesn't change (it does)
2. Unforgiving: Doesn't allow for any variation in template design
3. Really Unforgiving: No way to override this behavior
4. Undocumented: No mention in the documentation, or it's too hard for me to find
*/
$('.form-group').removeClass('row');

$('#youtubeForm').submit(function(e) {
  e.preventDefault();
  form = $('#youtubeForm');
    $.ajax({
    type: "POST",
    url: /app/,
    data: form.serializeArray(),
    beforeSend: function() {
      $('.results-holder').empty();
      $('.results-holder').append('<h3 class="text-center">Analyzing your results...</h3>');
    },
    success: function(comment){
      $('.results-holder').empty();
      console.log(comment);
      var results = JSON.parse(comment);
      for(i = 0; i < 3; i++){
        var counter = i+1;
        console.log(results[0].scores[i].tone_name);
        if(parseInt(results[0].scores[i].score) < .5){
          $('.results-holder').append('<p>The #' + counter + ' emotion in this video\'s comments is '+ results[0].scores[i].tone_name + '.');
        }
        else if(parseInt(results[0].scores[i].score) > .5 && parseInt(results[0].scores[i].score) < .75){
          $('.results-holder').append('<p>The #' + counter + ' emotion in this video\'s comments is '+ results[0].scores[i].tone_name + '.');
        } else {
          $('.results-holder').append('<p>The #' + counter + ' emotion in this video\'s comments is '+ results[0].scores[i].tone_name + '.');
        }
      }
    },
  });
});
