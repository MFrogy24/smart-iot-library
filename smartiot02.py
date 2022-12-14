# Smart IoT Library 
import requests
import torchaudio
import matplotlib.pyplot as plt
from IPython.display import Audio, display


def version():
  '''Shows Smart IoT library version'''
  print('Smart Iot Library ver. 1.5')
  print('torchaudio ver. ', torchaudio.__version__)
 
def wave_size(wave):
  if wave.ndim == 1:
    channels, frames = 1, wave.shape[0]
  else:
    channels, frames = wave.shape
  return wave.element_size() * channels * frames

def load_audio(url, fname):
  '''Regresa la señal de audio, sample-rate- metada, bytes-size'''
  r = requests.get(url)
  with open(fname, 'wb') as f:
    f.write(r.content)
  sz = len(r.content)
  meta= torchaudio.info(fname)
  wave, sr = torchaudio.load(fname)
  return (wave, sr, meta, sz)

def print_info(info, fname=None):
  '''Muestra los metadatos de un archivo de audio con la tupla que regresa load_audio'''
  if fname:
    print('-' * 30)
    #print('Filename: ' fname)
    print('-' * 30)
  wave, sr, meta, sz = info 
  channels, frames = wave.shape
  print(f'           Frames: {frames}')
  print(f'         Channels: {channels}')
  print(f'  Audio File size: {sz} bytes')
  print(f'      Tensor size: {wave.element_size() * meta.num_channels * meta.num_frames} bytes')
  print(f'            Dtype: {wave.dtype}' )
  print(f'              Max: {wave.max().item():6.3f}')
  print(f'              Min: {wave.min().item():6.3f}')
  print(f'             Mean: {wave.mean().item():6.3f}')
  print(f'          Std Dev: {wave.std().item():6.3f}')
  print(wave)

def plot_wave(wave, torch=True):
  '''Graficar una señal de audio de PyTorch o NumPy'''
  plt.figure()
  plt.plot(wave[0].numpy() if torch else wave)  

def plot_fft(wave, max_freq=None):
  '''Graficar la señal transformada FFT desde 0 - max_freq range'''
  wave2 = wave[:max_freq] if max_freq else wave 
  wave3 = np.abs(wave2.real)
  plt.figure()
  plt.plot(wave3,  lw=1, color='green')
  
def play_audio(wave, sample_rate, torch=True):
  '''Reproducir señal de audio'''
  channels = (1 if wave.ndim == 1 else wave.shape[0])
  if torch:
    wave = wave.numpy()
    if channels == 1:
      display(Audio(wave, rate=sample_rate))
    elif channels == 2:
      display(Audio((wave[0], wave[1]), rate=sample_rate))
    else: 
      raise ValueError("Forma de la señal no soport mas de 2 canales")
  else: #Numpy array 
    if channels == 1:
      display(Audio(wave, rate = sample_rate))
    else:
      display(Audio(wave[0],wave[1]), rate=sample_rate)
  
 
  
