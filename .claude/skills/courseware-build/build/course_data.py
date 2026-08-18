"""
SINGLE SOURCE OF TRUTH — CompTIA Certified A+ Training (Core 1 and Core 2).

Every artifact (PPT deck, Lesson Plan, Learner Guide, LG Markdown mirror, labs
index and the assessment) is generated from this module plus data_domain1..9.py,
so titles, lab numbering, learning outcomes, the schedule and the assessment can
never drift apart.

Alignment principle: the course material is 100% aligned to the CompTIA A+
Core 1 (220-1101) and Core 2 (220-1102) exam domains and to the WSQ TSC
ICT-OUS-3007-1.1 (Infrastructure Support), so learners who complete the course
are prepared for both the WSQ assessment and the A+ certification exams.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "CompTIA Certified A+ Training (Core 1 and Core 2)"
SHORT_TITLE  = "CompTIA-Certified-A-Training-Core-1-and-Core-2"
COURSE_CODE  = "TGS-2024048317"
VERSION      = "v7.1"
VERSION_DATE = "19 August 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 5
HOURS        = 40
COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-comptia-certified-a-training-core-1-and-core-2.html"
REPO_URL     = "https://github.com/tertiarycourses/TGS-2024048317-CompTIA-Certified-A-Training-Core-1-and-Core-2"

# ------------------------------------------------------------------ skills framework
TSC_TITLE = "Infrastructure Support"
TSC_CODE  = "ICT-OUS-3007-1.1"
# The K and A sets MUST match the codes the assessment actually tests: the WA covers
# K1–K6 and the PP covers A1–A8, mirroring the original TMS papers. Declaring a
# shorter set here would mean assessing learners on outcomes the courseware never
# stated — so these lists are the single source for the deck, the LP and the LG.
TSC_KNOWLEDGE = [
    "K1 Diagnostic tools and processes to identify technical issues or disruptions in network infrastructure",
    "K2 Infrastructure and network configuration techniques",
    "K3 Troubleshooting techniques for infrastructure technical issues and problems",
    "K4 Potential benefits and impact of infrastructure upgrades and improvements",
    "K5 Sources of information for the development of infrastructure user guides and documentation",
    "K6 Types and purposes of system tests for infrastructure operating requirements",
]
TSC_ABILITIES = [
    "A1 Diagnose technical issues in network operations",
    "A2 Implement procedures to resolve root causes of technical issues",
    "A3 Troubleshoot technical issues in infrastructure systems",
    "A4 Perform advanced infrastructure configurations",
    "A5 Develop action plans for infrastructure upgrades",
    "A6 Propose infrastructure improvement ideas based on user needs",
    "A7 Test infrastructure systems against operating requirements",
    "A8 Organise information for the development of user guides",
]

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Diagnose technical issues in network operations and implement procedures to resolve root causes.",
    "LO2: Troubleshoot technical issues and perform advanced infrastructure configurations.",
    "LO3: Develop action plans for upgrades and propose improvement ideas based on user needs.",
    "LO4: Test infrastructure systems and organise information for developing user guides.",
]

# ------------------------------------------------------------------ exam domains
# CompTIA A+ Core 1 (220-1101) and Core 2 (220-1102) official domain weightings.
EXAM_DOMAINS = [
    ("Core 1 (220-1101)", [
        ("1.0 Mobile Devices", "13%"),
        ("2.0 Networking", "23%"),
        ("3.0 Hardware", "25%"),
        ("4.0 Virtualization and Cloud Computing", "11%"),
        ("5.0 Hardware and Network Troubleshooting", "28%"),
    ]),
    ("Core 2 (220-1102)", [
        ("1.0 Operating Systems", "28%"),
        ("2.0 Security", "28%"),
        ("3.0 Software Troubleshooting", "23%"),
        ("4.0 Operational Procedures", "21%"),
    ]),
]

# ------------------------------------------------------------------ topics (= exam domains)
# num, code, title, subtitle, weighting (share of course time), concept bullets
TOPICS = [
    dict(num=1, code="01", core="Core 1",
         title="Mobile Devices",
         subtitle="Laptop hardware · display components · accessories and ports · cellular and wireless · MDM and synchronisation",
         weighting="7%",
         exam_weight="13% of Core 1",
         concepts=[
            "Laptop hardware replacement covers the battery, keyboard and keys, RAM (SODIMM), HDD/SSD migration and replacement, and the wireless cards — each is a field-replaceable unit with its own removal sequence and anti-static precautions.",
            "LCD panels do not produce their own light: they need a backlight, historically a CCFL driven by an inverter, and today a strip of LEDs. Flickering or a dim image on an older panel points at the inverter or the backlight rather than the panel itself.",
            "LCD panel technologies trade off against each other. TN is fast with poor colour, IPS gives excellent colour and viewing angles, and VA sits between them with the best contrast. OLED needs no backlight at all, giving the deepest blacks and the highest contrast ratio.",
            "A digitizer converts analog touch or pen input into digital coordinates. When touch stops working but the image is perfect, the digitizer has failed, not the display panel — on many laptops the two are bonded and replaced as one unit.",
            "Connection methods differ in reach and purpose: USB-C, micro-USB and mini-USB for data and power, Lightning on older Apple devices, NFC for payments within about 4 cm, Bluetooth for peripheral pairing, and hotspot tethering to share a cellular connection.",
            "A port replicator reproduces a laptop's existing ports, while a docking station adds capability the laptop never had — full-size drive bays, expansion slots, optical drives and additional display outputs.",
            "Cellular generations step up in capability: 2G (GSM and CDMA) carried voice and SMS, 3G added mobile internet and video calling, 4G LTE reached hundreds of megabits per second, and 5G targets multi-gigabit speeds with very low latency.",
            "Bluetooth pairing follows a fixed sequence every time — enable Bluetooth, enable pairing mode, discover the device, enter the PIN or confirm the passkey, then test connectivity. Troubleshooting almost always means restarting that sequence.",
            "Mobile device management (MDM) and mobile application management (MAM) let an organisation push corporate email profiles, enforce two-factor authentication, deploy corporate applications and remotely wipe a lost device.",
            "Synchronisation binds a device to an account — Microsoft 365, Google Workspace or iCloud — and replicates mail, photos, calendar and contacts. Always check the data cap before enabling a full photo sync over a cellular connection.",
         ]),
    dict(num=2, code="02", core="Core 1",
         title="Networking",
         subtitle="Protocols and ports · network devices · wireless standards · SOHO networks · IP addressing · networking tools",
         weighting="12%",
         exam_weight="23% of Core 1",
         concepts=[
            "TCP is connection-oriented, sequenced and acknowledged with a 20–60 byte header, so it is used where delivery must be guaranteed. UDP is connectionless with an 8-byte header, so it is used where speed matters more than certainty — DNS queries, streaming and VoIP.",
            "The A+ exam tests a fixed list of ports by number: FTP 20/21, SSH and SFTP 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, NetBIOS 137–139, IMAP 143, SNMP 161/162, LDAP 389, HTTPS 443, SMB/CIFS 445 and RDP 3389.",
            "Insecure legacy protocols have secure replacements you should be able to name on sight: Telnet gives way to SSH, FTP to SFTP, HTTP to HTTPS, and SNMPv1/v2 to SNMPv3, which is the first version to encrypt its traffic.",
            "Network devices sit at different layers. A hub blindly repeats traffic to every port, a switch forwards frames by MAC address, a router forwards packets between broadcast domains by IP address, and a firewall filters traffic by rule.",
            "A SOHO router collapses several devices into one box: router, switch, wireless access point, firewall and DHCP server, and often adds content filtering, port forwarding and a VPN endpoint.",
            "Power over Ethernet carries both data and electrical power over one Ethernet cable, powering access points, IP cameras and VoIP phones. A PoE switch powers many devices, while a PoE injector powers a single device where no PoE switch exists.",
            "The 2.4 GHz band travels further and penetrates walls better but is slower and more congested, offering only three non-overlapping channels — 1, 6 and 11. The 5 GHz band is faster with far more non-overlapping channels but has a shorter usable range.",
            "IPv4 addresses are split by a subnet mask into a network portion and a host portion. The number of host bits determines how many usable addresses a subnet provides — always two fewer than the block size, because the network and broadcast addresses are reserved.",
            "Private address ranges (10.0.0.0/8, 172.16.0.0/12 and 192.168.0.0/16) are not routable on the internet and must be translated by NAT. An APIPA address in 169.254.0.0/16 means the client asked for DHCP and got no answer.",
            "A VPN builds an encrypted tunnel across the public internet so a remote host can reach private LAN resources, while a VLAN partitions one physical switch into several isolated logical networks that each need a router to talk to one another.",
            "Networking tools each answer one question: a crimper terminates RJ45 plugs, a cable tester confirms the pinout end to end, a toner probe finds which cable is which in a bundle, a punch-down tool seats wires into a patch panel, a loopback plug proves a port works, and a Wi-Fi analyser shows channel congestion.",
            "Common server roles you must recognise are DNS, DHCP, file share, print server, mail server, syslog, web server, proxy, spam gateway, unified threat management appliance and load balancer.",
         ]),
    dict(num=3, code="03", core="Core 1",
         title="Hardware",
         subtitle="Cables and connectors · RAM · storage and RAID · motherboards · CPUs and cooling · power supplies · printers",
         weighting="13%",
         exam_weight="25% of Core 1",
         concepts=[
            "Copper cable carries electrical signals and is cheap and easy to terminate but is limited to about 100 metres per run and is susceptible to electromagnetic interference. Fibre carries light, is immune to EMI, and reaches tens of kilometres at far higher speeds.",
            "Twisted-pair categories set the speed ceiling: Cat 5e carries 1 Gbps, Cat 6 carries 10 Gbps to 55 m, and Cat 6a carries 10 Gbps to the full 100 m. Shielded twisted pair adds a foil or braid screen for use near motors and fluorescent lighting.",
            "T568A and T568B are the two RJ45 pinouts. Matching both ends makes a straight-through patch cable; using A at one end and B at the other makes a crossover. Modern switch ports auto-negotiate with Auto-MDIX, so crossover cables are now rare.",
            "Display connectors differ in what they can carry. HDMI and DisplayPort carry digital video and audio, DVI carries digital and sometimes analog video only, and VGA is analog only. A passive adapter can change the plug shape but can never convert analog to digital.",
            "RAM comes as DIMMs in desktops and SODIMMs in laptops, and DDR generations are physically keyed so they cannot be mixed. Populating channels in matched pairs enables dual-channel mode and measurably improves memory bandwidth.",
            "ECC memory detects and corrects single-bit errors, which makes a server more stable but not faster. It requires a CPU and motherboard that explicitly support it, and it cannot be mixed with non-ECC modules.",
            "Storage is chosen on the trade-off between cost and speed. A hard disk drive gives the lowest cost per terabyte but has moving parts, a SATA SSD is far faster with no moving parts, and an NVMe M.2 drive on PCIe lanes is faster still.",
            "RAID trades disks for speed or safety. RAID 0 stripes for speed with no redundancy, RAID 1 mirrors for redundancy, RAID 5 stripes with distributed parity and survives one disk failure, and RAID 10 mirrors then stripes for both speed and redundancy.",
            "Motherboard form factors — ATX, micro-ATX, Mini-ITX — set the physical size and how many expansion slots are available. The chipset and CPU socket together decide which processors, memory types and features the board supports.",
            "BIOS/UEFI firmware initialises hardware and starts the boot process; CMOS backed by a coin cell stores the settings. A clock that resets to a default date on every boot is the classic sign of a dead CMOS battery.",
            "A Trusted Platform Module is a hardware chip that generates and stores cryptographic keys, and it is what BitLocker binds a drive to so the disk cannot simply be moved to another machine and read.",
            "A power supply must be sized on total wattage and must supply the right connectors — 24-pin ATX for the board, EPS 4/8-pin for the CPU, PCIe 6/8-pin for the graphics card, and SATA power for drives.",
            "The laser printing process runs in a fixed seven-step order — processing, charging, exposing, developing, transferring, fusing and cleaning — and knowing the order is what lets you turn a print defect into a specific failed component.",
            "Printer types suit different jobs: laser for fast, low-cost mono volume, inkjet for affordable colour, impact for multi-part carbon forms, thermal for receipts, and 3D printers using FDM filament or SLA resin for prototyping.",
         ]),
    dict(num=4, code="04", core="Core 1",
         title="Virtualization and Cloud Computing",
         subtitle="Hypervisors · virtual machines · resource requirements · cloud models · shared resources and metered use",
         weighting="6%",
         exam_weight="11% of Core 1",
         concepts=[
            "Virtualization runs several operating systems on one physical machine through a hypervisor, cutting hardware cost, power and rack space while letting you snapshot and roll back a whole machine in seconds.",
            "A Type 1 (bare-metal) hypervisor such as ESXi or Hyper-V runs directly on the hardware and is used in data centres. A Type 2 (hosted) hypervisor such as VirtualBox or VMware Workstation runs as an application on top of a desktop OS.",
            "Each virtual machine needs the same resources a physical machine would — its own vCPU allocation, RAM, disk and network adapter. Over-committing RAM across many VMs is the most common cause of a host grinding to a halt.",
            "Hardware virtualization support (Intel VT-x or AMD-V) must be enabled in BIOS/UEFI before a 64-bit guest will start. A hypervisor refusing to launch a VM is very often this setting rather than a software fault.",
            "Virtual desktop infrastructure hosts user desktops centrally and streams them to thin clients, which simplifies patching and secures data by keeping it in the data centre rather than on the endpoint.",
            "Cloud characteristics that define the model are shared resources, rapid elasticity, high availability, file synchronisation and metered utilisation — you pay for what you consume rather than for the capacity you provisioned.",
            "Deployment models describe who owns the infrastructure: public cloud is shared multi-tenant, private cloud is dedicated to one organisation, community cloud is shared by organisations with common requirements, and hybrid cloud spans private and public.",
            "Service models describe how much you manage. With IaaS you manage the OS and everything above it, with PaaS you manage only your application and data, and with SaaS the provider manages everything and you simply use the software.",
         ]),
    dict(num=5, code="05", core="Core 1",
         title="Hardware and Network Troubleshooting",
         subtitle="The CompTIA troubleshooting methodology · POST and boot faults · storage and RAID · display faults · printer and network symptoms",
         weighting="15%",
         exam_weight="28% of Core 1",
         concepts=[
            "The CompTIA six-step methodology is examinable in order: identify the problem, establish a theory of probable cause, test the theory to determine the cause, establish a plan of action and implement the solution, verify full system functionality and implement preventive measures, then document findings, actions and outcomes.",
            "Always question the obvious first and ask what changed. Most faults in the field are a recent change — a new driver, a moved cable, an installed update — rather than a spontaneous hardware failure.",
            "When a theory is not confirmed, you establish a new theory or escalate. Escalation is a legitimate step in the methodology, not an admission of failure, and it belongs in the documentation.",
            "POST beep codes and diagnostic LEDs report faults before any video output exists. A repeating beep pattern usually indicates RAM or graphics, and reseating the module is the correct first action.",
            "A blue screen of death or a macOS pinwheel points at a driver, failing RAM or a failing disk. Read the stop code, note what changed immediately before it, and test memory before replacing anything.",
            "Symptom clusters point at causes: a burning smell means shut down and unplug immediately, a grinding noise means a failing fan or drive, capacitor swelling means the motherboard is finished, and a date that resets each boot means the CMOS battery is dead.",
            "Overheating shows as thermal throttling, random reboots or shutdown under load. Check that fans spin, that intakes and heatsink fins are free of dust, that ambient airflow is adequate, and that thermal paste has not dried out.",
            "S.M.A.R.T. reports a drive's own health data — reallocated sectors, pending sectors and read error rate. A S.M.A.R.T. warning means back up the data now and replace the drive; it does not mean you have time.",
            "RAID recovery depends on the level. RAID 1, 5 and 10 survive a single disk failure and rebuild after you replace the drive, but RAID 0 has no redundancy at all and any single failure means restoring from backup.",
            "Display faults follow a short checklist: wrong input source, a physical cable fault, a dead backlight or projector bulb producing a dim image, burn-in from a static image, dead pixels, and colour problems from a wrong or damaged cable.",
            "Print defects map to components in the laser process — vertical lines mean a scratched drum, garbled output means the wrong driver, toner that wipes off means the fuser has failed, and repeated ghost images mean the drum is not being cleaned.",
            "Network symptoms have distinct signatures: an APIPA address means DHCP failed, high latency and jitter degrade VoIP and need QoS, port flapping points at a physical cable or connector fault, and intermittent wireless usually means distance, interference or channel overlap.",
         ]),
    dict(num=6, code="06", core="Core 2",
         title="Operating Systems",
         subtitle="Windows editions and installation · command line · Windows tools and MMC · file systems · macOS and Linux",
         weighting="17%",
         exam_weight="28% of Core 2",
         concepts=[
            "Windows editions differ in capability, and choosing correctly avoids paying for features nobody needs. Home has no domain join or BitLocker, Pro adds domain join, BitLocker, Group Policy and Remote Desktop hosting, and Enterprise adds large-scale management features.",
            "Installation types serve different situations: a clean install wipes and starts fresh, an in-place upgrade keeps files and applications, a network deployment images many machines at once over the wire, and cloning duplicates a prepared reference image.",
            "MBR partitioning is limited to four primary partitions and 2 TB disks, while GPT supports far more partitions and much larger disks and is required for UEFI Secure Boot. Getting this wrong is a common cause of an installer refusing to proceed.",
            "Windows file systems differ in what they can do. NTFS supports permissions, encryption, compression, journaling and very large files. FAT32 is limited to 4 GB files but is universally readable, and exFAT lifts the size limit for removable media.",
            "Navigation and file commands you must know are cd, dir, md, rd, copy, xcopy and robocopy — where robocopy is the resilient choice for large or resumable transfers and is what you use in real migrations.",
            "Networking commands each answer a specific question: ipconfig /all shows the full configuration, ping tests reachability, tracert shows the path, nslookup queries DNS directly, netstat lists active connections and pathping combines ping and tracert.",
            "Repair commands fix specific damage. sfc /scannow repairs protected system files, chkdsk /f fixes file system errors while /r also locates bad sectors, and DISM repairs the component store that sfc itself depends on.",
            "Task Manager is the first stop for performance triage — Processes shows what is consuming CPU, memory, disk and network, Performance graphs the trend, and Startup shows what is slowing the boot.",
            "The Microsoft Management Console hosts snap-ins you must be able to launch by name: eventvwr.msc, diskmgmt.msc, taskschd.msc, devmgmt.msc, lusrmgr.msc, perfmon.msc and gpedit.msc.",
            "Additional utilities cover the rest of the toolkit: msconfig for boot and startup, cleanmgr for disk cleanup, dfrgui to optimise drives, regedit for the registry and resmon for detailed resource analysis.",
            "A workgroup is a decentralised peer-to-peer arrangement using local accounts and is right for a SOHO, while a domain centralises authentication and policy in Active Directory and is what any organisation of scale uses.",
            "macOS provides Time Machine for backup, Disk Utility for partitioning and First Aid, FileVault for full-disk encryption, Keychain for credentials, Mission Control for window and desktop management, and Gatekeeper to control what may install.",
            "Linux command-line essentials are ls, cd, pwd, cp, mv, rm, mkdir, cat, grep, find, df, du, ps, top, chmod, chown, sudo, apt and man. These appear directly in Core 2 objective 1.11.",
            "Linux permissions are read, write and execute applied to owner, group and others, expressed either symbolically (rwxr-xr--) or numerically (754). chmod changes the permission bits and chown changes ownership.",
         ]),
    dict(num=7, code="07", core="Core 2",
         title="Security",
         subtitle="Physical and logical security · authentication and MFA · wireless security · malware · social engineering · workstation and mobile hardening",
         weighting="17%",
         exam_weight="28% of Core 2",
         concepts=[
            "Physical controls stop an attacker reaching the hardware at all: access control vestibules defeat tailgating, badge readers and biometrics control entry, cameras and alarms detect intrusion, and bollards and fences protect the perimeter.",
            "The principle of least privilege gives every user exactly the access their job requires and nothing more, which limits the blast radius when any single account is compromised.",
            "Multifactor authentication combines factors from different categories — something you know, something you have and something you are. Two passwords are not MFA because both come from the same category.",
            "Wireless security has a clear generational order. WEP is broken, WPA with TKIP is deprecated, WPA2 with AES-CCMP is the practical minimum today, and WPA3 adds SAE which defeats offline dictionary attacks against the handshake.",
            "Enterprise authentication is centralised through RADIUS, TACACS+ or Kerberos so that credentials live in one directory rather than being configured device by device.",
            "Malware types are distinguished by behaviour: a virus needs a host file and human action, a worm spreads by itself across a network, a trojan hides inside apparently legitimate software, ransomware encrypts data for payment, a rootkit hides at or below the OS, spyware exfiltrates information, and a keylogger records what you type.",
            "The seven-step malware removal procedure is examinable in order: investigate and verify symptoms, quarantine the system, disable System Restore, remediate by updating the anti-malware and scanning in safe mode, schedule scans and updates, re-enable System Restore and create a restore point, and finally educate the end user.",
            "Social engineering attacks the person, not the machine. Phishing, spear phishing, whaling, vishing and smishing all use a fabricated pretext and manufactured urgency to get the target to act before they think.",
            "In-person techniques include tailgating through a controlled door, shoulder surfing to read credentials, dumpster diving for discarded information, and impersonating IT support or a senior executive.",
            "Network attacks you must recognise are denial of service and its distributed form, on-path (man-in-the-middle) interception, DNS poisoning, ARP spoofing, SQL injection, cross-site scripting and the zero-day exploit for which no patch yet exists.",
            "Windows security settings that matter in practice are Defender Antivirus with current definitions, Defender Firewall, NTFS and share permissions where the most restrictive of the two wins, User Account Control, and BitLocker for full-volume encryption.",
            "Workstation hardening means strong password policies, account lockout thresholds, screensaver locks, disabling AutoRun, removing unused accounts and restricting administrative rights to those who genuinely need them.",
            "Mobile hardening relies on screen locks, biometrics, full-device encryption, remote wipe, locator services, current OS patches and installing applications only from the official store.",
            "Data destruction must match the sensitivity of the data. Physical destruction by drilling, shredding, degaussing or incinerating is irreversible, while wiping and low-level formatting allow reuse — and outsourced destruction must return a certificate.",
         ]),
    dict(num=8, code="08", core="Core 2",
         title="Software Troubleshooting",
         subtitle="Windows OS symptoms · recovery tools · malware removal · browser problems · mobile OS and application faults",
         weighting="8%",
         exam_weight="23% of Core 2",
         concepts=[
            "The common repair sequence escalates from cheap to expensive: reboot, restart the service, uninstall or reinstall the application, add resources, verify requirements, run the system file checker, use System Restore, repair Windows, then reimage as the last resort.",
            "Windows recovery options differ in what they preserve. System Restore rolls back system files and the registry but not personal data, Reset reinstalls Windows with an option to keep files, and the Windows Recovery Environment provides startup repair and a command prompt when Windows will not boot.",
            "A blue screen of death is caused by a driver fault, failing RAM or disk corruption. Record the stop code, roll back the most recent driver or update, and run memory and disk diagnostics before replacing hardware.",
            "Sluggish performance is diagnosed with Task Manager and Resource Monitor to find which resource is saturated — CPU, memory, disk or network — and only then treated by trimming startup items, adding RAM or replacing a failing disk.",
            "A 'no OS found' message means the firmware cannot find a boot loader: check the boot order, remove any USB device that is being booted first, confirm the disk is detected, and repair the boot record from the recovery environment.",
            "Malware symptoms include unexpected pop-ups, browser redirection, certificate warnings, sudden slowdown, disabled security tools and unexplained network traffic — and any of them justifies quarantining the machine immediately.",
            "Browser problems map to specific causes: certificate warnings mean an expired, untrusted or misconfigured certificate, redirection points at adware or a hijacked search provider, and rogue extensions must be removed from the browser rather than from Windows.",
            "Mobile application faults are treated in a fixed order — force close, clear the cache, clear the application data, uninstall and reinstall, then check for OS and application updates.",
            "Mobile performance symptoms have common causes: battery drain from background applications or a weak signal forcing the radio to full power, overheating from sustained load or charging faults, and random reboots from a failing update or a swollen battery.",
            "Mobile security symptoms — high data usage, unexpected ads, sluggish response and unfamiliar applications — often trace back to sideloaded APKs, a rooted or jailbroken device, or an application spoofing a legitimate one.",
        ]),
    dict(num=9, code="09", core="Core 2",
         title="Operational Procedures",
         subtitle="Documentation and ticketing · asset management · change management · backup and recovery · safety and environment · professionalism · scripting and remote access",
         weighting="5%",
         exam_weight="21% of Core 2",
         concepts=[
            "A ticket is the unit of work and the audit trail. It must capture user and device information, a clear problem description, category, severity, escalation level, the steps attempted and the final resolution, written in plain professional language.",
            "Asset management tracks what the organisation owns through inventory lists, asset tags and barcodes, the procurement life cycle, warranty and licensing status, and the user each asset is assigned to.",
            "Documentation types each serve a purpose: acceptable use policies, network topology diagrams, standard operating procedures, new-user setup and end-user termination checklists, incident reports and knowledge-base articles.",
            "Change management protects production. Every change needs a documented business process, a stated purpose and scope, a risk analysis, a scheduled date and time, an approval, a rollback plan and a sandbox test before it goes live.",
            "The 3-2-1 backup rule requires three copies of the data on two different media with one copy off site, and it is the single most examinable backup fact in Core 2.",
            "Backup types trade time against restore complexity. A full backup copies everything, an incremental copies what changed since the last backup of any type and clears the archive bit, and a differential copies what changed since the last full backup and leaves the archive bit set.",
            "An untested backup is not a backup. Restore testing on a schedule is what proves the backup chain, the media and the documented restore procedure actually work.",
            "Electrostatic discharge damages components at voltages far below what a person can feel, so use an anti-static strap and mat, hold cards by the edges, store parts in anti-static bags and equalise potential before touching a component.",
            "Personal and electrical safety means disconnecting power before working inside a machine, never opening a power supply or CRT, using correct lifting technique, and knowing which fire extinguisher class is right for an electrical fire.",
            "Environmental controls cover safe disposal of batteries, toner and devices under the relevant MSDS/SDS, temperature and humidity management, dust control, and protecting equipment with surge suppressors and an uninterruptible power supply.",
            "Regulated data carries legal obligations: PII, PCI DSS for card data, GDPR for EU personal data, PHI under HIPAA for health data, and Singapore's PDPA — and the chain of custody must be preserved for anything that may become evidence.",
            "Professional conduct is assessable: dress appropriately, use plain language rather than jargon, maintain a positive attitude, listen without interrupting, be culturally sensitive, avoid distractions, set realistic expectations and follow up afterwards.",
            "Scripting automates repetitive support work — restarting machines, remapping drives, installing applications, running backups and gathering inventory — using .bat, .ps1, .vbs, .sh, .py or .js, with the risks of unintended system changes and browser or resource overload.",
            "Remote access methods differ in security and use case: RDP for Windows desktops, VNC for cross-platform screen sharing, SSH for encrypted command line, VPN for network-level access, and third-party screen-sharing tools for supporting end users.",
        ]),
]

# ------------------------------------------------------------------ day themes (8 training hours/day)
DAY_THEMES = {
    1: "Mobile Devices and Networking",
    2: "Hardware, Virtualization and Cloud",
    3: "Hardware and Network Troubleshooting",
    4: "Operating Systems and Security",
    5: "Software Troubleshooting, Operational Procedures and Assessment",
}

# ------------------------------------------------------------------ lab tools
LAB_TOOLS = [
    ("IP Calculator", "https://alfredang.github.io/ipcalculator/",
     "Browser subnet calculator for IPv4 and IPv6 — CIDR, netmask, network and broadcast addresses, usable host ranges and batch processing with CSV export."),
    ("PCAP Analyzer", "https://alfredang.github.io/pcapanalyzer/",
     "Browser packet-capture analyser — protocol distribution, top talkers, top conversations and a packet table with per-packet detail. Files are parsed locally and never uploaded."),
    ("Cybersecurity Simulator", "https://alfredang.github.io/cybersecuritysimulator/",
     "Safe threat-simulation lab covering phishing, XSS, SQL injection, password strength, malware, ransomware, social engineering and data leakage."),
    ("RegexLab", "https://alfredang.github.io/regexgenerator/",
     "Live regular-expression tester with flags, match explanation and substitution — used to filter and parse support logs."),
    ("Killercoda Ubuntu Playground", "https://killercoda.com/playgrounds/scenario/ubuntu",
     "Free browser-based Ubuntu terminal with root access — no install required. Used for every Linux command-line lab in this course."),
]

# ------------------------------------------------------------------ practice exam
PRACTICE_EXAM = dict(
    name="CompTIA A+ Core 1 and Core 2 Practice Exam",
    url="https://exams.tertiaryinfotech.com",
    note="Sit the practice exam before your certification attempt. It mirrors the Core 1 and Core 2 domain weightings so your score by domain shows exactly where to revise.",
)

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Practical Performance (PP) — hands-on support, configuration and troubleshooting tasks, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

# ------------------------------------------------------------------ recommended courses
RECOMMENDED_COURSES = [
    "WSQ - CompTIA Certified Network+ Training",
    "WSQ - CompTIA Certified Security+ Training",
    "WSQ - CompTIA Certified Server+ Training",
    "WSQ - CompTIA Certified Linux+ Training",
    "WSQ - CompTIA Certified Cloud+ Training",
    "WSQ - CompTIA PenTest+ Training",
]
