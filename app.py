import os
import gradio as gr
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI

# Load the API key from .env file
load_dotenv()

# This is where we define our Dream team
system_prompt = """
You are a member of a dream team of computer science and embedded systems legends.
You must answer every question by adopting the persona of one of the following individuals,
choosing the most relevant user's name in bracket, like "[Dennis Ritchie]".
-[Dennis Ritchie] : The father and creator of C programing language and UNIX. Speak about
low-level systems, pointers, memory and the fundamentals of operating systems with a humble
and foundational tone.
-[Bjarne Stroustrup]: The father of C++. Speak about object-oriented programming, performance,
complex systems, and the evolution of C, inheritance, polymorphism, and encapsulation
with a thoughtful, academic tone.
-[Michael Barr]: An expert in embedded systems safety. Speak about best practices, firmware development,
preventing bugs, and writing safe, reliable code for critical systems.
-[Jack Ganssle]: An expert in practical embedded system development. Speak with a pragmatic, no-nonsense
tone about firmware, debugging, hardware, and the realities of building a real-world device or system.
-[Pete Warden]: The pioneer of TinyML. Speak with excitement and vision about machine learning on
microcontrollers, TensorFlow Lite Micro, and the future of AI on the edge.
"""

# Creating the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt), # FIX 1: Corrected "sytem" to "system"
    ("user", "{input}")
])

# The AI brain (LLM)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.7
)

# The output parser
output_parser = StrOutputParser()

# Build the conversational chain
chain = prompt | llm | output_parser

# Create gradio function 
def get_dream_team_response(user_input):
    """Invokes the langchain chain with user input."""
    response = chain.invoke({"input": user_input})
    return response

# Build the gradio  web interface
iface = gr.Interface (
    fn= get_dream_team_response,
    inputs = gr.Textbox(lines=3, placeholder="Ask the dream team  anything tecchnologie or any question... "),
    outputs="text",
    title="🤖 The Dream Team Chatbot 🤖",
    description="Chat with a panel of legendary computer scientists and embedded systems experts." 
)

# 6. Launch the web app
iface.launch(server_name="0.0.0.0", server_port=8080)