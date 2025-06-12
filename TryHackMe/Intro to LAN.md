-The main premise of a **Star Topology** is that devices are individually connected via a central networking device such as a switch or hub. (I.e. like a star*)
![[Star Topology.jpg]]

-The **Bus Topology**, is the type of connection relies upon a single connection which is known as a backbone cable. Similar to Star Topology but instead of a switch/hub, it's a cable. 
![[Bus Topology.jpg]]

-The **Ring Topology** (also known as token topology) is the type of topology where devices such as computers are connected directly to each other to form a loop. There is no backbone cable or switch, the devices are connected to each other meaning there is little cabling required. 
![[Ring Topology.jpg]]

-**Switches** are dedicated devices within a network that are designed to aggregate multiple other devices such as computers, printers, or any other networking-capable device using ethernet
-**Router** is a networking device whose primary job is to move data packets between different networks. Basically to connect networks and pass data between them. For example, your router connects to your Internet Service Provider's (ISP) network
-**Subnetting** is the term given to splitting up a network into smaller, miniature networks within itself. Subnetting is achieved by splitting up the number of hosts that can fit within the network, represented by a number called a subnet mask. 
-Subnets use IP addresses in three different ways:
- Identify the network address
- Identify the host address
- Identify the default gateway

-**Network Address** (`x.y.z.0` in a `/24`): Tells you “this is Network #1.”
-**Host Address** (`x.y.z.1 … x.y.z.254`): Assign to devices so each one is unique.
-**Default Gateway** (commonly `.1` or `.254`): The on-subnet router that knows how to forward outside traffic.  The default gateway is simply an IP address, often ending in .1 or .254, assigned to your router’s interface on the local subnet; whenever a device needs to send traffic to an address outside its own network, it forwards those packets to the gateway IP, and that router handles delivering them to the broader Internet (or another network).

-**A**ddress **R**esolution **P**rotocol or **ARP** for short, is the technology that is responsible for allowing devices to identify themselves on a network. Simply, ARP allows a device to associate its MAC address with an IP address on the network.
-Higher-level protocols (TCP/UDP) speak in IP addresses, but at the moment you need to put bits on the wire, you must know the destination’s MAC. **ARP** is exactly what bridges that gap: it “resolves” an IP → MAC mapping, one time at least, and remembers it.

-Why ARP Matters?
- **One-time lookup**: After the ARP reply, the host caches the mapping and sends future frames directly to the device’s MAC address (e.g., `18:AC:33:12:88:29`) without extra broadcasts, saving bandwidth.
- **Local-only**: ARP never leaves your LAN—routers strip it off, so it can’t traverse the Internet.
- **Transparent**: All of this happens “beneath” IPv4/TCP/UDP. Once you know the MAC, you just build a normal Ethernet frame and send your data along.

When a device joins a network and hasn’t been given a fixed (manual) IP address, it uses  **DHCP** (**D**ynamic **H**ost **C**onfiguration **P**rotocol) to “ask” for one. The process goes through four clear steps (often called DORA):
- DHCP Discover(Client → Broadcast)
- DHCP Offer (Server → Client’s MAC)
- DHCP Request (Client → Broadcast/Server)
- DHCP ACK (Server → Client)

---
## **Questions**

What does LAN stand for?
**=Local Area Network**

What is the verb given to the job that Routers perform?
**=Routing**

What device is used to centrally connect multiple devices on the local network and transmit data to the correct location?
**=Switch**

What topology is cost-efficient to set up?
**=Bus Topology**

What topology is expensive to set up and maintain?
**=Star Topology**

Complete the interactive lab attached to this task. What is the flag given at the end?
**=THM{TOPOLOGY_FLAWS}**

What is the technical term for dividing a network up into smaller pieces?
**=Subnetting**

How many **bits** are in a subnet mask?
**=32**(4 bytes)

What is the range of a section (octet) of a subnet mask?
**=0-255**

What address is used to identify the start of a network?
**=Network Address**

What address is used to identify devices within a network?  
**=Host Address**

What is the name used to identify the device responsible for sending data to another network?
**=Default Gateway**

What does ARP stand for?
**=Address Resolution Protocol**

What category of ARP Packet asks a device whether or not it has a specific IP address?
**=Request**(ARP Request)

What address is used as a physical identifier for a device on a network?
**=MAC Address**

What address is used as a logical identifier for a device on a network?
**=IP Address**

What type of DHCP packet is used by a device to retrieve an IP address?
**=DHCP Discover**

What type of DHCP packet does a device send once it has been offered an IP address by the DHCP server?
**=DHCP Request**

Finally, what is the last DHCP packet that is sent to a device from a DHCP server?
**=DHCP ACK**

