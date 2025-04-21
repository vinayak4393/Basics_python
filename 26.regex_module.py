#r"\+?\d{1,3}?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}"
#r"...": (Raw String Notation)
#a-z: Lowercase letters (a to z).
#A-Z: Uppercase letters (A to Z).
#0-9: Digits (0 to 9).
#.: Period (.).
#_: Underscore (_).
#%: Percent (%).
#+: Plus (+).
#-: Hyphen (-).

#+: The quantifier + means "one or more" of the preceding characters. 
#So, this part matches a sequence of one or more characters from the list above.

#\.: (Literal Dot)
#{2,}: This is a quantifier that means "two or more".
#So, the TLD must have at least two letters.
#For example, .com, .org, and .net are valid, but .x would not match.



import re

def find_all_emails(text):
    """Find all email addresses in the given text."""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails = re.findall(pattern, text)
    print("Found Emails:", emails)


#r"\+?\d{1,3}?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}"

#\+? (Optional Plus Sign):
#\+: The backslash escapes the plus sign (+), 
#which is a special character in regular expressions. 
#It ensures that the literal + character is matched.

#?: This is a quantifier that makes the preceding character (the +) optional. 
#The phone number may or may not start with a +.

#This part matches an optional plus sign (+), 
#which is common in international phone numbers.

#\d{1,3}? (Country Code):
#\d: This matches any digit (0-9).

#{1,3}: This is a quantifier that means "match between 1 and 3 digits". 
#This part is used to match a country code, which can be 1, 2, or 3 digits long 
#(e.g., 1 for the USA, 44 for the UK, or 91 for India).

#?: The ? after {1,3} makes the match non-greedy,
# meaning it will try to match the smallest number of digits possible (1, 2, or 3).
# This helps to prevent overmatching in some cases.

#[ -]? (Optional Space or Hyphen): (e.g., +1 123 456 7890 or +1-123-456-7890).



def extract_phone_numbers(text):
    """Extract phone numbers from text (supports different formats)."""
    pattern = r"\+?\d{1,3}?[ -]?\(?\d{3}\)?[ -]?\d{3}[ -]?\d{4}"
    phones = re.findall(pattern, text)
    print("Found Phone Numbers:", phones)

def validate_date_format(date_string):
    """Check if a date follows the format YYYY-MM-DD."""
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    match = re.match(pattern, date_string)
    print(f"Date '{date_string}' is valid:" if match else f"Date '{date_string}' is invalid")

def replace_urls(text):
    """Replace all URLs in text with [LINK]."""
    pattern = r"\d{4}-\d{2}-\d{2}"
    updated_text = re.sub(pattern, "[LINK]", text)
    print("Updated Text:", updated_text)

def regex_examples():
    print("--- Regex Module Examples ---")
    sample_text = """
        Contact us at support@example.com or admin@test.com.
        Visit https://example.com for more info.
        Call us at +1 (555) 123-4567 or 555-987-6543.
        Today's date is 2025-03-23.
    """


    find_all_emails(sample_text)
    extract_phone_numbers(sample_text)
    validate_date_format("2025-03-23")
    validate_date_format("23-03-2025")
    replace_urls(sample_text)

if __name__ == "__main__":
    regex_examples()
