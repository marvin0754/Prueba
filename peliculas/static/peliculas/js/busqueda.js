function buscador(keyword){
    if(filtrar_space(keyword)){
        keyword=keyword.trim()
        ajax(keyword,function(){
           data=this;
           
           data=procesar_data(data);
           
           document.getElementById('busqueda').innerHTML=data
        });
    }
    
}
function ajax(key,callback){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var data=JSON.parse(this.responseText);
            callback.apply(data);

        }
    };
    xhttp.open("GET", "/buscar?keyword="+key, true);
    xhttp.send();
}
function procesar_data(data){
    var context="<p>Resultados de la busqueda</p>";
    for(i in data){
        dat=data[i];
        context += "\
        <div class=\"card margin\"> "+
            "<div class =\"row no-gutters\">\
            <div class=\"col-md-4\">\
                <img src=\"/static/peliculas"+dat.imagen +"\" class=\"card-img\" alt= \"...\">\
            </div>\
            <div class= \"col-md-8\">\
                <div class= \"card-body\">\
                    <h5 class=\"card-title\">"+dat.titulo+"</h5>\
                    <p class=\"card-text\">"+dat.sinopsis+"</p>\
                    <p class=\"card-text\"><small class=\"text-muted\">"+dat.fecha.substring(0,10)+"</small></p>\
                    <a href=\"#\" class=\"btn btn-primary small\">Leer Mas</a>\
                </div>\
            </div>\
            </div>\
        </div>";
    }
    return context;
}
function filtrar_space(keyword){
    if(keyword === "" || !keyword.trim()){
        document.getElementById('busqueda').innerHTML="";
        return false;
    }else{
        return true;
    }
}