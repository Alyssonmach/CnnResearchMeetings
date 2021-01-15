filename = "content_m_files_exceptions/files/pi_digits.txt"

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))