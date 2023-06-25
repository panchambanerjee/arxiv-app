#!/bin/sh

n_files=10
keyword1="chatgpt"
keyword2="risk"

echo "Running research helper pipeline"
echo "################################"
echo "Running python download script"
echo "This will download the most recent pdfs of the papers with specified keywords"
python download_papers.py -n $n_files -kw1 $keyword1 -kw2 $keyword2
echo "Done downloading papers to paper_data/ directory"
echo "################################"
echo "Loading downloaded documents and creating a pinecone vector database"
python load_and_embed.py
echo "Done loading and embedding papers"
echo "################################"
echo "Running the chatbot"
python -m streamlit run run_chatbot.py