from typing import List, Tuple
import json
import pandas as pd
import emoji
from collections import Counter, defaultdict

# Función para extraer los emojis en base a EMOJI_DATA
def extract_emojis(text):
  emoji_count = defaultdict(int)
  for char in text:
    if char in emoji.EMOJI_DATA:
      emoji_count[char] += 1
  return emoji_count

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
  # Inicializar el Counter de emojis
  emoji_counter = Counter()

  # Abrir archivo
  with open(file_path, 'r+') as fp:
    # Procesar cada línea del archivo
    for line in fp:
      line_json = json.loads(line)
      content = line_json.get("content", "")

      # Extraer los emojis
      emojis = extract_emojis(content)
      emoji_counter.update(emojis)

  # Devolver el top 10 de emojis
  return emoji_counter.most_common(10)
