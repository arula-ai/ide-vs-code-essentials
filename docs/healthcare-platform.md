# Healthcare Payment & Patient Management Platform

**Version:** 3.7.0
**Classification:** INTERNAL — RESTRICTED
**Owner:** Healthcare Information Technology Division
**Compliance Frameworks:** HIPAA, CMS, OIG
**Last Updated:** 2024-10-08
**Next Review:** 2025-04-01

---

## System Overview

The Healthcare Payment & Patient Management Platform (HP3M) is the enterprise system of record for patient intake, clinical data management, treatment tracking, insurance billing, and payment adjudication across the organization's affiliated hospital network. The platform serves 47 hospital sites, 312 outpatient clinics, and over 8,500 registered providers.

HP3M processes more than 180,000 insurance claims per month and manages patient records for over 1.2 million active patients. The platform integrates with all major commercial insurance carriers, Medicare, and Medicaid to support automated eligibility verification, claims submission, remittance processing, and denial management.

A critical function of HP3M is healthcare billing fraud detection. Healthcare fraud represents one of the most significant financial risks to both the organization and its insurance partners. The Centers for Medicare & Medicaid Services (CMS) estimates that improper payments — including fraud, waste, and abuse — account for billions of dollars in losses annually across the US healthcare system. HP3M's integrated fraud detection and compliance modules are designed to identify anomalous billing patterns, duplicate claims, upcoded procedures, and other indicators of healthcare billing fraud before claims are submitted or paid.

---

## Platform Architecture

### Core Modules

**1. Patient Registration and Identity Management (PRIM)**
Manages patient master records including demographic data, insurance coverage, primary care relationships, and contact preferences. PRIM enforces duplicate patient detection using probabilistic matching across name, date of birth, SSN partial hash, and address to prevent identity-based billing fraud.

**2. Clinical Data Repository (CDR)**
Immutable store of all clinical encounter data including diagnoses (ICD-10 codes), procedures (CPT codes), laboratory results, imaging reports, and clinical notes. The CDR serves as the source of truth for medical necessity validation during claims adjudication.

**3. Claims Processing Engine (CPE)**
The CPE translates clinical encounter data into standardized insurance claims (ANSI X12 837 format) and submits them to payer systems. The CPE applies a pre-submission fraud and abuse screening pass using the rules defined in the Claims Validation module.

**4. Risk Scoring Engine (RSE)**
The RSE produces a continuous risk score (0.0–1.0) for each patient encounter and associated claim, based on clinical profile analysis, billing pattern history, payer benchmarks, and anomaly detection models. Risk scores are stored in the patient record and are used by care coordinators, compliance officers, and billing auditors.

**5. Insurance Integration Framework (IIF)**
Manages real-time eligibility checks, prior authorization workflows, electronic remittance processing, and payer-specific claim formatting requirements. The IIF maintains direct connections to over 200 payer endpoints via clearinghouse and direct EDI channels.

**6. Compliance and Audit Module (CAM)**
The CAM provides compliance officers and internal audit with a complete view of flagged billing activity, open investigation cases, prior audit findings, and regulatory report generation capabilities. All fraud-related investigations are tracked in the CAM case management system.

---

## Patient Data Schema

The primary patient dataset (`healthcare_patients.csv`) conforms to the following schema. Each row represents one patient encounter or admission record.

| Column | Data Type | Description |
|---|---|---|
| `patient_id` | String | Unique patient identifier assigned at registration. Format: `P` followed by a numeric sequence. Links to the Patient Master Record in PRIM. |
| `hospital` | String | The name of the treating facility where the encounter occurred. |
| `diagnosis` | String | Primary diagnosis for the encounter, expressed as a human-readable description. The full ICD-10 code set is stored in the CDR; this field contains the principal diagnosis description for reporting purposes. |
| `treatment_type` | String | Classification of the treatment modality delivered during the encounter (e.g., Inpatient, Outpatient, Emergency, Surgical, Rehabilitation). |
| `treatment_cost_usd` | Numeric | Total billed cost of treatment in US Dollars as submitted to the insurance carrier. This is the billed amount, not the allowed or paid amount. |
| `insurance_provider` | String | The name of the primary insurance carrier responsible for adjudicating the claim. |
| `risk_score` | Float | Composite risk score assigned by the Risk Scoring Engine at the time of encounter. Scale: 0.0 (lowest risk) to 1.0 (highest risk). See Risk Score Interpretation for thresholds. |
| `region` | String | Two-letter US state code representing the geographic location of the treating facility. |
| `admission_date` | Date | Date of patient admission or encounter date for outpatient visits. Format: `YYYY-MM-DD`. |

---

## Payment Processing Workflow

### Standard Claims Lifecycle

```
Patient Encounter
      │
      ▼
Clinical Documentation (CDR)
      │
      ▼
Charge Capture & Coding (ICD-10 / CPT)
      │
      ▼
Pre-Submission Fraud Screening (Claims Validation Rules)
      │
      ├─ PASS ──► Electronic Claims Submission (ANSI X12 837)
      │                    │
      │                    ▼
      │             Payer Adjudication
      │                    │
      │            ┌───────┴────────┐
      │            ▼                ▼
      │         Approved          Denied
      │            │                │
      │            ▼                ▼
      │     Remittance (ERA)   Denial Management
      │            │                │
      │            ▼                ▼
      │     Payment Posting    Appeal Workflow
      │
      └─ FAIL ──► Compliance Hold → CAM Investigation
```

### Automated Eligibility Verification
Before every scheduled encounter, HP3M performs real-time insurance eligibility verification (ANSI X12 270/271) to confirm:
- Active coverage on the date of service
- Applicable deductible and out-of-pocket status
- Prior authorization requirements for planned procedures
- Coordination of benefits for patients with multiple payers

Eligibility failures are flagged in the scheduling system and escalated to the patient access team for resolution before the encounter occurs.

---

## Risk Scoring Model

### Risk Score Interpretation (0.0–1.0 Scale)

The Risk Scoring Engine assigns a composite risk score to each patient encounter based on a weighted combination of clinical, financial, and behavioral factors. Risk scores are recalculated at each encounter and are updated retrospectively if new information becomes available.

| Score Range | Risk Level | Clinical Interpretation | Billing/Compliance Action |
|---|---|---|---|
| 0.00 – 0.24 | Very Low | Routine encounter; standard risk profile | Standard processing; no additional review |
| 0.25 – 0.49 | Low | Minor deviations from expected norms | Periodic batch audit; no immediate action |
| 0.50 – 0.64 | Moderate | Elevated clinical complexity or billing anomaly | Care coordinator review; pre-authorization verification |
| 0.65 – 0.79 | High | Significant clinical risk or billing irregularity | Compliance officer review; additional documentation required |
| 0.80 – 0.89 | Very High | Strong indicators of high-cost or atypical care | Full clinical audit; billing hold pending review |
| 0.90 – 1.00 | Critical | Potential fraud, abuse, or serious clinical safety concern | Immediate escalation; payment hold; compliance investigation |

### High Risk Indicators

The Risk Scoring Engine weights the following factors most heavily in computing the composite risk score. Encounters exhibiting multiple high-risk indicators concurrently receive significantly elevated scores.

**Clinical Risk Indicators:**
- Diagnosis-Treatment Mismatch: The billed treatment type is not consistent with the documented diagnosis based on clinical evidence guidelines
- Procedure Upcoding Signal: Billed CPT code represents a higher complexity or resource level than documented clinical findings would support
- Excessive Frequency: The same procedure is billed for the same patient more frequently than clinical guidelines consider medically necessary
- Unbundling: Procedures that should be billed as a single bundled code are billed as separate line items to maximize reimbursement
- Duplicate Claim Indicator: A claim with identical patient, date of service, diagnosis, and procedure has been submitted previously

**Financial Risk Indicators:**
- Treatment cost significantly exceeds the regional and payer benchmark for the same diagnosis and treatment type
- Treatment cost significantly exceeds the same provider's own historical billing average for equivalent encounters
- Claim submitted more than 180 days after date of service (late filing anomaly)
- High concentration of maximum-allowable-benefit claims from a single provider

**Patient-Level Risk Indicators:**
- Patient has received the same diagnosis and treatment from multiple providers within 30 days (potential duplicate services)
- Patient's insurance coverage was added or changed within 90 days prior to a high-cost encounter
- Patient has a history of denied or reversed claims at this or other facilities

---

## Insurance Integration Framework

HP3M maintains active integrations with the following payer categories:

| Payer Category | Integration Method | Claim Format | Real-Time Eligibility |
|---|---|---|---|
| Commercial Insurers (Aetna, BCBS, Cigna, UHC) | Clearinghouse EDI | ANSI X12 837P/837I | Yes |
| Medicare (Part A & B) | Direct CMS Connectivity | ANSI X12 837 | Yes |
| Medicaid (State Programs) | State-specific EDI gateways | ANSI X12 837 / State formats | Varies by state |
| Workers Compensation | Clearinghouse EDI | ANSI X12 837 | No |
| Self-Pay / Uninsured | Internal billing system | N/A | N/A |

### Prior Authorization Management
Procedures requiring prior authorization (PA) are identified automatically at the point of order entry using the Procedure-to-Payer PA requirement matrix. HP3M submits electronic PA requests via ANSI X12 278 transaction sets and tracks authorization status in real time. Encounters with incomplete or expired authorizations are flagged at claims submission and routed to the authorization team for remediation. Submitting claims without required prior authorization is a compliance violation and may constitute billing fraud if done systematically.

---

## Compliance (HIPAA, Fraud Detection in Healthcare Billing)

### HIPAA Privacy and Security Requirements

The Health Insurance Portability and Accountability Act (HIPAA) establishes mandatory standards for the protection of Protected Health Information (PHI). HP3M's HIPAA compliance controls include:

- **Access Controls:** Role-based access control (RBAC) limits access to patient data based on job function. All data access is logged and audited.
- **Encryption:** PHI is encrypted at rest (AES-256) and in transit (TLS 1.3). Encryption keys are managed through a dedicated key management service.
- **Audit Logging:** All PHI access, modification, and transmission events are logged in tamper-evident audit logs retained for a minimum of 6 years.
- **Breach Notification:** Data breach response procedures comply with the HIPAA Breach Notification Rule, requiring notification to affected individuals within 60 days of discovery.
- **Business Associate Agreements (BAAs):** All third-party vendors with access to PHI are required to execute a BAA prior to data access.

### Healthcare Billing Fraud Detection

Healthcare billing fraud is a federal crime under the False Claims Act (31 U.S.C. § 3729) and the Health Care Fraud statute (18 U.S.C. § 1347). HP3M's fraud detection framework is designed to identify and prevent the following categories of healthcare billing fraud:

**Upcoding Fraud:** Billing for a higher-complexity service than was actually delivered. HP3M's coding audit module cross-references billed CPT codes against clinical documentation to identify discrepancies that may constitute upcoding fraud.

**Phantom Billing:** Billing for services, procedures, or equipment that were never provided to the patient. The RSE flags encounters where the billed procedure has no corresponding clinical documentation in the CDR.

**Duplicate Billing Fraud:** Submitting the same claim to multiple payers or submitting the same claim multiple times to the same payer. The Claims Processing Engine performs duplicate claim detection using a composite matching key before each submission.

**Unbundling Fraud:** Billing for individual components of a procedure separately when a bundled code (which reimburses at a lower rate) should be used. The CPE applies NCCI (National Correct Coding Initiative) edits to identify and correct unbundling.

**Kickback Violations:** The Anti-Kickback Statute (42 U.S.C. § 1320a-7b) prohibits payments for patient referrals. HP3M's compliance module monitors referral patterns for anomalies that may indicate kickback arrangements.

**Identity Fraud:** Using a patient's insurance information without their knowledge to submit fraudulent claims. The PRIM module's duplicate detection and the RSE's patient-level risk scoring are designed to detect identity-based healthcare billing fraud.

HP3M submits mandatory reports to the Department of Health and Human Services Office of Inspector General (OIG) when confirmed instances of fraud are identified. All internal fraud investigations are documented in the CAM system and retained for a minimum of 7 years.

### OIG Exclusion Screening
HP3M screens all providers, vendors, and contractors against the OIG List of Excluded Individuals and Entities (LEIE) monthly. Billing for services provided by an excluded individual is a significant compliance violation and is considered a form of healthcare billing fraud that can result in False Claims Act liability.

---

## Claims Validation Rules

The following validation rules are applied by the Claims Processing Engine before every claim submission. Claims failing any of these rules are held for manual review.

| Rule ID | Rule Name | Description | Action on Failure |
|---|---|---|---|
| CV-001 | Active Coverage Check | Confirms patient has active insurance coverage on the date of service | Hold; route to eligibility team |
| CV-002 | Prior Authorization Required | Confirms required prior authorization is on file for the billed procedure | Hold; route to authorization team |
| CV-003 | Diagnosis-Procedure Consistency | Validates that the billed CPT procedure is clinically consistent with the ICD-10 diagnosis using CMS LCD/NCD policies | Flag; coding review required |
| CV-004 | Duplicate Claim Detection | Checks for exact or near-exact duplicate claims in a 90-day lookback window | Reject; route to billing review |
| CV-005 | Provider Licensure Active | Confirms the billing provider holds an active, unrestricted license in the state of service | Hold; credentialing team notified |
| CV-006 | OIG Exclusion Check | Confirms neither the billing provider nor the treating provider is on the OIG LEIE | Block; immediate compliance escalation |
| CV-007 | Timely Filing Compliance | Confirms claim is submitted within the payer's required timely filing window | Reject with timely filing denial |
| CV-008 | NCCI Edit Compliance | Applies National Correct Coding Initiative edits to detect unbundling | Auto-bundle or flag for review |
| CV-009 | Risk Score Threshold | Claims with RSE risk score ≥ 0.80 are held for compliance review before submission | Hold; compliance officer review |
| CV-010 | Maximum Frequency Check | Confirms the same procedure has not been billed for the same patient more than the CMS-allowed frequency within the lookback period | Flag; medical necessity review |

---

## Data Quality Standards

HP3M enforces the following data quality standards across all patient and claims records:

- **Completeness:** All required fields must be populated. Claims with missing required data elements are rejected at ingestion.
- **Consistency:** Diagnosis codes must conform to the current ICD-10-CM code set. Procedure codes must conform to the current CPT code set. Code validation is performed against quarterly-updated reference tables.
- **Accuracy:** Patient demographic data is validated against government-issued identity documents at registration. Mismatches flag the account for identity verification review.
- **Timeliness:** Clinical documentation must be completed within 24 hours of the encounter by the treating provider. Documentation completed more than 72 hours post-encounter is flagged in the audit log.
- **Uniqueness:** Patient Master Record deduplication runs nightly. Potential duplicate records are flagged for manual review by the health information management team.

---

## Glossary

| Term | Definition |
|---|---|
| APC | Ambulatory Payment Classification. The Medicare payment system for outpatient hospital services. |
| CDR | Clinical Data Repository. The immutable clinical data store within HP3M. |
| CPE | Claims Processing Engine. The HP3M module responsible for claims generation and submission. |
| CPT | Current Procedural Terminology. The standardized medical code set used for billing professional services. |
| DRG | Diagnosis-Related Group. The Medicare inpatient payment classification system. |
| EDI | Electronic Data Interchange. The electronic exchange of standardized business documents between systems. |
| ERA | Electronic Remittance Advice. Electronic payment explanation sent by a payer upon claim adjudication. |
| False Claims Act | Federal statute (31 U.S.C. § 3729) imposing civil liability for submitting fraudulent claims to government healthcare programs. |
| HIPAA | Health Insurance Portability and Accountability Act. Federal law establishing privacy, security, and transaction standards for health information. |
| ICD-10 | International Classification of Diseases, 10th Revision. Standardized diagnosis coding system. |
| LEIE | List of Excluded Individuals/Entities. OIG database of individuals and entities excluded from participation in federal healthcare programs. |
| NPI | National Provider Identifier. Unique 10-digit identifier for healthcare providers. |
| OIG | Office of Inspector General. HHS agency responsible for oversight and fraud enforcement in federal healthcare programs. |
| PHI | Protected Health Information. Individually identifiable health information protected under HIPAA. |
| RSE | Risk Scoring Engine. The HP3M module that produces composite risk scores for patient encounters. |
| Upcoding | The fraudulent practice of billing for a higher-complexity or higher-cost service than was actually provided. |
