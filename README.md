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

🧱 CI/CD Security Gate Explanation

This pipeline is intentionally designed to fail if any HIGH or CRITICAL vulnerabilities are detected during the container security scan.
The goal is to demonstrate real DevSecOps best practices, where security is integrated as a mandatory gate in the CI/CD process rather than an afterthought.

By enforcing this behavior, the pipeline:

Prevents deployment of vulnerable images to production.

Highlights the importance of “shift-left security”, where developers address issues early in the software lifecycle.

Ensures compliance with modern security standards used in enterprise DevSecOps pipelines.

A failed build in this context doesn’t indicate a broken project — it shows that the security gate is working as intended ✅
