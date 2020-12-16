filename = 'content_m_files_exceptions/files/pi_million_digits.txt'

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + "...")
print(len(pi_string))