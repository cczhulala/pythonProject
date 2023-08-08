class GmailProvider:
    def send(self, msg):
        return "Sending `{}` using Gmail".format(msg)


class YahooMailProvider:
    def send(self, msg):
        return "Sending `{}` using Yahoo Mail!".format(msg)

class EmailClient:
                    email_provider = GmailProvider()

    def setup(self):
        return "Initialization and configurations"

    def set_provider(self, provider):
        self.email_provider = provider

    def send_email(self, msg):
        print(self.email_provider.send(msg))


client = EmailClient()
client.setup()
client.send_email("Hello 1 !")

client.set_provider(YahooMailProvider())
client.send_email("Hello 2 !")
