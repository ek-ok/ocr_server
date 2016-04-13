// hide buttons
$("#results").hide()

// when an url is submited
$(function() {
  $('#post-form').on('submit', function(event) {
    url = $("#image_url").val()
    $.ajax({
      type: "POST",
      url: "/ocr",
      contentType: "application/json",
      dataType: "json",
      data: JSON.stringify({"image_url": url}),
      success: function(response) {
        $("#post-form").hide();
        $("#results").show();
        $("#results_image").attr("src", response.url);
        $("#results_text").text(response.text);
      }
    });
  });
});