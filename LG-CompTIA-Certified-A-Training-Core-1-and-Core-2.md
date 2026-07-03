# Learner Guide - CompTIA Certified A+ Training (Core 1 and Core 2)

## Course Overview

This learner guide supports practical CompTIA A+ training for learners preparing for help desk, desktop support, field technician, and junior IT support roles. The course covers both Core 1 and Core 2 skills with hands-on tasks, troubleshooting methods, and documentation habits.

Core 1 focuses on hardware, mobile devices, networking, virtualization/cloud, and hardware/network troubleshooting. Core 2 focuses on operating systems, security, software troubleshooting, and operational procedures.

## Before You Start

### Safety Rules

1. Do not open a power supply.
2. Disconnect power before handling internal PC components.
3. Use ESD protection when handling RAM, storage, adapters, and motherboards.
4. Do not erase, format, or wipe a real user disk in class.
5. Use demo devices, virtual machines, or trainer-provided images for risky tasks.
6. Ask before changing BIOS/UEFI, disk partitions, or security settings on shared equipment.

### Recommended Lab Environment

- Windows 10 or Windows 11 PC.
- One Windows virtual machine where available.
- Optional Linux virtual machine or live environment.
- Smartphone or tablet for settings review.
- Demo PC hardware or photos of components.
- Internet access for documentation lookup.

### Lab Journal

For every lab, record:

- Device or VM used.
- Symptoms or task objective.
- Tools opened.
- Commands run.
- Screenshots or notes.
- Result and verification.
- Documentation entry.

## Learning Outcomes

By the end of the course, you should be able to:

1. Identify common PC hardware components and connectors.
2. Explain laptop and mobile device hardware and connectivity.
3. Configure basic network settings and identify common ports.
4. Explain Wi-Fi, Bluetooth, and network device roles.
5. Explain virtualization and cloud service models.
6. Use a structured troubleshooting method.
7. Use Windows administrative and command-line tools.
8. Identify file systems and storage tools.
9. Apply security best practices such as MFA, least privilege, and malware prevention.
10. Troubleshoot common OS, application, boot, and malware symptoms.
11. Create backup and recovery plans.
12. Document work using tickets, asset records, and change notes.
13. Apply safety, professionalism, and communication best practices.

## Course Flow

### Day 1

| Time | Activity |
| --- | --- |
| 09:00 | Course briefing, exam overview, safety checklist |
| 09:30 | Lab 01 - PC Hardware, Components, Cables, and Peripherals |
| 11:30 | Lab 02 - Mobile Devices, Networking, and Wireless |
| 14:00 | Lab 03 - Virtualization, Cloud, and Hardware Troubleshooting |
| 16:00 | Lab 04 - Network Troubleshooting Tools |
| 17:00 | Core 1 review |

### Day 2

| Time | Activity |
| --- | --- |
| 09:00 | Day 1 recap |
| 09:30 | Lab 05 - Operating Systems, Command Line, and Admin Tools |
| 11:30 | Lab 06 - Security, Malware, Authentication, and Best Practices |
| 14:00 | Lab 07 - Software Troubleshooting, Backup, and Recovery |
| 15:45 | Lab 08 - Operational Procedures, Documentation, Change, and Safety |
| 17:00 | Final exam readiness checklist |

## Lab 01 Guide - PC Hardware, Components, Cables, and Peripherals

### Objectives

- Identify internal PC components.
- Compare storage, RAM, motherboard, CPU, and power components.
- Recognize common cables and connectors.
- Review peripheral and printer basics.

### Steps

1. Review a desktop or laptop hardware diagram.
2. Identify motherboard, CPU, RAM, storage, cooling, expansion slots, and power connectors.
3. Compare DIMM and SO-DIMM memory.
4. Compare HDD, SATA SSD, and NVMe SSD.
5. Identify USB-A, USB-C, HDMI, DisplayPort, VGA, Ethernet, audio, SATA, and power connectors.
6. Identify common printer types and consumables.
7. Match symptoms to hardware categories, such as no power, overheating, no display, no boot, or grinding noise.
8. Create a hardware inventory table.
9. Record safety precautions for each component type.

### Deliverables

- Hardware identification worksheet.
- Cable and connector table.
- Storage and RAM comparison.
- Basic hardware symptom table.

### Checkpoint

You can identify common parts and explain what each component does.

## Lab 02 Guide - Mobile Devices, Networking, and Wireless

### Objectives

- Review mobile device hardware and accessories.
- Configure basic network settings.
- Identify common ports and protocols.
- Compare wireless standards and security.

### Steps

1. Review laptop parts: display, battery, keyboard, touchpad, webcam, wireless antennas, and DC jack.
2. Review mobile accessories: USB-C, Lightning, docking stations, headsets, and Bluetooth peripherals.
3. On a PC or VM, view IP configuration.
4. Identify IPv4 address, subnet mask, gateway, and DNS server.
5. Review private IPv4 ranges and IPv6 link-local addresses.
6. Match common ports: HTTP 80, HTTPS 443, DNS 53, DHCP 67/68, SSH 22, RDP 3389, SMB 445.
7. Identify router, switch, access point, firewall, modem, and patch panel roles.
8. Compare 2.4 GHz and 5 GHz Wi-Fi behavior.
9. Review Bluetooth pairing and mobile synchronization concepts.
10. Document one small network diagram.

### Deliverables

- Mobile device notes.
- Port and protocol table.
- Network settings screenshot or notes.
- Simple network diagram.

### Checkpoint

You can explain how a client gets an IP address and reaches network services.

## Lab 03 Guide - Virtualization, Cloud, and Hardware Troubleshooting

### Objectives

- Explain virtualization and cloud models.
- Review VM resource requirements.
- Apply hardware troubleshooting methodology.
- Match symptoms to probable causes.

### Steps

1. Compare Type 1 and Type 2 hypervisors.
2. Identify VM resource needs: CPU, RAM, storage, network, and security.
3. Compare IaaS, PaaS, and SaaS.
4. Compare public, private, hybrid, and community cloud.
5. Create or inspect a simple VM if permitted.
6. Record VM settings and virtual network mode.
7. Review the troubleshooting methodology.
8. Match symptoms to likely causes: no power, POST beep codes, overheating, BSOD, black screen, boot failure, slow performance.
9. Create a troubleshooting plan for one hardware symptom.
10. Document verification and escalation criteria.

### Deliverables

- Virtualization and cloud comparison table.
- VM settings notes.
- Hardware troubleshooting worksheet.
- Escalation criteria.

### Checkpoint

You can explain when to use a VM and how to approach hardware faults safely.

## Lab 04 Guide - Network Troubleshooting Tools

### Objectives

- Use common network commands.
- Diagnose basic connectivity symptoms.
- Interpret command output.
- Document network troubleshooting.

### Steps

1. Open Command Prompt or PowerShell.
2. Run `ipconfig /all`.
3. Identify IP address, gateway, DNS, MAC address, and DHCP status.
4. Run `ping 127.0.0.1`.
5. Ping the default gateway.
6. Ping a public IP address if permitted.
7. Run `nslookup` for a known domain.
8. Run `tracert` to a known domain.
9. Run `netstat -ano`.
10. Identify symptoms such as APIPA address, DNS failure, gateway unreachable, and intermittent connectivity.
11. Create a troubleshooting decision table.
12. Write a ticket note summarizing findings.

### Deliverables

- Command output notes.
- Connectivity test table.
- Network symptom decision table.
- Ticket note.

### Checkpoint

You can use basic tools to separate IP, gateway, DNS, and application connectivity issues.

## Lab 05 Guide - Operating Systems, Command Line, and Admin Tools

### Objectives

- Use Windows administrative tools.
- Run command-line utilities.
- Review file systems and disk tools.
- Compare Windows, macOS, and Linux basics.

### Steps

1. Open Task Manager and identify CPU, memory, disk, and startup tabs.
2. Open Device Manager and identify device categories.
3. Open Disk Management and review partitions and volumes without changing them.
4. Open Event Viewer and locate system/application logs.
5. Run `sfc /?`, `chkdsk /?`, `diskpart`, `gpupdate /?`, and `gpresult /?` only in safe/help mode unless instructed.
6. Review NTFS, FAT32, exFAT, ext4, APFS, and HFS+.
7. Run safe file commands such as `dir`, `copy`, and `xcopy /?`.
8. Review basic Linux commands: `ls`, `cd`, `pwd`, `ps`, `grep`, `chmod`.
9. Compare macOS Finder, Spotlight, Time Machine, and Keychain concepts.
10. Document which tool fits each support task.

### Deliverables

- Windows tool notes.
- Command-line reference table.
- File system comparison.
- OS support task map.

### Checkpoint

You can choose the right OS tool for performance, device, disk, event, and command-line tasks.

## Lab 06 Guide - Security, Malware, Authentication, and Best Practices

### Objectives

- Apply basic security best practices.
- Compare authentication methods.
- Review malware types and response.
- Explain data destruction and physical security.

### Steps

1. Review password policy, account lockout, and least privilege.
2. Identify where MFA can be enabled.
3. Compare password, PIN, biometric, smart card, token, and SSO concepts.
4. Review malware types: virus, worm, Trojan, ransomware, spyware, rootkit, keylogger, adware.
5. Create a safe malware response flow.
6. Include investigation, quarantine, remediation, updates, restore point, and user education.
7. Review host firewall and anti-malware settings.
8. Compare data disposal methods: shredding, wiping, degaussing, drilling.
9. Review physical security controls: locks, badges, privacy screens, cable locks.
10. Write a short security checklist for a new workstation.

### Deliverables

- Authentication comparison.
- Malware response checklist.
- Data destruction table.
- Workstation security checklist.

### Checkpoint

You can explain how to reduce risk without disrupting normal support operations.

## Lab 07 Guide - Software Troubleshooting, Backup, and Recovery

### Objectives

- Troubleshoot common OS and software symptoms.
- Review Windows recovery options.
- Create backup and recovery notes.
- Document the repair process.

### Steps

1. Review symptoms: slow performance, freezing, app crash, service failure, slow boot, missing OS, invalid boot disk.
2. Open Services and identify running/stopped services.
3. Review Startup Apps in Task Manager.
4. Review Safe Mode, Startup Repair, System Restore, and WinRE concepts.
5. Create a restore point if permitted.
6. Compare full, incremental, and differential backups.
7. Explain the 3-2-1 backup rule.
8. Create a sample user data backup plan.
9. Build a troubleshooting worksheet for one software symptom.
10. Include verification and prevention steps.
11. Write a user-friendly closure note.

### Deliverables

- Software symptom table.
- Recovery options notes.
- Backup plan.
- Troubleshooting worksheet.
- Closure note.

### Checkpoint

You can plan a safe repair path that protects user data and verifies the fix.

## Lab 08 Guide - Operational Procedures, Documentation, Change, and Safety

### Objectives

- Write professional ticket notes.
- Apply change management.
- Maintain asset documentation.
- Follow safety and communication best practices.

### Steps

1. Create a sample support ticket from a user report.
2. Record user, device, symptom, impact, priority, and contact details.
3. Write clear troubleshooting notes.
4. Create a change request with purpose, scope, risk, backout plan, and approval.
5. Create an asset inventory record with hostname, serial, asset tag, owner, location, warranty, and OS.
6. Review ESD prevention and component handling.
7. Review power safety and lifting safety.
8. Practise a professional user update message.
9. Write a knowledge base article for one resolved issue.
10. Complete the final A+ readiness checklist.

### Deliverables

- Sample ticket.
- Change request.
- Asset record.
- Knowledge base article.
- Professional communication example.

### Checkpoint

You can document technical work clearly and follow operational procedures that protect users and the business.

## Final Readiness Checklist

Before finishing the course, confirm that you can:

- Identify PC hardware components and connectors.
- Explain laptop and mobile device features.
- Configure and troubleshoot basic network settings.
- Recognize common ports and protocols.
- Explain virtualization and cloud models.
- Apply the troubleshooting methodology.
- Use Windows administrative and command-line tools.
- Compare common file systems.
- Apply security best practices.
- Explain malware response.
- Plan backup and recovery.
- Write tickets, change records, asset records, and knowledge articles.
