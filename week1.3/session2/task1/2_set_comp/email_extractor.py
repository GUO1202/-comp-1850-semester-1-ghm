# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]
clean_emails = {email.lower() for email in raw_emails}
print(clean_emails)

raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
valid_emails = {email.lower() for email in raw_emails2 if '@' in email}
print(valid_emails)
