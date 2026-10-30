# FRENCH-ENGLISH FLASHCARD DATASET
This dataset contains a list of the most commonly used French words along with their corresponding English translations. 

# File Structure & Location:
- Original Dataset File: data/french_words.csv
- Processed/Learned File: data/words_to_learn.csv (Generated dynamically when user removes known words)

# Usage in Python (Pandas & Random):
1. Reading the CSV and converting to a list of dictionaries:

   import pandas as pd

   import random

   data = pd.read_csv("data/french_words.csv")

   to_learn = data.to_dict(orient="records")

2. Picking a random word pair:

   current_card = random.choice(to_learn)

   print(f"French: {current_card['French']}")

   print(f"English: {current_card['English']}")

3. Removing known words and updating the progress file:

   to_learn.remove(current_card)

   new_data = pd.DataFrame(to_learn)

   new_data.to_csv("data/words_to_learn.csv", index=False)
