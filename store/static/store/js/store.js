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
               data: args.data,
               
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


//function for add to cart btn on product details
   
    $("#add-btn2").on("click",function(e){
       
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
        addToCart2(args);
        
        // console.log($(this).data("csrftoken"));
        // console.log(csrf_token);
    });
    // $(document).on("click","#add-btn2",addToCart2);
//add to cart2
    var addToCart2 = function(args) {

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


// var btns = document.getElementById('add-btn2');

    

// btns.addEventListener('click', function(){
//     alert("btn clicked");
//     console.log('clicked')
// });
// $(document).on("click",".add-btn",function(e){
//     e.preventDefault();
//     alert("add btn clicked");
//     console.log('clicked')
// });

function test(args) {
    alert('hello '+args+' well done');
    
}