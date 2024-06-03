from typing import List, Tuple
import json
import pandas as pd
import emoji
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
  # Crear Counter para los emojis
  emoji_counter = Counter()

  # Abrir archivo
  with open(file_path, 'r') as fp:
    # Procesar cada línea del archivo
    for line in fp:
      line_json = json.loads(line)
      content = line_json.get("content", "")

      # Extraer los emojis
      for char in content:
        if char in emoji.EMOJI_DATA:
          emoji_counter.update(char)

  # Devolver el top 10 de emojis
  return emoji_counter.most_common(10)
