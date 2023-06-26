# AnonFTP   
![Built with Love](https://img.shields.io/badge/Built%20with-%E2%9D%A4%EF%B8%8F-red)
## AnonFTP is a python script that gets an input of a given hosts names and checks if the ftp server in the given host names can be logged in with "anonymous" credentials or not  

## anonymous credentials in ftp 
When it comes to File Transfer Protocol (FTP), anonymous credentials refer to a type of login credentials that allow users to access an FTP server without providing any personal identification information. This feature is often used in public FTP servers or anonymous FTP servers that are designed to provide public access to files.The purpose of anonymous credentials in FTP is to allow users to connect to the server and access certain files or directories without the need for individual user accounts. It is particularly useful for sharing public files, such as software updates, patches, or general information that can be freely distributed.

![Screenshot (133)](https://github.com/ISLAM-XGAMER/AnonFTP/assets/65929613/1f8cb6a3-5f43-4aaf-b9d2-941d422a5779)

The password field is often left empty or disregarded by FTP servers.


## Setup 
```
python3 pip install -r requirements.txt
```
```
python3 AnonFTP.py
```

## Usage
- Check single host ftp server 
```
python3 AnonFTP.py -H hostname
```
- Check multiple host ftp server from txt file
```
python3 AnonFTP.py -f path/to/txt
```
