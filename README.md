Inventory tracking web application implemented using **FastAPI**.

Additional feature implemented: `Push a button export product data to a CSV`.

## 🛠️ Deployment

### 1. Optional: Create a virtual environment

```bash
conda create -n webapp python=3.9
conda activate webapp
```

### 2. Download FastAPI and all its dependencies

```bash
pip install fastapi[all]
```

### 3. Run the app

```bash
uvicorn src.main:app --reload
```

You should then be able to see the app running on http://127.0.0.1:8000/

## 📚 User's Guide

The main page redirects to the automatically generated Swagger docs, which allows us to test our API endpoints.
![swagger-main](/assets/swagger-main.jpg)

### Adding a product to inventory

As an example, we can add a product to our inventory using Swagger:

1. Click on `POST /product` to expand it and see the API details.
![swagger-create](/assets/swagger-create.jpg)

2. Click on `Try it out` and fill in desired values for the product to add.
![swagger-create-request](/assets/swagger-create-request.jpg)

3. Click on `Execute` and Swagger will initiate the API request and display the response:
![swagger-create-response](/assets/swagger-create-response.jpg)

### Exporting inventory to CSV

We can export the inventory as CSV and download it at the click of a button using Swagger as well!

1. Click on `GET /export_csv` to expand it, then `Try it out` and `Execute` as before.
![swagger-csv-request](/assets/swagger-csv-request.jpg)

2. Click on `Download file` to launch a download of the inventory in CSV format to your computer.
![swagger-csv-response](/assets/swagger-csv-response.jpg)

3. You now have access to the exported inventory in `products.csv`!
![csv-example](/assets/csv-example.jpg)
