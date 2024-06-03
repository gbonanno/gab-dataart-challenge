from typing import List, Tuple
import json
import pandas as pd
import emoji
from collections import Counter

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
  # Crear Counter para los usuarios mencionados
  mention_counter = Counter()

  # Abrir archivo
  with open(file_path, 'r') as fp:
    # Procesar cada línea del archivo
    for line in fp:
      line_json = json.loads(line)
      mentioned_users = line_json.get("mentionedUsers", [])

      # Actualizar el Counter para los usuarios mencionados
      if mentioned_users:
        for user in mentioned_users:
          mention_counter[user["username"]] += 1

  # Devolver el top 10 de usuarios mencionados
  return mention_counter.most_common(10)
