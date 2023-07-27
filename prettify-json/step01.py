import glob

# Find all files with a .jsonl extension in the current directory

dir_ls = ["Yara/coleta01"]



for dir in dir_ls:
    files_ls = glob.glob(f"../data/{dir}/*.jsonl")
    for file_path in files_ls:
        with open(file_path, "r") as file:
            content = file.read()
            print(content)
