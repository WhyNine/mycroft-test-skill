from mycroft import MycroftSkill, intent_file_handler


class MycroftTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.mycroft.intent')
    def handle_test_mycroft(self, message):
        self.speak_dialog('test.mycroft')


def create_skill():
    return MycroftTest()

