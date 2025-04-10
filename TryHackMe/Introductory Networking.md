---
title: Introductory Networking
date: 2025-04-08
tags:
  - Networking
  - OSI
  - TCP/IP
  - Cybersecurity
  - TryHackMe
---

# Introductory Networking – Fundamentals & Tools

## Intro
This room laid the groundwork for understanding the architecture and protocols that underpin computer networking. It combines theoretical models with practical command-line tools, offering both conceptual clarity and operational know-how—vital for progressing in cybersecurity and networking.

---

## Lab Overview
**Objectives:**
- Grasp the layered models (OSI & TCP/IP) that explain how data traverses networks.
- Understand key functions of each OSI layer along with their real-world counterparts in TCP/IP.
- Learn fundamental network communication principles such as the TCP three-way handshake.
- Explore essential networking tools (ping, traceroute, whois, dig) and their role in troubleshooting and reconnaissance.

**Scope:**
- **Theory:** OSI Model (7 layers with mnemonics and roles) versus the leaner TCP/IP model.
- **Practical:** Applying networking commands to query and verify connectivity and domain information.

---

## Core Concepts

### The OSI Model
- **Purpose:**  
  Provides a standardized framework (7 layers) for understanding network communication.
- **Layers (Mnemonic: _Anxious Pale Shakespeare Treated Nervous Drunks Patiently_):**
  1. **Physical:** Transmission of raw bit streams.
  2. **Data Link:** Physical addressing (MAC addresses) and error checking.
  3. **Network:** Logical addressing (IP addresses) and routing.
  4. **Transport:** Protocol selection (TCP/UDP) and data segmentation (TCP segments).
  5. **Session:** Management of sessions between hosts.
  6. **Presentation:** Data translation, encryption, and compression.
  7. **Application:** Network services to end-user applications.

### The TCP/IP Model
- **Overview:**  
  A practical suite of protocols driving modern networks, mapped roughly to 4 layers:
  - **Application:** Encompasses OSI layers 5–7.
  - **Transport:** Mirrors the OSI Transport layer (choice between TCP and UDP).
  - **Internet:** Handles IP addressing and routing, akin to the OSI Network layer.
  - **Network Interface (Link):** Combines OSI’s Physical and Data Link layers.
- **Key Points:**  
  - Introduced by the DoD in 1982, TCP/IP is the de facto standard.
  - Its simplification (4 layers) streamlines how we understand encapsulation and de-encapsulation.

### Networking Tools & Protocols

#### TCP Three-Way Handshake
- **Concept:**  
  TCP is connection-based; establishing a connection requires:
  1. **SYN:** Client requests connection.
  2. **SYN/ACK:** Server acknowledges and synchronizes.
  3. **ACK:** Client confirms, finalizing the connection.
- **Importance:**  
  Ensures reliable, lossless data transmission (retransmission of missing packets as needed).

#### Practical Utilities
- **Ping:**  
  - Uses ICMP to test network reachability.
  - Also reveals IP addresses behind domain names.
- **Traceroute:**  
  - Maps the journey (hops) a packet takes from source to destination.
  - Useful for diagnosing routing issues.
- **Whois:**  
  - Queries domain registration details.
  - Helps uncover registrant information, domain history, and tech contacts.
- **DNS & Dig:**  
  - **DNS:** Resolves human-friendly domain names to IP addresses.
  - **Dig:** Manually queries DNS servers; reveals detailed DNS record data including TTL values.

---

## Flags Captured / Key Answers

- **OSI Model Questions:**
  - Layer for TCP/UDP protocol selection: **4**
  - Layer for error checking received info: **2**
  - Layer for formatting data pre-transmission: **2**
  - Layer handling transmission/reception: **1**
  - Layer for encryption/compression: **6**
  - Layer tracking communications: **5**
  - Layer accepting application requests: **7**
  - Layer for logical addressing: **3**
  - TCP segments: **Segments**
  - FTP protocol communicates at: **7**
  - Best for live video (transport): **UDP**

- **TCP/IP & Three-Way Handshake:**
  - Model introduced first: **TCP/IP**
  - TCP/IP layer for Transport functions: **Transport**
  - TCP/IP layer for Session functions: **Application**
  - Network Interface covers Data Link & **Physical**
  - OSI Network functionality in TCP/IP: **Internet**
  - Nature of TCP: **Connection-Based**
  - SYN stands for: **Synchronise**
  - Second step of handshake: **SYN/ACK**
  - Acknowledgement abbreviation: **ACK**

- **Ping & Traceroute:**
  - Command to ping bbc.co.uk: `ping bbc.co.uk`
  - Sample IPv4 result: **217.160.0.152**
  - Ping interval switch: **-i**
  - Force IPv4: **-4**
  - Verbose output switch: **-v**
  - Traceroute interface switch: **-i**
  - Traceroute TCP SYN switch: **-T**
  - Traceroute defaults on (Windows): **Internet**

- **Whois:**
  - facebook.com postal code: **94025**
  - facebook.com first registration: **29/03/1997**
  - microsoft.com registrant city: **Redmond**
  - Nearby golf course: **Belleveue Golf Course**
  - microsoft.com Tech Email: **msnhst@microsoft.com**

- **DNS & Dig:**
  - DNS stands for: **Domain Name System**
  - Initial DNS query: **Recursive**
  - DNS server for domain extensions: **Top-Level Domain**
  - First lookup location: **Hosts File**
  - Alternate Google DNS IP: **8.8.4.4**
  - TTL of a 24-hour record: **86400**

---




