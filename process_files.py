import re
import os

# Define the folder path containing your CSS files
# Use '.' for the current folder, or './assets/css', etc.
folder_path = './' 

# Mapeamento COMPLETO baseados no _variables.scss
replacements = {
    # --- Entidades Principais ---
    r'\.icon-agent:before\{content:"[^"]+"\}': '.icon-agent:before{content:"\\\\e08a"}',
    r'\.icon-event:before\{content:"[^"]+"\}': '.icon-event:before{content:"\\\\e023"}',
    r'\.icon-space:before\{content:"[^"]+"\}': '.icon-space:before{content:"\\\\e0ef"}',
    r'\.icon-project:before\{content:"[^"]+"\}': '.icon-project:before{content:"\\\\68"}',
    r'\.icon-opportunity:before\{content:"[^"]+"\}': '.icon-opportunity:before{content:"\\\\e007"}',
    r'\.icon-subsite:before\{content:"[^"]+"\}': '.icon-subsite:before{content:"\\\\e0df"}',
    r'\.icon-seal:before\{content:"[^"]+"\}': '.icon-seal:before{content:"\\\\e078"}',
    r'\.icon-developers:before\{content:"[^"]+"\}': '.icon-developers:before{content:"\\\\e035"}',
    
    # --- UI & Navegação ---
    r'\.icon-add:before\{content:"[^"]+"\}': '.icon-add:before{content:"\\\\4c"}',
    r'\.icon-about:before\{content:"[^"]+"\}': '.icon-about:before{content:"\\\\e060"}',
    r'\.icon-help:before\{content:"[^"]+"\}': '.icon-help:before{content:"\\\\e064"}',
    r'\.icon-home:before\{content:"[^"]+"\}': '.icon-home:before{content:"\\\\e074"}',
    r'\.icon-panel:before\{content:"[^"]+"\}': '.icon-panel:before{content:"\\\\e0f2"}',
    r'\.icon-search:before\{content:"[^"]+"\}': '.icon-search:before{content:"\\\\55"}',
    r'\.icon-group:before\{content:"[^"]+"\}': '.icon-group:before{content:"\\\\e08b"}',
    r'\.icon-notifications:before\{content:"[^"]+"\}': '.icon-notifications:before{content:"\\\\e065"}',
    r'\.icon-login:before\{content:"[^"]+"\}': '.icon-login:before{content:"\\\\e06c"}',
    r'\.icon-api:before\{content:"[^"]+"\}': '.icon-api:before{content:"\\\\e102"}',
    
    # --- Ações (Verbos) ---
    r'\.icon-close:before\{content:"[^"]+"\}': '.icon-close:before{content:"\\\\4d"}',
    r'\.icon-delete:before\{content:"[^"]+"\}': '.icon-delete:before{content:"\\\\e051"}',
    r'\.icon-download:before\{content:"[^"]+"\}': '.icon-download:before{content:"\\\\e092"}',
    r'\.icon-edit:before\{content:"[^"]+"\}': '.icon-edit:before{content:"\\\\6c"}',
    r'\.icon-go-back:before\{content:"[^"]+"\}': '.icon-go-back:before{content:"\\\\23"}',
    r'\.icon-return:before\{content:"[^"]+"\}': '.icon-return:before{content:"\\\\4a"}',
    r'\.icon-success:before\{content:"[^"]+"\}': '.icon-success:before{content:"\\\\e052"}',
    
    # --- Status e Cadeados ---
    r'\.icon-private-info:before\{content:"[^"]+"\}': '.icon-private-info:before{content:"\\\\e06c"}',
    r'\.icon-publication-status-locked:before\{content:"[^"]+"\}': '.icon-publication-status-locked:before{content:"\\\\e06c"}',
    r'\.icon-publication-status-open:before\{content:"[^"]+"\}': '.icon-publication-status-open:before{content:"\\\\e000"}',
    
    # --- Setas e Filtros ---
    r'\.icon-arrow-left:before\{content:"[^"]+"\}': '.icon-arrow-left:before{content:"\\\\34"}',
    r'\.icon-arrow-right:before\{content:"[^"]+"\}': '.icon-arrow-right:before{content:"\\\\35"}',
    r'\.icon-arrow-up:before\{content:"[^"]+"\}': '.icon-arrow-up:before{content:"\\\\32"}',
    r'\.icon-select-arrow:before\{content:"[^"]+"\}': '.icon-select-arrow:before{content:"\\\\33"}',
    r'\.icon-show-advanced-filters:before\{content:"[^"]+"\}': '.icon-show-advanced-filters:before{content:"\\\\54"}',
    r'\.icon-show-advanced-search:before\{content:"[^"]+"\}': '.icon-show-advanced-search:before{content:"\\\\67"}',
    r'\.icon-show-map:before\{content:"[^"]+"\}': '.icon-show-map:before{content:"\\\\e081"}',
    r'\.icon-show-search-on-list:before\{content:"[^"]+"\}': '.icon-show-search-on-list:before{content:"\\\\e056"}',
    r'\.icon-show-search-on-map:before\{content:"[^"]+"\}': '.icon-show-search-on-map:before{content:"\\\\e083"}',
    
    # --- Classes utilitárias ---
    r'\.add:before\{content:"[^"]+"\}': '.add:before{content:"\\\\e050"}',
    r'\.check:before\{content:"[^"]+"\}': '.check:before{content:"\\\\4e"}',
    r'\.insert:before\{content:"[^"]+"\}': '.insert:before{content:"\\\\37"}',
    r'\.send:before\{content:"[^"]+"\}': '.send:before{content:"\\\\e091"}',
    r'\.attachment-title:before\{content:"[^"]+"\}': '.attachment-title:before{content:"\\\\e016"}',
    
    # --- Form Elements ---
    r'\.icon-radio-button:before\{content:"[^"]+"\}': '.icon-radio-button:before{content:"\\\\5b"}',
    r'\.icon-radio-button\.selected:before\{content:"[^"]+"\}': '.icon-radio-button.selected:before{content:"\\\\5c"}',
    
    # --- Diversos ---
    r'\.icon-em-cartaz:before\{content:"[^"]+"\}': '.icon-em-cartaz:before{content:"\\\\e033"}',
    r'\.icon-info:before\{content:"[^"]+"\}': '.icon-info:before{content:"\\\\e007"}',
    
    # --- Social Media ---
    r'\.icon-share:before\{content:"[^"]+"\}': '.icon-share:before{content:"\\\\e0a0"}',
    r'\.icon-facebook:before\{content:"[^"]+"\}': '.icon-facebook:before{content:"\\\\e093"}',
    r'\.icon-twitter:before\{content:"[^"]+"\}': '.icon-twitter:before{content:"\\\\e094"}',
    r'\.icon-instagram:before\{content:"[^"]+"\}': '.icon-instagram:before{content:"\\\\e09a"}',
    r'\.icon-googleplus:before\{content:"[^"]+"\}': '.icon-googleplus:before{content:"\\\\e096"}',
    r'\.icon-linkedin:before\{content:"[^"]+"\}': '.icon-linkedin:before{content:"\\\\e09d"}',
    r'\.icon-spotify:before\{content:"[^"]+"\}': '.icon-spotify:before{content:"\\\\e0a8"}',
    r'\.icon-youtube:before\{content:"[^"]+"\}': '.icon-youtube:before{content:"\\\\e0ba"}',
    r'\.icon-pinterest:before\{content:"[^"]+"\}': '.icon-pinterest:before{content:"\\\\e095"}'
}

# Verify if folder exists
if not os.path.exists(folder_path):
    print(f"Erro: A pasta '{folder_path}' não foi encontrada.")
    exit()

print(f"Iniciando correção na pasta: {folder_path}")

# Iterate through all files in the directory
files_processed = 0
for filename in os.listdir(folder_path):
    if filename.endswith(".css"):
        input_file = os.path.join(folder_path, filename)
        
        print(f"Lendo: {filename}...")
        
        try:
            # Read with latin-1 (as per original script to handle binary/mixed content)
            with open(input_file, 'rb') as f:
                content = f.read().decode('latin-1')

            # Apply all replacements
            changes_count = 0
            for pattern, replacement in replacements.items():
                # We can't easily count regex replacements without running subn,
                # but for speed we just run sub.
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    changes_count += 1
                content = new_content

            # Write back to the same file (overwrite) in UTF-8
            with open(input_file, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f" -> Salvo (UTF-8).")
            files_processed += 1

        except Exception as e:
            print(f" -> Erro ao processar {filename}: {e}")

print(f"\nConcluído! Total de arquivos CSS processados: {files_processed}")
