from re import fullmatch

# you need to create a text file with emails (check the emails.txt)
# the output will be a text file "clear_emails.txt"


with open(f"emails.txt", "r", encoding="utf-8") as old:
    emails = old.readlines()

count_before = len(emails)

# this regular expression can be modified according to your preferences
new_emails = set(email.strip().lower() for email in emails if fullmatch(r"[-.\w]{1,25}@[-\w]{1,12}.[rucom]{2,3}", email.strip()))

count_after = len(new_emails)

with open("clear_emails.txt", "w", encoding="utf-8") as new:
    for email in new_emails:
        new.write(email + "\n")

print(f"Total emails: {count_before}")
print(f"Deleted duplicates or nonexistent: {count_before - count_after}")
print(f"Available for anything: {count_after}")
_ = input()
