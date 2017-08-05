/**
 * Created by ddkon on 05.08.2017.
 */
function row_class(score){
    var cls;
    if (score >= 4){
        cls = "success";
    }
    else if(score == 3){
        cls = "warning";
    }
    else {
        cls = "danger";
    }
    return cls;
}

$(document).ready(function () {
   $.ajax('/table').then(function (data) {
       data = $.parseJSON(data);
       $(function () {
           $.each(data, function(i, item){
               var $tr = $('<tr>', {"class": row_class(item.score)}).append(
                   $('<td>').text(item.group),
                   $('<td>').text(item.last_name),
                   $('<td>').text(item.first_name),
                   $('<td>').text(item.score)
               );
               $tr.appendTo('#results-table')
           })
       })
   })
});