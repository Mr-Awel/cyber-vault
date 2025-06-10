
---

## Port Forwarding  
- **What it does:** Maps an external (public) port on your router to an internal (private) IP + port, so services behind NAT are reachable from the Internet.  
- **Analogy:**  
  - Public IP = apartment-building street address  
  - Port number = apartment + room number  
  - Router’s port-forward rule = doorman’s instruction: “If someone rings door 80, send them to Apt 10, living room.”  
- **Packet flow:**  
  1. Client → `PublicIP:80`  
  2. Router matches WAN port 80 → `192.168.1.10:80`  
  3. Router rewrites packet destination → private IP  
  4. Response is rewritten back to public IP so TCP session stays intact  
- **Key point:** Opens the tunnel; a firewall still controls who can walk through it.

---

## Firewall  
- **What it does:** Border‐control device that inspects packets/flows and permits or blocks based on rules.  
- **Questions it asks:**  
  - Source IP/subnet?  
  - Destination IP/subnet?  
  - Destination port (e.g. 80, 443)?  
  - Protocol (TCP, UDP, ICMP)?  
- **Types:**  
  - **Stateful:**  
    - Keeps track of full connection state (TCP handshakes, session tables).  
    - Dynamic decisions, blocks entire flows if something goes wrong.  
    - Good for deep inspection but resource-heavy.  
  - **Stateless:**  
    - Applies simple, static rules to each packet in isolation.  
    - Very fast, but can’t see multi‐packet exploits or fragmented attacks.  
- **Real-world stacks:**  
  1. Bulk stateless filters soak up noise/DDOS  
  2. Stateful NGFW for nuanced traffic  
  3. (Optionally) app-layer proxies/IDS  

---

## Virtual Private Network (VPN)  
- **What it does:** Creates an encrypted “tunnel” over the Internet so remote devices appear on the same private LAN.  
- **Benefits:**  
  - **Site-to-site connectivity:** Link offices (e.g. 192.168.1.x ↔ 10.0.0.x).  
  - **Wi-Fi security:** Encrypt on public hotspots.  
  - **Privacy & anonymity:** Hide traffic from ISPs or censors (provider trust required).  
  - **Isolated hack labs:** e.g. TryHackMe uses VPNs so vulnerable VMs aren’t exposed publicly.  
- **Common protocols:**  
  | Protocol        | Notes & 2025 recommendation                        |
  |-----------------|-----------------------------------------------------|
  | PPTP            | Easy but weak; **do not** use today.                |
  | L2TP/IPsec      | Strong crypto but NAT-tricky; OK for corporate gear.|
  | OpenVPN         | Battle-tested SSL/TLS; flexible but heavier.        |
  | **WireGuard**   | Modern, minimal codebase, ChaCha20, blazing fast.   |

---

## Router vs. Switch

### Switch  
- **Layer 2** (MAC-based forwarding) or **Layer 3** (adds basic IP routing/VLAN routing).  
- **Layer 2 switch:**  
  - Learns MAC ↔ port mappings, forwards frames only to the correct port.  
  - Fast, local only.  
- **Layer 3 switch:**  
  - Can also route between VLANs/subnets without leaving the switch chassis.

### Router  
- **Layer 3 device** that maintains a routing table and forwards packets between distinct networks or out to the Internet.  
- **Decides best path** using metrics (hop count, link speed, reliability).  
- **Configurable features:** Port-forwarding, NAT, basic firewall, QoS, fail-over.

---

## VLANs (Virtual LANs)  
- **What they are:** Logical “sub-floors” on the same physical switch.  
- **Usage:**  
  - Assign switch ports into separate VLAN IDs (e.g. VLAN 10 = Sales, VLAN 20 = Accounting).  
  - Each VLAN gets its own IP subnet (`192.168.1.0/24`, `192.168.2.0/24`).  
  - Traffic between VLANs must traverse a router or L3-switch interface, enforcing isolation and security.

----
## **Questions**

What is the name of the device that is used to configure port forwarding?
**=Router**

What layers of the OSI model do firewalls operate at? For this answer, just provide the numbers in ascending order, separated by an ampersand (&)
**=3&4**

What category of firewall inspects the **entire connection**?
**=Stateful**

What category of firewall inspects individual packets?
**=Stateless**

What VPN technology **only** encrypts & provides the authentication of data?
**=PPP**

What VPN technology **only** encrypts & provides the authentication of data?
**=IPSec**

What is the verb for the action that a router does?
**=routing**

What are the two different layers of switches? Separate these by a comma I.e.: Layer X,Layer Y
**=Layer 2,Layer 3**