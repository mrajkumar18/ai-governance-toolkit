# Applicability Guide: Which Frameworks Apply to You?

> *Status reviewed: October 2026. Regulatory timelines are moving; verify every item against the official source and with Legal before relying on it. Not legal advice.*

Use this guide at G0 to decide which regimes are **binding**, which are **advisory**, and which are **benchmarks only**.

## 1. Quick decision table

| Framework | Nature | Applies when | Notes |
|---|---|---|---|
| **EU AI Act** (Reg. 2024/1689) | Binding law | You place AI on the EU market, deploy it in the EU, or its output is used in the EU | Extraterritorial reach. Otherwise use as a **benchmark** |
| **GDPR** | Binding law | You process personal data of people in the EU, or are established in the EU | Art. 22 (automated decisions) and DPIAs matter most for AI |
| **India DPDPA 2023 + DPDP Rules 2025** | Binding law (phased) | Digital personal data processed in India, or offered goods/services to people in India | Rules notified 13 Nov 2025; obligations phase in over roughly 18 months. Check commencement dates for each obligation |
| **RBI FREE-AI report** (Aug 2025) | Advisory expert-committee report | RBI-regulated entities (banks, NBFCs, payment operators, co-operative banks, credit information companies) | 7 guiding principles, 6 pillars, 26 recommendations. Treat as a strong signal; becomes binding only if adopted via RBI directions |
| **MeitY India AI Governance Guidelines** (Nov 2025) | Voluntary guidelines | Any organisation in India | Government has said it is not planning umbrella AI legislation for now; guidelines build on sector regulators and existing law |
| **CERT-In directions** | Binding | Service providers, intermediaries, data centres, body corporates in India | 6-hour incident reporting |
| **NIST AI RMF; NIST AI 600-1** | Voluntary | Anyone | Common reference for risk management |
| **ISO/IEC 42001** | Voluntary, certifiable | Anyone | AI management system standard; certification is optional |
| **ISO/IEC 27001** | Voluntary, certifiable | Anyone | The security foundation AI controls build on |
| **Other sector regulators** (SEBI, IRDAI, health, telecom) | Binding / advisory | Depending on sector | Check circulars for AI, outsourcing, model risk and cyber |

## 2. EU AI Act status (verify)

- **Prohibited practices** and **AI literacy** have applied since 2 February 2025. The Digital Omnibus rewords Art. 4 as an obligation to take measures to promote AI literacy (an obligation of means, not a guaranteed level of literacy for any person).
- **General-purpose AI** obligations for providers have applied since 2 August 2025. Deployers building on a GPAI model should obtain the provider's documentation (see G1).
- **Digital Omnibus on AI:** Regulation (EU) 2026/1744 was published in the Official Journal on 24 July 2026 and entered into force on 27 July 2026. It:
  - postpones **Annex III (stand-alone) high-risk obligations to 2 December 2027** and **Annex I (product-embedded) to 2 August 2028**;
  - adds two **new prohibited practices**: generating or manipulating non-consensual intimate material of identifiable people, and child sexual abuse material. These apply from **2 December 2026**;
  - gives providers of generative systems placed on the market before 2 August 2026 until **2 December 2026** to meet the Art. 50(2) machine-readable marking duty;
  - requires the Commission to publish guidance, including a voluntary template, on the post-market monitoring plan by **2 September 2027**.
- **Planning stance:** the internal tiers in this toolkit apply from day one regardless of legal dates; the delay changes legal exposure, not good practice.
- **Source note:** dates above were checked against law-firm analyses of the published regulation. Confirm them against the Official Journal text on EUR-Lex and with Legal, including any transitional rules, before relying on them.

## 3. Role determination (EU AI Act)

| If you... | You are probably... |
|---|---|
| Build a system and offer it under your name | **Provider** |
| Use a third-party system under your authority | **Deployer** |
| Build in-house and use it yourself | **Provider and deployer** |
| Modify a third-party high-risk system substantially, or rebrand it | **Provider** (Art. 25) |
| Import or distribute systems in the EU | **Importer / distributor** |

Duties differ sharply by role, so record the role in the [register](../02-inventory/ai-system-register.csv).

## 4. India-specific checks for AI

- **DPDPA:** itemised notice and valid consent, or a clear legitimate use; accuracy of data used for decisions (s.8(3)); security safeguards; breach intimation (s.8(6), Rule 7); erasure and retention; children's data (s.9); grievance redressal; cross-border transfer restrictions (s.16); additional duties for Significant Data Fiduciaries (s.10), which can include DPIAs and independent audit.
- **Financial sector:** map your controls to RBI FREE-AI pillars (the matrix includes an advisory pillar column), plus outsourcing, model-risk and customer-protection expectations.
- **Cyber:** CERT-In 6-hour reporting alongside DPDP timelines.

## 5. Maintenance

Review this guide **twice a year** and after any major regulatory announcement. Record the review date at the top.
