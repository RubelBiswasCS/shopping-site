
$(document).ready(function() {
  
    loadDashboardOverview();

    $("#nav-overview").on("click", function() {
        loadDashboardOverview();
            });
    
    // nav-products function, for loading products
    $("#nav-products").on("click", function() {
        $('#db-content').load(product_list_url,
                function () {
                //   alert("Load was performed.");
                });
            });

    // nav-orders function
    $("#nav-orders").on("click", function() {
        $('#db-content').load(order_list_url,
                function () {
                //   alert("Load was performed.");
                });
            });

});

// function for loading dashboard overview
var loadDashboardOverview =  function() {

    $('#db-content').load(dashboard_overview_url,
        function () {
        //   alert("Load was performed.");
        });
}


// //nav-overview function
// $(document).ready(function() {
//     $("#nav-overview").on("click", function() {
//       $('#db-content').load("{% url 'dashboard-overview' %} ",
//               function () {
//               //   alert("Load was performed.");
//               });
//             });
//   });

//funciton for heighlight active nav
$('.dash-nav').click(function() {
    $('.dash-nav').removeClass('nav-active');
      $(this).addClass('nav-active');
  });