# Download the TinyStories dataset.
downloader = TinyStoriesDownloader("/workspace/nemo_curator/download/bce.py")
tinystories_fp = downloader.download("https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt")
write_jsonl(tinystories_fp, jsonl_dir)