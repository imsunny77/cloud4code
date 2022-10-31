var method_type = 'POST';
var category_api ='/category-api/'

function deleteCategory(category_id){
    $.ajax({
        type: 'DELETE',
        url: `/category-api/${category_id}/`,
        headers: { "X-CSRFToken": csrf_token },
        success: function () {
            categoryList();
            location.reload();
        }
    })
}


$('#close').click(function () {
    $('#id_parent_category').val('');
    $('#id_category').val('');
});

function editCategory(category_id){
    method_type = 'PUT'
    var category = $(`#${category_id}`).attr('data-category')
    var parent_category = $(`#${category_id}`).attr('data-parent-category')
    category_api = `/category-api/${category_id}/`;
    if (parent_category != '-'){
        $('#id_parent_category').val(parent_category).attr("selected", "selected");
    }
    $('#id_category').val(category)
}

$('#add_data').click(function () {
    var parent_category = $('#id_parent_category').find(":selected").val();
    var category = $('#id_category').val();
    var csrf = $("input[name='csrfmiddlewaretoken']").val()
    $.ajax({
        type: method_type,
        url: category_api,
        data: {
            'parent_category': parent_category,
            'category': category,
            csrfmiddlewaretoken: csrf ,
        },
        headers: { "X-CSRFToken": csrf_token },
        success: function () {
            $('#close').click();
            $('#id_parent_category').val('');
            $('#id_category').val('');
            categoryList();
            location.reload();

        }
    })
})

function deleteCategoryPopup(category_id) {
    $('#id_delete_category').attr('id',category_id);
 }

function categoryData(category) {
    var parent = '-'
    var parent_id = '-'

    if(category.parent_category != null){
        parent = category.parent_category.category
        parent_id =  category.parent_category.id

    }
    return `
    <tr>
    <td>${parent}</td>
    <td>${category.category}</td>
    <td>
        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#add" id=${category.id} 
        data-category = '${category.category}'
        data-parent-category = '${parent_id}'
        onClick='editCategory(this.id)'>Edit</button>
        <button type="button" class="btn btn-primary" data-toggle="modal" 
        id='${category.id}' onClick="deleteCategoryPopup(this.id)"
        data-target='#delete_categorydata'>
            Delete </button>
    </td>
</tr>
 `
}

function categoryList() {
    $.ajax({
        type: "GET",
        url: `/category-api/`,
        success: function (response) {
            console.log(response)
            document.getElementById('category_list').innerHTML = ` ${response.map(categoryData).join('')}`
        },
    });
}

$(document).ready(function () {
    categoryList();
})
