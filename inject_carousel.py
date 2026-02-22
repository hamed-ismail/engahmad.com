import os

root_dir = r"c:\Users\User\Desktop\Templates\web sites"
files_to_edit = [
    os.path.join(root_dir, "index.html"),
    os.path.join(root_dir, "en", "index.html")
]

# The HTML for the carousel section
carousel_html_en = """

        <!-- Image Carousel Section -->
        <section class="carousel-section section-padding" style="background-color: var(--clr-primary); overflow: hidden;">
            <div class="container fade-in-up" style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: var(--clr-white);">Featured Projects</h2>
                <div style="width: 50px; height: 3px; background: var(--clr-accent); margin: 0.5rem auto 0;"></div>
            </div>
            
            <div class="carousel-container">
                <div class="carousel-track">
                    <!-- Images duplicated for infinite scrolling effect -->
                    <img src="https://images.unsplash.com/photo-1541881451961-0b5c172a2754?auto=format&fit=crop&w=400&q=80" alt="Project 1">
                    <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=400&q=80" alt="Project 2">
                    <img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=400&q=80" alt="Project 3">
                    <img src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=400&q=80" alt="Project 4">
                    <img src="https://images.unsplash.com/photo-1590486803833-1c5dc8ddd4c8?auto=format&fit=crop&w=400&q=80" alt="Project 5">
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=400&q=80" alt="Project 6">
                    <!-- Duplicates -->
                    <img src="https://images.unsplash.com/photo-1541881451961-0b5c172a2754?auto=format&fit=crop&w=400&q=80" alt="Project 1">
                    <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=400&q=80" alt="Project 2">
                    <img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=400&q=80" alt="Project 3">
                    <img src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=400&q=80" alt="Project 4">
                    <img src="https://images.unsplash.com/photo-1590486803833-1c5dc8ddd4c8?auto=format&fit=crop&w=400&q=80" alt="Project 5">
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=400&q=80" alt="Project 6">
                </div>
            </div>
        </section>
"""

carousel_html_ar = """

        <!-- Image Carousel Section -->
        <section class="carousel-section section-padding" style="background-color: var(--clr-primary); overflow: hidden;">
            <div class="container fade-in-up" style="text-align: center; margin-bottom: 2rem;">
                <h2 style="color: var(--clr-white);">مشاريع مميزة</h2>
                <div style="width: 50px; height: 3px; background: var(--clr-accent); margin: 0.5rem auto 0;"></div>
            </div>
            
            <div class="carousel-container">
                <div class="carousel-track">
                    <!-- Images duplicated for infinite scrolling effect -->
                    <img src="https://images.unsplash.com/photo-1541881451961-0b5c172a2754?auto=format&fit=crop&w=400&q=80" alt="مشروع 1">
                    <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=400&q=80" alt="مشروع 2">
                    <img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=400&q=80" alt="مشروع 3">
                    <img src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=400&q=80" alt="مشروع 4">
                    <img src="https://images.unsplash.com/photo-1590486803833-1c5dc8ddd4c8?auto=format&fit=crop&w=400&q=80" alt="مشروع 5">
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=400&q=80" alt="مشروع 6">
                    <!-- Duplicates -->
                    <img src="https://images.unsplash.com/photo-1541881451961-0b5c172a2754?auto=format&fit=crop&w=400&q=80" alt="مشروع 1">
                    <img src="https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=400&q=80" alt="مشروع 2">
                    <img src="https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=400&q=80" alt="مشروع 3">
                    <img src="https://images.unsplash.com/photo-1582268611958-ebfd161ef9cf?auto=format&fit=crop&w=400&q=80" alt="مشروع 4">
                    <img src="https://images.unsplash.com/photo-1590486803833-1c5dc8ddd4c8?auto=format&fit=crop&w=400&q=80" alt="مشروع 5">
                    <img src="https://images.unsplash.com/photo-1504307651254-35680f356dfd?auto=format&fit=crop&w=400&q=80" alt="مشروع 6">
                </div>
            </div>
        </section>
"""

# Insert right after the hero section
for path in files_to_edit:
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We will insert it just before the <!-- Services Section -->
    target = '<!-- Services Section -->'
    if target in content:
        if 'en/index.html' in path.replace('\\', '/'):
            content = content.replace(target, carousel_html_en + target)
        else:
            content = content.replace(target, carousel_html_ar + target)
            
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
            print(f"Injected into {path}")
    else:
        print(f"Target not found in {path}")

