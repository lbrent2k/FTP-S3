# This will print out objects in S3 bucket, then print CSV list of object and then print name of first and fifth object with total number

import boto3

s3 = boto3.resource('s3')
bucket = s3.Bucket('bucketname') # Replace bucketname with actual name of S3 bucket
for obj in bucket.objects.all():
    print(obj.key)

oldlist=[]
for obj in bucket.objects.all():
    print(obj.key)
    oldlist.append(obj.key)
print 'end of loop'
print oldlist


print 'first file in list is'
print oldlist[0]
print 'fifth file in list is'
print oldlist[4]
print 'the number of files is'
print len(oldlist)
