## 🚦 Why this chapter matters

- **Exam Obj 2.4 core** — every bullet shows up in Security+ questions.
    
- Attacks evolve fast; spotting _indicators_ early keeps incidents small (cost, reputation, job 🤝).
    
- Think like blue-team triage: “What signal screams _ransomware_ vs _DNS spoof_?” Chapter 8
    

---

### 🦠 Malware Zoo (know the tell-tale tracks) Chapter 8

|Type|Fast ID|Real-world hook|
|---|---|---|
|**PUPs / Bloatware**|CPU spikes, nag ads|Free PDF converters dragging toolbars|
|**Ransomware 💰**|Files suddenly _.locked_, ransom note w/ crypto address|“FBI virus” splash screen|
|**Trojans / RATs 🐴**|Legit-looking installer, stealth C2 callback|PE file pops UAC → backdoor|
|**Worms**|Bandwidth surge, duplicate traffic|NIMDA renaming _.eml_|
|**Viruses / Polymorphic**|AV false-negatives via shape-shifting hash|Resident boot-sector infections|
|**Spyware / Keylogger ⌨️**|Unknown outbound to ad networks|Python `pynput` script logs creds|
|**Logic bomb**|Repeats on set trigger (e.g., every Monday 09:00)|Insider deletes CFO files|
|**Rootkit**|Missing AV logs, hidden procs|Kernel-level hook detours syscalls|

🛡️ _Quick wins_: layered AV, EDR with sandbox detonation, user-priv hygiene.

---

### 🏃‍♂️ Physical Attack Vector Chapter 8

- **Brute-force entry**: crowbar vs server cage → stolen drives.
    
- **RFID cloning 📶**: badge skim → door pop; add fingerprint readers (MFA).
    
- **Environmental chaos**: cut power line → DB corruption; design for redundancy + DR.
    

---

### 🌐 Network Offense Patterns Chapter 8

**Pivoting / VM-escape** → compromised dev box fans out with `nmap` inventory.  
**DDoS family**

- _Volumetric_: botnet ➜ SYN flood.
    
- _Amplified_ (Smurf 🥁): tiny ICMP ping → 4× replies.
    
- _Reflected_: spoofed DNS query bounces at victim.  
    **ARP poisoning**: MAC spoof inside LAN → traffic detour.  
    **DNS games**: cache-poison → fake banking site; defenders use DNSSEC, sinkholes.
    

---

### 📶 Wireless Playground Chapter 8

- **Rogue AP**: Pi-based hotspot named “Starbucks Free WiFi”.
    
- **Evil twin**: same SSID, better signal → no intranet share access? Red flag.
    
- **Deauth / jamming**: sudden drops, auto-reconnect storms.
    
- **MAC spoof**: duplicate address seen in ARP table.
    

---

### 🔄 On-Path & Replay Tricks Chapter 8

- Session token stolen via XSS → _session hijack_.
    
- **Replay**: attacker re-sends old Kerberos blob; sequence numbers stop it.
    
- **Credential replay / stuffing**: breached combo lists sprayed at scale; MFA + unique pw each site.
    

---

### 🐍 Malicious Code Genres Chapter 8

- Bash reverse-shell one-liner → outbound to `nc -lvp 4444`.
    
- Python keylogger (DEBUG log to `mykeylog.txt`).
    
- JavaScript ad-malware button triggers `badscript.js`.  
    _Indicator_: odd outbound ports, new `.sh/.py` in temp dirs.
    

---

### 🏗️ Application Exploits Chapter 8

- **Injection (SQL, XSS)**: `1=1` or `<script>` in logs.
    
- **Buffer overflow**: DEP alerts, unexplained crashes.
    
- **Privilege escalation**: normal user runs `whoami → root`.
    
- **Forgery (CSRF, SSRF)**: server makes internal calls for attacker.
    
- **Directory traversal**: `../../etc/passwd` in URI.
    

---

### 🔐 Crypto Attacks Chapter 8

|Attack|Signal|Mitigation|
|---|---|---|
|**Downgrade / SSL-strip**|HTTPS→HTTP fallback|HSTS, TLS 1.3-only|
|**Collision**|Same hash, diff file|Retire MD5; use SHA-3|
|**Birthday**|Fast hash brute via math|Longer hash len (256-bit+)|
|**Pass-the-Hash**|NTLM auth seen|Enforce Kerberos, LSASS guard|

---

### 🔑 Password Assault Matrix Chapter 8

- **Dictionary**: real words; fix w/ misspell + symbols.
    
- **Spraying**: one pw vs many users; watch lockout spikes.
    
- **Brute/Rainbow**: massive offline crack; salt + slow KDF.
    
- **Hybrid**: word + digits (`Winter2025!`).
    

---

### 🕵️ Indicators of Attack (IoAs) — quick triage list Chapter 8

|IoA|What to flag|
|---|---|
|Account lockouts|3-strike rule hits many users = brute-force|
|Concurrent sessions|Same user, LA & Moscow, 2 min apart|
|Impossible travel|Geo-velocity > 500 mph|
|Resource spike|CPU/RAM 100 % on one web node|
|Resource inaccessibility|CRM offline but WAN OK → DDoS|
|Out-of-cycle logs|03:17 AM auth success from service acct|
|Missing logs|Gap in firewall syslog during incident|
|Blocked content alerts|DLP prevented upload to dropbox.com|

---

### 🧠 Retrieval Boosters

- Map each _indicator_ back to its likeliest attack in 3-column flash tables.
    
- Quiz yourself: “File deletion at exact time each week — which malware?”