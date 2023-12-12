$(document).ready(function(){
    get_projects(1);
});

function get_projects(page=1){
    var number_page = page;
    var count_itens = parseInt($('#id_page_itens').val());
    console.log("itens page: ", $('#id_page_itens').val());
    const queryString = window.location.search;
    const urlParams = new URLSearchParams(queryString);


    $("#id_search").hide();
    $("#loading_search").show();

    if (count_itens == 1 && number_page>1){
        number_page = number_page - 1;
        console.log("new page itens: ", number_page);
    }
    url = '/projects/?page='+number_page

    $.ajax({
        type: 'GET',
        url: url,
        data: {},
        success: function(data){
            $("#my_projects").html(data);
        }
    });
}
