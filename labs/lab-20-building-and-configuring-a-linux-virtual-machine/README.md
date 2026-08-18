# Lab 20 — Building and Configuring a Linux Virtual Machine

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 04:** Virtualization and Cloud Computing — Core 1, 11% of Core 1  
> **Exam objective:** Provision, configure and verify a Linux virtual machine, and perform the post-installation tasks a technician must complete on any new guest (Core 1 objective 4.2).

## Goal

You provision a working Linux environment and complete the full post-installation checklist — updates, networking, users, storage and a snapshot — using the Killercoda Ubuntu playground so that no local install or licence is required and every learner gets an identical environment.

## What you'll produce

A configured Linux environment with verified networking, a created user, installed packages and a documented build record.

## Tools and equipment

Killercoda Ubuntu Playground (https://killercoda.com/playgrounds/scenario/ubuntu)

### Browser tools used in this lab

- **Killercoda Ubuntu Playground** — <https://killercoda.com/playgrounds/scenario/ubuntu>

![Killercoda Ubuntu Playground interface map](../../courseware/assets/tool-killercoda.png)

*Killercoda Ubuntu Playground — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open https://killercoda.com/playgrounds/scenario/ubuntu and wait for the terminal to become available. This is a real Ubuntu machine with root access, running in your browser.
2. Record the guest's identity: distribution, version, kernel and architecture — the first thing to establish on any unfamiliar machine.

   ```bash
   cat /etc/os-release && uname -a
   ```

3. Record the allocated resources: CPU count, total and available memory, and disk capacity and usage.

   ```bash
   nproc && free -h && df -h /
   ```

4. Update the package index and apply available upgrades, the mandatory first post-installation task on any new guest.

   ```bash
   apt-get update -qq && apt-get upgrade -y -qq
   ```

5. Install the tool set this course uses across the Linux labs.

   ```bash
   apt-get install -y net-tools iproute2 dnsutils curl vim tree htop
   ```

6. Record the network configuration: interface addresses, the default route and the configured DNS resolvers.

   ```bash
   ip -brief addr show && ip route show && cat /etc/resolv.conf
   ```

7. Verify outbound connectivity and DNS resolution in one test, then record the result.

   ```bash
   ping -c 3 8.8.8.8 && dig +short www.tertiarycourses.com.sg
   ```

8. Create a standard non-root user for daily work, following the principle of least privilege.

   ```bash
   useradd -m -s /bin/bash aplus && echo 'aplus:Training2026!' | chpasswd
   ```

9. Grant that user administrative rights through sudo rather than by using the root account directly.

   ```bash
   usermod -aG sudo aplus && groups aplus
   ```

10. Create a working directory structure for the course labs and confirm it was created as expected.

   ```bash
   mkdir -p /home/aplus/labs/{core1,core2,evidence} && tree /home/aplus
   ```

11. Set correct ownership on the new directories so the standard user, not root, owns their own files.

   ```bash
   chown -R aplus:aplus /home/aplus/labs && ls -ld /home/aplus/labs
   ```

12. Write the build record capturing the OS version, resources, installed packages, created user and network settings, so the machine could be rebuilt identically.

   ```bash
   echo "Built $(date) on $(cat /etc/os-release | grep PRETTY | cut -d'\"' -f2)" > /home/aplus/labs/build-record.txt && cat /home/aplus/labs/build-record.txt
   ```


## Test it — verification

The OS version and resources are recorded, updates complete without error, ping and dig both succeed, the aplus user exists in the sudo group, and the labs directory tree is owned by aplus rather than root.

## Troubleshooting this lab

| Symptom | What to check |
| --- | --- |
| A command returns "command not found" | Re-run the `apt-get install` step at the start of the lab — the playground starts with a minimal package set. |
| The Killercoda terminal has reset | The playground times out when idle. Reopen it and re-run the setup commands from step 1. |
| A browser tool will not load | Check the URL against `labs/tools.md`. All four tools run entirely client-side and need no login. |
| Output differs from the guide | Record what you actually observed — your environment differs from the reference, and explaining the difference is part of the exercise. |

## Review questions

1. State the exam objective this lab maps to, in your own words.
2. Which single step in this lab would you perform first on a real support call, and why?
3. What evidence would you attach to a support ticket to show this work was completed correctly?
4. Name one thing that would make this procedure fail, and how you would recognise it.

## Record your evidence

Complete [worksheet.md](worksheet.md) as you work through this lab and keep it — the Practical Performance assessment mirrors these tasks.

---

[← Labs index](../README.md)  ·  [Learner Guide](../../LG-CompTIA-Certified-A-Training-Core-1-and-Core-2.md)  ·  [Course page](https://www.tertiarycourses.com.sg/wsq-comptia-certified-a-training-core-1-and-core-2.html)
