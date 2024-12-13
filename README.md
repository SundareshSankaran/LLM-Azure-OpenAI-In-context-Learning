# LLM - Azure OpenAI Zero-Shot Prompting
This custom step helps you interact with a Large Language Model (LLM) interacting with an [Azure OpenAI](https://microsoftlearning.github.io/mslearn-openai/Instructions/Exercises/01-get-started-azure-openai.html) service to process simple instructions on specified input data. It uses a technique called zero-shot prompting which is useful for cases where the instruction provided to the LLM does not require additional detail or context.  

There exist both simple and involved (e.g. Retrieval Augmented Generation (RAG)) approaches for interacting with an LLM. Zero-shot prompting is useful for cases where the input data provides all the necessary context and information required for the LLM to process an instruction, and also, the instruction provided does not require a query to other data sources.  

Run inside a SAS session, this custom step takes either a SAS dataset or a CAS table as input and returns a SAS dataset (or CAS table) as output, with the response added as a new variable.
