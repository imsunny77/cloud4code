function addSubCategory(current_id) {
    $(`.${current_id}`).find("ul").last().remove();
    $(`.${current_id}`).find("li").remove();

    $(`.${current_id}`).append($(`<ul class="submenu dropdown-menu ${current_id}"><ul>`));
    $.ajax({
        type: "GET",
        url: `/sub-category/${current_id}/`,
        success: function (response) {
            data = response['sub_category_list']
            for (let i = 0; i < data.length; i++) {
                sub_category_html = `
                <li class="nav-item dropdown ${data[i]['id']}">
                <a class="nav-link ${data[i]['is_parent']}" href="#" data-toggle="dropdown" id='${data[i]['id']}' onClick='addSubCategory(this.id);'>${data[i]['category']}
                </a>
                </li>
                `
                $(sub_category_html).appendTo(`.${current_id}`)
            }

        }
    })
}


function categoryOne(category) {
    return ` 
    <li class="nav-item dropdown ${category.id}">
    <a class="nav-link dropdown-toggle" href="#" data-toggle="dropdown" id='${category.id}' onClick='addSubCategory(this.id);'>${category.category}
    </a>
    </li>
    <hr>

 `
}

function categorytwo(category) {
    return ` 
    <li class="nav-item">
    <a class="nav-link" id="${category.id}" href="#" data-toggle="dropdown">${category.category}
    </a>
    </li>
 `
}

function categoryList() {
    $.ajax({
        type: "GET",
        url: category_list,
        success: function (response) {
            data1 = response['productcategory_list']
            document.getElementById('categories_1').innerHTML = ` ${data1.map(categoryOne).join('')}`

            data2 = response['productcategory_list2']
            document.getElementById('categories_2').innerHTML = ` ${data2.map(categorytwo).join('')}`
        },
    });
}

$(document).ready(function () {
    categoryList();
})
