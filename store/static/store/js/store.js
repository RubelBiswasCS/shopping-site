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

 // cart action 
 $(document).on("click",".cart-action",function(e){
    // var user_id = '{{ request.user.id }}';
    // var id = $(this).val();
       e.preventDefault();
       $.ajax({
           method:"POST",
           url: $(this).data("url"),
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


