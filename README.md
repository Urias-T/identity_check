# Identity Check 🕵🏽

Identity Check is an endpoint built to facilitate KYC (Know Your Customer) processes in digital products. 

## Use Case 📝

On a digital product, the user uploads his/ her identification card, takes a live picture with their device's camera and fills out a form with their details. 
The live image, the identification card and their name is sent to this endpoint and the endpoint verifies using **image recognition** that the face in the identity card matches that
which is in the live image. After which, using **optical character recognition**, verification is made that the name passed in from the form matches that on the identity card. 


## Running Locally 💻

Follow these steps to set up and run the service locally :

### Installation
Clone the repository :

```
git clone https://github.com/Urias-T/identity_check.git
```

Navigate to the project directory :

```
cd identity_check
```

Create a virtual environment and activate it :

```
python -m venv venv
venv/Scripts/activate
```

Install the required dependencies in the virtual environment :

```
pip install -r requirements.txt
```

Launch the copilot service locally :

```
python main.py
```

That's it! The service is now up and running on ```localhost:8080```. 🤗

## Endpoint Documentation 📖

**Endpoint:**

- Method: POST
- Route: /verify

**Request Parameters:**
- image1: Live image file (Required)
- image2: ID image file (Required)
- name: Name associated with the ID (Required)

**Supported File Types:**
- Supported file types for image uploads: jpg, jpeg, png

**Example Usage:**
```bash
curl -X POST \
  -F 'image1=@live_image.jpg' \
  -F 'image2=@id_image.jpg' \
  -F 'name=John Doe' \
  http://localhost:8080/verify
```

**Response Codes:**
- 200: Successful verification.
- 400: Bad request - Missing image files, no selected file, or invalid file format.
- 401: Unauthorized - Face mismatch or name mismatch.
- 500: Internal Server Error - An unexpected error occurred during the verification process.

**Response Body:**

1. Success Response (HTTP 200):
```json
  {
    "status": "Success",
    "message": "Verified",
    "details": {
        "face_match": true,
        "name_match": true
    }
}
```

2. Failure Response (HTTP 401):
- Face Mismatch:
```json
    {
        "status": "Failure",
        "message": "Face Mismatch",
        "details": {
            "face_match": false,
            "name_match": false
        }
    }
```

- Name Mismatch:

```json
    {
        "status": "Failure",
        "message": "Name Mismatch",
        "details": {
            "face_match": true,
            "name_match": false
        }
    }
```

3. Error Response (HTTP 500):
```json
{
    "status": "Error",
    "message": "An error occurred",
    "details": {
        "error": "<error_message>"
    }
}
```

**Error Conditions:**
- If any required parameter is missing, the endpoint will return a 400 error with an appropriate error message.
- If the selected file for either image is empty or the file format is not supported, a 400 error will be returned.
- In case of face or name mismatch, the endpoint returns a 401 error with details indicating the reason for failure.
- If an unexpected error occurs during the verification process, a 500 error will be returned with details of the error.

## Contributing 🙌🏽
If you want to contribute to this project, please open an issue and submit a pull request.


## License ⚖️
This project is made available under the [MIT License](https://github.com/Urias-T/identity_check/blob/main/LICENSE). 
