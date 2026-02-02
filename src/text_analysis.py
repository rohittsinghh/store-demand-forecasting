# src/text_analysis.py
import re
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text

def extract_keywords(file_path):
    with open(file_path, "r") as f:
        text = clean_text(f.read())
    return Counter(text.split()).most_common(10)
