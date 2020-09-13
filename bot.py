from irc.bot import SingleServerIRCBot
import requests
from Auth.auth import oauth, client_id
from lib import db, cmds, react


class Bot(SingleServerIRCBot):
    """Initializing Class"""
    def __init__(self):
        self.HOST = "irc.chat.twitch.tv"
        self.PORT = 6667
        self.bot_name = 'amiparinaaa'
        self.client_id = client_id
        self.token = oauth
        self.channel = f"#amiparina"
        # self.channel = f"#vultplay"

        url = f"https://api.twitch.tv/kraken/users?login={self.bot_name}"
        headers = {"Client-ID": self.client_id, "Accept": "application/vnd.twitchtv.v5+json"}
        response_data = requests.get(url, headers=headers).json()
        self.channel_id = response_data["users"][0]["_id"]

        super().__init__([(self.HOST, self.PORT, f"oauth:{self.token}")], self.bot_name, self.bot_name)

    """On ready event"""
    def on_welcome(self, cxn, event):
        for req in ("membership", "tags", "commands"):
            cxn.cap("REQ", f":twitch.tv/{req}")

        cxn.join(self.channel)
        db.build()
        self.send_message("Now online!!!")

    """On public messages"""
    @db.with_commit
    def on_pubmsg(self, cxn, event):
        tags = {kvpair["key"]: kvpair["value"] for kvpair in event.tags}
        user = {"name": tags["display-name"], "id": tags["user-id"]}
        message = event.arguments[0]

        if user["name"] != self.bot_name:
            react.process(bot, user, message)
            cmds.process(bot, user, message)
            # print(f"{user['name']}: {message}")

    """Send message"""
    def send_message(self, message):
        self.connection.privmsg(self.channel, message)


if __name__ == '__main__':
    bot = Bot()
    bot.start()

