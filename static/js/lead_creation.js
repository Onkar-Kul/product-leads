document.addEventListener('DOMContentLoaded', async function() {
    const productsDropdown = document.getElementById('interested_products');

    try {

        const response = await fetch('http://127.0.0.1:8000/api/product/list');
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const products = await response.json();


        products.data.forEach(product => {
            const option = document.createElement('option');
            option.value = product.id;
            option.textContent = product.product_name;
            productsDropdown.appendChild(option);
        });

    } catch (error) {
        console.error('Error fetching products:', error);
    }
});

document.getElementById('lead-form').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const selectedProducts = Array.from(formData.getAll('interested_products'));
    const data = {
        name: formData.get('name'),
        email: formData.get('email'),
        phone_number: formData.get('phone_number'),
        interested_products: selectedProducts
    };

    try {
        const response = await fetch('http://127.0.0.1:8000/api/lead/create/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const result = await response.json();
        document.getElementById('response-message').innerText = "Lead created successfully!";
    } catch (error) {
        document.getElementById('response-message').innerText = "Error creating lead: " + error.message;
    }
});
