## 1 Editors on the CLI

### 1.1 Nano — friendly default

- `nano <file>` open or create
    
- **Keys**
    
    - `Ctrl-O` save `Ctrl-X` quit
        
    - `Ctrl-W` search `Ctrl-_` goto line
        
    - `Ctrl-^ / Ctrl-K / Ctrl-U` mark → cut → paste
        
- Status bar legend: `^` = Ctrl, `M` = Alt
    

### 1.2 VIM — survive in 30 s

bash

CopyEdit

`vim <file>      # or vi i               # insert mode <Esc>           # back to normal :wq             # write & quit /word ENTER     # search, n for next`

- Ubiquitous, syntax-highlighted, fully scriptable
    

---

## 2 Moving Files Around

### 2.1 `wget` — pull from the web

bash

CopyEdit

`wget <URL>                       # grab file wget -q --show-progress <URL>    # quiet + progress`

### 2.2 `scp` — encrypted copy over SSH

bash

CopyEdit

`# local ➜ remote scp <local>  user@host:/path/file  # remote ➜ local scp user@host:/path/file  <local>`

- `-r` recurse, `-P <port>` custom SSH port
    

### 2.3 One-liner web server

bash

CopyEdit

`cd /dir/to/share python3 -m http.server 8000 # client: wget http://<IP>:8000/<file>`

---

## 3 Process Kung-Fu

### 3.1 See what’s running

bash

CopyEdit

`ps                    # session ps aux | head         # system snapshot top / htop            # live stats (q to quit)`

### 3.2 Control them

bash

CopyEdit

`kill -15 <PID>   # SIGTERM – graceful kill -9  <PID>   # SIGKILL – force kill -19 <PID>   # SIGSTOP – pause (SIGCONT = 18)`

### 3.3 Background vs Foreground

bash

CopyEdit

`long_job.sh &   # run in background Ctrl-Z          # suspend bg %1           # resume bg fg %1           # bring fg jobs -l         # list`

### 3.4 `systemd` service helper

bash

CopyEdit

`systemctl start|stop apache2 systemctl enable|disable apache2   # on-boot toggle systemctl status apache2`

---

## 4 Scheduled Tasks with Cron

cron

CopyEdit

`# MIN HOUR DOM MON DOW    CMD 0 */12 * * *  cp -R /home/cmnatic/Documents /var/backups/`

- `crontab -e` edit `crontab -l` list
    
- Use full paths; redirect output for debug
    

---

## 5 Packages & Repositories (APT)

### 5.1 Routine package ops

bash

CopyEdit

`sudo apt update && sudo apt install <pkg> sudo apt remove <pkg> && sudo apt autoremove`

### 5.2 Add a third-party repo (manual)

bash

CopyEdit

`wget -qO- https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add - echo "deb https://download.sublimetext.com/ apt/stable/" \   | sudo tee /etc/apt/sources.list.d/sublime-text.list sudo apt update && sudo apt install sublime-text`

- Quick helper: `add-apt-repository ppa:vendor/ppa --remove` to drop
    

---

## 6 Logs & Monitoring

- **Locations** `/var/log/…`
    
    - `apache2/access.log` & `error.log` web hits / issues
        
    - `fail2ban.log` blocked brute-forces
        
    - `ufw.log` firewall events
        
    - `auth.log` sudo & SSH
        
    - `syslog` kernel + misc
        
- **Watch live**
    
    bash
    
    CopyEdit
    
    `sudo tail -f /var/log/apache2/error.log journalctl -u ssh -r | head      # newest first`
    
- Rotation via `logrotate`; rules in `/etc/logrotate.d/`
    

---

## 7 Pitfalls / Pro-Tips

1. Try **SIGTERM before SIGKILL** to avoid orphaned files
    
2. Cron runs with a minimal `$PATH`; specify full binaries
    
3. Keep each external repo in its own `.list` for quick audits
    
4. Check disk use: `du -sh /var/log/*`; tweak `logrotate` if needed
    
5. Fast staging in CTFs: `python3 -m http.server`, no FTP fuss
---
## **Questions**

Edit "task3" located in "tryhackme"'s home directory using Nano. What is the flag?
**=run "nano task3" and got "THM{TEXT_EDITORS}"**

Now, use Python 3's "HTTPServer" module to start a web server in the home directory of the "tryhackme" user on the deployed instance.
**=run "python3 -m http.server"**

Download the file [http://10.10.246.238:8000/.flag.txt] onto the TryHackMe AttackBox. Remember, you will need to do this in a new terminal.
**=run "wget http://10.10.246.238:8000/.flag.txt" and got "THM{WGET_WEBSERVER}"**

If we were to launch a process where the previous ID was "300", what would the ID of this new process be?
**=301**

If we wanted to **cleanly** kill a process, what signal would we send it?
**=SIGTERM**

Locate the process that is running on the deployed instance (10.10.246.238). What flag is given?
**=run "ps aux" and found the flag "THM{PROCESSES}"**

What command would we use to stop the service "myservice"?
**=systemctl stop myservice**

What command would we use to start the same service on the boot-up of the system?
**=systemctl enable myservice**

What command would we use to bring a previously backgrounded process back to the foreground?
**=fg**

When will the crontab on the deployed instance (10.10.244.206) run?
**=run "crontab -e" and saw "@reboot /var/opt/processes.sh", the answer is @reboot**


