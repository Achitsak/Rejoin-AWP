import requests
from datetime import datetime
from time import sleep

class RobloxTracker():
    def __init__(self):
        self.webhook_url = 'https://discord.com/api/webhooks/1289108538899300403/4ddZyTFRT8b_qwvbTgp4PSxOKKbS1__SVjBcGDKDG71zHZAMywalZwxGdEKoJTxOU4OA'
        self.current_version = None
        self.last_version = None

    def send_discord_alert(self, new_version):
        now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        embed = {
            "color": 16711680,  # สีแดง
            "description": f"**🚨 [Roblox] New Version: `{new_version}` {now}**"
        }

        data = {
            "content": None,
            "embeds": [embed],
            "attachments": []
        }
        try:
            response = requests.post(self.webhook_url, json=data)
            if response.status_code == 204:
                print('success!')
            else:
                pass
        except Exception as e:
            pass

    def get_version_roblox(self):
        response = requests.get('https://clientsettings.roblox.com/v2/client-version/WindowsPlayer')
        if response.status_code == 200:
            data = response.json()
            new_version = data.get('clientVersionUpload', None)

            if self.current_version is None:
                self.current_version = new_version
                self.last_version = new_version
            elif new_version != self.current_version:
                self.last_version = self.current_version
                self.current_version = new_version
                # Update
                self.send_discord_alert(self.last_version, self.current_version)
        else:
            pass

if __name__ == '__main__':
    tracker = RobloxTracker()
    while True:
        tracker.get_version_roblox()
        sleep(600)

