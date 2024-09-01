document.getElementById('view-products-btn').addEventListener('click', function() {
    document.getElementById('product-list').classList.remove('hidden');
    document.getElementById('create-product-form').classList.add('hidden');
    document.getElementById('product-details').classList.add('hidden');
    document.getElementById('product-details-for-update').classList.add('hidden');
    fetchProducts();
});

document.getElementById('create-product-btn').addEventListener('click', function() {
    document.getElementById('create-product-form').classList.remove('hidden');
    document.getElementById('product-list').classList.add('hidden');
    document.getElementById('product-details').classList.add('hidden');
    document.getElementById('product-details-for-update').classList.add('hidden');

});

document.getElementById('product-details-for-update').addEventListener('click', function() {
    document.getElementById('create-product-form').classList.remove('hidden');
    document.getElementById('product-list').classList.add('hidden');
    document.getElementById('product-details').classList.add('hidden');

});

document.getElementById('create-product').addEventListener('submit', function(event) {
    event.preventDefault();

    const product_name = document.getElementById('name').value;
    const description = document.getElementById('description').value;
    const price = document.getElementById('price').value;

    fetch('http://127.0.0.1:8000/api/product/create/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        },
        body: JSON.stringify({ product_name, description, price })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('create-message').textContent = 'Product Created Successfully';
        document.getElementById('name').value = '';
        document.getElementById('description').value = '';
        document.getElementById('price').value = '';
        fetchProducts(); // Refresh the product list
    })
    .catch(error => {
        document.getElementById('create-message').textContent = 'Error creating product';
        console.error('Error:', error);
    });
});

function fetchProducts() {
    fetch('http://127.0.0.1:8000/api/product/list/', {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        }
    })
    .then(response => response.json())
    .then(data => {
        const tbody = document.getElementById('product-table-body');
        tbody.innerHTML = '';
        data.data.forEach(product => {
            const tr = document.createElement('tr');
            tr.innerHTML = `
                <td>${product.id}</td>
                <td>${product.product_name}</td>
                <td>${product.price}</td>
                <td>
                    <button onclick="viewProduct(${product.id})">View</button>
                    <button onclick="viewProductForUpdate(${product.id})">Update</button>
                    <button onclick="deleteProduct(${product.id})">Delete</button>
                </td>
            `;
            tbody.appendChild(tr);
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function viewProduct(id) {
    fetch(`http://127.0.0.1:8000/api/product/retrieve/${id}/`, {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        }
    })
    .then(response => response.json())
    .then(data => {
        const product = data.data;
        const container = document.getElementById('details-container');
        container.innerHTML = `
            <p><strong>ID:</strong> ${product.id}</p>
            <p><strong>Name:</strong> ${product.product_name}</p>
            <p><strong>Name:</strong> ${product.description}</p>
            <p><strong>Price:</strong> ${product.price}</p>
        `;
        document.getElementById('product-list').classList.add('hidden');
        document.getElementById('create-product-form').classList.add('hidden');
        document.getElementById('product-details').classList.remove('hidden');
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function deleteProduct(id) {
    fetch(`http://127.0.0.1:8000/api/product/delete/${id}/`, {
        method: 'DELETE',
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        }
    })
    .then(response => {
        if (response.ok) {
            fetchProducts(); // Refresh the product list
        } else {
            console.error('Error deleting product');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

document.getElementById('back-to-list-btn').addEventListener('click', function() {
    document.getElementById('product-list').classList.remove('hidden');
    document.getElementById('product-details').classList.add('hidden');
});


function viewProductForUpdate(id) {
    fetch(`http://127.0.0.1:8000/api/product/retrieve/${id}/`, {
        headers: {
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        }
    })
    .then(response => response.json())
    .then(data => {
        const product = data.data;
        console.log(product)
        document.getElementById('update-name').value = product.product_name;
        document.getElementById('update-description').value = product.description;
        document.getElementById('update-price').value = product.price;

        document.getElementById('product-list').classList.add('hidden');
        document.getElementById('product-details').classList.add('hidden');
        document.getElementById('create-product-form').classList.add('hidden');
        document.getElementById('product-details-for-update').classList.remove('hidden');

        // Attach event listener to the update button
        document.getElementById('update-product-btn').onclick = function() {
            updateProduct(id);
        };
    })
    .catch(error => {
        console.error('Error fetching product details:', error);
    });
}

function updateProduct(id) {
    const product_name = document.getElementById('update-name').value;
    const description = document.getElementById('update-description').value;
    const price = document.getElementById('update-price').value;

    fetch(`http://127.0.0.1:8000/api/product/update/${id}/`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + localStorage.getItem('access_token')
        },
        body: JSON.stringify({ product_name, description, price })
    })
    .then(response => {
        if (response.ok) {
            alert('Product updated successfully');
            fetchProducts(); // Refresh the product list
            document.getElementById('product-list').classList.remove('hidden');
            document.getElementById('product-details').classList.add('hidden');
            document.getElementById('create-product-form').classList.add('hidden');

        } else {
            alert('Failed to update product');
        }
    })
    .catch(error => {
        console.error('Error updating product:', error);
    });
}

