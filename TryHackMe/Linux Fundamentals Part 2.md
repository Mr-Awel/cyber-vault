### 1 SSH (Remote Terminal Super-power)

- **What it is:** Secure Shell = encrypted tunnel to run commands on another machine.
    
- **Syntax:** `ssh username@IP`
    
    - Example: `ssh tryhackme@10.10.43.102`
        
- **Login flow:** first-time **yes** → type password (no on-screen feedback) → you now control the _remote_ shell, not your own.
    
- **Why it matters:** same protocol pros use; lets you practise on TryHackMe AttackBox + target VM.
    

---

### 2 Flags & Help on Any Command

- **Short flag:** `-a`  Long flag: `--all`
    
- **Default vs. extended:** `ls` shows visible files; `ls -a` reveals hidden `.` files.
    
- **Quick reference:** `<command> --help`
    
- **Deep dive manual:** `man <command>` (scroll ↑↓ / quit with `q`).
    

---

### 3 Core Filesystem Commands

|Command|Purpose|Example|
|---|---|---|
|`touch`|Create empty file|`touch note`|
|`mkdir`|Create directory|`mkdir project`|
|`cp`|Copy file/dir|`cp note note_backup`|
|`mv`|Move _or_ rename|`mv note_backup note_final`|
|`rm`|Delete file|`rm note_final`|
|`rm -R`|Delete directory recursively|`rm -R project`|
|`file`|Identify file type|`file note` → “ASCII text”|

**Pro-tip:** use full paths (`cp src/file /tmp/target`).

---

### 4 Permissions 101 (`ls -l`)

- Pattern: `<type><owner><group><other>` → `-rw-r--r--`
    
    - `r` read `w` write `x` execute
        
- Ownership columns: user • group.
    
- Granularity: owner + group + everyone-else can each have different rights.
    

---

### 5 Switching Users (`su`)

- Become another user: `su user2` (asks for user2’s password).
    
- Full login shell: `su -l user2` (drops you in `/home/user2`, loads their env).
    
- Requires root or knowledge of target user’s password.
    

---

### 6 Key Root Directories (Mental Map)

|Directory|“District” Analogy|Typical Contents / Why You Care|
|---|---|---|
|`/etc`|City Hall (configs)|`sudoers`, `passwd`, `shadow`|
|`/var`|Factory & Logyard|Logs (`/var/log`), databases, backups|
|`/root`|Mayor’s Mansion|Root user’s home directory|
|`/tmp`|Public Drop-off|World-writable scratch space, wiped on reboot|

---

### 7 Practice Workflow

1. **SSH in**: `ssh tryhackme@IP`
    
2. **Create test assets**: `mkdir lab && cd lab && touch demo`
    
3. **Copy / move / delete** until commands feel automatic.
    
4. **Inspect permissions**: `ls -l`, then try accessing as another user with `su`.
    
5. **Explore system**:
    
    - Configs: `ls /etc`
        
    - Logs: `ls /var/log`
        
    - Temp stash: `cp script.sh /tmp`


---
## **Questions**

What directional arrow key would we use to navigate down the manual page?
**=down**

What flag would we use to display the output in a "human-readable" way?
**=-h**

How would you create the file named "newnote"?
**=touch newnote**

On the deployable machine, what is the file type of "unknown1" in "tryhackme's" home directory?
**=ASCII text**

How would we move the file "myfile" to the directory "myfolder"
**=mv myfile myfolder**

What are the contents of this file?
**=command "cat myfile" gave THM{FILESYSTEM}-> **

On the deployable machine, who is the owner of "important"?
**=command "ls -lh" showed it was user2**

What would the command be to switch to the user "user2"?
**=su user2**

Output the contents of "important", what is the flag?
**=command "su user2" then run command "Cat important and it's output is THM{SU_USER2}**

What is the directory path that would we expect logs to be stored in?
**=/var/log**

What root directory is similar to how RAM on a computer works?
**=/tmp**

Name the home directory of the root user
**=/root**

