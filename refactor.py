import os

root_dir = r"c:\Users\User\Desktop\Templates\web sites"
en_dir = os.path.join(root_dir, "en")

# Arabic files in root
ar_files = ["index.html", "projects.html", "contact.html"]
for f in ar_files:
    path = os.path.join(root_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Switch EN links to en/
    content = content.replace('href="index.html"', 'href="en/index.html"')
    content = content.replace('href="projects.html"', 'href="en/projects.html"')
    content = content.replace('href="contact.html"', 'href="en/contact.html"')
    
    # Switch AR links to root names
    content = content.replace('href="index-ar.html', 'href="index.html')
    content = content.replace('href="projects-ar.html', 'href="projects.html')
    content = content.replace('href="contact-ar.html', 'href="contact.html')
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

# English files in en/
en_files = ["index.html", "projects.html", "contact.html"]
for f in en_files:
    path = os.path.join(en_dir, f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Asset paths
    content = content.replace('href="styles.css"', 'href="../styles.css"')
    content = content.replace('src="script.js"', 'src="../script.js"')
    content = content.replace('src="logo.jpg"', 'src="../logo.jpg"')
    
    # Switch AR language selector links to point to parent
    content = content.replace('href="index-ar.html"', 'href="../index.html"')
    content = content.replace('href="projects-ar.html"', 'href="../projects.html"')
    content = content.replace('href="contact-ar.html"', 'href="../contact.html"')
    
    # Ensure internal navigation links stay clean (no change needed for contact.html, projects.html as they resolve to same dir)
    # Actually wait, in en/contact.html, href="index.html" is correct because it's in the same folder.
    
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Replacement complete")
