import re

def is_valid_email(email):
    # Define a regular expression for a valid email
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Match the input email against the regex
    if re.match(email_regex, email):
        return True
    return False

# Take email input from the user
email_input = input("Enter an email address to validate: ")

# Validate the email
if is_valid_email(email_input):
    print(f"'{email_input}' is a valid email address.")
else:
    print(f"'{email_input}' is NOT a valid email address.")
