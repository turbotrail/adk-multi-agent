from google.adk import Agent
from google.adk.agents.llm_agent import LlmAgent
from google.adk.agents.sequential_agent import SequentialAgent
from google.adk.agents.parallel_agent import ParallelAgent

explainer_agent=LlmAgent(
    name="Explainer",
    description="Explainer Agent is designed to provide clear and concise explanations on a wide range of topics. It can break down complex concepts into easily understandable language, making it an invaluable resource for learning and comprehension.",
    mode="chat",
    model="ollama_chat/gemma4:e4b-mlx"
)

philosophy_agent=LlmAgent(
    name="Philosophy",
    description="Philosophy Agent is designed to provide deep insights and perspectives on philosophical questions and concepts. It can engage in thoughtful discussions and offer nuanced viewpoints on complex philosophical issues.",
    mode="chat",
    model="ollama_chat/gemma4:e4b-mlx"
)

parallel_agent=ParallelAgent(
    name="Parallel_Agent",
    sub_agents=[explainer_agent, philosophy_agent],
    description="Execute the sub-agents in parallel to provide a comprehensive understanding of the topic at hand.",
)

merger_agent=LlmAgent(
    name="Merger",
    description="Merger Agent is designed to synthesize and integrate information from multiple sources or perspectives. " \
    "primay task is to merge the outputs of the sub-agents into a cohesive and comprehensive summary, ensuring that all relevant insights are captured and presented in a clear and organized manner.",
    mode="chat",
    model="ollama_chat/gemma4:e4b-mlx"
)

root_agent=SequentialAgent(
    name="Root_Agent",
    sub_agents=[parallel_agent, merger_agent],
    description="Execute the sub-agents in sequence to provide a comprehensive understanding of the topic at hand.",
)