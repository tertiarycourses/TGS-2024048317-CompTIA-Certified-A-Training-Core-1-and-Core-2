# Lab 46 Worksheet — Log Analysis with Regular Expressions

**Name:** ______________________    **Date:** ______________

**Exam objective:** Filter and parse system logs with regular expressions to isolate the events that matter during troubleshooting (Core 2 objectives 3.1 and 4.8).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Open RegexLab at https://alfredang.github.io/regexgenerator/ and review the cheatsheet covering character classes, anchors, quantifiers and groups. |  |
| 2 | Record the core building blocks: \d matches a digit, \w a word character, \s whitespace, . any character, ^ start of line, $ end of line and \b a word boundary. |  |
| 3 | Build a pattern matching an IPv4 address and test it against sample text: \b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b. Record the match count. |  |
| 4 | Build a pattern matching a timestamp in HH:MM:SS format and record the matches: \b\d{2}:\d{2}:\d{2}\b. |  |
| 5 | Build a pattern matching error severity keywords using alternation and the ignore-case flag: (ERROR\|CRITICAL\|FATAL\|WARN). |  |
| 6 | Build a pattern matching an email address and test it against the sample text already loaded in the tool. |  |
| 7 | Build a pattern matching a MAC address in colon-separated form: ([0-9A-Fa-f]{2}:){5}[0-9A-Fa-f]{2}. |  |
| 8 | Experiment with the flags and record what each changes: g for all matches, i for case insensitivity, m for multiline anchors and s for dot matching newlines. |  |
| 9 | Open the Killercoda Ubuntu playground and create a realistic log file to apply your patterns to. |  |
| 10 | Apply the severity pattern with grep and confirm it returns exactly the error, warning and critical lines. |  |
| 11 | Apply the IP address pattern to extract every address mentioned in the log, then sort them uniquely. |  |
| 12 | Combine patterns to answer a real support question — which IP addresses appear in error lines only — and record the answer. |  |

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
