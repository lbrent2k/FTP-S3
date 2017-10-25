from ftplib import FTP
import io 
import boto3

#Build a list of filenames already in an s3 bucket. 
#List is called oldlist.
s3 = boto3.resource('s3')
bucket = s3.Bucket('bucketname') # Replace bucketname with actual name of S3 bucket
oldlist=[]
for obj in bucket.objects.all():
    oldlist.append(obj.key)
#next we get a list of the names of files on the FTP server into filelist
address='ftp.bla_bla_bla/'
ftp = FTP(address)
ftp.login('name','password')
ftp.cwd('change to sub-directory of interest if needed')
filelist = ftp.nlst()

#Now we compare the lists of filenames to list those that are needed to put in s3
newfiles=[item for item in filelist if item not in oldfilelist]
#get file from ftp server and directly put int s3 for all newfiles
for x in range(0, len(newfiles)-1):
    myfile = io.BytesIO()
    filename = 'RETR ' + newfiles[x]
    resp = ftp.retrbinary(filename, myfile.write)
    myfile.seek(0)
    path = address + newfiles[x]    # I think I may have an error in the value of address??
    #putting file on s3
    s3.Object(s3Bucketname, path).put(Body = myfile)
    
ftp.quit()
