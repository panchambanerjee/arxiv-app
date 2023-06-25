# arxiv-app
Get your own personal research helper chatbot

## Inspiration

Back when I did my PhD, I always found looking for new directions of research to be one of the more challenging aspects. In addition, once most of the paper was done, it took so much time to find the relevant papers to cite. It would have been extremely helpful to have a tool that I can query to get me the latest papers, and then have a chatbot interface that I can ask intelligent questions to regarding the areas of research, and get an idea of future directions of research. This also applies to writing review articles about a topic. 

## What it does

It downloads the pdf versions of the most recent research papers from arxiv.org according to the user's specifications. It then converts these documents into a vector representation via Pinecone, and then uses a Large Language Model (via Langchain and OpenAI) and Streamlit to build a chatbot interface to enable the user to ask research specific questions. 

## How I built it

This is currently in the form of a pipeline (using shell scripting and python scripting) with 3 major parts.
1. Part 1 queries the arXiv.org API based on keywords provided and downloads the pdf versions of the most recent "n" papers for a particular combination of keywords. 
2. Part 2 then loads in the downloaded pdfs and chunks them and converts them into vectors for a Pinecone database via Langchain and OpenAI embeddings.
3. Part 3 builds a chatbot using Streamlit, that uses OpenAI's ChatOpenAI() LLM and Langchain to query the stored documents

A master shell script runs the entire pipeline comprising 3 Python scripts. 

Built via::
1. Bash scripting
2. Python scripting
3. The arXiv API queried via the arxiv package to download pdfs of research papers
4. Langchain for document loading and Document chunking
5. Pinecone vector database created using the split documents and the default OpenAI Embeddings model 
6. A Streamlit chatbot, built to use the ChatOpenAI() model and the Pinecone dB to create a QA chatbot.
7. Some simple CSS formatting for the Streamlit bot appearance 


## What's next for arxiv_app

1. Make the pdf downloader part more intuitive, and add more options for keywords, time of query etc.
2. Address the API call timeout issues for the arXiv API
3. Try other LLMs (HuggingFace specifically)
4. Implement Conversational Memory and Agents when querying the Chatbot
5. Give the LLM access to other tools such as Wikipedia (might help with broader context) and Google Search
6. Try and wrap the whole pipeline in a Streamlit webapp
7. Deploy the app via Heroku
