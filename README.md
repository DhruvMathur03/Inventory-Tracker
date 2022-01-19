# Shopify Challenge Summer 2022

## Added Feature

I have added the following feature -
- Ability to create “shipments” and assign inventory to the shipment, and adjust inventory appropriately

## Requirements

This project is made using Python and HTML. 
It requires the following libraries/modules :

- flask
- Flask-SQLAlchemy
- Flask-Testing

This project works on a virtual environment (venv in this case)

Create a virtual environment with venv :
```
python3 -m venv <name-of-virtual-environment>
```
Activate the virtual environment :
```
source <name-of-virtual-environment>/bin/activate
```
Deactivate the virtual environment :
```
deactivate
```

## Installation : 
Installing Python on MacOS :

First you'll need Xcode on your Mac, you might already have it, if not then you can get it from the app store
[Xcode](https://apps.apple.com/us/app/xcode/id497799835?ls=1&mt=12)

Now you will need to install homebrew :
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Your terminal will ask for Super User level access, which means you'll need to type your password to run this command.

Finally you can install python3 :
```
brew install python3
```

Installing Python on Windows :

- Navigate to [Python Downloads for Windows](https://www.python.org/downloads/windows/) and install 
  your desired version of python3 (Python 3.10.1 in this case)
- Run the executable installer(select install for all Users and Add Python to PATH checkboxes)
- Verify installation by navigating to the directory in which Python was installed, and then double clicking 'python.exe'
- OR you could go to command prompt, navigate to said directory, and entering 'python3'

- 

Install with pip3 in the virtual environment:

Virtual Environment :
```
pip3 install virtualenv
```
Flask : 
```
pip3 install flask
```
SQLALchemy : 
```
pip3 install -U Flask-SQLAlchemy
```
Flask-Testing : 
```
pip3 install Flask-Testing
```

## Test Data
Add some test data to play around with

```
python3 test_data.py
```

## Run the app

```
python3 server.py
```

## Using the app

Once you run the app, you'll see a url for the server in the terminal/cmd, copy-paste it onto your web browser. 
To see the home page, add a "/home" to the server url. 
You will see 3 tables, with multiple buttons and input fields.
Create Functionality -

To create an inventory item :
- Enter item name in the 'Item Name' input field.
- Enter item description in the 'Item Description' input field.
- Enter quantity in the 'Quantity' input field.
- Click on the Create an Item button

To create a shipment :
- Enter shipment description in the 'Shipment Description' input field.
- Enter carrier in the 'Carrier' input field, you can input 'None' if the shipment hasn't been shipped yet.
- Enter tracking number in the 'Tracking Number' input field, again you can input 'None' if it hasn't been shipped.
- Enter True or False in the 'Is Expedited' input field (whether the shipment has been shipped or not).
- Click on the Create a Shipment button

To add an item to the shipment(create a shipment detail) :
- Enter the inventory id of the item in the 'Inventory ID' input field.
- Enter the shipment id of the shipment in the 'Shipment ID' input field.
- Enter the quantity of the item added in the 'Quantity' input field.
- Click on the Add Shipment Detail button

Update Functionality -

To update an inventory item :
- Enter the updated details in the specified input fields.
- Click on the Edit button

To update a shipment :
- Enter the updated details in the specified input fields.
- Click on the Edit button

To update a shipment detail (quantity of item in shipment) :
- Enter the updated quantity in the specified input field.
- Click on the Edit button

Delete Functionality -

To delete an inventory item :
- Click on the Delete button next to the item you want deleted.

To delete a shipment :
- Click on the Delete button next to the shipment you want deleted.

To delete an shipment detail(item in the shipment) :
- Click on the Delete button next to the detail you want deleted.

## Run Tests

```
python3 test.py
```