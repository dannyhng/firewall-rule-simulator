# Firewall Rule Simulator

This project simulates basic firewall logic using Python. It mimics how real firewalls use rules to block or allow traffic based on IP, port, and protocol.

## 🛡️ What It Does

- Reads firewall rules from a JSON file
- Processes simulated traffic
- Applies rules and prints if the packet is **allowed** or **denied**

## 🔍 Example Output
```bash
Packet to 192.168.1.10:22 via TCP is DENY.
Packet to 192.168.1.15:80 via TCP is ALLOW.
Packet to 192.168.1.25:22 via TCP is ALLOW.
```
## 📚 What You'll Learn (CCNA + Cyber)

- How Access Control Lists (ACLs) work
- Layer 3/4 filtering (IP, port, protocol)
- Why order of rules matters in real-world firewalls
