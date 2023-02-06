Anvil folder contains the code that goes into the Anvi app. 

chatbotAnvi is the Python code that will run on your desktop/server.

Anvil will take user inputs through the web app (message, list of users, and file to attach with message) and call the sendText() function in 
chatbotAnvi which will run the WhatsApp web automation.

Connect your Anvil app with chatbotAnvi by creating an Anvil Uplink. You will get a code after creating an Uplink which will be placed into the
anvil.server.connect() function at the top of chatbotAnvi. 

To maintain the UI I built, copy paste the Form, HTML, and CSS files in the anvi folder to their corresponding locations in your Anvil app.
This is how the current UI looks: https://rha-bulk-whatsapp-messenger.anvil.app/
