$(inicio);

function inicio(){
    $("button").click(function(){
        //coge los datos de la url y busca con el id que heos introducido en el input, para sacar solo esos datos
        $.get("https://jsonplaceholder.typicode.com/users/" + $("#idData").val(),
        function(data, status){
            console.log(status);
            console.log(data);
            $("#salida").html(data.name + "<br>" + data.email); //mete en salida los datos que ha extraido, en concreto el nombre y el email

        })
    });
}
