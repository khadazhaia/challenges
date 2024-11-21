from main import remove_domain

print("remove_domain('test@gmail.com')", remove_domain('test@gmail.com') == 'test')
print("remove_domain('test')", remove_domain('test@gmail.com') == 'test')
print("remove_domain('@gmail.com')", remove_domain('@gmail.com') == '')
print("remove_domain('')", remove_domain('') == '')
print("remove_domain(1)", remove_domain(1) == -1)
print("remove_domain(None)", remove_domain(None) == -1)
print("remove_domain('1@gmail.com')", remove_domain('1@gmail.com') == '1')
