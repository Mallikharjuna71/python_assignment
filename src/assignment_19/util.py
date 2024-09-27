import re
def matching(s):
    ex = r'^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]{3})$'
    return bool(re.search(ex, s))
email_list = ['arjun37ca@gmail.com', 'abc@qwe', 'asdfghjoiuytrew']
result = filter(matching, email_list)
