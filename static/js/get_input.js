// how input works
$(document).ready(
    function() {
        $('#send_input').click(function() { 
            var x = $('#input2').val(); 
            $.ajax({
                async: false,
                type: 'GET',
                url: "http://localhost:5000/input?name="+x
                })
            }
        )
    }
);
var res = '<p> responde </p>';
$('#respon').html(res);

console.log('over')