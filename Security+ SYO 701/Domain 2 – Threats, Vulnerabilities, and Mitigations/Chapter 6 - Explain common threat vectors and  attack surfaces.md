_(CompTIA Security+ ▶ Exam Obj 2.2)_

---

### 💌 Message-Based Vectors – “Inbox & IM as Trojan Horse”

_Why it matters:_ Most breaches still start with a click.

- **Email phishing** → fake IRS refund, rogue invoices, malware-rigged attachments.
    
- **Smishing (SMS)** → “Your package is stuck, tap to track” text harvests creds.
    
- **IM threats** → end-to-end encrypted apps can still relay weaponized links or files. Chapter 6
    

---

### 🖼️ Image-Based Vectors – “Malware in the Pixels”

_Why it matters:_ Steganography hides code where antivirus seldom looks.

- Embedded code or hidden URLs fire on open / preview.
    
- Defense: deep-image scanning & content-disarm-reconstruct (CDR). Chapter 6
    

---

### 📂 File-Based Vectors – “Attachments with a Payload”

- Malicious docs exploit macros / zero-days, then beacon out.
    
- Screen & sandbox unknown files; strip active content at the gateway. Chapter 6
    

---

### 📞 Voice-Call Vectors – “Vishing & Caller-ID Spoof”

- Social-engineered calls request wire transfers or MFA codes.
    
- Mitigation: call-back verification & STIR/SHAKEN anti-spoofing. Chapter 6
    

---

### 🔌 Removable-Device Vectors – “USB = Digital Candy”

- Dropped-USB trick auto-runs malware when curiosity wins.
    
- Enforce port control, auto-scan in sandbox, user training. Chapter 6
    

---

### 🛠️ Vulnerable Software

- **Unpatched code ≈ unlocked front door.**
    
- Client-based vs agentless scans (Nmap, Wireshark) find weak spots; patch ASAP. Chapter 6
    

---

### ⏳ Unsupported Systems / Legacy Apps

- No vendor patches → attacker playground (e.g., old Windows 7 kiosk).
    
- Isolate, virtualize, or retire. Chapter 6
    

---

### 🌐 Unsecure Networks

**Wireless 🛜**

- Open Wi-Fi sends creds in cleartext; hide SSID, use WPA3, MAC filtering.
    

**Wired 🔌**

- Live port in lobby = free network drop; disable unused jacks, 802.1X auth.
    

**Bluetooth 🔵**

- Easy pairing → Bluejacking, Bluesnarfing; keep BT off when idle. Chapter 6
    

---

### 🔓 Open Service Ports

- Attackers sweep 0–65535 for RDP/SSH left open.
    
- Close, firewall, or port-knock; principle of least functionality. Chapter 6
    

---

### 🔑 Default Credentials

- “admin/admin” still found on routers & cameras.
    
- Force credential change at install; maintain password vault. Chapter 6
    

---

### 🚚 Supply-Chain Threats

- **MSPs**: one breach echoes to every client.
    
- **Vendors / Suppliers**: weaker partner gets popped → lateral into you (SolarWinds).
    
- Contractual security clauses, continuous third-party risk scoring. Chapter 6
    

---

### 🧠 Human Vectors & Social Engineering

|Tactic|Hook|Real-World Example|
|---|---|---|
|**Phishing / Spear**|Urgency, authority|“CEO needs gift cards now”|
|**Smishing**|Fake delivery SMS|Malicious tracking link|
|**Vishing**|Voice trust|“Bank fraud dept” asks OTP|
|**Misinformation / Disinfo**|Panic, bias|Fake outage news moves stock|
|**Impersonation / BEC**|Trusted identity|CFO wire-transfer scam|
|**Pretexting**|Fabricated scenario|“IT support” asks for login|
|**Watering-Hole**|Compromised legit site|Dept-of-Labor 2013 exploit|
|**Brand Impersonation**|Look-alike portal|Spoofed PayPal login|
|**Typosquatting**|URL typo trap|microsooft[.]com steals creds|

---

### 📝 Quick Recap

- **Vectors** = paths attackers use; **attack surfaces** = exposed assets.
    
- Reduce risk by shrinking surfaces (patching, hardening) & disrupting vectors (filters, training).
    
- Remember: tech controls fail if humans click—layer defenses accordingly.