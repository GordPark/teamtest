from data_processor import reader, writer

data = reader.read_data('test.txt')
print('data', data)
writer.write_data("have a goodday", 'test.txt')