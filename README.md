# EvaluAI: Automated Exam Grading and Feedback Platform Using Large Language Models

EvaluAI is an open-source web application for automated exam grading and feedback generation using Large Language Models (LLMs). The platform allows instructors to define structured digital rubrics, upload student exams, automatically evaluate responses, review AI-generated feedback, manually adjust results, and download structured PDF reports.

EvaluAI supports both digital and scanned handwritten submissions. It is designed as a domain-independent platform for AI-assisted assessment, enabling instructors and researchers to evaluate open-ended student artifacts in a more scalable, consistent, and traceable way.

## Main Features

* Creation and management of structured digital rubrics.
* Automated grading of individual exams.
* Batch grading of multiple exams.
* Support for PDF submissions, including scanned handwritten answers.
* Rubric-guided LLM evaluation using Google Gemini.
* Human-in-the-loop review of AI-generated grades and feedback.
* Manual correction and grade adjustment by the instructor.
* Storage of temporary and definitive exam results.
* Downloadable PDF feedback reports.
* Docker-based deployment for easy execution.

A video demonstration of the application workflow and main features is available here:

https://youtu.be/0obclKtnpmQ

## System Architecture

EvaluAI follows a modular client-server architecture designed to separate the user interface, application logic, data persistence, and external LLM-based evaluation services.

<img width="762" height="425" alt="fig1" src="https://github.com/user-attachments/assets/7c76e494-d442-4c14-aec9-0ac92bdbf13f" />


* **Presentation Layer (Frontend):** Implemented as a React single-page application. This layer provides the user interface for rubric management, exam upload, correction review, and report download. React Router is used to support asynchronous navigation without full-page reloads, providing a fluid user experience.

* **Logic Layer (Backend):** Implemented with FastAPI in Python. The backend exposes REST endpoints for user, rubric, and exam management, and coordinates the automated evaluation workflow. This includes document processing, prompt construction, communication with the Gemini API, and result handling.

* **Data Persistence Layer:** Implemented with MongoDB. The document-oriented database model allows EvaluAI to store flexible data structures such as rubrics, exam metadata, temporary corrections, and definitive results.




## Repository Structure

The repository is organized into two main components: the backend, which provides the API and coordinates the automated evaluation workflow, and the frontend, which provides the web interface used by instructors. Additional configuration files are included to support Docker-based execution, environment configuration, and example-based testing.

```text
EvaluAI-Project-main/
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── orchestrator.py
│   ├── requirements.txt
│   ├── dockerfile
│   ├── routers/
│   │   ├── exams.py
│   │   ├── rubrics.py
│   │   ├── temp_exams.py
│   │   └── users.py
│   ├── repo/
│   │   ├── exam_repo.py
│   │   ├── rubric_repo.py
│   │   ├── temp_exams_repo.py
│   │   └── user_repo.py
│   └── utils/
│       ├── gemini_client.py
│       ├── openai_client.py
│       └── openrouter_client.py
├── frontend/
│   ├── dockerfile
│   ├── package.json
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── index.js
│       ├── UserContext.js
│       ├── PrivateRoute.js
│       ├── Navbar.js / Navbar.css
│       ├── Home.js / Home.css
│       ├── Login.js / Login.css
│       ├── Register.js / Register.css
│       ├── HomeLayout.js / HomeLayout.css
│       ├── LayoutWithNavbar.js
│       ├── TeacherDashboard.js / .css
│       ├── CreateRubric.js / .css
│       ├── MyRubrics.js / .css
│       ├── GradeSingleExam.js / .css
│       ├── GradeBatchExams.js / .css
│       ├── MyExams.js / .css
│       ├── EditCorrection.js / .css
│       ├── ViewBatchExams.js / .css
│       ├── ViewResults.js
│       ├── LoadingOverlay.js
│       └── assets/
├── examples/                
│   ├── example_exam.pdf
│   └── example_rubric.docx
├── docker-compose.yml
├── package.json
├── .env / .env.example
└── temp/
```

The `examples/` folder contains an example exam that can be used to test the platform after installation.

## Requirements

### Recommended: Docker Execution

* Git
* Docker Engine
* Docker Compose v2
* A valid Google Gemini API key

### Local Execution Without Docker

* Python 3.10 or later
* Node.js 18 or later
* npm
* MongoDB
* A valid Google Gemini API key

For review purposes, a valid Gemini API key is provided with the artifact to allow reviewers to test the system without creating their own key.

## Installation and Execution with Docker

Docker is the recommended way to run EvaluAI.

### 1. Clone the Repository

```bash
git clone https://github.com/ArturoBarriga/EvaluAI-Project.git
cd EvaluAI-Project
```

### 2. Create the Environment File

Linux or macOS:

```bash
cp .env.example .env
```

Windows CMD:

```cmd
copy .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

### 3. Configure the Gemini API Key

Open the `.env` file and set the Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

For peer review, a valid Gemini API key has been created specifically to allow reviewers to assess the tool without needing to generate their own key. The key includes a limited budget that is sufficient to execute the example workflow included in this repository:

```env
GEMINI_API_KEY= 
```

### 4. Start the Application

```bash
docker compose up -d --build
```

### 5. Check That the Containers Are Running

```bash
docker compose ps
```

### 6. Open the Application

Frontend:

```text
http://localhost:3000
```

### 7. Stop the Application

```bash
docker compose down
```

To stop the application and remove stored data:

```bash
docker compose down -v
```

## Installation and Execution Without Docker

The system can also be executed manually. In this case, MongoDB must be running locally and the required environment variables must be configured in the `.env` file.

### 1. Clone the Repository

```bash
git clone https://github.com/ArturoBarriga/EvaluAI-Project.git
cd EvaluAI-Project
```

### 2. Create the Environment File

Linux or macOS:

```bash
cp .env.example .env
```

Windows CMD:

```cmd
copy .env.example .env
```

### 3. Configure the Environment Variables

Open the `.env` file and configure the Gemini API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Although the Gemini API key is configured in the .env file, when running the backend manually it may be necessary to also define the environment variable in the same active terminal session used to start the server.

Linux or macOS:

```bash
export GEMINI_API_KEY=your_gemini_api_key_here
```

Windows CMD:

```bash
set GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Start the Backend

From the repository root, create the Python virtual environment inside the `backend/` folder:

```bash
cd backend
python -m venv .venv
```

Activate the virtual environment.

Linux or macOS:

```bash
source .venv/bin/activate
```

Windows CMD:

```cmd
.venv\Scripts\activate
```

Install the backend dependencies:

```bash
pip install -r requirements.txt
```

Then return to the repository root:

```bash
cd ..
```

Start the backend from the repository root:

```bash
python -m uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Start the Frontend

Open a new terminal from the repository root:

```bash
cd frontend
npm install
npm run dev
```

Then open the frontend in your browser. Depending on the frontend configuration, the application will usually be available at:

```text
http://localhost:3000
```

or:

```text
http://localhost:5173
```

## Example Exam and Rubric

The rubric and exam provided as examples are inspired by the subject **Design and Analysis of Algorithms**. They do not contain real student submissions and were created as synthetic materials for demonstration and reproducibility purposes.

The rubric is organized by questions. Each question contains several criterion–point pairs that guide the LLM during the automated evaluation.

The complete rubric and exam are available in:

- `examples/example_rubric.docx`
- `examples/example_exam.pdf`

These files allow users and reviewers to test the complete EvaluAI workflow without preparing their own assessment material.

Suggested testing procedure:

1. Start the application.
2. Open the frontend in the browser.
3. Create or log in with a user account.
4. Go to the rubric management section.
5. Load or manually create the example rubric.
6. Go to the exam grading section.
7. Select the example rubric.
8. Upload the example exam.
9. Run the automated evaluation.
10. Review the AI-generated grade and feedback.
11. Confirm or manually adjust the result.
12. Download the generated PDF report.

## Authors

* José A. Barriga jose@unex.es
* Jesús Moruno jmorunom@alumnos.unex.es
* Arturo Barriga arturobc@unex.es
* Julio D. Arjona julioda@unex.es
* Pedro J. Clemente pjclemente@unex.es

Quercus Software Engineering Group, Departamento de Ingeniería de Sistemas Informáticos y Telemáticos, Universidad de Extremadura, Avenida de la Universidad s/n, 10003 Cáceres, Spain

**CRediT authorship contribution statement:**

José A. Barriga: Conceptualization, Methodology, Supervision, Writing – review & editing. Jesús Moruno: Conceptualization, Writing – original draft, Software, Implementation, Validation. Arturo Barriga: Writing – original draft, Writing – review & editing. Julio D. Arjona: Writing – original draft, Writing – review & editing. Pedro J. Clemente: Conceptualization, Methodology, Supervision, Writing – review & editing, Funding acquisition.




Academic use of EvaluAI should cite the associated SoftwareX paper.
