class DevOpsExperiments:
    def exp2(self):
        steps = [
            (
                "Create the Flask Application",
                "app.py",
                "from flask import Flask\n\n"
                "app = Flask(__name__)\n\n"
                "@app.route('/')\n"
                "def test():\n"
                "    return '<h1>hello from flask<h1>'\n\n"
                "if __name__ == '__main__':\n"
                "    app.run(host='0.0.0.0', port=9898, debug=True)"
            ),
            (
                "Create the Requirements File",
                "requirements.txt",
                "flask"
            ),
            (
                "Create the Dockerfile",
                "Dockerfile",
                "FROM python:3.10-slim\n"
                "WORKDIR /app\n"
                "COPY requirements.txt .\n"
                "RUN pip install --no-cache-dir -r requirements.txt\n"
                "COPY . .\n"
                "CMD [\"python\", \"app.py\"]"
            ),
            (
                "Build the Docker Image",
                "Terminal Command",
                "docker build -t <username>/exp2:latest ."
            ),
            (
                "Run the Container (Mapping Port 9898 to 9898)",
                "Terminal Command",
                "docker run -p 9898:9898 <username>/exp2:latest"
            ),
            (
                "Push to Docker Hub",
                "Terminal Commands",
                "docker login\n"
                "docker push <username>/exp2:latest"
            ),
            (
                "View the App",
                "Browser URL",
                "http://localhost:9898"
            )
        ]

        print("==================================================")
        print("  Exp 2: Flask Containerization & Docker Push     ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Experiment 2 ready! Remember the DOT at the end of build.")
        print("==================================================")

    def exp3(self):
        steps = [
            (
                "Create the Server (The API)",
                "app.py",
                "from flask import Flask, jsonify, request\n\n"
                "app = Flask(__name__)\n"
                "students = {}\n"
                "int_id = 1\n\n"
                "@app.route('/getstudents', methods=['GET'])\n"
                "def get_students():\n"
                "    return jsonify(list(students.values()))\n\n"
                "@app.route('/students', methods=['POST'])\n"
                "def add_students():\n"
                "    global int_id\n"
                "    data = request.get_json()\n"
                "    students[int_id] = {'id': int_id, 'name': data['name'], 'roll': data['roll']}\n"
                "    int_id += 1\n"
                "    return jsonify(students)\n\n"
                "@app.route('/delete', methods=['POST'])\n"
                "def delete_students():\n"
                "    data = request.get_json()\n"
                "    students.pop(data['id'], None)\n"
                "    return jsonify({'status': 'deleted'})\n\n"
                "if __name__ == '__main__':\n"
                "    app.run(port=5000)"
            ),
            (
                "Create the Client (The Requester)",
                "client.py",
                "import requests\n\n"
                "url = 'http://127.0.0.1:5000'\n\n"
                "def add_student():\n"
                "    name = input('Enter name: ')\n"
                "    roll = input('Enter roll: ')\n"
                "    res = requests.post(f'{url}/students', json={'name': name, 'roll': roll})\n"
                "    print(f'Status: {res.status_code}, Response: {res.text}')\n\n"
                "def get_students():\n"
                "    res = requests.get(f'{url}/getstudents')\n"
                "    print(f'Students List: {res.text}')\n\n"
                "add_student()\n"
                "get_students()"
            ),
            (
                "Install Requirements",
                "Terminal Command",
                "pip install flask requests"
            ),
            (
                "Step 1: Start the Server",
                "Terminal 1",
                "python app.py"
            ),
            (
                "Step 2: Run the Client (While Server is running)",
                "Terminal 2",
                "python client.py"
            )
        ]

        print("==================================================")
        print("  Exp 3: Flask Client-Server Interaction Guide    ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Remember: You need TWO terminal windows open!")
        print("==================================================")

    def exp4(self):
        steps = [
            (
                "Create the Python Application",
                "app.py",
                "print('hello from exp4')"
            ),
            (
                "Create the Dockerfile",
                "Dockerfile",
                "FROM python:3.10-slim\n\n"
                "WORKDIR /app\n\n"
                "COPY . .\n\n"
                "EXPOSE 9000\n\n"
                "CMD [\"python\",\"app.py\"]"
            ),
            (
                "Create the GitHub Actions Directories",
                "Terminal Command",
                "mkdir .github\\workflows"
            ),
            (
                "Create the Tiny CI/CD Pipeline",
                ".github/workflows/cicd.yml",
                "on: push\n"
                "jobs:\n"
                "  b:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - uses: actions/checkout@v4\n"
                "      - run: |\n"
                "          docker login -u ${{secrets.DOCKER_USERNAME}} -p ${{secrets.DOCKER_PASSWORD}}\n"
                "          docker build -t ${{secrets.DOCKER_USERNAME}}/app:latest .\n"
                "          docker push ${{secrets.DOCKER_USERNAME}}/app:latest"
            ),
            (
                "Build and Run Locally (To Verify)",
                "Terminal Commands",
                "docker build -t <username>/app:latest .\n"
                "docker run <username>/app:latest"
            ),
            (
                "Push to GitHub to Trigger Pipeline",
                "Terminal Commands",
                "git add .\n"
                "git commit -m \"Exp 4: Docker Build and Push\"\n"
                "git push"
            )
        ]

        print("==================================================")
        print("  Exp 4: Docker & GitHub Actions Reference        ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Files ready! Run the commands to push to Docker Hub.")
        print("==================================================")

    def exp5(self):
        files = {
            "app5.py": """print('Success! Hello from Experiment 5 Automated Pipeline')""",
            "Dockerfile": """FROM python:3.10-slim
WORKDIR /app5
COPY . .
EXPOSE 9776
CMD [\"python\",\"app5.py\"]""",
            "Jenkinsfile": """pipeline {
    agent any
    stages {
        stage('Build & Push') {
            steps {
                sh 'docker build -t <username>/app5:latest .'
                sh 'docker push <username>/app5:latest'
            }
        }
    }
}"""
        }

        commands = [
            ("1. Start Jenkins Container", "docker run -d --name jenkins -p 9890:8080 -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts"),
            ("2. Get Admin Password", "docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword"),
            ("3. Install Docker in Jenkins", "docker exec -u root jenkins bash -c 'apt-get update && apt-get install -y docker.io'"),
            ("4. Fix Permissions", "docker exec -u root jenkins chmod 666 /var/run/docker.sock"),
            ("5. Log in to Docker Hub", "docker exec -it jenkins docker login"),
            ("6. Push to GitHub", "git add .\ngit commit -m 'exp5 final'\ngit push origin main")
        ]

        def print_section(title, content):
            print("=" * 60)
            print(f"  {title}")
            print("=" * 60)
            print(content)
            print("\n")

        print("EXPERIMENT 5: FULL AUTOMATION WORKFLOW\n")

        for filename, content in files.items():
            print_section(f"FILE: {filename}", content)

        cmd_list = ""
        for i, (desc, cmd) in enumerate(commands, start=1):
            cmd_list += f"STEP {i}: {desc}\n{cmd}\n{'-'*30}\n"
        print_section("TERMINAL COMMANDS (Run in order)", cmd_list)

        print_section(
            "JENKINS UI SETUP",
            "1. URL: http://localhost:9890\n"
            "2. New Item -> Pipeline -> 'exp5-job'\n"
            "3. Definition: Pipeline script from SCM\n"
            "4. SCM: Git\n"
            "5. Branch Specifier: */main\n"
            "6. Click BUILD NOW"
        )

    def exp6(self):
        commands = [
            ("Start Minikube", "minikube start --driver=docker"),
            ("Create Deployment", "kubectl create deployment myapp --image=nginx"),
            ("Expose the App", "kubectl expose deployment myapp --port=80 --type=NodePort"),
            ("Scale the Pods", "kubectl scale deployment myapp --replicas=3"),
            ("Verify Everything", "kubectl get all"),
            ("View Webpage", "minikube service myapp"),
            ("Clean Up (Delete App)", "kubectl delete deployment myapp"),
            ("Clean Up (Delete Network)", "kubectl delete service myapp")
        ]

        print("==================================================")
        print("  Kubernetes Imperative Workflow - Lab Reference  ")
        print("==================================================\n")

        for _, cmd in commands:
            print(cmd)

    def exp7(self):
        steps = [
            (
                "Create the Python Application",
                "app2.py",
                "print('hello from exp7')"
            ),
            (
                "Create the Docker Blueprint",
                "Dockerfile",
                "FROM python:3.10-slim\n"
                "WORKDIR /app2\n"
                "COPY . .\n"
                "EXPOSE 8900\n"
                "CMD [\"python\",\"app2.py\"]"
            ),
            (
                "Create the GitHub Actions Directories (Windows)",
                "Terminal Command",
                "mkdir .github\\workflows"
            ),
            (
                "Create the CI/CD Pipeline",
                ".github\\workflows\\cicd.yml",
                "on: push\n"
                "jobs:\n"
                "  b:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - uses: actions/checkout@v4\n"
                "      - run: |\n"
                "          docker login -u ${{secrets.DOCKER_USERNAME}} -p ${{secrets.DOCKER_PASSWORD}}\n"
                "          docker build -t ${{secrets.DOCKER_USERNAME}}/app2:latest .\n"
                "          docker push ${{secrets.DOCKER_USERNAME}}/app2:latest"
            ),
            (
                "Push to GitHub to Trigger the Pipeline",
                "Terminal Commands",
                "git add .\n"
                "git commit -m \"Trigger CI/CD\"\n"
                "git push"
            )
        ]

        print("==================================================")
        print("  Exp 7: Docker + GitHub Actions CI/CD Reference  ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Pipeline triggered! Check your GitHub Actions tab.")
        print("==================================================")

    def exp8(self):
        steps = [
            (
                "Create the Flask Application",
                "app3.py",
                "from flask import Flask\n\n"
                "app=Flask(__name__)\n\n"
                "@app.route('/')\n"
                "def test():\n"
                "    return \"<h1>hello from flask app <h1>\"\n\n"
                "app.run(host='0.0.0.0',debug=True,port=9798)"
            ),
            (
                "Create the Requirements File (CRITICAL)",
                "requirements.txt",
                "flask"
            ),
            (
                "Create the Docker Blueprint",
                "Dockerfile",
                "FROM python:3.10-slim\n\n"
                "WORKDIR /app3\n\n"
                "COPY requirements.txt .\n"
                "RUN  pip install --no-cache-dir -r requirements.txt\n\n"
                "COPY . .\n"
                "EXPOSE 9798\n\n"
                "CMD [\"python\",\"app3.py\"]"
            ),
            (
                "Build the Docker Image",
                "Terminal Command",
                "docker build -t <username>/app3:latest ."
            ),
            (
                "Run the Docker Container",
                "Terminal Command",
                "docker run -p 9789:9798 <username>/app3:latest"
            ),
            (
                "View the Application",
                "Browser URL",
                "http://localhost:9789"
            )
        ]

        print("==================================================")
        print("  Exp 8: Flask App + Docker Reference Guide       ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Experiment 8 complete! Open the URL to verify.")
        print("==================================================")

    def exp9(self):
        steps = [
            (
                "Step 1: Clone the Repository",
                "Terminal Command",
                "git clone https://github.com/hishamkarunya/devops_lab.git\n"
                "cd devops_lab"
            ),
            (
                "Step 2: Check Status (See what's happening)",
                "Terminal Command",
                "git status"
            ),
            (
                "Step 3: Modify the README file",
                "Terminal Command",
                "echo # Updated Experiment 9 Content >> README.md\n"
                "cat README.md\n"
                "git diff"
            ),
            (
                "Step 4: Stage the changes",
                "Terminal Command",
                "git add README.md"
            ),
            (
                "Step 5: Commit the changes",
                "Terminal Command",
                "git commit -m \"docs: update README with new content\""
            ),
            (
                "Step 6: Push to GitHub",
                "Terminal Command",
                "git push origin main"
            ),
            (
                "Step 7: Verify the History",
                "Terminal Command",
                "git log --oneline -3"
            )
        ]

        print("==================================================")
        print("  Exp 9: Git Clone, Modify, and Push Reference    ")
        print("==================================================\n")

        for description, target, content in steps:
            print(description)
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Changes pushed! Check your GitHub repo to see it live.")
        print("==================================================")

    def exp10(self):
        steps = [
            (
                "Create the Application Code",
                "app.py",
                "def add(a, b):\n"
                "    return a + b\n\n"
                "def greet(name):\n"
                "    return f'Hello {name}'"
            ),
            (
                "Create the Test Code",
                "test_app.py",
                "from app import add, greet\n\n"
                "def test_add():\n"
                "    assert add(2, 3) == 5\n\n"
                "def test_greet():\n"
                "    assert greet('World') == 'Hello World'"
            ),
            (
                "Create the GitHub Actions Directories",
                "Terminal Command",
                "mkdir .github\\workflows"
            ),
            (
                "Create the Tiny Test Pipeline",
                ".github/workflows/python-test.yml",
                "on: push\n"
                "jobs:\n"
                "  b:\n"
                "    runs-on: ubuntu-latest\n"
                "    steps:\n"
                "      - uses: actions/checkout@v4\n"
                "      - run: |\n"
                "          pip install pytest\n"
                "          pytest test_app.py -v"
            ),
            (
                "Run Local Test (Optional but Recommended)",
                "Terminal Command",
                "pip install pytest\n"
                "pytest test_app.py -v"
            ),
            (
                "Push to GitHub to Trigger",
                "Terminal Commands",
                "git add .\n"
                "git commit -m \"Exp 10: Automated Testing\"\n"
                "git push"
            )
        ]

        print("==================================================")
        print("  Exp 10: Python Automated Testing Guide          ")
        print("==================================================\n")

        for i, (description, target, content) in enumerate(steps, start=1):
            print(f"Step {i}: {description}")
            print(f"--- [ {target} ] ---")
            print(content)
            print("-" * 30 + "\n")

        print("==================================================")
        print("Files ready! Push to see the Green Checkmark.")
        print("==================================================")


if __name__ == "__main__":
    runner = DevOpsExperiments()
    # Example: run exp2 output
    runner.exp3()
