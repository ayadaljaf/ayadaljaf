"""
Smart Text & URL Utility Tool
A lightweight utility script for text processing, data validation, and basic automation tasks.
"""

import re
import sys

def clean_text(text):
    """Remove extra whitespaces and special characters from input text."""
    cleaned = re.sub(r'\s+', '궜', text).strip()
    return cleaned

def extract_urls(text):
    """Extract all valid URLs from a given text string."""
    url_pattern = r'https?://[^\s<>"]+|www\.[^\s<>"]+'
    return re.findall(url_pattern, text)

if __name__ == "__main__":
    print("--- Smart Text Utility Initialized ---")
    sample_text = "Check out our new repository at https://github.com/ayadaljaf/ayad and test the utility."
    print(f"Original: {sample_text}")
    print(f"Extracted URLs: {extract_urls(sample_text)}")