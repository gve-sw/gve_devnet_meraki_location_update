# GVE DevNet Meraki Location Update
This prototype utilitizes the Meraki webhooks and APIs to update the location of a Meraki switch in the dashboard once the switch is powered on.

![/IMAGES/meraki-location-update-workflow.png](/IMAGES/meraki-location-update-workflow.png)

## Contacts
* Danielle Stacy

## Solution Components
* Meraki APIs
* Meraki Switch
* Flask
* Ngrok

## Prerequisites
#### Meraki API Keys
In order to use the Meraki API, you need to enable the API for your organization first. After enabling API access, you can generate an API key. Follow these instructions to enable API access and generate an API key:
1. Login to the Meraki dashboard.
2. In the left-hand menu, navigate to `Organization > Settings > Dashboard API access`.
3. Click on `Enable access to the Cisco Meraki Dashboard API.`
4. Go to `My Profile > API access`.
5. Under API access, click on `Generate API key`.
6. Save the API key in a safe place. The API key will only be shown once for security purposes, so it is very important to take note of the key then. In case you lose the key, then you have to revoke the key and a generate a new key. Moreover, there is a limit of only two API keys per profile.

> For more information on how to generate an API key, please click [here](https://developer.cisco.com/meraki/api-v1/#!authorization/authorization). 

> Note: You can add your account as Full Organization Admin to your organizations by following the instructions [here](https://documentation.meraki.com/General_Administration/Managing_Dashboard_Access/Managing_Dashboard_Administrators_and_Permissions).

#### Switch serial and locations
This prototype was built to update the location of switch. For the purposes of this demo, the location is included in a CSV file along with the serial number of the switch. The location could also be obtained with a GPS location tracker if the code had a way to communicate with the GPS tracker (API call), but this demo did not have access to one. 
To get the serial of the switch, follow these steps:
1. Login to the Meraki dashboard.
2. In the left-hand menu, navigate to `Switch > Monitor > Switches`.
3. From here, a list of switches in the network will be displayed. Click an entry for a switch.
4. The screen will now display details for that particular switch. The serial can be found on the left side of the screen under the `Serial` section. Note the serial for later.
5. Notice in this table, there is also a location detail. This is the information that will be edited by the script. Be sure to have the latitude and longitude coordinates of where the switch will be for later.
5. To navigate to other switches, click the arrows `<>` above the left column with the switch details.

#### Ngrok
For this prototype, ngrok was used for local testing purposes. To use ngrok, you will need to set up an account at [dashboard.ngrok.com](https://dashboard.ngrok.com/login). 
1. Click `Sign up for free!` to create an account. 
2. Once you have created an account, download ngrok from either the dashboard with the `Download` button or from [ngrok.com/download](https://ngrok.com/download) by following those directions. 
3. Then you must add your authtoken with the command `ngrok authtoken <token>`. You may find your token on the ngrok dashboard.

## Installation/Configuration
1. Clone this repository with `https://github.com/gve-sw/gve_devnet_meraki_location_update`
2. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).
3. Add Meraki API key that you retrieved in the Prerequisites section to environment variables in the file .env
```
API_KEY = "API key goes here"
```
4. Install the requirements with `pip3 install -r requirements.txt`.
5. Add the switch serials and location coordinates to the CSV file that you retrieved in the Prerequisites section.

## Usage
To run the program, use the command:
```
$ flask run
```

Then, Meraki requires https servers to send webhooks to. To launch a public url, start an ngrok tunnel with the following command in a new terminal:
```
$ ngrok http 5000
```

Copy the `https` forwarding address from the window where you started the ngrok tunnel.

Now create a webhook in the Meraki dashboard with the `https` forwarding address as the URL.
1. Login to the Meraki dashboard
2. In the left-hand menu, navigate to `Network-wide > Configure > Alerts`
3. Scroll down to the Webhooks section and click `Add an HTTP server`
4. Give the server a name, paste the `https` forwarding address as the URL, and leave the Payload template as Meraki
5. Add the newly created server as a default recipient at the top of the page under `Alert Settings`
6. Click `Save` at the bottom of the page.

Now that the server and webhook are set up, the location of the Meraki switches in the network where the webhook is set up will update upon power up.

> To learn more about Meraki Webooks, you can read the documentation shared [here](https://developer.cisco.com/meraki/webhooks/#!introduction/overview)

# Screenshots

![/IMAGES/0image.png](/IMAGES/0image.png)

Spinning up web servers
![/IMAGES/web-server-launched.png](/IMAGES/web-server-launched.png)

Adding server to Meraki Webhook server
![/IMAGES/webhook-servers.png](/IMAGES/webhook-servers.png)

Adding Webhook server as alert recipient
![/IMAGES/alert-recipients.png](/IMAGES/alert-recipients.png)

Webhook payload when switch powers on
![/IMAGES/webhook-payload.png](/IMAGES/webhook-payload.png)

Switch location before the script  
![/IMAGES/before-script.png](/IMAGES/before-script.png)

Switch location after the script  
![/IMAGES/after-script.png](/IMAGES/after-script.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
