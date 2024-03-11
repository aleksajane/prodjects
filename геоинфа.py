import scipy.io.wavfile as read
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def hilbert(data):
    analytical_signal = signal.hilbert(data)
    amplitude_envelope = np.abs(analytical_signal)
    return amplitude_envelope


def resampling_graph(data, fs):
    resample = 7
    data = data[::resample]
    fs = fs // resample
    data_crop = data[240*fs:241*fs]

    plt.figure(figsize=(12, 4))

    plt.plot(data_crop)
    plt.xlabel("Samples")
    plt.ylabel("Amplitude")
    plt.title("Signal")
    plt.show()
    plt.savefig("Laba2")
    return


def find_impulse(data, start_point, max0, min0, fs):
    id = start_point
    end = len(data) - 84
    if fs != 0 and start_point + int(fs * 0.5) < len(data):
        end = start_point + int(fs * 0.5)
    for i in range(start_point, end):
        counter = 0
        for j in range(0, 84, 14):
            if data[i + j] > 2.5 * min0 or data[i + j + 7] < 0.7 * max0 or abs(data[i + j + 7] - data[i + j]) > 0.8 * (max0 - min0):
                counter += 1
        if counter <= 2:
            id = i
            break
    print(id)
    return id


def formatting(data_am, id0, fs, max0, min0):
    final_format = np.zeros((len(data_am) - id0, 1))
    data_am = data_am[id0:]
    index = 0
    i = 0
    while len(data_am) - index > int(fs * 0.5) and len(data_am) - i > int(fs * 0.5):
        for j in range(i, i + int(fs * 0.5)):
            final_format[index] = data_am[j]
            index += 1
        id = find_impulse(data_am, i + int(fs * 0.5), max0, min0, fs)
        i = id
    return final_format


def main():
    fs, data = read.read('C://Users/evgen/Downloads/signal.wav')

    data_am = hilbert(data)

    resampling_graph(data_am, fs)

    max0 = max(data_am)
    print(max0)
    min0 = min(data_am)
    print(min0)

    id0 = find_impulse(data_am, 0, max0, min0, 0 )
    print(id0)

    data_am = formatting(data_am, id0, fs, max0, min0)

    frame_width = int(0.5 * fs)
    w, h = frame_width, data_am.shape[0] // frame_width
    image = Image.new('RGB', (w, h))

    px, py = 0, 0

    for i in range(len(data_am)):
        data_am[i] = (data_am[i] - min0) / (max0 - min0) * 255

        image.putpixel((px, py), (int(data_am[i]), int(data_am[i]), int(data_am[i])))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break

    image = image.resize((w, 4 * h))
    plt.imshow(image)
    plt.show()
    return


main()