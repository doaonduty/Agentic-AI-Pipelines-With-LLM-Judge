# Agentic-AI-Pipelines-With-LLM-Judge
An Automated Generative AI Framework with LLM Judge 

This is just an exploration of the possibilities of utilizing LLM as a Judge concept (LLM Judge,  is a concept by using the LLM to assess the quality, correctness, or appropriateness of text to evaluate written content according to specific criteria). I followed through the Hugging Face - Open-Source AI Cookbook (https://huggingface.co/learn/cookbook/en/llm_judge). The pipelines are not 100% autonomous but it should give a clear and concise idea of how the agentic approach works in generative AI.

In terms of highlights:
- Automated agentic pipeline with automated model customization per log source type, prompt customization on the fly.
- Judgement of output for each pipeline with ranking to reduce hallucination ensuring we get what we want.
- Working 100% local LLMs via ollama (I used the gguf model file in my huggingface repo -> [doaonduty/llama-3.1-8b-instruct-gguf](https://huggingface.co/doaonduty/llama-3.1-8b-instruct-gguf/tree/main) that I converted from vanilla llama-3.1-8b-instruct).
- ollama's gguf support is relatively recent at the time of writing so if you have not already updated it for a while, consider doing so.

Below is the diagram of the approach:
![PipelineDiagram](https://github.com/user-attachments/assets/5d6264b3-2aeb-428b-801f-2ce78f36fdff)

