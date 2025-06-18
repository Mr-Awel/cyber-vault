### 📚 Exam Objective 1.4 — Using Appropriate Cryptographic Solutions

_(expanded & clarified per your feedback)_

---

#### 🔑 Public Key Infrastructure (PKI)

- **Key-pair roles** – **Public key** = open padlock anyone can snap shut on data; **Private key** = hidden master key that opens the padlock and can also stamp unforgeable “wax-seal” signatures (non-repudiation).
    
- **Root of trust & chain** – A self-signed _root_ certificate vouches for one or more _intermediate_ CAs, which in turn sign _leaf_ certificates. If any link is broken or revoked, the entire chain fails validation.
    
- **Key escrow** – Encrypted backup copy of a private key held by a trusted custodian (often inside an HSM) so an org can decrypt data even if the original key holder leaves or loses the key.
    
- **PKCS container types** –
    
    - **.p7b / .cer** (PKCS#7): cert chain + publics only, no private key.
        
    - **.p12 / .pfx** (PKCS#12): full bundle with private key, always password-protected.
        
- **CSR (Certificate Signing Request)** – You generate a fresh key-pair locally, then send the _public_ half plus identifying info to a CA; they sign and return your certificate.
    

---

#### 🏷️ Cert Status & Revocation

- **CRL (Certificate Revocation List)** – Periodic downloadable “blacklist” of serial numbers. Think printed phonebook: you must fetch the whole thing and check manually; may be hours or days old.
    
- **OCSP (Online Certificate Status Protocol)** – Real-time query: your browser pings the CA’s responder and gets a simple _good / revoked / unknown_ reply. Analogy: **“text me now”** to confirm someone’s still legit rather than riffling through yesterday’s phonebook.
    

---

#### 🛠️ Crypto Hardware & Key Management

- **HSM (Hardware Security Module)** – Tamper-resistant appliance (rack device, PCIe card, or cloud service) that _generates, stores, and uses_ high-value keys **inside sealed hardware**. Keys never leave in plaintext; the HSM performs signing/encryption internally at high speed (banks, CAs, payment processors).
    
- **TPM (Trusted Platform Module)** – Tiny soldered-on chip that seals disk-encryption keys and attests a clean boot chain; perfect for client devices.
    
- **Secure Enclave / SE** – Isolated CPU region (e.g., Apple T2/T-series, Intel SGX) for biometric templates and small private keys.
    
- **KMS (Key Management Service)** – Central software layer (AWS KMS, Azure Key Vault) that enforces policy: create, rotate, disable, destroy keys; logs every use for audit.
    

---

#### 🔒 Encryption Scopes & Algorithms

|**Scope**|Typical Tool|Use-case highlight|
|---|---|---|
|**Full-disk**|BitLocker, FileVault|“Laptop stolen? Drive unreadable.” Keys sealed in TPM.|
|**Volume/Partition**|LUKS, VeraCrypt|Secure external drives; traveler unlocks with passphrase.|
|**File/Folder**|EFS, GPG|Protect one document or folder regardless of storage medium.|
|**Database/Record**|TDE, field-level AES|Limits breach blast-radius to single column/row.|
|**Transport**|TLS, IPsec|Data-in-motion confidentiality & integrity.|

**Algorithm families**

- **Symmetric (AES, ChaCha20)** – One shared secret; lightning-fast bulk encryption.
    
- **Asymmetric (RSA, ECC)** – Two keys; ideal for exchange and signatures but slower.
    
- **Key exchange** – _Diffie-Hellman_ mixes two public numbers like paint colors in public to create a shared secret nobody else can separate.
    
- **Homomorphic encryption** – Enables cloud servers to run computations on ciphertext without ever decrypting it (still niche but growing).
    

---

#### #️⃣ Integrity & Password Protection

- **Hashes** – One-way fingerprints (SHA-256, SHA-3) prove data hasn’t changed.
    
- **Salting** – Random bytes prepended to a password before hashing so identical passwords have different digests.
    
- **Key stretching** – bcrypt, PBKDF2, Argon2 loop the hash thousands of times, turning each password guess into a time-sink for attackers.
    
- **Digital signatures** – Hash the data ➜ encrypt hash with sender’s private key ➜ receiver decrypts with sender’s public key and compares hashes: authenticity + integrity + non-repudiation.
    

---

#### 🕵️‍♂️ Data-Hiding & Privacy Extras

- **Tokenization** – Replace sensitive value (e.g., credit-card PAN) with random token; real data locked in vault.
    
- **Data masking** – Show fake yet realistic values in dev/analytics environments.
    
- **Steganography** – Conceal a secret file/phrase inside image-pixels or audio-LSBs; “security by obscurity,” not substitute for encryption.
    
- **Obfuscation** – Transform source code or binaries into hard-to-read forms to deter reverse-engineering.
    

---

#### ⛓️ Blockchain Snapshot

Distributed ledger where each block’s hash links to the previous; altering one copy breaks consensus. Beyond crypto-coins, useful for tamper-evident logs, medical records, smart contracts.

---

#### 💡 Memory Hooks

- **Padlock vs. Master key** – Public encrypts, private decrypts.
    
- **Paint-mix DH** – Shared secret created in plain sight.
    
- **CRL = phonebook; OCSP = “text me now.”**
    
- **TPM boots, HSM signs, KMS minds.**

---
