import speech_recognition as sr
import wave
import contextlib
from os import path
from multiprocessing.dummy import Pool as ThreadPool

recognizer = sr.Recognizer()

def recognize(audio):
	try:
		value = recognizer.recognize_google(audio)
	except sr.UnknownValueError:
		print("Couldn't understand the audio")
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
	return value

meeting_audio = sr.AudioFile('meeting_audio.wav')
fname = 'meeting_audio.wav'

with contextlib.closing(wave.open(fname,'r')) as f:
	frames = f.getnframes()
	rate = f.getframerate()
	duration = frames/float(rate)
	print(duration)

audio = []
sample_time = 0
i = 0

with meeting_audio as source:
	recognizer.adjust_for_ambient_noise(source, duration=0.5)
	while sample_time<duration:
		audio[i] = recognizer.record(source, duration=4)
		i+=1
		sample_time+=4

pool = ThreadPool(13)
results = pool.map(recognize(), audio)