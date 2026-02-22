import os

root_dir = r"c:\Users\User\Desktop\Templates\web sites"
en_dir = os.path.join(root_dir, "en")

# Process root files (Arabic files)
ar_files = ["index.html", "مشاريعنا.html", "تواصل-معنا.html"]
for f in ar_files:
    path = os.path.join(root_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Internal navigation in Arabic
    content = content.replace('href="projects.html"', 'href="مشاريعنا.html"')
    content = content.replace('href="contact.html"', 'href="تواصل-معنا.html"')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

# Process en files (English files)
en_files = ["index.html", "projects.html", "contact.html"]
for f in en_files:
    path = os.path.join(en_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Language Switchers pointing back to Root Arabic files
    content = content.replace('href="../projects.html"', 'href="../مشاريعنا.html"')
    content = content.replace('href="../contact.html"', 'href="../تواصل-معنا.html"')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replacement complete")
