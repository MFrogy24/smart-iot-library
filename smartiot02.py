# Smart IoT Library 
import requests
import torchaudio

def version():
  '''Shows Smart IoT library version'''
  print('Smart Iot Library ver. 1.1')

def load_audio(url, fname):
  '''Regresa la señal de audio, sample-rate- metada, bytes-size'''
  r = requests.get(url)
  with open(fname, 'wb') as f:
    f.write(r.content)
  sz = len(r.content)
  meta= torchaudio.info(fname)
  wave, sr = torchaudio.load(fname)
  return (wave, sr, meta, sz)
