#Unique Email Addresses

def numUniqueEmails(self, emails):

    res = set()
    for email in emails:
        name, domain = email.split("@")
        name = name.split("+")[0].replace(".", "")
        res.add(name + "@" + domain)
    return len(res)

