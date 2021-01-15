filename = "content_m_files_exceptions/files/pi_digits.txt"

with open(filename, 'r') as file_object:
    for line in file_object:
        print(line.rstrip())