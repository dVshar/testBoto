from django.shortcuts import render
from django.http import HttpResponse
import boto3
# Create your views here.






def Test(request):
    aws_access_key_id = "AKIA2AWISJYAYXHT3RHC"
    aws_secret_access_key = "JS1iRf8TUe1u9bWaaCRK/IC09hh+I3YpjhXlgubu"
    if request.method=="POST":
        filename = request.POST["file1"]
        client = boto3.client('s3',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
        # s = client.upload_file(r'C:\Users\welcome\Desktop\Requests Python\Boto3\test.jpg', 'eazotel-client-images', "Divyanshu/Picture5.png",ExtraArgs={'ContentType': "image/png"})
        s = client.upload_file(filename, 'eazotel-client-images', "Divyanshu/Picture5.png",ExtraArgs={'ContentType': "image/png"})
        
    return render(request,'Bucket/index.html')