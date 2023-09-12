import boto3
import warcio
import csv

# ALL YOU HAVE TO DO IS FILLING HERE #
ACCESS_KEY = ''
SECRET_KEY = ''
FILE_EXTENSION= '.dgn'
CSV_FILENAME=''
# ----------- #

s3 = boto3.Session().client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
with open(CSV_FILENAME) as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    a = 1
    for row in reader_obj:
        warc_filename = row[1]
        warc_record_offset= int(row[2])
        warc_record_length= int(row[3])
        warc_range = 'bytes={}-{}'.format(warc_record_offset, warc_record_offset + warc_record_length - 1)
        obj = s3.get_object(Bucket="commoncrawl", Key=warc_filename, Range=warc_range)
        stream = obj['Body']
        record = next(warcio.ArchiveIterator(stream))
        file_data = record.content_stream().read()
        file_to_write= str(a) + FILE_EXTENSION
        filem=open(file_to_write,'wb')
        filem.write(file_data)
        filem.close()
        a = a+1;
