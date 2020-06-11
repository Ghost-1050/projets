import miniaudio
def son_chrono():
    stream = miniaudio.stream_file("buzzer1.mp3")
    device = miniaudio.PlaybackDevice()
    device.start(stream)
    input("\n Appuyer sur Enter pour passer à la suite du programme :")
    device.close()


