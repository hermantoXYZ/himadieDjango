
        // Mobile menu toggle
        function toggleMobileMenu() {
            const mobileMenu = document.getElementById('mobile-menu');
            const menuIcon = document.getElementById('menu-icon');
            
            mobileMenu.classList.toggle('hidden');
            
            if (mobileMenu.classList.contains('hidden')) {
                menuIcon.classList.remove('fa-times');
                menuIcon.classList.add('fa-bars');
            } else {
                menuIcon.classList.remove('fa-bars');
                menuIcon.classList.add('fa-times');
            }
        }

        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                    
                    // Close mobile menu if open
                    const mobileMenu = document.getElementById('mobile-menu');
                    const menuIcon = document.getElementById('menu-icon');
                    if (!mobileMenu.classList.contains('hidden')) {
                        mobileMenu.classList.add('hidden');
                        menuIcon.classList.remove('fa-times');
                        menuIcon.classList.add('fa-bars');
                    }
                }
            });
        });

        // Back to top functionality
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Show/hide back to top button
        window.addEventListener('scroll', function() {
            const backToTop = document.getElementById('backToTop');
            if (window.pageYOffset > 300) {
                backToTop.classList.remove('opacity-0', 'invisible');
                backToTop.classList.add('opacity-100', 'visible');
            } else {
                backToTop.classList.remove('opacity-100', 'visible');
                backToTop.classList.add('opacity-0', 'invisible');
            }
        });

        // Add navbar background on scroll
        window.addEventListener('scroll', function() {
            const navbar = document.querySelector('nav');
            if (window.pageYOffset > 100) {
                navbar.classList.add('backdrop-blur-md', 'bg-white/95');
            } else {
                navbar.classList.remove('backdrop-blur-md', 'bg-white/95');
            }
        });

        // Add fade-in animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        // Observe all articles
        document.querySelectorAll('article').forEach(article => {
            article.style.opacity = '0';
            article.style.transform = 'translateY(20px)';
            article.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(article);
        });
    

    
    
        // Hero Slider functionality
        const sliderItems = document.querySelectorAll('.slider-item');
        const sliderDots = document.querySelectorAll('.slider-dot');
        let currentSlide = 0;
        let slideInterval;

        function showSlide(index) {
            sliderItems.forEach((item, i) => {
                if (i === index) {
                    item.classList.add('opacity-100');
                    item.classList.remove('opacity-0');
                } else {
                    item.classList.add('opacity-0');
                    item.classList.remove('opacity-100');
                }
            });

            sliderDots.forEach((dot, i) => {
                if (i === index) {
                    dot.classList.add('opacity-100');
                } else {
                    dot.classList.remove('opacity-100');
                    dot.classList.add('opacity-50');
                }
            });
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % sliderItems.length;
            showSlide(currentSlide);
        }

        function startSlider() {
            slideInterval = setInterval(nextSlide, 5000); // Change slide every 5 seconds
        }

        function stopSlider() {
            clearInterval(slideInterval);
        }

        // Initialize slider
        showSlide(currentSlide);
        startSlider();

        // Pause slider on hover
        document.getElementById('hero-slider').addEventListener('mouseenter', stopSlider);
        document.getElementById('hero-slider').addEventListener('mouseleave', startSlider);

        // Dot navigation
        sliderDots.forEach(dot => {
            dot.addEventListener('click', function() {
                stopSlider();
                currentSlide = parseInt(this.dataset.slide);
                showSlide(currentSlide);
                startSlider();
            });
        });
    
    
        document.addEventListener('DOMContentLoaded', function() {
            const slider = document.getElementById('team-slider');
            const btnLeft = document.getElementById('team-scroll-left');
            const btnRight = document.getElementById('team-scroll-right');
            if (slider && btnLeft && btnRight) {
                btnLeft.addEventListener('click', () => {
                    slider.scrollBy({ left: -300, behavior: 'smooth' });
                });
                btnRight.addEventListener('click', () => {
                    slider.scrollBy({ left: 300, behavior: 'smooth' });
                });
            }
        });
    