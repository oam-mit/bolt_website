window.addEventListener('load',()=>{

    $.ajax({

        type:'GET',
        url:"/user/bulb_status",
        credentials:"include",
        success:function(response)
        {
            if(response == 'high')
            {
                document.getElementById("myBulb").src="https://www.w3schools.com/js/pic_bulbon.gif"

            }
            else
            {
                document.getElementById("myBulb").src="https://www.w3schools.com/js/pic_bulboff.gif"
            }
        }

    });

});

window.setInterval(function(){ $(document).ready(function(e){

    $.ajax({

        type:'GET',
        url:"/user/status",
        credentials:"include",
        success:function(response)
        {
            if(response == 'Please Log In again')
            {
                $('#on').css("display","none");
                $('#off').css("display","none");
                $('#myBulb').css("display","none");
            }
            document.getElementById('status').innerHTML=response

        }

    });

});
},10000);
$(document).on('click','#on',function(e){
    e.preventDefault();

    $.ajax({

        type:'GET',
        url:"/user/action/1",
        credentials:"include",
        success:function(response)
        {
            if(response=="Turned On")
            {
                document.getElementById("myBulb").src="https://www.w3schools.com/js/pic_bulbon.gif"
            }
            else{

            alert(response);
            }
        }
    });


});


$(document).on('click','#off',function(e){
    e.preventDefault();

    $.ajax({

        type:'GET',
        url:"/user/action/0",
        
        success:function(response)
        {
            if(response=="Turned off")
            {
                document.getElementById("myBulb").src="https://www.w3schools.com/js/pic_bulboff.gif"
            }
            else{

                alert(response);
            }
           
        }
    });


});