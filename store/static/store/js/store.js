// $(document).ready(function() {
//     $("#online-payment").on("click", function() {
//         var $url = 'this.dataset.url';
//       $('#payment-method').load(" url #method-cod",
//               function () {
//                 alert("Load was performed.");
//               });
//             });
//   });


//fuction for add item to the cart
$(".add-btn").on("click",function(e){
       
    // alert("add btn clicked");
   
    e.preventDefault();
    var args = {
        url: $(this).data("url"),
        data: {
            // csrfmiddlewaretoken : $(this).data("csrftoken"),
            csrfmiddlewaretoken : csrf_token,
            product_id : $(this).data("id"),
        },
    };
    addToCart(args);
    
    // console.log($(this).data("csrftoken"));
    // console.log(csrf_token);
});


//function for add to cart btn on product details
   
    // $("#add-btn2").on("click",function(e){
       
    //     // alert("add btn clicked");
       
    //     e.preventDefault();
    //     var args = {
    //         url: $(this).data("url"),
    //         data: {
    //             // csrfmiddlewaretoken : $(this).data("csrftoken"),
    //             csrfmiddlewaretoken : csrf_token,
    //             product_id : $(this).data("id"),
    //         },
    //     };
    //     addToCart2(args);
        
    //     // console.log($(this).data("csrftoken"));
    //     // console.log(csrf_token);
    // });
    // $(document).on("click","#add-btn2",addToCart2);
//add to cart2
    var addToCart = function(args) {

        $.ajax({
            method:"POST",
            url:args.url,
            data:args.data,
            
            success: function(response){
            console.log('success function fired')
             var myObj = JSON.parse(response);
             console.log(myObj.user_id+' '+myObj.product_id);
             console.log('data successfully send');
         },

         error: function(){
             console.log("something went wrong");
           
         },
        });      
}

 

//function for cart view

$(document).ready(function(){
    setInterval(function(){
        $.ajax({
            method:'POST',
            url: cart_url,
            data : {
                 csrfmiddlewaretoken: csrf_token,
                 
            },
            success:function(response){

             var myObj = JSON.parse(response);
                console.log("Success get data");
                console.log(myObj[2]);
                document.getElementById("subtotal").innerHTML = myObj[0];
                document.getElementById("total").innerHTML = myObj[0];
           
             //    console.log(myObj[0].image);
                $("#cart-items").empty();
                var total_item = 0;
                for (var i=0 in myObj[1]){
                 console.log(myObj[1][i].product_name);
     //                var temp = `<div class="cart-item" id="cart-item">
     //     <section class="item-unit flex-center">
     //         ${myObj[i].quantity}
     //     </section>
     //     <section class="name flex-center" id="current-p-name">
     //         ${myObj[i].product_name}
     //     </section>
     //     <section class="price flex-center">
     //         ${myObj[i].price}$
     //     </section>
     //     <section class="item-action flex-center">
     //         <button class='rm-cart-item' id='rm-cart-item' value=" ${myObj[i].product_id}">x</button>
     //     </section>
     // </div>`;
       //loading item in cart
             var temp = `<div class="cart-item" id="cart-item">
           <section class="item-img">
             <img src="${myObj[1][i].image}"  alt= "image" />
           </section>
          <section class="cart-item-sec-2">
             <p>${myObj[1][i].product_name}</p>
             <div class="quantity_n_actions">
                 <button class="cart-action" data-product="${myObj[1][i].product_id}" data-action="+" data-url="{% url 'cart-action' %}">+</button>
               ${myObj[1][i].quantity}
               <button class="cart-action" data-product="${myObj[1][i].product_id}" data-action="-" data-url={% url 'cart-action' %}" >-</button>
                 </div>
             
          </section>
           <section class="cart-item-sec-3">
             <p>${myObj[1][i].price} $</p>
             <button class="cart-action" data-product="${myObj[1][i].product_id}" data-action="remove" data-url="{% url 'cart-action' %}">Remove</button>

           </section>
           
       </div>`
       
     // $("#cart-items").append("<p>Hi</p>");
                 
                 $("#cart-items").append(temp);

    
       //  var items = myObj[1];
       //   $(document).ready(function(items) {
       //     $('#cart-items').load("{% url 'cart-item' %} ",
       //             function () {
       //               // alert("Load was performed.");
       //               console.log(i, 'cart item loaded')
       //             });
                
       //   });

                 total_item ++;
                 
                 console.log("Success call");
                 
                };
                document.getElementById("total-item").innerHTML = total_item.toString();
                

                
                

            },
            error:function(){
                console.log("An Error Occured");

            },
        });

    },2000);
});


// cart action 

$(document).ready(function(){
$(document).on("click",".cart-action",function(e){
    // var user_id = '{{ request.user.id }}';
    // var id = $(this).val();
       e.preventDefault();
       $.ajax({
           method:"POST",
           url: cart_action,
           data:{
                product_id : $(this).data("product"),
                action : $(this).data("action"),
               
                csrfmiddlewaretoken: csrf_token, 
           },
           
          

        success: function(response){
            console.log(response);
        },
        error: function(){
          console.log("error");
            console.log("error while performing action");
        },
       });

   });
}); 

     // show and hide cart
     $("#cart-btn").click(function () {
        $("#cart").toggle("slow");
        // $( ".products" ).addClass( "wd-75" );
    });

    $("#close-cart").click(function () {
        $("#cart").toggle("slow");
        // $( ".products" ).addClass( "wd-75" );
    }); 


function test(args) {
    alert('hello '+args+' well done');
    
}


