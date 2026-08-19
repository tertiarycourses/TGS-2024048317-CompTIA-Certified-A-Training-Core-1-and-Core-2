# Lab 44 Worksheet — Data Destruction, Disposal and Regulated Data Handling

**Name:** ______________________    **Date:** ______________

**Exam objective:** Select the correct data destruction method for a stated sensitivity and retention requirement, and handle regulated data according to its legal obligations (Core 2 objectives 2.8 and 4.6).

## Record as you go

| Step | What you did | What you observed |
| --- | --- | --- |
| 1 | Separate the two destruction goals: physical destruction where the media will never be reused, and sanitisation where the media is to be reused or resold. |  |
| 2 | Record the physical destruction methods: drilling through the platters, shredding into small fragments, degaussing with a strong magnetic field, and incineration. |  |
| 3 | Record the critical exception: degaussing does not work on solid state drives, because SSDs store data in flash cells rather than magnetically. Shredding or cryptographic erase is required instead. |  |
| 4 | Record the sanitisation methods for reuse: a standard format which only clears the file table, a low-level format, and a multi-pass overwrite wipe which is the only reliable software method on a hard disk. |  |
| 5 | Record why a standard format is not destruction: it removes the index but leaves the data recoverable with freely available tools. |  |
| 6 | Record cryptographic erase for self-encrypting drives: destroying the encryption key renders all data unrecoverable instantly, which is the fastest correct method for an SED or an encrypted SSD. |  |
| 7 | Build the decision table matching data sensitivity to method: public data may simply be deleted, internal data must be wiped, confidential data must be wiped and verified, and regulated data must be physically destroyed with a certificate. |  |
| 8 | Record the outsourcing requirements: use a certified vendor, obtain a certificate of destruction listing serial numbers, and retain that certificate for the audit period. |  |
| 9 | Build the regulated data reference: personally identifiable information, PCI DSS for payment card data, GDPR for EU personal data, PHI under HIPAA for health data, and Singapore's PDPA. |  |
| 10 | For each regulation record what data it covers, the core obligation it imposes and the consequence of a breach. |  |
| 11 | Record the chain of custody: the chronological documentation of who held evidence, when, and what they did with it, and note that a gap in the chain can render evidence inadmissible. |  |
| 12 | Complete a chain-of-custody form for a hypothetical drive removed from a compromised machine, recording every handover with date, time, person and purpose. |  |

## Verification

**Success criterion:** Your decision table gives a method for all four sensitivity levels; you correctly state that degaussing does not work on SSDs; the regulated data reference covers at least five frameworks with obligations; and the chain-of-custody form has no gaps between handovers.

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
