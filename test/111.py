class EmailClient:
    def setup(self):
        return "Initializions and configurations!"

    def send_email(self, msg):
        raise NotImplementedError("Use a subclass!")


class GmailClient(EmailClient):
    def send_email(self, msg):
        return "Sending `{}` from Gmail Client".format(msg)


class YahooMailClient(EmailClient):
    def send_email(self, msg):
        return "Sending `{}` from YMail! Client".format(msg)


client = GmailClient()
client.setup()
client.send_email("Hello 1 !")
# If we want to send using Yahoo, we have to construct a new client
yahoo_client = YahooMailClient()
yahoo_client.setup()
yahoo_client.send_email("Hello 2 !")
