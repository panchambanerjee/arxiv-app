## A script to download abstracts from arxiv for the most recent papers
## based on keywords

import os
import arxiv
from tqdm import tqdm

def get_results(n, kw1, kw2):

  slow_client = arxiv.Client(
  page_size = 1000,
  delay_seconds = 10,
  num_retries = 5
    )

  results_gen = slow_client.results(arxiv.Search(
      query = f"{kw1} AND {kw2}",
      max_results = n,
      sort_by = arxiv.SortCriterion.SubmittedDate
                            ))
    
  return results_gen


def write_abstract(results_lst, file_index):
    cwd = os.getcwd()
    make_dir_path = os.path.join(cwd, 'abstract_data')
    
    try:
        os.mkdir(make_dir_path)
    except FileExistsError:
        pass
        
    total_path = os.path.join(make_dir_path, f"{results_lst[file_index].title}.txt")
    f = open(f"{total_path}", "w")
    
    try:
        f.write(results_lst[file_index].summary)
    except FileExistsError:
        pass
        
    f.close()


def get_and_write_abstracts(n, kw1, kw2):

  print("Getting arxiv data...")  
  gen_results = get_results(n, kw1, kw2)
    
  print("Converting data to list...")
  search_results_lst = list(gen_results)
  # print(len(search_results_lst))

  print("Writing abstract to txt files...")
  for idx in tqdm(range(len(search_results_lst))):
      # print(idx)
      print(f"Writing abstract for {search_results_lst[idx].title}")
      print()
      
      try: # Necessary because sometimes arxiv papers have special characters like '/' in their titles
          write_abstract(results_lst=search_results_lst, file_index=idx)
      except FileNotFoundError:
          pass
          
      print()

  print("All abstracts written!")


  if __name__ == "__main__":
      
      get_and_write_abstracts(1000, "cosmology", "artificial intelligence")