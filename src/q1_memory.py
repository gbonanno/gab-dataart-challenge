from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd
from collections import Counter

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
  
  # Abrir archivo
  fp = open(file_path, 'r+')
  
  # Se bajan los tweets a una lista
  tweets = []

  for line in fp:
    line_json = json.loads(line)
    tweets.append({
        'date': line_json["date"],
        'user': line_json["user"]["username"]
    })

  # Convertir en dataframe
  tweets_df = pd.DataFrame(tweets)

  # Convertir 'date' a datetime
  tweets_df['date'] = pd.to_datetime(tweets_df['date']).dt.date

  # Contar tweets por día y quedarse con los índices del top 10
  date_counts = tweets_df['date'].value_counts().head(10)
  top_dates = date_counts.index

  # Filtrar dataframe con los índices
  top_tweets_df = tweets_df[tweets_df['date'].isin(top_dates)]

  # Contar los tweets por user en las fechas del top 10
  user_date_counts = top_tweets_df.groupby(['date', 'user']).size().reset_index(name='count')

  # Quedarse con el usuario con más tweets por fecha
  top_user_per_date = user_date_counts.loc[user_date_counts.groupby('date')['count'].idxmax()]

  # Devolver los resultados en tuplas
  return [(row.date, row.user) for row in top_user_per_date.itertuples(index=False)]
