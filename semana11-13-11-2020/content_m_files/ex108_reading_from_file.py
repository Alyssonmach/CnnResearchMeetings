with open("content_m_files_exceptions/files/pi_digits.txt", 'r') as file_object:
    contents = file_object.read()
    print(contents.rstrip())