# Privacy and Security

## Data flow

For each evaluation, EvaluAI sends to the configured LLM provider (Google Gemini by default) the evaluation prompt, the grading rubric when rubric-guided evaluation is used, and the student submission (PDF pages or page images). No user accounts, student rosters, e-mail addresses, or database contents are transmitted. All other application data, including rubrics, evaluations, and user accounts, is stored in the MongoDB instance configured by the operator.

## Anonymization of submissions

EvaluAI does not automatically remove personal identifiers from student submissions. Submissions must therefore be anonymized before being uploaded when required. In the validation reported in the accompanying paper, all student names and direct identifiers were removed in accordance with the criteria established by the Data Protection Officer of the University of Extremadura, under which examinations processed in this form do not allow the identification of students. Automated redaction support is on the roadmap.

## Provider data-use terms

Under the paid tier of the Gemini API, Google states that submitted content is not used to improve its products. Under the free tier, submitted content may be used to improve Google products (see Google's official Gemini API pricing/terms, verified September 2026, terms may change). Deployments processing student work must use a paid-tier API key. For institutions that require stricter guarantees or data residency, the modular LLM-client layer allows integrating an institutionally hosted or region-constrained model instead. Assessing the data-use terms of any alternative provider integrated through this layer is the responsibility of the deploying institution.

## Storage, retention, deletion, and logging

Evaluation records (temporal and definitive exams), rubrics, and user accounts are stored in the operator's MongoDB deployment (Atlas or self-hosted via Docker Compose). Retention is entirely under the deploying institution's control, and stored evaluations and rubrics can be deleted through the platform. Submissions are processed in memory. Temporary files created during batch PDF splitting are deleted immediately after processing, and the platform does not maintain log files of submission content. Data sent to the LLM provider is additionally subject to the provider's own retention terms.

## Encryption

Communication with the Gemini API uses HTTPS/TLS. Connections to MongoDB Atlas use TLS, and Atlas encrypts data at rest by default. Self-hosted MongoDB deployments should enable equivalent protections.

## Authentication and authorization

All API endpoints except registration and login require a JWT bearer token issued at login (HS256, 8-hour expiry, signed with the operator-provided `JWT_SECRET` environment variable). User identity is taken exclusively from the validated token, and per-resource ownership is enforced server-side for all exam, temporary-exam, and rubric operations. Requests targeting another user's resources return 404. Credentials are stored as salted bcrypt hashes. Known limitations, kept on the roadmap: the frontend stores the session token in `localStorage` (exposed to XSS on hostile pages), there are no refresh tokens (re-login after expiry), and login is not rate-limited.

## Prompt-injection considerations

A submission could contain text attempting to manipulate the grading model. EvaluAI mitigates this risk through two mechanisms: (1) every AI-generated evaluation is reviewed and confirmed by the instructor through the Human-in-the-Loop workflow before becoming definitive; and (2) the prompt templates explicitly instruct the model to treat student-submission content strictly as material to be evaluated and never as instructions.

## Ethics of the reported validation

The validation used previously collected examination submissions. Before processing, student names and other direct identifiers were removed in accordance with the criteria established by the Data Protection Officer of the University of Extremadura for the use of examination data in this study.
