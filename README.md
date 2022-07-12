# ESXi-Phish
Phishing server for ESXi logins with integrated Telegram notifications.

Demo:
![esxi_demo](https://user-images.githubusercontent.com/15061132/178599191-ea7e1710-d6ce-4dae-9407-d9493a5c6b8b.gif)

1. Create a Telegram bot and add it to a group
3. Enter bot API token and group chat id into config.json
4. ??????
5. Profit

BTW you can easily find the Telegram chat ID here:
https://api.telegram.org/bot{{YOUR_TOKEN_HERE}}/getUpdates

Also, you can easily change what port this runs on, or run it with gunicorn, etc. Just read the Flask docs.
