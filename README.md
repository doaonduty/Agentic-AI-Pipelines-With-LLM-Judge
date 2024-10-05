# Agentic-AI-Pipelines-With-LLM-Judge
Automated Agentic AI Pipelines for Event Synthesis: A Generative AI Framework with LLM Judge 

This is just an exploration of the possibilities of utilizing LLM as a Judge concept (LLM Judge,  is a concept by using the LLM to assess the quality, correctness, or appropriateness of text to evaluate written content according to specific criteria). I followed through the Hugging Face - Open-Source AI Cookbook (https://huggingface.co/learn/cookbook/en/llm_judge)

In terms of highlights:
- Automated agentic pipeline with automated model customization per log source type, prompt customization on the fly.
- Judgement of output for each pipeline with ranking to reduce hallucination ensuring we get what we want.
- Working 100% local LLMs (llama3.1:8b) via ollama.

Below is the diagram of the approach:
![PipelineDiagram](https://github.com/user-attachments/assets/d7401298-fbf0-401c-a72b-d06d0b681bec)
