from mycroft import MycroftSkill, intent_file_handler


class GetTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.get.intent')
    def handle_time_get(self, message):
        self.speak_dialog('time.get')


def create_skill():
    return GetTime()

