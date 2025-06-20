### Why it matters 🤔

- Attackers look for weak points first; knowing them = better defenses and exam points. Chapter 7

---

### 1️⃣ Application Vulnerabilities

|Weakness|What / Why|Hooks & Fixes|
|---|---|---|
|**Memory Injection**|Malicious code sneaks into a process’s RAM, often invisible.|Code Red worm ➜ input validation, DEP, signed code. Chapter 7|
|**Buffer Overflow**|Extra data spills into neighbor memory, hijacks flow.|SQL Slammer ➜ bounds-checking, safe languages. Chapter 7|
|**Race Condition (TOC/TOU)**|Two threads clash over the same data ⇒ inconsistent state.|Airline seat race ➜ locks, atomic ops. Chapter 7|
|**Malicious Update**|“Official” patch laced with malware.|CCleaner 2017 ➜ code-sign checks, update via MFA. Chapter 7|

---

### 2️⃣ OS-Based Vulnerabilities 🖥️

- Kernel / service flaws grant remote code execution (e.g., **BlueKeep** RDP).  
    _Patch early, disable unused services._ Chapter 7
    

---

### 3️⃣ Web-Based Vulnerabilities 🌐

|Attack|Core Idea|Fast Mitigation|
|---|---|---|
|**SQL Injection**|Unsanitized input rewrites queries → dumps DB.|Prepared statements, stored procs.|
|**XSS**|Injected script runs in victim browser.|Output encode, CSP, input validation. Chapter 7|

_Retrieval cue:_ Can you explain why SQLi targets the **backend** while XSS targets the **frontend**?

---

### 4️⃣ Hardware Vulnerabilities 🔧

- **Bad firmware**, **EOL** or **legacy** gear lack patches → root access risk.  
    _Mitigate with signed firmware & retire unsupported kit._ Chapter 7
    

---

### 5️⃣ Virtualization ⚙️

|Issue|Impact|Guardrail|
|---|---|---|
|**VM Escape**|Hop from guest to host.|Patch hypervisor, strong isolation.|
|**Resource Reuse**|Data remnants on shared disks.|Secure wipe before re-assign.|
|**VM Sprawl**|Too many unmanaged VMs.|Automated lifecycle + audits. Chapter 7|

---

### 6️⃣ Cloud-Specific Vulnerabilities ☁️

- **Shared tenancy leaks**, **bad configs**, weak **IAM**.
    
- **CASB** = policy enforcer + visibility across SaaS/IaaS. Chapter 7
    

---

### 7️⃣ Supply-Chain Risks 🔗

|Provider|Typical Pitfall|Prevent|
|---|---|---|
|Service|Poor 3rd-party controls.|SLA + pen-test.|
|Hardware|Counterfeit parts.|Trusted vendor attestations.|
|Software|Tainted libraries.|SBOM, static scans. Chapter 7|

---

### 8️⃣ Cryptographic Vulnerabilities 🔐

- **CA compromise**, **weak keys**, **SSL/TLS downgrade (POODLE)**, **SSL stripping**.
    
- Use HSM/key escrow, rotate keys, enforce TLS 1.3+.
    
- **CRL vs OCSP**: both revoke certs; OCSP = “real-time ping.” Chapter 7
    

---

### 9️⃣ Misconfiguration 🚧

- Default creds, open ports, lax ACLs, unpatched firmware.
    
- Firewalls: too open = breach; too strict = outage. Balance! Chapter 7
    

---

### 🔟 Mobile Device Vulnerabilities 📱

|Action|Risk|Control|
|---|---|---|
|Jailbreak / Root|Disable OS protections.|MDM block, no support.|
|Sideload APK/IPA|Counterfeit apps.|Allow only signed store apps.|
|Lost device|Data theft.|Remote wipe, strong PIN. Chapter 7|

---

### 11️⃣ Zero-Day ⚡

- Unknown flaw exploited before patch (e.g., **Stuxnet**). Only behavior-based defenses help. Chapter 7
    

---

### Quick Self-Check 🧠

1. Which attack leverages timing gaps in checks vs. use?
    
2. How does VM escape differ from resource reuse?
    
3. Why does jailbreaking void warranty _and_ weaken security?
    

_(Answer mentally — retrieval practice!)_