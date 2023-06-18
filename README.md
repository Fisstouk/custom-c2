# Custom Command & Control in Python

This script allows you to get the network information of the host or the target, and ping them by parsing the addresses in a text file.  
It allows you to scan the ports opened and get the banners from them, displaying the service started.

## Secure tunnel

You can create a TCP tunnel between your target (client) and your host (server). To do so, you need to have a certificate and a key, `cert.pem` and `key.pem` files respectively.  
To do so, please use the command below:

`openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem`

The DNS exfiltration and persistence on Windows can be improved.
