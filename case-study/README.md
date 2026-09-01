# EvaluAI Case Study

This directory contains the materials and experimental configuration associated with the validation study reported in Section 3.4, **“Validation and performance analysis,”** of the associated paper.

The purpose of this directory is to improve the transparency and reproducibility of the reported experiments by documenting the assessment materials, experimental conditions, prompt templates, LLM configuration, evaluation procedure, and output-handling strategy used in the case study.

## Contents

The directory contains the following files:

- `exam_EN.pdf` and `exam_ES.pdf`: assessment used in the validation study.
- `rubric_EN.pdf` and `rubric_ES.pdf`: complete structured rubric used in the rubric-guided condition.
- `README.md`: complete description of the experimental setup and reproduction information.

No personally identifiable student information is included in the materials provided in this directory.


## 1. Participants and Student Submissions

The validation involved 14 students enrolled in undergraduate Software Engineering courses. 

Participation in the study was voluntary. Students were informed about the possibility of participating, and the exams of those who agreed to participate were included in the study.

One submission was excluded because its corresponding instructor score could not be retrieved from the original grading records, leaving 13 submissions for analysis.

The same set of 13 students was used consistently across the analysis of all assessment questions included in the case study.


## 2. Assessment Materials

The complete assessment and rubric used in the case study are available in this directory in PDF format, both in the original Spanish version (ES) and in an English translation (EN):

- [`exam_EN.pdf`](exam_EN.pdf)
- [`exam_ES.pdf`](exam_ES.pdf)
- [`rubric_EN.pdf`](rubric_EN.pdf)
- [`rubric_ES.pdf`](rubric_ES.pdf)

The rubric is organized by assessment question and contains the grading criteria and associated scores used by EvaluAI during rubric-guided evaluation.

The materials included here correspond to those used in the reported case study and are provided in both formats to facilitate inspection and reproducibility of the experimental setup.


## 3. Experimental Design

Each student submission was evaluated under two experimental conditions:

1. **Evaluation without a structured rubric**
2. **Rubric-guided evaluation**

Each of the 13 student submissions was independently evaluated three times under each experimental condition to account for the non-deterministic behavior of the LLM. This resulted in three repeated evaluations per submission and condition, using the same model and generation configuration across all executions.

### 3.1. Evaluation Without a Structured Rubric

In this condition, the student submissions were evaluated without providing the structured digital rubric.

The exact prompt template used in the reported experiment is reproduced below.

```text
Grade the exam according to the instructions and rubric (if provided).

Additional teacher instructions:
Do not penalize minor grammatical or spelling errors unless they affect the clarity or meaning of the response.

If a question has no student answer, explicitly indicate it in the "answer" field with the value "No answer", add a clarifying comment, and assign a score of 0.

If you detect a block of code or a complex mathematical expression in the student answer, it is not necessary to transcribe it literally. Instead, provide a brief and clear summary of the function or purpose of that code or expression.

If the exam content or the student answers are written in Spanish, translate them into natural academic English in the output.
Specifically, the fields "statement", "answer", "comments", and "general_comment" must always be written in English, even if the original exam is in Spanish.
Preserve the original meaning faithfully and do not omit relevant technical details.
Do not keep the transcription in Spanish unless a technical term, identifier, or code element must remain unchanged.

Output format:
Return EXCLUSIVELY a JSON object with this structure:
{
  "correction": [
    {
      "question": "question number or name",
      "statement": "literal text",
      "answer": "detected answer or 'No answer'",
      "max_score": maximum score for the question,
      "assigned_score": the score you assign to the student answer,
      "comments": "correction made to the student exercise and what they need to improve to obtain the maximum score for that exercise"
    }
  ],
  "student_name": "name of the student who took the exam; if not detected leave blank; format: LastName1 LastName2, FirstName",
  "general_comment": "General analysis summarizing performance, strengths, areas for improvement, and recommendations."
}
All numeric values must be unquoted numbers.
Do not include anything outside that JSON.
```

### 3.2. Rubric-Guided Evaluation

In the rubric-guided condition, EvaluAI provided the LLM with the assessment context, the student submission, and the structured digital rubric containing the grading criteria and associated scores.

The exact prompt template used in the reported experiment is reproduced below.

```text
Grade the exam according to the instructions and rubric (if provided).

Use the following rubric:

Question: Describe the data structures needed to model this problem. Define the relevant variables and provide a graphical representation of these structures.
- Recognizes that a graph must be used. (0.5 points)
- Recognizes structures (adjacency matrix or adjacency set) as suitable for implementing it. (0.4 points)
- Recognizes that the edges must be weighted. (0.4 points)
- Recognizes vertices as pins and edges as cables (even if not stated explicitly). (0.3 points)
- Provides a graphical representation of the structures. (0.4 points)

Question: State known algorithms that solve this optimization problem. Briefly describe each algorithm and justify its suitability for meeting the company's requirements.
- Mentions Prim and Kruskal as suitable algorithms. (0.3 points)
- Does not mention unrelated algorithms (e.g. DFS/BFS). (0.1 points)
- Correctly defines Prim (random starting vertex + lowest-weight adjacent edge). (0.2 points)
- Correctly defines Kruskal (adds lowest-weight edges globally). (0.2 points)
- Recognizes that neither algorithm can form cycles. (0.1 points)
- Recognizes the complexity of both algorithms. (0.1 points)

Question: Implement an algorithm that, given the optimized circuit resulting from the previous section, identifies the two pins whose distance, defined as the length of the shortest path between them, is maximum. The algorithm must return this distance and the intermediate pins that make up the shortest path between the corresponding pair of pins. The code must include comments explaining how it works. Show an example call to the algorithm from a main program, specifying the initial parameter values.
- Solves it with an optimal approach based on BFS or DFS. (0.6 points)
- Solves it with a non-optimal approach based on Floyd-Warshall. (0.4 points)
- If using Floyd-Warshall, implements the Path function to obtain intermediate vertices (not just mentions it). (0.5 points)
- Comments the code sufficiently well. (0.5 points)
- The code is free of errors. (1 points)

Additional teacher instructions:
Do not penalize minor grammatical or spelling errors unless they affect the clarity or meaning of the response.

If a question has no student answer, explicitly indicate it in the "answer" field with the value "No answer", add a clarifying comment, and assign a score of 0.

If you detect a block of code or a complex mathematical expression in the student answer, it is not necessary to transcribe it literally. Instead, provide a brief and clear summary of the function or purpose of that code or expression.

If the exam content or the student answers are written in Spanish, translate them into natural academic English in the output.
Specifically, the fields "statement", "answer", "comments", and "general_comment" must always be written in English, even if the original exam is in Spanish.
Preserve the original meaning faithfully and do not omit relevant technical details.
Do not keep the transcription in Spanish unless a technical term, identifier, or code element must remain unchanged.

Output format:
Return EXCLUSIVELY a JSON object with this structure:
{
  "correction": [
    {
      "question": "question number or name",
      "statement": "literal text",
      "answer": "detected answer or 'No answer'",
      "max_score": maximum score for the question,
      "assigned_score": the score you assign to the student answer,
      "comments": "correction made to the student exercise and what they need to improve to obtain the maximum score for that exercise"
    }
  ],
  "student_name": "name of the student who took the exam; if not detected leave blank; format: LastName1 LastName2, FirstName",
  "general_comment": "General analysis summarizing performance, strengths, areas for improvement, and recommendations."
}
All numeric values must be unquoted numbers.
Do not include anything outside that JSON.
```


## 4. LLM and Generation Configuration

The experiments were performed using the following LLM configuration.

| Parameter | Configuration |
| --- | --- |
| Provider | Google |
| Model | Gemini 2.5 Flash |
| Exact model identifier | `gemini-2.5-flash` |
| SDK | Google Generative AI Python SDK (`google.generativeai`) |
| Temperature | `0.3` |
| Top-p | Provider default |
| Top-k | Provider default |
| Maximum output tokens | `8000` |
| Other generation parameters | Provider defaults |

Only `temperature` and `max_output_tokens` were explicitly configured by EvaluAI. Other generation parameters, including `top_p` and `top_k`, were not explicitly specified and therefore used the defaults provided by the Google Gemini API. The same model and generation configuration were used throughout the reported evaluation. 

The implementation used the Google Gemini API through the Google Generative AI Python SDK (`google.generativeai`). The model was instantiated using the exact identifier `gemini-2.5-flash`.


## 5. Malformed Outputs and API Failure Handling

EvaluAI expects the LLM to return a structured JSON response. The system first attempts to extract JSON from a Markdown `json` code block and, if this is not available, searches the response for a JSON object or array. The extracted content is then cleaned and parsed using Python's `json` library.

If the response is empty, does not contain valid JSON, or cannot be parsed, the evaluation is considered unsuccessful. For PDF-based evaluation, EvaluAI also checks whether the response was truncated because the maximum token limit was reached (`MAX_TOKENS`) and raises an error in this case.

For image-based evaluation, unsuccessful requests are automatically retried up to three times, with an increasing delay between attempts. After the final unsuccessful attempt, no result is returned. PDF-based evaluation does not implement an internal retry loop; errors are propagated to the calling layer.


## 6. Operational metrics and cost model

### 6.1. Observed operational metrics

The following metrics were recorded during the six repeated batch evaluations of the 13 student submissions (13 submissions × 3 executions × 2 conditions = 78 LLM evaluations in total).

- **Processing time.** Median inter-submission time of ≈ 25 s in the no-rubric runs (per-run medians: 32 s, 25 s, 23 s) and ≈ 21 s in the rubric-guided runs (21 s, 22 s, 21 s). Uninterrupted intervals ranged from 14 to 63 s. A complete 13-submission batch finished in 4.5–7.5 minutes. Evaluations are dispatched sequentially by the orchestrator, parallel dispatch is a straightforward scalability improvement.
- **Execution success rate.** All 78 evaluations returned valid structured JSON and produced an evaluation report (78/78 successful). The handling of malformed outputs and API failures is described in Section 5.

### 6.2. Cost model

The cost of one evaluation can be estimated as:

```
C = (P_in / 10^6) · (T_prompt + T_rubric + T_doc)  +  (P_out / 10^6) · (T_answer + T_thinking)
```

**Token accounting (Gemini API):**

- PDF inputs: each page is billed as a fixed 258 input tokens, independently of its content, i.e. `T_doc = 258 · p` for a `p`-page submission.
- Image inputs (scanned pages sent as PNG): images with both dimensions ≤ 384 px are billed as 258 tokens; larger images are tiled into 768 × 768 crops billed at 258 tokens per tile (a typical scanned page corresponds to roughly 4–8 tiles).
- Measured in this case study: prompt template ≈ 500 tokens in the no-rubric condition and ≈ 1,050 tokens in the rubric-guided condition (including the complete three-question rubric, ≈ 560 tokens); visible output per evaluation: median ≈ 775–810 tokens, maximum ≈ 1,000 tokens. Thinking tokens are billed as output tokens and vary per request; total output is bounded by the configured `max_output_tokens = 8000`.

**Prices** (Gemini 2.5 Flash, Standard paid tier; list prices verified in August 2026 and subject to change): `P_in` = $0.30 and `P_out` = $2.50 per million tokens. The Batch API offers both at a 50% discount for non-interactive workloads.

**Worked example** (rubric-guided evaluation of a 4-page PDF submission): input ≈ 1,050 + 258 · 4 ≈ 2,080 tokens ≈ $0.0006; output ≈ 775 visible tokens plus thinking tokens (assuming 500–1,500) ≈ $0.003–0.006. The typical total cost is therefore **below $0.01 per submission**, with a hard upper bound of ≈ $0.021 imposed by the maximum output length. Evaluating a full 13-submission batch costs on the order of $0.05–0.10.
