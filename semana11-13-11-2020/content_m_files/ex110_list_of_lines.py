filename = "content_m_files_exceptions/files/pi_digits.txt"

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())