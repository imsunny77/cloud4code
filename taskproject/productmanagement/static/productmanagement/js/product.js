product_api = `/product-api/`
var method_type = 'POST';

function editProduct(product_id) {
    method_type = 'PUT'
    var product_name = $(`#${product_id}`).attr('data-product_name')
    var product_category = $(`#${product_id}`).attr('data-category')
    var product_price = $(`#${product_id}`).attr('data-price')
    var product_description = $(`#${product_id}`).attr('data-description')
    product_api = `/product-api/${product_id}/`;
    $('#id_product_name').val(product_name);
    $('#id_product_category').val(product_category).attr("selected", "selected");
    $('#id_price').val(product_price);
    $('#id_description').val(product_description);
}

function deleteProductPopup(product_id) {
   $('#id_delete_product').attr('id',product_id);
}

function deleteProduct(product_id) {
    $.ajax({
        type: 'DELETE',
        url: `/product-api/${product_id}/`,
        headers: { "X-CSRFToken": csrf_token },
        success: function () {
            productList();
            $('#close_modal').click();
        }
    })
}

function productData(product) {
    return `
    <tr>
        <td>
            <img src="${product.feature_image}" class="item-picture img-fluid">
        </td>
        <td>${product.product_name}</td>
        <td>${product.category_name}</td>
        <td>${product.price}</td>
        <td>
            <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#add" id=${product.id}
                data-product_name='${product.product_name}' data-category='${product.product_category}'
                data-price='${product.price}' data-description='${product.description}'
                onClick='editProduct(this.id)'>Edit</button>
            <button type="button" class="btn btn-primary" data-toggle="modal" 
            id='${product.id}' onClick="deleteProductPopup(this.id)"
            data-target='#delete_productdata'>
                Delete </button>
        </td>
    </tr>
    `

}

function productList() {
    $.ajax({
        type: 'GET',
        url: `/product-api/`,
        success: function (response) {
            document.getElementById('product_list').innerHTML = `${response.map(productData).join('')}`;
        },
    });
}


$("#id_form").submit(function (e) {
    e.preventDefault();
    var serializedData = $(this).serialize();
    console.log(method_type, product_api);
    $.ajax({
        type: method_type,
        url: product_api,
        data: serializedData,
        headers: { "X-CSRFToken": csrf_token },
        success: function () {
            $('#close').click();
            $("#id_form").trigger('reset');
            productList();
        }
    });
});

$(document).ready(function () {
    productList();
})
