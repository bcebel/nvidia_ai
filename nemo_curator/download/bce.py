import requests
from nemo_curator.download.doc_builder import DocumentDownloader
 
class TinyStoriesDownloader(DocumentDownloader):
    def __init__(self, download_dir: str):
        super().__init__()
 
        if not os.path.isdir(download_dir):
            os.makedirs(download_dir)
 
        self._download_dir = download_dir
        print("Download directory: ", self._download_dir)
 
    def download(self, url: str) -> str:
        filename = os.path.basename(url)
        output_file = os.path.join(self._download_dir, filename)
 
        if os.path.exists(output_file):
            print(f"File '{output_file}' already exists, skipping download.")
            return output_file
 
        print(f"Downloading TinyStories dataset from '{url}'...")
        response = requests.get(url)
 
        with open(output_file, "wb") as file:
            file.write(response.content)
 
        return output_file