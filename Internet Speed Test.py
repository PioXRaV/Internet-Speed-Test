import socket
import speedtest

try:
    
    socket.create_connection(("www.google.com", 80))
    
    test = speedtest.Speedtest()
    
    print("Internet Speed ​​Testing, Please Wait.")
    
    print("\nDownload Speed Testing")
    ds = test.download() / 1048576
    print("Upload Speed Testing")
    us = test.upload() / 1048576
    
    ping = round(test.results.ping)
    
    print(f"\nPing: {ping} ms\nDownload: {ds:.2f} Mbps, Upload: {us:.2f} Mbps")
    
except OSError:
        
    print("No Internet Connection")