# Interactive JSON Dictionary in Python
A lightweight command-line dictionary application built in Python. This tool reads definitions from a JSON file, 
performs exact word lookups, and uses fuzzy string matching to suggest alternative words if a typo is detected.

# Features
1. Exact Match Lookups: Instantly retrieves definitions for valid words found in the dataset.
2. Smart Typo Correction: Automatically suggests the closest matching word if the user makes a spelling mistake (powered by Python's built-in difflib module).
3. Interactive CLI: Runs in a continuous loop so you can look up multiple words without restarting the program.
4. Case-Insensitive: Handles capitalized or lowercase inputs gracefully.

# Usage Example
Enter Word: rain

['Precipitation falling from clouds.']
