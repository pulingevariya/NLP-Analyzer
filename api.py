import paralleldots

class API:

    def __init__(self):
        paralleldots.set_api_key('v2k3r4A4FuHR6uaaaBYhv4W12lnywhWsZfarZ6ypTuQ')

    def ner(self, text):
        ner = paralleldots.ner(text)

        return ner

    def sa(self, text):
        sa = paralleldots.sentiment(text)

        return sa

    def acc(self, text):
        acc = paralleldots.abuse(text)

        return acc