user_email = input("Enter your email address: \r\n")
# ifemidecole@gmail.com
user_list = user_email.split('@')
username = user_list[0]
domain_name = user_list[1].split('.')

popular_domains = {
"gmail": "Google",
"icloud": "Apple",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

if domain_name[0] in popular_domains.keys():
    print(f"Hey {username}, I see your email is registered with {popular_domains[domain_name[0]]}. That's cool.")    
else:
    print(f"Hey {username}, looks like you've got your own custom setup at {domain_name[0].title()}. Impressive!")