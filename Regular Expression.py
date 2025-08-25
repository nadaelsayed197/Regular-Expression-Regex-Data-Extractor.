import re

# Lists to store extracted data
names = []
emails = []
phones = []

# Open the input file and read all lines
with open("data.txt", "r") as file:
    lines = file.readlines()

# Regular expression patterns
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\+?\d[\d\s\-]{7,}\d"
name_pattern = r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})\b"

# Extract emails, phones, and names
for line in lines:
    # Find all email matches
    email_matches = re.findall(email_pattern, line)
    emails.extend(email_matches)

    # Find all phone matches
    phone_matches = re.findall(phone_pattern, line)
    phones.extend(phone_matches)

    # Remove emails and phones from line to clean the text
    line_cleaned = re.sub(email_pattern, '', line)
    line_cleaned = re.sub(phone_pattern, '', line_cleaned)

    # Find all name matches in the cleaned line
    name_matches = re.findall(name_pattern, line_cleaned)
    names.extend(name_matches)

# Print results to console
print("Names:", names)
print("Phones:", phones)
print("Emails:", emails)

# Save results to an output file
with open("output.txt", "w") as f:
    f.write("Names:\n")
    for name in names:
        f.write(name + "\n")

    f.write("\nPhones:\n")
    for phone in phones:
        f.write(phone + "\n")

    f.write("\nEmails:\n")
    for email in emails:
        f.write(email + "\n")