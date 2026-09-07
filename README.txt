High-Speed Port Scanner

*_____________________________________*

Project Overview:
A fast and efficient port scanner designed to identify open ports on a target IP address, revealing available services for potential communication.

Technical Stack & Features:

socket Library: Utilized to handle the underlying networking logic and perform the actual TCP connections to check port status.

Multi-threading (concurrent.futures): Implemented to overcome the speed limitations of sequential scanning. A traditional for loop with a 0.5-second timeout per port would take roughly 8.5 minutes to scan 1024 ports. By leveraging multi-threading, this tool performs parallel scans, completing the task in a fraction of the time.


## Educational Purpose

This project was developed for educational and learning purposes to practice Python programming, networking concepts, socket programming, and basic port-scanning techniques. It is intended to be used only on systems and networks that you own or have explicit permission to test. Do not use this tool to scan or access unauthorized systems.
