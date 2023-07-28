import os
import glob
import re
from pathlib import Path

# Find all files with a .jsonl extension in the current directory
dir_ls = ["Yara/coleta01"]

for dir in dir_ls:

    # A pasta que atravessamos
    path_s = f"../data/{dir}/*.jsonl"

    # Criar a pasta nova
    dir_output_s = Path(path_s).parent.name + '-prettified'
    dir_output_path_s = str(Path(path_s).parent.parent) + '/' + dir_output_s
    Path(dir_output_path_s).mkdir(parents=True, exist_ok=True)

    # Copiar os arquivos até a pasta nova
    files_ls = glob.glob(path_s)
    for file_path in files_ls:
        cmd = f"cp '{os.path.abspath(file_path)}' '{os.path.abspath(dir_output_path_s)}/'"
        os.system(cmd)

    # Faz split de cada arquivo, ja que cada linha representa um objeto json distinto
    files_ls = glob.glob(f"{os.path.abspath(dir_output_path_s)}/*.jsonl")
    for file_path in files_ls:
        with open(file_path,'r') as f:
            text = f.read()
        text = re.sub(r'\{[\n\r ]*"data"[\n\r ]*\:','___SEP___{"data":',text)
        ls = text.split('___SEP___')
        ls = [
            i for i in ls
            if '"data"' in i and '{' in i
        ]
        for n in range(1,len(ls)+1):
            suffix = '_n_'+ str(n).zfill(5) + '.json'
            separated_file_path = file_path.replace('.jsonl',suffix)
            with open(separated_file_path,'w') as f:
                f.write(ls[n-1])

    # Eliminar os arquivos originais (da pasta nova)
    cmd = "find '" + os.path.abspath(dir_output_path_s) + "' -type f -name '*.jsonl' -delete"
    os.system(cmd)



