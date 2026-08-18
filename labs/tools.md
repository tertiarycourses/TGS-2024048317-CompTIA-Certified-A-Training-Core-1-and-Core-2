# Lab Toolkit Reference

Every tool used in the CompTIA Certified A+ Training (Core 1 and Core 2) labs. All are free, all run in the browser, and none requires an install or a login.

## Browser tools

| Tool | Link | What it does |
| --- | --- | --- |
| **IP Calculator** | <https://alfredang.github.io/ipcalculator/> | Browser subnet calculator for IPv4 and IPv6 — CIDR, netmask, network and broadcast addresses, usable host ranges and batch processing with CSV export. |
| **PCAP Analyzer** | <https://alfredang.github.io/pcapanalyzer/> | Browser packet-capture analyser — protocol distribution, top talkers, top conversations and a packet table with per-packet detail. Files are parsed locally and never uploaded. |
| **Cybersecurity Simulator** | <https://alfredang.github.io/cybersecuritysimulator/> | Safe threat-simulation lab covering phishing, XSS, SQL injection, password strength, malware, ransomware, social engineering and data leakage. |
| **RegexLab** | <https://alfredang.github.io/regexgenerator/> | Live regular-expression tester with flags, match explanation and substitution — used to filter and parse support logs. |
| **Killercoda Ubuntu Playground** | <https://killercoda.com/playgrounds/scenario/ubuntu> | Free browser-based Ubuntu terminal with root access — no install required. Used for every Linux command-line lab in this course. |

## Which lab uses which tool

| Tool | Labs |
| --- | --- |
| IP Calculator | Lab 3, Lab 4, Lab 6, Lab 9, Lab 28, Lab 42 |
| PCAP Analyzer | Lab 7, Lab 11, Lab 28 |
| Cybersecurity Simulator | Lab 38, Lab 39, Lab 40, Lab 41, Lab 47 |
| RegexLab | Lab 46 |
| Killercoda Ubuntu Playground | Lab 5, Lab 6, Lab 9, Lab 11, Lab 14, Lab 20, Lab 22, Lab 24, Lab 28, Lab 34, Lab 35, Lab 46, Lab 49, Lab 52, Lab 54 |

## Killercoda Ubuntu Playground

A real Ubuntu machine with root access, running in a browser tab. Used for every Linux command-line lab in this course.

```bash
# Every Killercoda lab starts by refreshing the package index
apt-get update -qq
apt-get install -y <the packages that lab needs>
```

The playground resets when idle. If your terminal disappears, reopen it and re-run the setup commands from the start of the lab.

## Windows command reference

```text
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /flushdns
ping <host>
tracert <host>
nslookup <domain>
netstat -ano
sfc /scannow
DISM /Online /Cleanup-Image /RestoreHealth
chkdsk C: /scan
robocopy <src> <dst> /MIR /R:2 /W:2
net accounts
net user
net localgroup Administrators
manage-bde -status C:
netsh advfirewall show allprofiles state
taskmgr
msconfig
eventvwr.msc
diskmgmt.msc
devmgmt.msc
taskschd.msc
lusrmgr.msc
perfmon.msc
gpedit.msc
cleanmgr
dfrgui
resmon
msinfo32
```

## Linux command reference

```bash
pwd
ls -la
cd <dir>
cp <src> <dst>
mv <src> <dst>
rm -r <dir>
mkdir -p <dir>
cat <file>
less <file>
grep -n '<pattern>' <file>
find <path> -name '<glob>'
df -h
du -sh <dir>
free -h
ps aux
top
htop
chmod 750 <file>
chown user:group <file>
useradd -m <user>
usermod -aG sudo <user>
ip -brief addr show
ip route show
ping -c 3 <host>
dig +short <domain>
traceroute <host>
ss -tulnp
tcpdump -i any -c 100 -w capture.pcap
apt-get update && apt-get install -y <pkg>
smartctl -H /dev/sda
lsblk
man <command>
```
