# Lab 38 Worksheet — Password Strength Analysis and Authentication Policy

**Name:** ______________________    **Date:** ______________

**Exam objective:** Analyse password strength quantitatively and write an authentication policy grounded in entropy and crack-time evidence (Core 2 objectives 2.2 and 2.6).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open https://alfredang.github.io/cybersecuritysimulator/ and select Password Lab from the top menu. |  |
| 2 | Enter the password 'password' and record the strength indicator, the estimated crack time and the approximate entropy in bits. |  |
| 3 | Enter 'Password1' and record the same three metrics, noting how little a capital letter and a digit actually add. |  |
| 4 | Enter 'P@ssw0rd!' and record the metrics, then note that character substitution on a dictionary word is exactly what cracking tools try first. |  |
| 5 | Enter a 16-character passphrase such as 'correct horse battery staple' and record how the metrics change against the substituted password. |  |
| 6 | Enter a 20-character random string and record the metrics, then compare the entropy against the passphrase to see which strategy wins. |  |
| 7 | Build the analysis table with all five passwords, their length, character set size, entropy in bits and estimated crack time. |  |
| 8 | State the conclusion the evidence supports: length increases entropy far more effectively than character substitution, so a long passphrase beats a short complex password. |  |
| 9 | Review the weak and strong password examples the tool lists, and record the pattern that makes the weak ones weak. |  |
| 10 | Write the authentication policy: minimum length, complexity requirements, expiry rules, reuse prevention, and the account lockout threshold and duration. |  |
| 11 | Justify each policy rule with a measured figure from your table rather than a general assertion. |  |
| 12 | Add the MFA requirement to the policy, stating which factor categories are acceptable and which accounts must use MFA without exception. |  |

## Verification

**Success criterion:** Your analysis table records the actual entropy and crack time from the tool for all five passwords; the conclusion that length beats substitution is supported by your own figures; and every policy rule cites a measured value.

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
