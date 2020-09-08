# Subdomain_bruteforce

### whats this Subdomain bruteforcer do?
 This script helps to brute force the subdomain specified inside the file. We just have to specify the target domain name example www.sample.com
 and our own specified subdomain file where we only check for our specified subdomain.
 

 ![](/usage.png)



Here I am using the shodan API to gather the information of the IP address and then using socket, able to find out about the open ports.

## Usage

### Arguments ...?
This script only takes two arguments first one is '-file' which is the subdomain file name of your own. please try to make sure that it lies inside the same directory otherwise specify the full path.
The second argument is the -target domain name like sample.com

Here in this script, i run on google.com with file name sub_domain.txt with few some real subdomain of google like mail, ads, and admin.


![](/usage1.png)


After finding the subdomain which is active, this script also helps us to find out about some common open ports like 80,443,8080



## Please do not try on google and on any other website, for which you don't have the authorisation to do so I am not responsible for anything done by you.


