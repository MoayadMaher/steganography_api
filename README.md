# Steganography API

Welcome to the Steganography API! This API allows you to hide messages within images or audio files, providing an extra layer of security for your communications.

## Features
- Easy Integration: Quickly integrate the API with your existing systems.
- High Performance: Leverage the power of FastAPI for fast and efficient operations.
- Scalable and Secure: Built with Docker, ensuring scalability and secure deployment.

## Installation
### Prerequisites
- Docker
- Python 3.8+

### Clone the Repository
```bash
git clone https://github.com/yourusername/steganography-api.git
cd steganography-api
```

### Build and Run with Docker
```bash
docker build -t steganography-api .
docker run -p 8000:8000 steganography-api
```

### Run Locally without Docker
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Environment Variables
To configure the Steganography API, you need to set up the environment variables in an `.env` file in the root directory of your project. Here are the variables you can set:
```makefile
CLOUDINARY_CLOUD_NAME=your_secret_cloud_name
CLOUDINARY_API_KEY=your_secret_key
CLOUDINARY_API_SECRET=your_secret_key
```

Make sure to restart the server after making changes to the `.env` file.

## Usage

### Encoding a Message
Send a POST request to the `/encode` endpoint with an image/audio file and the message you want to hide.

### Decoding a Message
Send a POST request to the `/decode` endpoint with the steganography file to extract the hidden message.

## API Endpoints

### Encode Message

URL: `/hide-text`

Method: POST

Request:
- `image_url`: Image URL (required)
- `text`: Message to hide (required)

Response: Returns the file with the hidden message.

### Decode Message

URL: `/extract-text`

Method: POST

Request:
- `image_url`: Image URL (required)

Response: Returns the hidden message.

## Examples

### Encode Example
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/hide-text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image_url": "image url",
  "text": "string"
}'
```

### Decode Example
```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/extract-text/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "image_url": "image url"
}'
```

## Using with Shield Stack

The Steganography API is also a component of the comprehensive Shield Stack cybersecurity platform. This means you can easily use it with other services offered by Shield Stack for a huge security solutions. 

