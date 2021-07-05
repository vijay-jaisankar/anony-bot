# anony-bot
Anonymous Discord Bot

# How to run
- popluate ```keys.py```
- Create a new google form (Can be automated)
- In the top right click on More option(three dots), from there click on Script Editor
- Copy and Paste the `notif.js` file in the script. Don't forget to replace the POST_URL variable with the discord webhook link.
- To get discord webhook link, go to your Server Settings -> Integrations -> Webhooks -> New Webhook
- Change the channel to your admin channel in the webhook settings
- Copy the webhook URL from there
- Paste it on the Google Script region.
- In the Google Scripts, on left you can find 5 options: Overview, Editor, Triggers, Executions and Project Settings
- Click on triggers
- Click on Add Triggers
- Change `Select Event Type` from `On Open` to `On Form Submit`
- Send a message to the form.
- python app.py
