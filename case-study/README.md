# EvaluAI Case Study

This directory contains the materials and experimental configuration associated with the validation study reported in Section 3.4, **“Validation and performance analysis,”** of the associated paper.

The purpose of this directory is to improve the transparency and reproducibility of the reported experiments by documenting the assessment materials, experimental conditions, prompt templates, LLM configuration, evaluation procedure, and output-handling strategy used in the case study.

## Contents

The directory contains the following files:

- `exam_EN.pdf and exam_ES.pdf`: assessment used in the validation study.
- `rubric_EN.pdf and rubric_ES.pdf`: complete structured rubric used in the rubric-guided condition.
- `README.md`: complete description of the experimental setup and reproduction information.

No personally identifiable student information is included in the materials provided in this directory.


## 1. Participants and Student Submissions

The validation involved 14 students enrolled in undergraduate Software Engineering courses. 

Participation in the study was voluntary. Students were informed about the possibility of participating, and the exams of those who agreed to participate were included in the study.

One submission was excluded because its corresponding instructor score could not be retrieved from the original grading records, leaving 13 submissions for analysis.

The same 13 students completed the different parts of the assessment.


## 2. Assessment Materials

The complete assessment and rubric used in the case study are available in this directory in PDF format both in the original version in Spanish (ES) and translated to English (EN):

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

The same LLM and generation configuration were used in both conditions. The experimental difference was the grading information supplied to the model through the corresponding prompt.

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

Question: Identify well-known algorithms that solve this optimization problem. Briefly describe each one and justify its suitability for meeting the company’s requirements.
- Correctly identifies Prim’s and Kruskal’s algorithms as appropriate algorithms for this optimization problem. (0.4 points)
- Avoids mentioning clearly inappropriate algorithms for this task, such as DFS or BFS as direct solutions to the optimization problem. (0.2 points)
- Correctly explains Prim’s algorithm as starting from a vertex and growing the minimum spanning tree by repeatedly selecting the minimum-weight adjacent edge. (0.15 points)
- Correctly explains Kruskal’s algorithm as constructing the minimum spanning tree by adding edges in increasing order of weight. (0.15 points)
- Recognizes that cycles must not be formed in either approach. (0.05 points)
- Correctly addresses the time complexity, avoiding incorrect claims such as stating that both algorithms are O(n). (0.05 points)

Question: Implement an algorithm that, given the optimized circuit obtained in the previous section, identifies the two pins whose distance, defined as the length of the shortest path between them, is maximum. The algorithm must return that distance and the intermediate pins forming the shortest path between the corresponding pair of pins. The code must include comments explaining how it works. Show an example of how to call the algorithm from a main program, specifying the initial parameter values.
- Correctly understands the objective of the problem: find the pair of pins whose shortest-path distance is maximum. (0.8 points)
- Uses an appropriate shortest-path strategy to solve the problem. (0.7 points)
- Correctly reconstructs and returns the intermediate pins forming the corresponding shortest path. (0.6 points)
- Provides a coherent and functional implementation. (0.4 points)
- Includes explanatory comments in the code. (0.2 points)
- Includes an example of how to call the algorithm from a main program, specifying the initial parameter values. (0.3 points)

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

