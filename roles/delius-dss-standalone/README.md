delius-interfaces-offloc standalone
=========

Deploy the Delius DSS Standalone components for offloc.
<hr/>

####This MUST only run on one server at most at any given time. 

<hr/>

This takes a file on a remote server named <yyyymmdd>.zip and extracts a valid prison file from it.

The system only accepts the offloc file from an https source.
The certificate on the server should be trusted by the java keytool. 

For example, for a local server instance on port 4443:
```bash
echo 'generate a local key'
 openssl req -new -x509 -keyout cert.pem -out cert.pem -days 365 -nodes
echo 'import key into java - first convert it'
openssl x509 -outform der -in cert.pem -out cert.der
sudo keytool -import -alias localhost4443 -keystore /usr/java/latest/jre/lib/security/cacerts -file cert.der

```

Then to create a local server for testing with the above certificate (taken from https://gist.github.com/dergachev/7028596) run the following python script
```python
import BaseHTTPServer, SimpleHTTPServer
import ssl

httpd = BaseHTTPServer.HTTPServer(('localhost', 4443), SimpleHTTPServer.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./cert.pem', server_side=True)
httpd.serve_forever()
```

It is then converted to an xml type, which is then sent to the nDeliusDSS-web interface over JAX-WS. This can be accessed over http or https by changing the URL.




Role Variables
--------------

Templates exist in [templates/](templates) folder.

* [DSSWebService.properties.j2](templates/DSSWebService.properties.j2)
    - The nDeliusDSS-web interface http/s location

* [encryption.properties.j2](templates/encryption.properties.j2)
    - The location of the files on the remote file system - which should not need to be changed -,\
     as well as an initialization vector. This should match the iv used in the other properties files, and should be randomised where possible.

* [FileImporter.properties.j2](templates/FileImporter.properties.j2)
    - File locations and the iv for decrypting. The file locations should not need changing.
    
* [FileTransfer.properties.j2](templates/FileTransfer.properties.j2)
    - Location of the unzip utility and other file locations. The file locations should not need changing.

* [HMPSServerDetails.properties.j2](templates/HMPSServerDetails.properties.j2)
    - The URL for the offloc file, as well as the username and password to access it.
    - *The URL MUST be an https URL.*
    - The offloc file should be in the given URL as https://[url]:[port]/[someDir]/yyyymmdd.zip
    

 
Additional variables are listed below:
```yaml
dependencies_s3_bucket: S3 bucket name, local filesystem will be used if not specified
```

Dependencies
------------
This playbook can run prior to the install of the below dependencies but will not be able to import the data into the delius-core product.
* delius-core
* delius-interfaces

Playbook
-----------
For development environment example with release 4.1.7.1 of nDelius: 
* ansible-playbook -i inventory/dev wli-offloc.yml --extra-vars ndelius_version=4.1.7.1

License
-------

BSD
