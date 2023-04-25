from pydub import AudioSegment

AudioSegment.from_mp3("audio/Shape Of You.mp3").export("audio/ShapeOfYou1.wav", format="wav")