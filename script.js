document.addEventListener('DOMContentLoaded', () => {

    /* --- Mobile Menu Toggle --- */
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.getElementById('main-nav');

    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            const isExpanded = menuToggle.getAttribute('aria-expanded') === 'true' || false;
            menuToggle.setAttribute('aria-expanded', !isExpanded);
            mainNav.classList.toggle('active');
        });

        // Close menu when a link is clicked
        const navLinks = mainNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                mainNav.classList.remove('active');
                menuToggle.setAttribute('aria-expanded', 'false');
            });
        });
    }

    /* --- Intersection Observer for Scroll Animations --- */
    const animatedElements = document.querySelectorAll('.fade-in-up');

    const animationObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Apply optional delay if defined in HTML data-delay
                const delay = entry.target.dataset.delay;
                if (delay) {
                    entry.target.style.transitionDelay = `${delay}ms`;
                }
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% visible
        rootMargin: "0px 0px -50px 0px" // Slight offset
    });

    animatedElements.forEach(el => animationObserver.observe(el));

    /* --- Number Counter Animation for Stats Section --- */
    const statsSection = document.querySelector('.stats-section');
    const counters = document.querySelectorAll('.stat-number');
    let counted = false;

    const runCounters = () => {
        counters.forEach(counter => {
            counter.innerText = '0';
            const target = +counter.getAttribute('data-target');

            // Speed of the counter
            const updateCounter = () => {
                const c = +counter.innerText;
                const increment = target / 100; // Divide to slow down the increment

                if (c < target) {
                    counter.innerText = `${Math.ceil(c + increment)}`;
                    setTimeout(updateCounter, 20);
                } else {
                    counter.innerText = target;
                }
            };
            updateCounter();
        });
        counted = true;
    };

    // Only run counter when the stats section scrolls into view
    if (statsSection && counters.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting && !counted) {
                runCounters();
            }
        }, { threshold: 0.5 });

        statsObserver.observe(statsSection);
    }

    /* --- Hero Slider --- */
    const slides = document.querySelectorAll('.hero-slider .slide');
    const dots = document.querySelectorAll('.slider-dots .dot');
    const prevBtn = document.querySelector('.slider-btn.prev-btn');
    const nextBtn = document.querySelector('.slider-btn.next-btn');

    if (slides.length > 0) {
        let currentSlide = 0;
        let slideInterval;

        const goToSlide = (index) => {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');

            currentSlide = (index + slides.length) % slides.length;

            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
        };

        const nextSlide = () => goToSlide(currentSlide + 1);
        const prevSlide = () => goToSlide(currentSlide - 1);

        const startSlider = () => {
            slideInterval = setInterval(nextSlide, 5000); // 5 seconds
        };

        const resetSlider = () => {
            clearInterval(slideInterval);
            startSlider();
        };

        // Event Listeners
        if (nextBtn) nextBtn.addEventListener('click', () => { nextSlide(); resetSlider(); });
        if (prevBtn) prevBtn.addEventListener('click', () => { prevSlide(); resetSlider(); });

        dots.forEach((dot, index) => {
            dot.addEventListener('click', () => {
                goToSlide(index);
                resetSlider();
            });
        });

        startSlider();
    }
});
