from typing import List, Tuple
from datetime import datetime
import json
import pandas as pd
from collections import Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
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

  # Agrupar por fecha y usuario, y contar los tweets
  user_date_counts = tweets_df.groupby(['date', 'user']).size().reset_index(name='count')

  # Quedarse con el top 10 de fechas
  top_dates = user_date_counts.groupby('date')['count'].sum().nlargest(10).index

  # Filtrar user_date_counts por las fechas
  top_user_per_date = user_date_counts[user_date_counts['date'].isin(top_dates)]

  # Quedarse con el usuario que tenga más tweets en cada fecha
  top_user_per_date = top_user_per_date.loc[top_user_per_date.groupby('date')['count'].idxmax()]

  # Devolver los resultados en tuplas
  return [(row.date, row.user) for row in top_user_per_date.itertuples(index=False)]
