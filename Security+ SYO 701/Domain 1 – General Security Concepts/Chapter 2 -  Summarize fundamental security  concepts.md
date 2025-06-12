
### 📋 Exam Objective 1.2  
Summarize the core principles and technologies that safeguard data and systems:  
- CIA Triad  
- Non-repudiation  
- AAA framework & protocols  
- Gap analysis  
- Zero-trust model (control vs. data plane, trust zones)  
- Physical security measures & sensors  
- Deception & disruption technologies 

---

### 🔐 CIA Triad (Confidentiality, Integrity, Availability)  
- **Confidentiality**: Only authorized parties see data.  
- **Integrity**: Data stays accurate (e.g. via hashing: SHA1, MD5).  
- **Availability**: Systems & data accessible when needed. 

> **Brain hack**: Visualize a fortified triangle—each side labeled C-I-A—and “walk” around it whenever you list the principles.  

---

### ✒️ Non-Repudiation  
- Prevents denial of actions (digital signatures, audit trails).  
- **Digital signatures** bind identity to content.  
- **Audit trails** log “who did what, when.” 

> **Brain hack**: Picture mailing a signed letter with a timestamp stamp—no one can claim they didn’t send it.  

---

### 🛂 AAA Framework & Protocols  
1. **Identification**: Who are you? (user account, smart card, biometrics)  
2. **Authentication**: Prove it (password/PIN, certificate via 802.1X).  
3. **Authorization**: What can you do? (least-privilege access).  
4. **Accounting**: Who did what? (logs: username, timestamp, IP, actions).   

**Key Protocols**  
- **Remote Authentication Dial-In User Service (RADIUS)**: remote access auth, shared secret between client/server.  
- **Diameter**: RADIUS’s successor for 4G/5G networks.  
- **Terminal Access Controller Access Control System Plus(TACACS+)**: Cisco’s device-access auth (routers, switches).   

> **Brain hack**: Map AAA to visiting a club: show ID (identify) → bouncer checks list (authenticate) → bouncer lets you into VIP area (authorize) → door camera logs entry (account).  

---

### 🕳️ Gap Analysis  
1. **Assess** current controls.  
2. **Benchmark** against standards (ISO, NIST).  
3. **Identify** gaps.  
4. **Prioritize** by risk level.  
5. **Remediate** with action plan.   

> **Brain hack**: Think “ABIPR” like “A Big Iguana Pokes Rocks”—each initial reminds you of a step.  

---

### 🛡️ Zero-Trust Model  
“Never trust, always verify.” Applies separation of:  
- **Control plane** (policy decisions)  
- **Data plane** (actual traffic)   

#### Control Plane Components  
- **Policy engine**: Decides “allow”/“deny” using policies + threat intel.  
- **Policy administrator**: Issues tokens, pushes rules to enforcement.  
- **Policy enforcement point**: Gatekeeper that enforces decisions.  
- **Adaptive identity**: Dynamic permissions based on context.  
- **Threat-scope reduction**: Shrink your attack surface.  
- **Policy-driven access control**: Automate enforcement.  

> **Brain hack**: Imagine a fortress command center (control plane) sending orders to each gate/turret (enforcement points).  

#### Data Plane & Trust Zones  
- **Subjects** (users/devices) vs. **Systems** (routers, firewalls).  
- **Implicit Trust Zone**: “safe” segment, minimal checks.  
- **Internal Zone**: Behind firewall (LAN).  
- **DMZ**: Semi-trusted screen subnet.  
- **External Zone**: Internet (untrusted).   

> **Brain hack**: Picture concentric circles around a castle: inner courtyard (internal), outer wall (DMZ), moat (external).  

---

### 🏗️ Physical Security Measures  
- **Bollards**: Impact-resistant posts.  
- **Access control vestibule**: Double-door identity check.  
- **Fencing**: Perimeter barrier.  
- **Video surveillance**: Cameras + analytics.  
- **Security guard**: Human patrol & response.  
- **Access badges**: RFID/smart entry + audit trail.  
- **Lighting**: Deters intruders, aids visibility.  
- **Visitors logs**: Records entry/exit, assigns responsibility.   

> **Brain hack**: Imagine your home: driveway bollards, front-door vestibule, backyard fence, porch light—all working together.  

---

### 📡 Sensor Technologies (Table 2.1)  
| Sensor Type  | Function & Application                                              |
|--------------|---------------------------------------------------------------------|
| **Infrared** | Detects heat signature changes (perimeter/in-room).               |
| **Pressure** | Senses force changes (floor mats, doors).                          |
| **Microwave**| Emits pulses, reads frequency shifts (wide-area movement).         |
| **Ultrasonic**| Sends sound waves, measures echo time (blind-spot detection).     |   

> **Brain hack**: Link each to a sense: heat (infrared), touch (pressure), radio (microwave), echolocation (ultrasonic).  

---

### 🎭 Deception & Disruption Technologies  
- **Honeypot**: Decoy system to observe attacker methods.  
- **Honeynet**: Network of honeypots.  
- **Honeyfile**: Bait file (“password.txt”) that triggers alerts.  
- **Honeytoken**: Fake data/credentials that ensnare intruders.  
- **Fake information**: DNS sinkhole (“black hole”), fake telemetry.   

> **Brain hack**: Picture jars of honey that alert you when a mouse (attacker) takes a taste.  

---

