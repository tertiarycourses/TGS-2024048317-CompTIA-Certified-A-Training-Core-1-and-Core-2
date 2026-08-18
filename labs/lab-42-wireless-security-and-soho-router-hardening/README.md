# Lab 42 — Wireless Security and SOHO Router Hardening

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 07:** Security — Core 2, 28% of Core 2  
> **Exam objective:** Configure wireless encryption and harden a SOHO router against the attacks the default configuration invites (Core 2 objectives 2.9 and 2.10).

## Goal

A SOHO router shipped with default settings is one of the most commonly compromised devices in any small network. You work through every hardening step in order of impact and record what each one actually defeats.

## What you'll produce

A completed router hardening checklist with the threat each step defeats, and a wireless security configuration record.

## Tools and equipment

SOHO router or emulator, Wi-Fi analyser, IP Calculator, router documentation

### Browser tools used in this lab

- **IP Calculator** — <https://alfredang.github.io/ipcalculator/>

![IP Calculator interface map](../../courseware/assets/tool-ipcalculator.png)

*IP Calculator — the panels and fields this lab uses.*

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Record the wireless encryption generations in order and their status: WEP is broken and must never be used, WPA with TKIP is deprecated, WPA2 with AES-CCMP is the practical minimum, and WPA3 with SAE is current.
2. Record what WPA3's SAE handshake adds: it defeats the offline dictionary attack that works against a captured WPA2 handshake.
3. Change the default administrator password first, and record that default credentials for every common router model are published online.
4. Change the default SSID to a name that does not identify the router make, model or the household or business, since the model name tells an attacker which exploits to try.
5. Set WPA2-AES or WPA3 encryption with a passphrase of at least 16 characters, and record why the passphrase length matters against offline cracking.
6. Record the truth about disabling SSID broadcast: it stops the network appearing in casual scans but any wireless analyser still sees it, so treat it as tidiness rather than security.
7. Record the truth about MAC filtering: MAC addresses are trivially spoofed once observed, so it deters casual users but stops no capable attacker.
8. Update the router firmware and record why this matters most of all — router vulnerabilities are publicly disclosed and actively scanned for within days.
9. Disable WPS, disable remote or WAN-side administration, and disable UPnP unless a specific application requires it, recording the risk each one carries.
10. Configure the guest network as an isolated SSID with no access to the internal LAN, and verify the isolation from a connected guest device.
11. Set DHCP reservations for infrastructure devices and record the address plan, verifying the ranges in IP Calculator at https://alfredang.github.io/ipcalculator/.
12. Complete the hardening checklist ordered by impact, with the threat each step defeats, and mark which three steps you would perform if you had only five minutes.

## Test it — verification

Your checklist covers at least ten hardening steps each with a named threat; WEP, WPA, WPA2 and WPA3 are correctly ordered by security; SSID hiding and MAC filtering are correctly described as weak controls; and firmware update appears in your five-minute priority set.

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
