import arxiv
import shutil
import os
from tqdm import tqdm
import time
import argparse


parser = argparse.ArgumentParser(description="Download the most recent paper pdfs\
                                  from arxiv based on entered keywords",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--number_of_files", type=int, \
                    help="number of files to download", default=5)
parser.add_argument("-kw1", "--keyword1", help="first keyword", default="chatgpt")
parser.add_argument("-kw2", "--keyword2", help="second keyword", default="risk")

args = parser.parse_args()
n_files = args.number_of_files
keyword1 = args.keyword1
keyword2 = args.keyword2

print(args)

config = vars(args)
print(config)


custom_arxiv_client = arxiv.Client(
  page_size = 1000,
  delay_seconds = 10,
  num_retries = 5
    )


def get_results(n, kw1, kw2, client=custom_arxiv_client):

  results_gen = custom_arxiv_client.results(arxiv.Search(
      query = f"{kw1} AND {kw2}",
      max_results = n,
      sort_by = arxiv.SortCriterion.SubmittedDate
                            ))
    
  return results_gen


def get_pdfs(n, kw1, kw2):

  cwd = os.getcwd()
  download_dir_path = os.path.join(cwd, 'paper_data')
    
  try:
        os.mkdir(download_dir_path)
  except FileExistsError:
        # shutil.rmtree(download_dir_path)
        pass
        
  results_gen = get_results(n, kw1, kw2)      

  for result in tqdm(results_gen): 
      
      print(result.entry_id[21:])
      
      paper = next(arxiv.Search(id_list=[result.entry_id[21:]]).results())
      
      print(f"Downloading:: {result.title}")

      try:
        paper.download_pdf(dirpath=download_dir_path)
      except FileNotFoundError:
        pass

      time.sleep(2)

  print("All Paper pdfs downloaded!")

  return download_dir_path


if __name__ == "__main__":

    # args = parser.parse_args()

    dir_path = get_pdfs(n=n_files, kw1=keyword1, kw2=keyword2)