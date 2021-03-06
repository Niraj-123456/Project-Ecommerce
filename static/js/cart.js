// add the product to the cart and update the quantity and delete product from the cart
var updateBtn = document.getElementsByClassName("add-cart")

for(i=0; i<updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('User:', user)

        if(user == 'AnonymousUser'){
            //addCookieItem(productId, action)
            console.log("User is not authenticated.")
            alert("Please, login to add the product to the cart.")
        }
        else{
            addUserOrder(productId, action)
        }
    })
}
function addUserOrder(productId, action){
    var url = '/add_to_cart/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})
    })
    .then((response) => {
        return response.json()
    })
    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}

//function addCookieItem(productId, action){
//    console.log("User is not Authenticated..")
//    if(action == 'add'){
//        if(cart[productId] == undefined){
//            cart[productId] = {'quantity': 1}
//            alert("Product added to your cart")
//        }
//        else{
//            cart[productId]['quantity'] += 1
//            alert("Product updated to your cart")
//        }
//    }
//    if(action == 'remove'){
//        cart[productId]['quantity'] -= 1
//        alert("Product updated to your cart")
//
//        if(cart[productId]['quantity'] <= 0){
//            console.log("Product removed")
//            alert("Product removed from your cart")
//            delete cart[productId]
//        }
//    }
//
//    if(action == 'delete'){
//        console.log("Product deleted")
//        delete cart[productId]
//        alert("Product removed from your cart")
//    }
//
//    console.log('Cart:', cart)
//    document.cookie = 'cart=' + JSON.stringify(cart) + ';domain=;path=/'
//    location.reload()
//}
//
