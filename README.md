# End-to-End CI/CD Pipeline (Python, Docker, Kubernetes) 🚀

This repository is a practical demonstration of a complete CI/CD (Continuous Integration & Continuous Deployment) pipeline. The goal is to fully automate the process of building, containerizing, and deploying a Python (Flask) web application to a Kubernetes cluster (Minikube) as soon as new code is pushed.

-----

## ⚙️ Tech Stack

  * 🐍 **Python (Flask):** The core application (a simple API returning JSON).
  * 🐳 **Docker:** Used to containerize the application.
  * ☸️ **Kubernetes (k8s):** Used for container orchestration.
  * 🏠 **Minikube:** Used to run a local Kubernetes cluster.
  * 🤖 **GitHub Actions:** The core CI/CD automation system.
  * 👟 **Self-Hosted Runner:** Allows GitHub Actions to run jobs on our local machine and access Minikube.
  * 📜 **Bash Scripting:** Used to run `sed` and `kubectl` commands within the pipeline.

-----

## 🗺️ Project Structure

```
Devops-Projects/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml       # (The CI/CD Pipeline brain)
│
├── my-tech-app/
│   ├── app/
│   │   ├── app.py          # (Flask application code)
│   │   └── requirements.txt
│   ├── k8s/
│   │   ├── deployment.yml  # (Instructions to deploy the app on k8s)
│   │   └── service.yml     # (Instructions to expose the app externally)
│   └── Dockerfile            # (The recipe to build the Docker Image)
│
└── README.md                 # (This file)
```

-----

## 🔄 The CI/CD Workflow

The entire process is automated and works as follows:

  * **Trigger:** A developer runs `git push` to the `main` branch.
  * **GitHub Actions:** Detects the push and triggers the workflow defined in `ci-cd.yml`.
  * **Job Dispatch:** The jobs are sent to the **Self-Hosted Runner** (running on the local machine).

### 1\. Build Job (build\_and\_push) - CI

  * **Checkout Code:** Downloads the latest version of the code.
  * **Set Short SHA:** Creates a unique version tag from the Git Commit hash.
  * **Login to Docker Hub:** Authenticates with Docker Hub using `Secrets`.
  * **Build and Push:** Builds the Docker Image (using `my-tech-app/Dockerfile`) and pushes it to Docker Hub (e.g., `monabawi/my-tech-app:latest` and `monabawi/my-tech-app:<sha>`).

### 2\. Deploy Job (deploy\_to\_k8s) - CD

  * **Needs:** (Waits for the `build_and_push` job to succeed).
  * **Checkout Code:** Downloads the code again.
  * **Set Kubeconfig:** Connects to the Minikube cluster using the `secrets.KUBECONFIG` (which was generated using `kubectl config view --flatten`).
  * **Substitute Values:** Uses `sed` (a Bash command) to replace the image name and version tag in the `deployment.yml` file with the new one.
  * **Deploy:** Uses `kubectl apply` to apply the changes. Kubernetes automatically performs a "Rolling Update" to the Pods.

-----

## 🚀 How to Run This Project

To get this pipeline running on your own machine:

### Prerequisites

  * A [GitHub](https://github.com/) account.
  * A [Docker Hub](https://hub.docker.com/) account.
  * `git` installed.
  * [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.
  * [Minikube](https://minikube.sigs.k8s.io/docs/start/) installed.

### Setup Steps

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/MoNabawy-2003/Devops-Projects.git
    cd Devops-Projects
    ```

2.  **Start Minikube:**

    ```bash
    minikube start
    ```

3.  **Set up GitHub Secrets:**
    Go to your repo's `Settings > Secrets and variables > Actions` and add the following:

      * `DOCKER_HUB_USERNAME`: Your Docker Hub username.
      * `DOCKER_HUB_TOKEN`: (Create an Access Token from your Docker Hub settings).
      * `KUBECONFIG`: (Copy the entire output of the `kubectl config view --flatten` command and paste it here).

4.  **Set up the Self-Hosted Runner:**

      * Go to `Settings > Actions > Runners > New self-hosted runner`.
      * Follow the instructions to download and configure the runner on your local machine (be sure to leave it running in a terminal).

5.  **Update Image Names:**

      * In the `ci-cd.yml` and `deployment.yml` files, change `monabawi/my-tech-app` to your own image name (e.g., `YourDockerUser/my-app`).

### 🚀 Test It\!

1.  Make a small change to the `my-tech-app/app/app.py` file (like changing the welcome message).
2.  **Push the change:**
    ```bash
    git add .
    git commit -m "My first test commit"
    git push origin main
    ```
3.  Go to the `Actions` tab in your GitHub repo and watch the pipeline run.
4.  **Once it succeeds, open a new terminal and run:**
    ```bash
    minikube service my-tech-app-service
    ```
5.  This will automatically open your browser to your running application\!
