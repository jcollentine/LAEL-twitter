import glob

# Find all files with a .txt extension in the current directory

dir_ls = ["Yara/coleta01"]

txt_files = glob.glob(f"../data/{dir}/*.jsonl")

for file_path in txt_files:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
