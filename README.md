# Custom Port Scanner



## Description
This is my custom implementation of a port scanner written in Python. It takes two command-line parameters: the first is the designated IPv4 address of the ports you wish to scan, and the second is the number of ports you want to scan. Once the scan is completed, the tool will return a list of open ports.
I've tested this with both public and private IP addresses, and it seems to work for both. Right now, the tool is only single-threaded, meaning that it is really slow when you start scanning hundreds to thousands of ports.
I plan to include more command-line arguments to allow options for multithreading, scanning specific ports and port ranges, or even just scanning well-known ports. I also plan to allow for the scanning of IPv6 addresses, but testing this will be harder because the network I have been testing on does not have IPv6 enabled.
 have been testing on does not have IPv6 enabled.

Note: because this is still in active development I would not recommend using it in its present state



## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
