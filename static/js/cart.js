// add the product to the cart and update the quantity and delete product from the cart
var updateBtn = document.getElementsByClassName("add-cart")

for(i=0; i<updateBtn.length; i++){
    updateBtn[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:', productId, 'Action:', action)
        console.log('User:', user)

        if(user == 'AnonymousUser'){
            console.log("User is not Authenticated..")
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