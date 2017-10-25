from ftplib import FTP
import io 
import boto3


s3= boto3.resource('s3')

s3Bucketname = 'bucketname' # Insert name of s3 bucket

ftp = FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()
ftp.cwd('pubchem/RDF/descriptor/compound')

address =  'ftp.ncbi.nlm.nih.gov/pubchem/RDF/descriptor/compound/'

filelist = ftp.nlst()

for x in range(0, len(filelist)-1):
    myfile = io.BytesIO()
    filename = 'RETR ' + filelist[x]
    resp = ftp.retrbinary(filename, myfile.write)
    myfile.seek(0)
    path = address + filelist[x]
    #putting file on s3
    s3.Object(s3Bucketname, path).put(Body = myfile)


ftp.quit()
