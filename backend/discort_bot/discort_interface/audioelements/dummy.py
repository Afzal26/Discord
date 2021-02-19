from backend.discort_bot.discort_interface.audioelements.audioelement import AudioElement


class Dummy(AudioElement):

    def __init__(self):
        AudioElement.__init__(self)
        self.info = None

    def play(self, guild, voice_client, volume, next_song):
        pass
