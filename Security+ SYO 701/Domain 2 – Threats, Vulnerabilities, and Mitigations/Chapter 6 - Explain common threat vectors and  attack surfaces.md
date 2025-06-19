
### 📋 Exam Objective 2.2 — Common Threat Vectors & Attack Surfaces

_Big picture: Know **where** the bad guys slip in so you can slam the door shut._ 

---

#### 📨 Message-Based Vectors

- **Email (phishing / spear-phishing)** – fake “action required” mails lure clicks or creds.
    
- **SMS (smishing)** – “Your package is held—pay $1” texts push malicious links.
    
- **Instant-Messaging** – DM with “funny video 😂” attachment = trojan ride-along.  
    _Real-world hook: 91% of breaches start with a phish; inbox = battlefield._ 
    

#### 🖼️ Image-Based Vectors

- Malware or C2 beacons hidden with steganography inside .jpg/.png.
    
- Opening or auto-previewing the file triggers the payload.  
    _Think of it as a postcard with invisible ink instructions for the attacker._ 
    

#### 📁 File-Based Vectors

- Weaponized docs, installers, or scripts exploit app flaws on open.
    
- Common faces: macro-laden Office docs, trojanized freeware, rogue PDFs.  
    _Hook: “Free PDF merger” that actually merges your machine into a botnet._ 
    

#### ☎️ Voice-Call Vectors

- **Vishing** & caller-ID spoofing harvest secrets (“This is your bank’s fraud team…”).
    
- Voicemail links or callbacks funnel victims to fake IVR systems.  
    _Treat unknown callers like unknown USBs—don’t plug in your info._ 
    

#### 💾 Removable-Device Vectors

- Infected USBs dropped in lobbies; curiosity = compromise.
    
- BadUSB firmware swaps turn drives into rogue keyboards.  
    _Defense: disable autorun, force scans, train staff to hand found drives to SecOps._ 
    

#### 🛠️ Vulnerable Software

- Bugs, weak defaults, or outdated libs invite exploits.
    
- **Client-based vs. agentless scans**: agents give depth; agentless (Nmap) gives speed/stealth.  
    _Patch Tuesday is cheaper than Breach Friday._ 
    

#### 🕰️ Unsupported Systems & Legacy Apps

- No vendor patches = public exploit playground.
    
- Isolate, virtualize, or retire—don’t pretend “internal only” is protection. Chapter 6
    

#### 🌐 Unsecure Networks

- **Wireless:** Open Wi-Fi = plaintext eavesdropping; hide SSID, enable WPA3, use MAC filtering.
    
- **Wired:** Live wall-jack is an unlocked basement window; enforce 802.1X, disable idle ports.
    
- **Bluetooth PAN:** Easy pairing → blue-snarfing; keep BT off unless in use.  
    _Bad RF doesn’t need physical keys to walk in._ Chapter 6
    

#### 🔓 Open Service Ports & Default Creds

- Port 3389 exposed + “admin/admin” = attacker fast-track.
    
- Conduct routine port sweeps; change factory logins day-zero.  
    _If Shodan can find it, so can everyone else._ Chapter 6
    

#### 🔗 Supply-Chain Weaknesses

- **MSPs:** One compromise, many clients burned. Demand audits & segmentation.
    
- **Vendors/Suppliers:** Third-party portals and firmware updates carry stowaways.
    
- Build security clauses into contracts; verify, don’t trust.  
    _You inherit every partner’s hygiene—good or bad._ Chapter 6
    

#### 🧠 Human Vectors / Social Engineering

- **Phishing / Smishing / Vishing** – broad net or laser-targeted.
    
- **Misinformation & Brand Impersonation** – distort reality, exploit trust.
    
- **Impersonation, Pretexting, BEC** – fake roles, forged invoices, CEO fraud.
    
- **Watering-Hole & Typosquatting** – poison the sites _you_ visit or URLs _you_ mistype.  
    _Primary patch: user awareness + just-in-time verification._ Chapter 6
    

---

### 🔑 Quick Recall Cues

- **“MMIV-R”** → Message, Media (image/file), Interactive (voice/Bluetooth), Vulnerable software, Remote devices.
    
- **Ports & Passwords first**: if it listens or logs in, lock it down.