# FTP-S3

## Automating the process of **directly** copying files from FTP server to S3.

By copying **directly** the files do not need to be stored on a local server or an EC2 instance.




### To do list

- [ ] Document existing code with detailed comments
- [X] S3 list function writing to variable
- [X] FTP list function writing to variable
- [X] Funtion comparing lists and wrting to variable files missing from S3 bucket
- [X] Copy from FTP to S3 of only missing files
- [ ] Quality check of content completeness and correctness (Are Delta files being copied?)
- [ ] Develop Lambda Function
- [ ] Load/Size Testing (Review times and resource usage for various loads)
- [ ] Security Review (Copy file with encryption at rest)
- [ ] Environment Variables in Lambda Function
- [ ] Multipart upload/large file approach
