# AgentFix

AgentFix is a sample Multi-Agent AI System built with the [AWS Multi-Agent Orchestrator](https://github.com/awslabs/multi-agent-orchestrator).
The prompt takes some json log data and provides some remediation actions to resolve the resulting issue.

## Installation

To get started with AgentFix, follow these steps to install the required packages:

1. Clone the repository:
    ```sh
    git clone https://github.com/baldcodr/agentfix.git
    cd agentfix
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```sh
    virtualenv -p python3.13 venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
4. Set up you aws cli credentials and also ensure you have access to the ``anthropic.claude-3-haiku-20240307-v1:0`` model on AWS.

## Running Locally

To run the project locally, follow these steps:

1. Ensure that you have completed the installation steps above.

2. Run the application:
    ```sh
    python main.py
    ```

3. Follow the prompts in the terminal to interact with the Multi-Agent system by inputing a sample log data as below.:
    ```
    {"source": "app_log", "error_code": 500, "message": "Database timeout"}
    ```