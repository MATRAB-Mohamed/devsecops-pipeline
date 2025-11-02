# devsecops-pipeline

## CI / DevSecOps pipeline

GitHub Actions runs automatically on every push and pull request to `main`:
1. Create Python virtual environment
2. Install dependencies
3. Run unit tests with pytest
4. Run Bandit for Python security static analysis
5. Build the Docker image
6. Scan the Docker image with Trivy (fails the pipeline if HIGH/CRITICAL CVEs are found)

Security artifacts (Bandit report and Trivy SARIF) are uploaded in the workflow so they can be reviewed.

