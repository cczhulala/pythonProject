## Composition
class GmailProvider:


    def send(self, msg):


        return "Sending `{}` from Gmail Client".format(msg)


class YahooMailProvider:


    def send(self, msg):


        return "Sending `{}` from YMail Client".format(msg)


class HotMailProvider:


    def send(self, msg):


        return "Sending `{}` from HotMail Client".format(msg)


class Mail_163_Provider:


    def send(self, msg):


        return "Sending `{}` from 163Mail Client".format(msg)


class MyEmailProvider:


    def send(self, msg):


        return "Sending `{}` from MyEmail Client".format(msg)


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

client.set_provider(HotMailProvider())
client.send_email("Hello 3 !")

client.set_provider(Mail_163_Provider())
client.send_email("Hello 4 !")

client.set_provider(MyEmailProvider())
client.send_email("Hello 5 !")
