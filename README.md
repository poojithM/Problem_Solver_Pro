# Problem Solver Crew

## Overview
The **Problem Solver Crew** is an automated system built using [CrewAI](https://docs.crewai.com/) to generate, validate, and write Python code for problem-solving. This system follows a structured workflow involving three specialized agents that collaborate to produce efficient and error-free Python code.

## Project Structure
This project consists of:
- **Agents**: AI-powered agents responsible for generating, testing, and writing Python code.
- **Tasks**: Defined tasks that each agent executes to achieve the final goal.
- **Tools**: Various CrewAI tools used for interpreting code, searching PDFs, and writing files.
- **Crew**: A structured pipeline that orchestrates the execution of tasks in a sequential manner.

## Setup Instructions
### Prerequisites
- Python 3.8+
- Install required dependencies:
  ```bash
  pip install crewai crewai_tools python-dotenv
  ```
- Create an `.env` file to load environment variables if needed.

### Running the Crew
1. Ensure the configuration files (`agents.yaml` and `tasks.yaml`) are correctly placed in the `config/` directory.
2. Run the Python script:
   ```bash
   python main.py
   ```
3. The crew will sequentially generate, test, and write Python code.

## Agents
### 1. **coder_pro**
   - **Role**: Senior Python Coder
   - **Goal**: Generate Python code based on provided problem statements and test cases.
   - **Tools**: PDFSearchTool, CodeInterpreterTool

### 2. **code_completor**
   - **Role**: Python Code Completor
   - **Goal**: Generate additional test cases and validate the code correctness.
   - **Tools**: PDFSearchTool, CodeInterpreterTool

### 3. **code_writer**
   - **Role**: Python Code Writer Specialist
   - **Goal**: Save validated and error-free code into a Python file.
   - **Tools**: FileWriterTool

## Tasks
### 1. **coder_pro_task**
   - Reads problem statements and test cases from a file.
   - Generates a complete Python solution that passes all given test cases.

### 2. **code_completor_task**
   - Reads the generated code and existing test cases.
   - Creates three additional test cases and ensures the code passes all.

### 3. **code_writer_task**
   - Writes the validated Python code into a `problem.py` file.

## Execution Flow
1. **coder_pro** generates the initial Python solution.
2. **code_completor** verifies the solution and adds test cases.
3. **code_writer** saves the final code in a file.

## Tools Used
- **CodeInterpreterTool**: Runs and interprets Python code.
- **PDFSearchTool**: Extracts relevant information from a problem statement in a PDF.
- **FileWriterTool**: Writes Python code into a `.py` file.

## Notes
- The workflow is sequential, meaning each agent completes its task before passing it to the next.
- You can customize agent configurations in `config/agents.yaml`.
- Modify task logic in `config/tasks.yaml` to fit different problem-solving needs.

## References
- [CrewAI Documentation](https://docs.crewai.com/)

