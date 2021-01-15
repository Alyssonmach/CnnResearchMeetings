non_sense_list = ['tree', [[1,2,3], [4, 5, 6]], 4, 55.6, 4 + 5j, (200, 50)]
non_sense_list.append(non_sense_list)

for i in range(0,7):
    print('Data: {}, Type: {}'.format(non_sense_list[i], type(non_sense_list[i])))