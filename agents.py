from multi_agent_orchestrator.agents import (BedrockLLMAgent, BedrockLLMAgentOptions)
from multi_agent_orchestrator.agents import ChainAgent, ChainAgentOptions

def issue_classifier():
    agent = BedrockLLMAgent(BedrockLLMAgentOptions(
            name='Application Debugging Agent',
            description='Specializes in classifying application logs.',
            model_id='anthropic.claude-3-haiku-20240307-v1:0',
            streaming=True,
            inference_config={
                'maxTokens': 1000,
                'temperature': 0.7,
                'topP': 0.9,
            },
            custom_system_prompt={
            "template": """You are an expert in log analysis, able to categorize log data across multiple systems to allow easier issue resolution..
                Core Competencies:
                1. DevOps
                2. Software Architecture
                3. Metrics, Traces and Logging
                4. Application Monitoring
                5. Applciation Log Classifier

                When classifying logs, organise them with the following headings:
                - Issue:  
                - Root Cause:
                - Actions to be Taken:
                """
                    }
        ))

    return agent

def remediator():
    agent = BedrockLLMAgent(BedrockLLMAgentOptions(
            name='Application Remediator Agent',
            description='Specializes in providing remedition actions for debugging specific application error logs.',
            model_id='anthropic.claude-3-haiku-20240307-v1:0',
            streaming=True,
            inference_config={
                'maxTokens': 1000,
                'temperature': 0.7,
                'topP': 0.9,
            },
            custom_system_prompt={
            "template": """You are a site reliability engineer with expertise in  providing remedition actions and resolving complex application error from the application logs..
                Core Competencies:
                1. Programming Languages
                2. Software Architecture
                3. Best Practices
                4. Performance Optimization

                When providing resolution for issues:
                - Point out what the exact issue is
                - From the logs in the past 15 to 30 minutes find out the root cause
                - Explore actions to be taken to resolve the issue
                - Also include exact commands to run for each step in a linux environment if needed
                - Break down the resolution into actionable steps based on specific issue"""
                    }
        ))

    return agent

def chain_agent():
    agent = ChainAgent(ChainAgentOptions(
        name='FixerChainAgent',
        description='A simple chain of multiple agents',
        agents=[issue_classifier(), remediator()]
    ))
    
    return agent