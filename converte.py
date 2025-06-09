# convert_to_utf8.py

input_file = "backup.json"
output_file = "backup_utf8.json"

with open(input_file, "r", encoding="latin-1") as source_file:
    content = source_file.read()

with open(output_file, "w", encoding="utf-8") as target_file:
    target_file.write(content)

print(f"Arquivo convertido com sucesso: {output_file}")
