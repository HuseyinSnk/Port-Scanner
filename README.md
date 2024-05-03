# Port-Scanner
This is a simple Python tool for scanning open ports of a URL specified by the user. Using the tool, you can obtain the IP address of a specific URL and then scan a specified list of ports to find open ports.

How to Use
1-Requirements: To run this tool, you'll need Python 3 and the tkinter module. tkinter is generally part of Python's standard library and comes bundled with most Python distributions.
2-Installation: First, clone this repository or download the files. Then, in your terminal or command prompt, navigate to the directory containing the files and run the command python port_scanner.py to start the tool.
3-Enter URL: Once you've started the tool, enter the URL you want to scan. For example: example.com.
4-Start Scan: Click the "Start Scan" button to initiate the scan. Once the scan is complete, the tool will display the open ports and the IP address.
5-Cancel Scan: If you wish to cancel the scan during the process, you can click the "Cancel" button to stop it.


Notes
This tool is designed solely for scanning open ports of a specific URL. Conducting security tests or unauthorized port scans may be illegal and unethical. Please adhere to laws and ethical guidelines.
This tool utilizes Python's tkinter module for the graphical user interface (GUI) and provides a simple user experience.
During the scan, TCP connections are used to resolve the IP address of a specific URL and then scan specific ports.
Open ports may indicate the availability of services on the target system and its accessibility from the internet.
