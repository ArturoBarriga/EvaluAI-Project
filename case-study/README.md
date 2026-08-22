# EvaluAI Case Study

This directory contains the materials and experimental configuration associated with the validation study reported in Section 3.4, **“Validation and performance analysis,”** of the associated paper.

The purpose of this directory is to improve the transparency and reproducibility of the reported experiments by documenting the assessment materials, experimental conditions, prompt templates, LLM configuration, evaluation procedure, and output-handling strategy used in the case study.

## Contents

The directory contains the following files:

- `case_study_exam.pdf and .docx`: assessment used in the validation study.
- `case_study_rubric.pdf and .docx`: complete structured rubric used in the rubric-guided condition.
- `README.md`: complete description of the experimental setup and reproduction information.

No personally identifiable student information is included in the materials provided in this directory.


## 1. Participants and Student Submissions

The validation involved 13 students enrolled in undergraduate Software Engineering courses.

A total of 13 student submissions were included in the analysis. Each submission contained two parts of the exam, both of which were considered in the validation.

The same 13 students completed both parts of the assessment.

No student submissions were excluded from the analysis.


## 2. Assessment Materials

The complete assessment and rubric used in the case study are available in this directory in both PDF and Word formats:

- [`case_study_exam.pdf`](case_study_exam.pdf)
- [`case_study_exam.docx`](case_study_exam.docx)
- [`case_study_rubric.pdf`](case_study_rubric.pdf)
- [`case_study_rubric.docx`](case_study_rubric.docx)

The rubric is organized by assessment question and contains the grading criteria and associated scores used by EvaluAI during rubric-guided evaluation.

The materials included here correspond to those used in the reported case study and are provided in both formats to facilitate inspection and reproducibility of the experimental setup.


## 3. Experimental Design

Each student submission was evaluated under two experimental conditions:

1. **Evaluation without a structured rubric**
2. **Rubric-guided evaluation**

The same LLM and generation configuration were used in both conditions. The experimental difference was the grading information supplied to the model through the corresponding prompt.

### 3.1. Evaluation Without a Structured Rubric

In this condition, the student submissions were evaluated without providing the structured digital rubric.

The exact prompt template used in the reported experiment is reproduced below.

```text
[TODO: INSERT THE EXACT NON-RUBRIC PROMPT USED IN THE EXPERIMENT]

Important:
- Reproduce the prompt exactly as used in the experiment.
- Preserve the original instructions and ordering.
- Preserve placeholders used by the implementation.
- Do not simplify or rewrite the prompt for documentation purposes.
```

### 3.2. Rubric-Guided Evaluation

In the rubric-guided condition, EvaluAI provided the LLM with the assessment context, the student submission, and the structured digital rubric containing the grading criteria and associated scores.

The exact prompt template used in the reported experiment is reproduced below.

```text
[TODO: INSERT THE EXACT RUBRIC-GUIDED PROMPT USED IN THE EXPERIMENT]

Important:
- Reproduce the prompt exactly as used by EvaluAI.
- Preserve the original instructions and ordering.
- Preserve placeholders such as {rubric}, {exam}, {question}, or equivalent variables.
- Do not simplify or rewrite the prompt for documentation purposes.
```


## 4. LLM and Generation Configuration

The experiments were performed using the following LLM configuration.

| Parameter | Configuration |
| --- | --- |
| Provider | Google |
| Model | Gemini 2.0 Flash |
| Exact model identifier | `[TODO]` |
| API / API version | `[TODO: exact version if explicitly available]` |
| Temperature | `[TODO: value or provider default]` |
| Top-p | `[TODO: value or provider default]` |
| Top-k | `[TODO: value or provider default]` |
| Maximum output tokens | `[TODO: value or provider default]` |
| Other generation parameters | `[TODO: values or provider defaults]` |

Only parameters explicitly configured during the experiment should be reported as fixed values.

If a parameter was not explicitly configured by EvaluAI, document it as:

```text
provider default
```

rather than assigning a value retrospectively.

### 4.1. Provider Interaction

The reported implementation used the Google Gemini API to perform LLM-based evaluation.

[TODO: If applicable, briefly specify the SDK/library and version used to access the API.]

Example:

```text
Google Generative AI Python SDK: [TODO: package/version]
```



## 5. Repeated Evaluations

Each student submission was evaluated **[TODO: N] time(s)** under each experimental condition.

[TODO: choose the statement that reflects the actual experiment.]

### If each submission was evaluated once

> Each submission was evaluated once under each experimental condition.

### If each submission was evaluated multiple times

> Each submission was independently evaluated [TODO: N] times under each experimental condition. The reported performance metrics were calculated using [TODO: explain whether all runs, averages, medians, or another aggregation procedure were used].

The same repetition procedure was applied to both conditions.



## 6. Experimental Procedure

For each student submission, the following procedure was followed.

### Rubric-guided condition

1. The student submission was provided to EvaluAI.
2. The structured rubric associated with the assessment was selected.
3. EvaluAI constructed the rubric-guided prompt.
4. The prompt and submission were sent to Gemini 2.0 Flash.
5. The generated score and feedback were returned by the model.
6. The model output was processed by EvaluAI.
7. The generated grade was compared with the instructor-assigned grade for the validation analysis.

### Non-rubric condition

1. The same student submission was used.
2. The structured rubric was not provided to the model.
3. EvaluAI constructed the corresponding non-rubric prompt.
4. The prompt and submission were sent to the same Gemini 2.0 Flash model.
5. The generated score and feedback were returned by the model.
6. The model output was processed using the same output-processing procedure.
7. The generated grade was compared with the instructor-assigned grade.

No manual modification of the AI-generated grades should be included in the experimental comparison unless such modification was explicitly part of the reported protocol.

[TODO: Verify the previous sentence against the actual experimental procedure and replace it if necessary.]



## 7. Output Format and Parsing

The expected LLM output followed the format defined in the prompt templates reproduced above.

[TODO: Describe the exact expected output structure.]

For example:

```text
[TODO: insert representative expected output schema or format]
```

If the implementation required structured fields, document them explicitly.

Example:

```text
Score: <numeric score>
Feedback: <textual feedback>
```

Do not document an output schema that was not actually enforced in the reported experiments.



## 8. Malformed Outputs and API Failure Handling

The following procedures describe how EvaluAI handled malformed responses and API failures during the reported experiments.

### 8.1. Malformed or Incomplete Model Outputs

[TODO: Describe the actual behavior.]

Examples of information to report:

- whether the response was rejected;
- whether parsing was retried;
- whether the model was queried again;
- whether a default value was assigned;
- whether the submission was excluded;
- whether the output was manually inspected.

### 8.2. Output Parsing Failures

[TODO: Describe the actual procedure followed when the returned model output could not be parsed.]

### 8.3. Gemini API Failures

[TODO: Describe the actual behavior when an API request failed.]

Examples:

- automatic retry;
- manual re-execution;
- no retry;
- request discarded;
- error propagated to the user.

### 8.4. Retry Policy

[TODO: State the number of retries, delay strategy, or explicitly state that no automatic retry mechanism was used.]

### 8.5. Failures Observed During the Experiment

- Malformed or incomplete outputs observed: **[TODO: N]**
- Output parsing failures observed: **[TODO: N]**
- API failures observed: **[TODO: N]**

If none occurred, state this explicitly:

> No malformed outputs, parsing failures, or API failures occurred during the reported experiments.



## 9. Reference Grades and Evaluation Metrics

The AI-generated grades were compared with grades assigned by the course instructor(s).

[TODO: If more than one human grader participated, describe how reference grades were obtained.]

The validation reported in the paper uses Mean Absolute Error (MAE) to quantify the difference between the AI-generated grades and the instructor-assigned grades.

The reported results show that rubric-guided evaluation achieved closer agreement with instructor grading than evaluation without the structured rubric, reaching MAE values as low as **0.15** and reducing the error by up to **70%** in the evaluated scenario.

[TODO: Add any additional metrics reported in the manuscript if applicable.]


