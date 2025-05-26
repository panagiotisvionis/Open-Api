# Prime Factorization API

A complete client-server Python project using Flask and OpenAPI 3.0 that calculates the prime factorization of input integers.

## 🔧 Project Structure

**Folder layout:**

- `python-flask-server-generated/`: Flask-based API server
  - Contains the API logic and implementation under `swagger_server/`
  - Includes the virtual environment `venv/`
- `python-client-generated/`: API client that sends requests
  - Main file: `my_client.py`
  - Client-side logic is under `swagger_client/`

## 🚀 How to Run

### 1. Server

```bash
cd python-flask-server-generated
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
FLASK_DEBUG=development python -m swagger_server
```

The server should be available at: http://localhost:8080

### 2. Client

```bash
cd python-client-generated
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python my_client.py 12 15 100
```

## 📦 API Description

### Endpoint

- `POST /primes`

### Request Body

```json
{
  "input_numbers": [4, 6, 10, 20]
}
```

### Response

```json
{
  "result": [
    { "input_number": 4, "prime_factors": [2, 2] },
    { "input_number": 6, "prime_factors": [2, 3] },
    { "input_number": 10, "prime_factors": [2, 5] },
    { "input_number": 20, "prime_factors": [2, 2, 5] }
  ]
}
```

## 🧠 Features

- Uses **OpenAPI 3.0** for API definition
- **Swagger Codegen** to auto-generate client and server
- **Flask** backend with actual prime factorization algorithm
- Handles input via **CLI** in the client
- Includes error handling and input validation

## 🧰 Technologies

- Python 3.10+
- Flask
- Connexion (for OpenAPI integration)
- Swagger/OpenAPI
- Virtual environments

## 📝 License

This project is licensed under the **MIT License**.

## 👤 Author

Developed by **Panagiotis Vionis**  
Feel free to fork, improve, or contribute!
