import matplotlib.pyplot as plt
import math
import numpy as np


# ### Generating a sin wave with time >>  x = amplitude *   sin(2* pi * (f/fs) * n + phase shift)
# # f -> frequency , fs -> sampling rate , n -> time interval of repeating the sampling ( should be inverse the ratio f/fs to get 1 wave)

# # cycles = 4
# # sampleRate = 160000
# # f1 = 800
# # waveform = [8 * math.sin(2.0 * math.pi * f1/ sampleRate * i ) for i in range(int(cycles * (sampleRate/f1)))]
# # Tperiod = [i / sampleRate for i in range(len(waveform))]

# # plt.plot(Tperiod,waveform)
# # plt.show()

# # spectrum = np.fft.rfft(waveform)
# # spectrumMod = 20 * np.log10(np.abs(spectrum))
# # spectrumPhase = 180 / math.pi * np.angle(spectrum)
# # frequencyBins = [i*len(spectrum) * sampleRate/2 for i in range(len(spectrum))]
# # plt.subplot(2,1,1)
# # plt.semilogx(spectrumMod, label = 'sin wave spectrum')
# # plt.legend(loc = 'upper right')
# # plt.grid(1)
# # plt.title("Spectrum")
# # plt.ylabel("Freqdsad")
# # plt.subplot(2,1,2)
# # plt.semilogx(spectrumPhase, label = "sin wave phase")
# # plt.grid(1)
# # plt.xlabel("power [db]")

# def stop(event):
# 	global STOP_FLAG
# 	STOP_FLAG = True

# fig = plt.figure(1)
# fig.canvas.mpl_connect('close_event',stop)

# STOP_FLAG = False
# f1 = 1000
# cycles = 4
# sampleRate = 20000
# for i in range(10):
# 	f1 += 1.1
# 	if f1 > 5000: f1 = 1000

# 	waveform = [ math.sin(2.0 * math.pi * f1/ sampleRate * i ) for i in range(int(cycles * (sampleRate/f1)))]
# 	Tperiod = [i / sampleRate for i in range(len(waveform))]
# 	plt.cla()
# 	plt.plot(Tperiod, waveform)
# 	plt.grid(1)
# 	plt.draw()
# 	plt.pause(2000)
	
def plotWindowClosedEvent(event):
	global STOP_FLAG
	STOP_FLAG = True

fig = plt.figure(1)
fig.canvas.mpl_connect("close_event",plotWindowClosedEvent)

STOP_FLAG = False
f1 = 1000.0
length = 0.05
sampleRate = 60000
while not STOP_FLAG:

	f1 *= 1.05
	if f1 > 5000: f1 = 1000

	waveform = [math.sin(2 * math.pi * f1 * i /sampleRate) for i in range (int(length * sampleRate))]
	timeBins = [1000 * i / sampleRate for i in range(len(waveform))]

	plt.cla()
	plt.plot(timeBins,waveform,label = 'sin wave of freq %.1f'%f1,)
	plt.xlim([0,3])
	plt.grid(1)
	plt.xlabel("asd")
	plt.ylabel("asda")
	plt.legend(loc = 'upper right')
	plt.draw()
	try:plt.pause(0.1)
	except:pass
