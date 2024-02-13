$(document).ready(function() {
    $('#myForm').submit(function(event) {
        // Prevent the default form submission
        event.preventDefault();
        
        // Serialize the form data
        var formData = $(this).serialize();
        
        // Send AJAX request
        $.ajax({
            type: 'POST',
            url: '/submit_form', // Change this to your Flask route
            data: formData,
            success: function(response) {
                // Handle success response
                console.log(response);
            },
            error: function(error) {
                // Handle error
                console.error('Error:', error);
            }
        });
    });
});