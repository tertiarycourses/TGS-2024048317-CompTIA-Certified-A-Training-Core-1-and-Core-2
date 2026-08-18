# Lab 43 — Windows Security Configuration and BitLocker Encryption

> **Course:** CompTIA Certified A+ Training (Core 1 and Core 2) (TGS-2024048317)  
> **Topic 07:** Security — Core 2, 28% of Core 2  
> **Exam objective:** Configure Windows security settings including Defender, the firewall, UAC, account policy and BitLocker encryption (Core 2 objectives 2.5 and 2.6).

## Goal

You configure and verify every Windows security setting the Core 2 objectives name, on a real machine, recording the command that checks each one — because in support work you need to verify state quickly, not click through settings pages.

## What you'll produce

A verified Windows security configuration record with a check command for each setting.

## Tools and equipment

Windows PC, Windows Security, Defender Firewall, gpedit, BitLocker, PowerShell as administrator

## Safety

- Disconnect mains power and hold the power button for 15 seconds before working inside any machine.
- Wear an anti-static strap connected to an earthed point; hold boards and cards by their edges.
- **Never open a power supply unit or a CRT monitor** — both retain a lethal charge after being unplugged.
- Never puncture, compress or charge a swollen lithium battery; isolate it and follow hazardous disposal procedure.

## Step-by-step

1. Open Windows Security and record the status of every protection area: virus and threat protection, firewall, app and browser control, device security and account protection.

   ```bash
   start windowsdefender:
   ```

2. Verify Defender Antivirus is enabled with current definitions, and record the definition version and date.

   ```bash
   powershell -Command "Get-MpComputerStatus | Select-Object AntivirusEnabled,RealTimeProtectionEnabled,AntivirusSignatureLastUpdated"
   ```

3. Record why definition currency matters: signature-based detection cannot identify a threat whose signature it does not yet hold.
4. Check the firewall state for all three profiles — domain, private and public — and record which are enabled.

   ```bash
   netsh advfirewall show allprofiles state
   ```

5. Examine the inbound rules and record how a rule is scoped by program, port, protocol and profile.

   ```bash
   netsh advfirewall firewall show rule name=all dir=in | findstr /C:"Rule Name" | head -10
   ```

6. Record the default firewall posture: block inbound unless explicitly allowed, permit outbound, and add exceptions only for a stated business need.
7. Check User Account Control's configured level and record what each level prompts for.

   ```bash
   reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v ConsentPromptBehaviorAdmin
   ```

8. Record the difference between running as a standard user and as an administrator, and why standard-user daily operation limits malware impact.
9. Examine the local account policy and record the password length, complexity, history and lockout threshold currently enforced.

   ```bash
   net accounts
   ```

10. Record the local users and their group memberships, and identify every account holding administrative rights.

   ```bash
   net user && net localgroup Administrators
   ```

11. Check BitLocker status on the system volume and record the protection state, the encryption method and the key protectors in use.

   ```bash
   manage-bde -status C:
   ```

12. Record what BitLocker protects against — theft of the physical drive — and note that it requires a TPM, that the recovery key must be stored somewhere other than the encrypted machine, and that BitLocker To Go covers removable drives.

## Test it — verification

Every check command returns output you have recorded; Defender is confirmed enabled with a definition date; all three firewall profiles have a recorded state; net accounts output is captured; and the BitLocker record states where the recovery key is stored.

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
