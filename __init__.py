from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.log import LOG


class MycroftTest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('test.mycroft.intent')
    def handle_test_mycroft(self, message):
        self.speak_dialog('test.mycroft')

    def initialize(self):
        self.add_event('recognizer_loop:record_begin', self.on_listener_started)
        self.add_event('recognizer_loop:record_end', self.on_listener_ended)
        self.add_event('mycroft.mic.listen', self.on_mycroft_mic_listen)
        self.add_event('mycroft.mic.mute', self.on_mycroft_mic_mute)
        self.add_event('mycroft.skill.handler.start', self.on_handler_start)
        self.add_event('mycroft.skill.handler.complete', self.on_handler_complete)
        self.add_event('play:query', self.on_query)
        self.add_event('play:start', self.on_play)

    def on_handler_start(self, message):
        LOG.info("mycroft.skill.handler.start")

    def on_handler_complete(self, message):
        LOG.info("mycroft.skill.handler.complete")

    def on_query(self, message):
        LOG.info("play:query")

    def on_play(self, message):
        LOG.info("play:start")

    def on_mycroft_mic_mute(self, message):
        LOG.info("mycroft.mic.mute")

    def on_mycroft_mic_listen(self, message):
        LOG.info("mycroft.mic.listen")

    def on_listener_started(self, message):
        LOG.info("recognizer_loop:record_begin")

    def on_listener_ended(self, message):
        LOG.info("recognizer_loop:record_end")


def create_skill():
    return MycroftTest()

