
$('.nav-link').click(function() {
    //window.location.href = '/';
    $('.nav-link').removeClass('nav-active');
      $(this).addClass('nav-active');
      
      $('.products').empty();
      var category = $(this).data('category');
      console.log(category)

      $.ajax({
        method:'GET',
        url: 'products',
        data : {
             
             
        },
        
        success:function(response){

         //var myObj = JSON.parse(response);
            var obj = response.products;
            var images= response.product_images;
            console.log(images)
            //var imageUrl=images.filter((element) => element.id == 24)[0].image;
            console.log(images)
            console.log("image url : ",images.filter((element) => element.id == 24)[0].image);
            for (let i in obj){
                if (obj[i].category.toLowerCase() == category){
                    console.log(obj[i].product_name);
                    console.log(obj[i])
                    var imageUrl=images.filter((element) => element.product_id == obj[i].id)[0].image;
                    var temp =` <div class="product-card">
                    
                    <figure data-target="${obj[i].id}/product-details" class="card-image">   
                        <img src="/media/${imageUrl}" alt="{{p.product_name}} image"/>
                    </figure>
            
                
                    <div class="card-item-details">
                        <p class="p-name">${obj[i].product_name}</p>
                        <p>${obj[i].unit_price}$</p>
                        <label>Quantity</label>
                        <input id="p-qty" class="p-qty" type="number" value="1" >
                        <button id="add-btn" class="add-btn" data-id="${obj[i].id}" data-url="add-to-cart"  class="add-btn" name="button" >Add to Cart</button>
                    </div>
                
            </div>` ;
            $('.products').append(temp);
                }
                
            }
            
            console.log("Success get data");
            //console.log(obj[0].product_name)            
            

        },
        error:function(){
            console.log("An Error Occured");

        },
    });

      //alert('clicked')
  });