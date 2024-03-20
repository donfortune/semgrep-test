# Semgrep AWS CodeBuild Workflow

This repository contains documentation and configurations for establishing a Semgrep scanning workflow within AWS CodeBuild. The main objective is to set up Semgrep scanning for AWS CodeBuild.

## Introduction

Semgrep is an open-source static analysis tool with various applications including code maintenance, security vulnerability identification, code quality enhancement, and enforcing best practices. It offers customizable rules and supports multiple programming languages including Python, Java, Go, and Ruby.

### Features of Semgrep:

- **Language Support**: Semgrep supports multiple programming languages.
- **Custom Rules**: Users can define custom rules using Semgrep.
- **Integration**: Semgrep can be seamlessly integrated into various CI/CD pipelines and workflows.
- **Community and Ecosystem**: Semgrep has an active community and ecosystem supporting its development.
- **Pattern Matching**: Semgrep facilitates pattern matching for effective code analysis.



### Steps to Accomplish the Task

1. **Local Test**:
   - Install Semgrep locally using `pip install semgrep`.
   - Write a simple Python program.
     ![Semgrep Scan](images/python_file.png)
   - Set up rules for Semgrep to follow.
     ![Semgrep Scan](images/ruleset.png)
   - Run the Semgrep command: `semgrep --config ruleset.yaml main.py`.
     ![Semgrep Scan](images/local_run.png)

2. **Integration with AWS CodeBuild Workflow**:
   - Push the Python file, ruleset, and buildspec files to GitHub.
     ![Semgrep Scan](images/git_code.png)
   - Create a project on AWS CodeBuild.
     ![Semgrep Scan](images/python_1.png)
     ![Semgrep Scan](images/python_2.png)
     ![Semgrep Scan](images/python_3.png)
     ![Semgrep Scan](images/python_4.png)
     ![Semgrep Scan](images/python_5.png)
   - Start the build.
     ![Semgrep Scan](images/start_build.png)
   - Build success
     ![Semgrep Scan](images/build_success.png)
   - logs
     ![Semgrep Scan](images/logs.png)
     
