$(document).ready(function(){
    get_form_contact_me();
});

function get_form_contact_me(){

    url = '/contact_me'

    $.ajax({
        type: 'GET',
        url: '/contact_me/',
        data: {},
        success: function(data){
            $("#id_form_contact_me").html(data);
            console.log('deu certo');

        }
    });
}

function post_form_contact_me(){
    $.ajax({
        method: "POST",
        url: '/contact_me/',
        data: $('#form_contact_me').serialize(),

        success: function (data) {

            if (data.message == 'success') {
                console.log("atualizado com sucesso!");
                $("#div_message").removeClass().addClass('alert alert-success alert-dismissible fade show')
                $('#message_form').append('Mensagem enviada com sucesso')
                $("#div_message").css("display", "block").
                css("background", "#fbf276c9").css("color", "#d24500");
                $('#btn_send_contact').attr("disabled","disabled");
                setTimeout(function() {
                    $("#div_message").css("display", "none");
                }, 5000);
            } else {
                console.log("error ao cadastrar!");
                $("#div_message").removeClass().addClass('alert alert-danger alert-dismissible fade show')
                $('#message_form').html('Verifique se existem campos não preenchidos!')
                $("#div_message").css("display", "block").
                css("background", "rgb(255, 216, 63)").css("color", "rgb(253, 0, 0)");
                $('#id_form_contact_me').empty();
                $('#id_form_contact_me').html(data);
                setTimeout(function() {
                    $("#div_message").css("display", "none");
                }, 4000);
            }
        }
     });
}