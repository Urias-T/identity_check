## Identity Check 🕵🏽

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

Create a virtual environment adn activate it :

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

