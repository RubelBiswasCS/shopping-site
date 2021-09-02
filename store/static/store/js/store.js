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
var addToCart = function(args) {

          
           $.ajax({
               method:"POST",
               url: args.url,
               data:{
                    user_id : args.user_id,
                    product_id : args.product_id,
                    csrfmiddlewaretoken: args. csrfmiddlewaretoken,
    
                    
               },
               
            success: function(response){
                var myObj = JSON.parse(response);
                console.log(myObj.user_id+' '+myObj.product_id);
                console.log('data successfully send');
            },
    
            error: function(){
                console.log("something went wrong on store.js");
            },
           });
    
      
} 

function test(args) {
    alert('hello '+args+' well done');
    
}