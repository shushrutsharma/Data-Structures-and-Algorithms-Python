from demo import bisection_iter, analyze_func, generate_emails

list_of_domains = ['gmail.com', 'yahoo.com', 'hotmail.com']

total_email = int(input("Number of emails in the list : "))

emails = generate_emails(list_of_domains, total_email)

email = 'shushrut@gmail.com'
email2 = 'sk6554@gmail.com'
emails.append(email)

sorted_emails = sorted(emails)

index, found = bisection_iter(email, sorted_emails)

print(found)

if index == None:
    print("Email not found")

else:
    print(f"Element at index : {index} is {sorted_emails[index]}")

analyze_func(bisection_iter, email, sorted_emails)
analyze_func(generate_emails, list_of_domains, total_email)

