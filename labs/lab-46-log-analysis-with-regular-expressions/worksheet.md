# Lab 46 Worksheet — Log Analysis with Regular Expressions

**Name:** ______________________    **Date:** ______________

**Exam objective:** Filter and parse system logs with regular expressions to isolate the events that matter during troubleshooting (Core 2 objectives 3.1 and 4.8).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open RegexLab at https://alfredang.github.io/regexgenerator/ and re... |  |
| 2 | Record the core building blocks: \d matches a digit, \w a word char... |  |
| 3 | Build a pattern matching an IPv4 address and test it against sample... |  |
| 4 | Build a pattern matching a timestamp in HH:MM:SS format and record ... |  |
| 5 | Build a pattern matching error severity keywords using alternation ... |  |
| 6 | Build a pattern matching an email address and test it against the s... |  |
| 7 | Build a pattern matching a MAC address in colon-separated form: ([0... |  |
| 8 | Experiment with the flags and record what each changes: g for all m... |  |
| 9 | Open the Killercoda Ubuntu playground and create a realistic log fi... |  |
| 10 | Apply the severity pattern with grep and confirm it returns exactly... |  |
| 11 | Apply the IP address pattern to extract every address mentioned in ... |  |
| 12 | Combine patterns to answer a real support question — which IP addre... |  |

## Verification

**Success criterion:** Every pattern is verified in RegexLab with its match count recorded; the severity grep returns exactly four lines from the log; the IP extraction returns four unique addresses; and the combined query correctly returns only the addresses from error and critical lines.

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
