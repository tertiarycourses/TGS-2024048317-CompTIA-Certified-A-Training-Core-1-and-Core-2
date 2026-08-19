# Lab 42 Worksheet — Wireless Security and SOHO Router Hardening

**Name:** ______________________    **Date:** ______________

**Exam objective:** Configure wireless encryption and harden a SOHO router against the attacks the default configuration invites (Core 2 objectives 2.9 and 2.10).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Record the wireless encryption generations in order and their status: WEP is broken and must never be used, WPA with TKIP is deprecated, WPA2 with AES-CCMP is the practical minimum, and WPA3 with SAE is current. |  |
| 2 | Record what WPA3's SAE handshake adds: it defeats the offline dictionary attack that works against a captured WPA2 handshake. |  |
| 3 | Change the default administrator password first, and record that default credentials for every common router model are published online. |  |
| 4 | Change the default SSID to a name that does not identify the router make, model or the household or business, since the model name tells an attacker which exploits to try. |  |
| 5 | Set WPA2-AES or WPA3 encryption with a passphrase of at least 16 characters, and record why the passphrase length matters against offline cracking. |  |
| 6 | Record the truth about disabling SSID broadcast: it stops the network appearing in casual scans but any wireless analyser still sees it, so treat it as tidiness rather than security. |  |
| 7 | Record the truth about MAC filtering: MAC addresses are trivially spoofed once observed, so it deters casual users but stops no capable attacker. |  |
| 8 | Update the router firmware and record why this matters most of all — router vulnerabilities are publicly disclosed and actively scanned for within days. |  |
| 9 | Disable WPS, disable remote or WAN-side administration, and disable UPnP unless a specific application requires it, recording the risk each one carries. |  |
| 10 | Configure the guest network as an isolated SSID with no access to the internal LAN, and verify the isolation from a connected guest device. |  |
| 11 | Set DHCP reservations for infrastructure devices and record the address plan, verifying the ranges in IP Calculator at https://alfredang.github.io/ipcalculator/. |  |
| 12 | Complete the hardening checklist ordered by impact, with the threat each step defeats, and mark which three steps you would perform if you had only five minutes. |  |

## Verification

**Success criterion:** Your checklist covers at least ten hardening steps each with a named threat; WEP, WPA, WPA2 and WPA3 are correctly ordered by security; SSID hiding and MAC filtering are correctly described as weak controls; and firmware update appears in your five-minute priority set.

- [ ] I completed every step in the lab.
- [ ] My result meets the success criterion above.
- [ ] I recorded my evidence (screenshots, output, completed tables).

## Reflection

**What surprised you in this lab?**

_______________________________________________________________

**Where would you apply this on the job?**

_______________________________________________________________

**What do you still need to revise before the exam?**

_______________________________________________________________
