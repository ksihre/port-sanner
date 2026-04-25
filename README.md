# 🔍 Port Scanner

#Overview
This project is a Python-based port scanner designed to identify open and closed ports on a target system. It helps in understanding how network services operate and how ports are used for communication in a network.

#Features
- Scan open and closed ports on a target IP address
- Supports scanning a range of ports
- Displays results in a clear and readable format
- Helps analyze network services running on different ports

#Technologies Used
- Python
- Socket Programming
- Basic Networking Concepts

#How It Works
The scanner attempts to establish a connection with each port on the target system.  
If the connection is successful, the port is marked as **open**; otherwise, it is considered **closed**.

#How to Run

1. Make sure Python is installed  
2. Clone the repository or download the file  
3. Run the script:

```bash
python port_scanner.py
