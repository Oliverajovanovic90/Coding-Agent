from pathlib import Path
from tools import AgentTools

from openai import OpenAI
from toyaikit.tools import Tools
from toyaikit.chat import IPythonChatInterface
from toyaikit.llm import OpenAIClient
from toyaikit.chat.runners import OpenAIResponsesRunner

# ---------------------------------
# 1. POINT TO DJANGO PROJECT ROOT
# ---------------------------------
project_path = Path("my_new_app").resolve()
agent_tools = AgentTools(project_path)

# ---------------------------------
# 2. REGISTER TOOLS
# ---------------------------------
tools = Tools()
tools.add_tools(agent_tools)

# ---------------------------------
# 3. LLM CLIENT
# ---------------------------------
llm_client = OpenAIClient(client=OpenAI())

# ---------------------------------
# 4. DEVELOPER PROMPT
# ---------------------------------
DEVELOPER_PROMPT = """
You are a coding agent.

You modify the Django project using the available tools.
Do not explain your reasoning.
Just perform the requested changes correctly.
"""

# ---------------------------------
# 5. RUNNER
# ---------------------------------
runner = OpenAIResponsesRunner(
    tools=tools,
    developer_prompt=DEVELOPER_PROMPT,
    chat_interface=IPythonChatInterface(),
    llm_client=llm_client,
)

# ---------------------------------
# 6. START AGENT
# ---------------------------------
runner.run()
