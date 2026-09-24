import re

with open('Portfolio/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Meta and Title
content = re.sub(
    r'<title>.*?</title>',
    '<title>Abdelbaki Nasri - Software Developer | Portfolio</title>',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<meta\s+name="description"\s+content=".*?"\s*/>',
    '<meta name="description" content="Portfolio of Abdelbaki Nasri - Software Developer specializing in React, Next.js, TypeScript, Go, Electron, Docker, and SQLite. Building high-performance business applications, POS workflows, and AI systems." />',
    content,
    flags=re.DOTALL
)

content = re.sub(
    r'<meta\s+name="keywords"\s+content=".*?"\s*/>',
    '<meta name="keywords" content="Abdelbaki Nasri, Software Developer, Full-Stack Developer, POS Systems, React, Next.js, TypeScript, Go, Electron, SQLite, Docker, MediaPipe, Algeria" />',
    content,
    flags=re.DOTALL
)

# 2. Offcanvas Contact Information & Socials
old_contact_info = r'<div class="twoffcanvas__contact-info">.*?</div>\s*<div\s+class="footer-social"'
new_contact_info = '''<div class="twoffcanvas__contact-info">
              <div class="twoffcanvas__contact-title">
                <h5 class="text-white">Get in touch</h5>
              </div>
              <ul>
                <li>
                  <span class="text-main-two-600 tw-text-xl"
                    ><i class="ph ph-map-pin-line"></i
                  ></span>
                  <span class="text-white">M\'sila, Algeria</span>
                </li>
                <li>
                  <span class="text-main-two-600 tw-text-xl"
                    ><i class="ph ph-envelope"></i
                  ></span>
                  <a class="text-white" href="mailto:abdelbaki.m.28@gmail.com"
                    ><span>abdelbaki.m.28@gmail.com</span></a
                  >
                </li>
                <li>
                  <span class="text-main-two-600 tw-text-xl"
                    ><i class="ph ph-phone-call"></i
                  ></span>
                  <a class="text-white" href="tel:+213676865376"
                    >+213 676 86 53 76</a
                  >
                </li>
                <li>
                  <span class="text-main-two-600 tw-text-xl"
                    ><i class="ph ph-file-pdf"></i
                  ></span>
                  <a class="text-white" href="abdelbaki_cv.pdf" download="Abdelbaki_Nasri_CV.pdf"
                    >Download Resume (PDF)</a
                  >
                </li>
              </ul>
            </div>
            <div
              class="footer-social"'''
content = re.sub(old_contact_info, new_contact_info, content, flags=re.DOTALL)

old_offcanvas_social = r'<div\s+class="footer-social".*?</ul>\s*</div>\s*</div>\s*</div>\s*</div>\s*<!-- ==================== Offcanvus Mobile Menu End Here ==================== -->'
new_offcanvas_social = '''<div
              class="footer-social"
              data-aos="fade-up"
              data-aos-duration="1000"
              data-aos-delay="200"
            >
              <ul class="tw-gap-2">
                <li>
                  <a href="https://github.com/Abdobaki" target="_blank">
                    <span class="active-media d-flex align-items-center tw-gap-1"
                      >GitHub <i class="ph ph-arrow-bend-up-right"></i
                    ></span>
                    <span class="hover-media"
                      ><i class="ph ph-github-logo"></i
                    ></span>
                  </a>
                </li>
                <li>
                  <a href="https://abdobaki.github.io/my portofilo" target="_blank">
                    <span class="active-media d-flex align-items-center tw-gap-1"
                      >Portfolio <i class="ph ph-arrow-bend-up-right"></i
                    ></span>
                    <span class="hover-media"
                      ><i class="ph ph-globe"></i
                    ></span>
                  </a>
                </li>
                <li>
                  <a href="mailto:abdelbaki.m.28@gmail.com">
                    <span class="active-media d-flex align-items-center tw-gap-1"
                      >Email <i class="ph ph-arrow-bend-up-right"></i
                    ></span>
                    <span class="hover-media"
                      ><i class="ph ph-envelope"></i
                    ></span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- ==================== Offcanvus Mobile Menu End Here ==================== -->'''
content = re.sub(old_offcanvas_social, new_offcanvas_social, content, flags=re.DOTALL)

# Offcanvas logo and mobile nav menu
content = content.replace(
    '''<div class="twoffcanvas__logo">
              <a class="logo-1" href="index.html"
                ><img src="assets/images/logo/logo.png" alt="logo"
              /></a>
            </div>''',
    '''<div class="twoffcanvas__logo">
              <a class="logo-1 d-inline-flex align-items-center text-decoration-none" href="index.html">
                <span class="tw-text-3xl font-heading fw-bold text-white">Abdelbaki<span class="text-main-two-600">.</span></span>
              </a>
            </div>'''
)

content = content.replace(
    '''<div class="tw-main-menu-mobile menu-hover-active counter-row">
            <nav></nav>
          </div>''',
    '''<div class="tw-main-menu-mobile menu-hover-active counter-row">
            <nav>
              <ul class="py-4">
                <li class="tw-mb-3"><a class="text-white tw-text-xl fw-semibold" href="#home">Home</a></li>
                <li class="tw-mb-3"><a class="text-white tw-text-xl fw-semibold" href="#about">About Me</a></li>
                <li class="tw-mb-3"><a class="text-white tw-text-xl fw-semibold" href="#services">Services &amp; Skills</a></li>
                <li class="tw-mb-3"><a class="text-white tw-text-xl fw-semibold" href="#projects">Featured Projects</a></li>
                <li class="tw-mb-3"><a class="text-white tw-text-xl fw-semibold" href="#contact">Contact</a></li>
                <li class="tw-mb-3"><a class="text-main-two-600 tw-text-xl fw-bold" href="abdelbaki_cv.pdf" download="Abdelbaki_Nasri_CV.pdf">Download CV (PDF)</a></li>
              </ul>
            </nav>
          </div>'''
)

# Header Logo
content = content.replace(
    '''<div class="header-three-logo tw-rounded-md">
            <a href="index.html" class="link">
              <img
                src="assets/images/logo/logo-secendary.png"
                alt="Logo"
                class="max-w-200-px"
              />
            </a>
          </div>''',
    '''<div class="header-three-logo tw-rounded-md">
            <a href="index.html" class="link d-inline-flex align-items-center text-decoration-none">
              <span class="tw-text-3xl font-heading fw-bold text-heading">Abdelbaki<span class="text-main-two-600">.</span></span>
            </a>
          </div>'''
)

# Header Socials
old_header_social = r'<div class="header-three-social d-none d-lg-block">.*?</div>\s*<!-- Menu End  -->'
new_header_social = '''<div class="header-three-social d-none d-lg-block">
            <ul class="d-flex tw-gap-205">
              <li>
                <a
                  class="tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md hover-bg-main-two-600 hover-text-white"
                  href="https://github.com/Abdobaki"
                  target="_blank"
                  title="GitHub Profile"
                  ><i class="ph-bold ph-github-logo"></i
                ></a>
              </li>
              <li>
                <a
                  class="tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md hover-bg-main-two-600 hover-text-white"
                  href="https://abdobaki.github.io/my portofilo"
                  target="_blank"
                  title="Live Portfolio"
                  ><i class="ph-bold ph-globe"></i
                ></a>
              </li>
              <li>
                <a
                  class="tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md hover-bg-main-two-600 hover-text-white"
                  href="mailto:abdelbaki.m.28@gmail.com"
                  title="Email"
                  ><i class="ph-bold ph-envelope"></i
                ></a>
              </li>
              <li>
                <a
                  class="tw-w-13 tw-h-13 lh-1 d-inline-flex justify-content-center align-items-center text-heading tw-text-xl tw-rounded-md hover-bg-main-two-600 hover-text-white"
                  href="tel:+213676865376"
                  title="Phone"
                  ><i class="ph-bold ph-phone-call"></i
                ></a>
              </li>
            </ul>
          </div>
          <!-- Menu End  -->'''
content = re.sub(old_header_social, new_header_social, content, flags=re.DOTALL)

# Header Download CV Button
content = content.replace(
    '''<div class="header-three-button d-none d-md-block">
              <a
                class="tw-hover-btn bg-black text-white fw-bold tw-py-4 tw-px-10 d-inline-block hover-text-white text-uppercase tw-rounded-md"
                href="contact.html"
              >
                download cv
                <span class="tw-hover-btn-circle-dot bg-main-two-600"></span>
              </a>
            </div>''',
    '''<div class="header-three-button d-none d-md-block">
              <a
                class="tw-hover-btn bg-black text-white fw-bold tw-py-4 tw-px-10 d-inline-block hover-text-white text-uppercase tw-rounded-md"
                href="abdelbaki_cv.pdf"
                download="Abdelbaki_Nasri_CV.pdf"
              >
                download cv
                <span class="tw-hover-btn-circle-dot bg-main-two-600"></span>
              </a>
            </div>'''
)

# 3. Hero Section (banner-three-area)
old_hero = r'<section class="banner-three-area">.*?</section>\s*<section class="about-three-area'
new_hero = '''<section class="banner-three-area" id="home">
          <div class="container tw-container-1800-px">
            <div class="row">
              <div class="col-xl-12">
                <div class="banner-three-wrapper position-relative z-1">
                  <div
                    class="banner-three-man position-absolute start-50 translate-middle-x"
                  >
                    <img
                      src="assets/images/thumbs/abdelbaki-hero.png"
                      alt="Abdelbaki Nasri"
                      style="max-height: 720px; object-fit: contain;"
                    />
                  </div>
                  <h1 class="banner-three-title text-black tw-mb-30">
                    developer
                  </h1>
                  <div
                    class="banner-three-wrap d-flex justify-content-between align-items-end position-relative z-1"
                  >
                    <div
                      class="banner-three-left tw-rounded-lg"
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="200"
                    >
                      <h2 class="banner-three-left-title tw-text-3xl tw-mb-6">
                        Hello! I'm Abdelbaki <br />
                        Nasri. A software developer &amp; systems builder based in Algeria.
                      </h2>
                      <div class="banner-three-list">
                        <ul>
                          <li
                            class="tw-text-lg fw-medium d-inline-flex align-items-center tw-gap-2 tw-mb-4"
                          >
                            <span
                              ><img
                                src="assets/images/icons/banner-three-pluse.svg"
                                alt="pluse"
                            /></span>
                            Full-Stack Web Development
                          </li>
                          <li
                            class="tw-text-lg fw-medium d-inline-flex align-items-center tw-gap-2 tw-mb-4"
                          >
                            <span
                              ><img
                                src="assets/images/icons/banner-three-pluse.svg"
                                alt="pluse"
                            /></span>
                            Desktop POS &amp; Business Systems
                          </li>
                          <li
                            class="tw-text-lg fw-medium d-inline-flex align-items-center tw-gap-2 tw-mb-4"
                          >
                            <span
                              ><img
                                src="assets/images/icons/banner-three-pluse.svg"
                                alt="pluse"
                            /></span>
                            Systems &amp; Backend (Go, Docker)
                          </li>
                          <li
                            class="tw-text-lg fw-medium d-inline-flex align-items-center tw-gap-2 tw-mb-4"
                          >
                            <span
                              ><img
                                src="assets/images/icons/banner-three-pluse.svg"
                                alt="pluse"
                            /></span>
                            AI &amp; Computer Vision (OpenCV)
                          </li>
                          <li
                            class="tw-text-lg fw-medium d-inline-flex align-items-center tw-gap-2 tw-mb-4"
                          >
                            <span
                              ><img
                                src="assets/images/icons/banner-three-pluse.svg"
                                alt="pluse"
                            /></span>
                            Database Architecture (SQLite, Supabase)
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div
                      class="banner-three-center text-center"
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="200"
                    >
                      <h3 class="banner-three-center-title tw-text-120">
                        High-performance software, intuitive POS, and intelligent digital solutions.
                      </h3>
                      <div class="banner-three-button">
                        <a
                          class="tw-hover-btn bg-black text-white fw-bold tw-py-4 tw-px-10 d-inline-block hover-text-white text-uppercase tw-rounded-lg"
                          href="#projects"
                        >
                          view projects
                          <span
                            class="tw-hover-btn-circle-dot bg-main-two-600"
                          ></span>
                        </a>
                      </div>
                    </div>
                    <div
                      class="banner-three-right tw-rounded-lg"
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="300"
                    >
                      <div
                        class="banner-three-counter-item tw-rounded-md tw-mb-4 position-relative"
                      >
                        <h4
                          class="banner-three-counter-title tw-text-101 fw-semibold font-heading text-heading tw-mb-2 lh-1"
                        >
                          <span
                            class="purecounter font-heading"
                            data-purecounter-duration="2"
                            data-purecounter-end="10"
                          ></span
                          >+
                        </h4>
                        <p
                          class="banner-three-counter-paragraph tw-text-lg fw-medium text-heading"
                        >
                          Projects Engineered
                        </p>
                      </div>
                      <div
                        class="banner-three-counter-item tw-rounded-md tw-mb-4 ms-auto bg-black"
                      >
                        <h4
                          class="banner-three-counter-title tw-text-101 fw-semibold font-heading text-white tw-mb-2 lh-1"
                        >
                          <span
                            class="purecounter font-heading"
                            data-purecounter-duration="3"
                            data-purecounter-end="99"
                          ></span
                          >%
                        </h4>
                        <p
                          class="banner-three-counter-paragraph tw-text-lg fw-medium text-white"
                        >
                          AI Model Test Accuracy (ASL)
                        </p>
                      </div>
                      <div
                        class="banner-three-counter-item tw-rounded-md tw-mb-4"
                      >
                        <h4
                          class="banner-three-counter-title tw-text-101 fw-semibold font-heading text-heading tw-mb-2 lh-1"
                        >
                          <span
                            class="purecounter font-heading"
                            data-purecounter-duration="2"
                            data-purecounter-end="100"
                          ></span
                          >%
                        </h4>
                        <p
                          class="banner-three-counter-paragraph tw-text-lg fw-medium text-heading"
                        >
                          Code Reliability &amp; Quality
                        </p>
                      </div>
                    </div>
                    <div
                      class="banner-three-line-shape position-absolute start-50 translate-middle-x z-n1"
                    >
                      <img
                        src="assets/images/shapes/banner-three-shape.png"
                        alt="shape"
                      />
                      <div class="banner-three-carcel-shape">
                        <div><span></span></div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="about-three-area'''
content = re.sub(old_hero, new_hero, content, flags=re.DOTALL)

# 4. About Section
old_about = r'<section class="about-three-area py-120 position-relative z-1">.*?</section>\s*<!-- ======================== Marquee section start =========================== -->'
new_about = '''<section class="about-three-area py-120 position-relative z-1" id="about">
          <div class="container tw-container-1800-px">
            <div class="about-three-top position-relative z-1">
              <div class="row justify-content-center tw-mb-21">
                <div class="col-xl-9">
                  <div class="text-center">
                    <h2
                      class="about-three-title text-heading tw-text-15 tw-itm-title tw-itm-anim"
                    >
                      I build practical, robust, and scalable software solutions designed to solve real business challenges, streamline operations, and deliver tangible impact.
                    </h2>
                  </div>
                </div>
              </div>
              <div class="row align-items-center">
                <div class="col-xl-6">
                  <div
                    class="about-three-thumb w-100 tw-clip-anim tw-rounded-lg shadow-sm"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <img
                      class="tw-anim-img w-100 tw-rounded-lg"
                      data-animate="true"
                      src="assets/images/thumbs/abdelbaki-about.jpg"
                      alt="Abdelbaki Nasri coding at laptop"
                    />
                  </div>
                </div>
                <div class="col-xl-6">
                  <div
                    class="about-three-right"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="300"
                  >
                    <div>
                      <p class="tw-text-xl tw-mb-10">
                        I am a Computer Science student at the University of M\'sila (2023–2026) with deep hands-on expertise building cross-platform applications across web, desktop, and systems.
                      </p>
                      <p class="tw-text-xl tw-mb-10">
                        My technical stack is centered around modern engineering tools: <strong>React, Next.js, TypeScript, Go, Electron, Docker, and SQLite</strong>. I also bring strong domain knowledge in retail operations and business software workflows, gained through hands-on store management.
                      </p>
                      <p class="tw-text-xl tw-mb-10">
                        Whether engineering real-time offline-first desktop POS systems with barcode scanning &amp; receipt generation, automated backend workflows with n8n and Go, or computer vision recognition pipelines, I bridge architectural rigor with smooth user experiences.
                      </p>
                    </div>
                    <div class="about-three-counter d-inline-block">
                      <div class="tw-hover-btn-wrapper d-inline-block">
                        <a
                          class="tw-btn-circle tw-hover-btn-item tw-hover-btn tw-w-160-px tw-h-160-px lh-1 d-inline-flex justify-content-center align-items-center rounded-circle position-relative overflow-hidden border border-1 border-neutral-200"
                          href="#contact"
                        >
                          <span
                            class="d-flex flex-column justify-content-center"
                          >
                            <span
                              class="tw-btn-circle-icon text-heading tw-text-8 tw-transition-3 font-heading fw-medium"
                              >2026</span
                            >
                            <span
                              class="text-heading fw-bold text-center tw-transition-3 tw-text-2xl fw-medium"
                              >CS Degree</span
                            >
                          </span>
                          <i class="tw-btn-circle-dot bg-main-two-600"></i>
                        </a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div
                class="about-three-wrap-shape d-flex justify-content-between"
              >
                <div
                  class="banner-three-counter-item tw-rounded-md position-relative"
                  data-aos="fade-up"
                  data-aos-duration="1000"
                  data-aos-delay="200"
                >
                  <h2
                    class="banner-three-counter-title tw-text-101 fw-semibold font-heading text-heading tw-mb-2 lh-1"
                  >
                    <span
                      class="purecounter font-heading"
                      data-purecounter-duration="2"
                      data-purecounter-end="6"
                    ></span
                    >+
                  </h2>
                  <p
                    class="banner-three-counter-paragraph tw-text-lg fw-medium text-heading"
                  >
                    Production-Ready Core Projects
                  </p>
                </div>
                <div
                  class="banner-three-counter-item tw-rounded-md position-relative"
                  data-aos="fade-up"
                  data-aos-duration="1000"
                  data-aos-delay="300"
                >
                  <h2
                    class="banner-three-counter-title tw-text-101 fw-semibold font-heading text-heading tw-mb-2 lh-1"
                  >
                    <span
                      class="purecounter font-heading"
                      data-purecounter-duration="2"
                      data-purecounter-end="99"
                    ></span
                    >%
                  </h2>
                  <p
                    class="banner-three-counter-paragraph tw-text-lg fw-medium text-heading"
                  >
                    AI Landmark Recognition Accuracy
                  </p>
                </div>
              </div>
            </div>
          </div>
          <div>
            <img
              class="about-three-shape position-absolute start-0 w-100"
              src="assets/images/shapes/about-three-shape.png"
              alt="shape"
            />
          </div>
        </section>
        <!-- ======================== Marquee section start =========================== -->'''
content = re.sub(old_about, new_about, content, flags=re.DOTALL)

# 5. Marquee Section: Tech Stack
old_marquee = r'<!-- ======================== Marquee section start =========================== -->.*?<!-- ======================== Marquee section end =========================== -->'
new_marquee = '''<!-- ======================== Marquee section start =========================== -->
        <div class="marquee tw-pt-17 bg-black">
          <div
            class="marquee_left d-flex align-items-center justify-content-between tw-gap-16 overflow-hidden"
          >
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-white">
                REACT &amp; NEXT.JS <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-stroke">
                TYPESCRIPT <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-white">
                GO / GOLANG <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-stroke">
                ELECTRON &amp; SQLITE <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-white">
                DOCKER &amp; SUPABASE <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-stroke">
                PYTHON &amp; OPENCV <span class="text-white">-</span>
              </h2>
            </div>
            <div>
              <h2 class="marquee-two-title marquee-three-title text-uppercase text-white">
                N8N AUTOMATION <span class="text-white">-</span>
              </h2>
            </div>
          </div>
        </div>
        <!-- ======================== Marquee section end =========================== -->'''
content = re.sub(old_marquee, new_marquee, content, flags=re.DOTALL)

# 6. Services Section (service-three-area)
old_service = r'<section class="service-three-area bg-black pt-120 tw-pb-15">.*?</section>\s*<section class="portfolio-three-area'
new_service = '''<section class="service-three-area bg-black pt-120 tw-pb-15" id="services">
          <div class="container tw-container-1800-px">
            <div class="row">
              <div class="col-12">
                <div class="service-three-wrapper">
                  <!-- Service 1 -->
                  <div
                    class="service-three-single"
                    data-aos="fade-right"
                    data-aos-duration="2000"
                    data-aos-delay="200"
                  >
                    <div
                      class="service-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="service-three-content d-flex tw-gap-14">
                        <div>
                          <span
                            class="service-three-number text-white tw-text-xl d-inline-flex align-items-center tw-gap-3 lh-1 tw-mt-5 tw-transition-3"
                            >01
                            <img
                              class="tw-transition-3"
                              src="assets/images/icons/service-three-arrow.svg"
                              alt="arrow"
                          /></span>
                        </div>
                        <div>
                          <div>
                            <h2
                              class="service-three-title tw-text-15 text-white tw-mb-4"
                            >
                              <a href="#projects"
                                >Full-Stack Web Engineering</a
                              >
                            </h2>
                          </div>
                          <div class="portfolio-list portfolio-two-list">
                            <ul class="d-flex tw-gap-205 flex-wrap">
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >React &amp; Next.js</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >TypeScript</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Tailwind CSS &amp; REST APIs</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <div class="service-three-thumb">
                        <a href="#projects"
                          ><img
                            src="assets/images/thumbs/proj-skillbridge.jpg"
                            alt="SkillBridge Web Platform"
                            style="width: 280px; height: 160px; object-fit: cover; border-radius: 8px;"
                        /></a>
                      </div>
                    </div>
                  </div>
                  <!-- Service 2 -->
                  <div
                    class="service-three-single ms-auto"
                    data-aos="fade-left"
                    data-aos-duration="2000"
                    data-aos-delay="300"
                  >
                    <div
                      class="service-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="service-three-content d-flex tw-gap-14">
                        <div>
                          <span
                            class="service-three-number text-white tw-text-xl d-inline-flex align-items-center tw-gap-3 lh-1 tw-mt-5 tw-transition-3"
                            >02
                            <img
                              class="tw-transition-3"
                              src="assets/images/icons/service-three-arrow.svg"
                              alt="arrow"
                          /></span>
                        </div>
                        <div>
                          <div>
                            <h2
                              class="service-three-title tw-text-15 text-white tw-mb-4"
                            >
                              <a href="#projects"
                                >Desktop &amp; Retail POS Systems</a
                              >
                            </h2>
                          </div>
                          <div class="portfolio-list portfolio-two-list">
                            <ul class="d-flex tw-gap-205 flex-wrap">
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Electron &amp; Vite</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >SQLite Local DB</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Barcode &amp; Receipt Hardware</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <div class="service-three-thumb">
                        <a href="#projects"
                          ><img
                            src="assets/images/thumbs/proj-pos-clothing.jpg"
                            alt="Clothing POS System"
                            style="width: 280px; height: 160px; object-fit: cover; border-radius: 8px;"
                        /></a>
                      </div>
                    </div>
                  </div>
                  <!-- Service 3 -->
                  <div
                    class="service-three-single"
                    data-aos="fade-right"
                    data-aos-duration="2000"
                    data-aos-delay="400"
                  >
                    <div
                      class="service-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="service-three-content d-flex tw-gap-14">
                        <div>
                          <span
                            class="service-three-number text-white tw-text-xl d-inline-flex align-items-center tw-gap-3 lh-1 tw-mt-5 tw-transition-3"
                            >03
                            <img
                              class="tw-transition-3"
                              src="assets/images/icons/service-three-arrow.svg"
                              alt="arrow"
                          /></span>
                        </div>
                        <div>
                          <div>
                            <h2
                              class="service-three-title tw-text-15 text-white tw-mb-4"
                            >
                              <a href="#projects">Backend &amp; Systems Engineering</a>
                            </h2>
                          </div>
                          <div class="portfolio-list portfolio-two-list">
                            <ul class="d-flex tw-gap-205 flex-wrap">
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Go (Golang)</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Docker Containers</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >n8n Workflow Automation</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <div class="service-three-thumb">
                        <a href="#projects"
                          ><img
                            src="assets/images/thumbs/proj-haios.jpg"
                            alt="HAIOS Operating System"
                            style="width: 280px; height: 160px; object-fit: cover; border-radius: 8px;"
                        /></a>
                      </div>
                    </div>
                  </div>
                  <!-- Service 4 -->
                  <div
                    class="service-three-single ms-auto"
                    data-aos="fade-left"
                    data-aos-duration="2000"
                    data-aos-delay="500"
                  >
                    <div
                      class="service-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="service-three-content d-flex tw-gap-14">
                        <div>
                          <span
                            class="service-three-number text-white tw-text-xl d-inline-flex align-items-center tw-gap-3 lh-1 tw-mt-5 tw-transition-3"
                            >04
                            <img
                              class="tw-transition-3"
                              src="assets/images/icons/service-three-arrow.svg"
                              alt="arrow"
                          /></span>
                        </div>
                        <div>
                          <div>
                            <h2
                              class="service-three-title tw-text-15 text-white tw-mb-4"
                            >
                              <a href="#projects"
                                >AI &amp; Computer Vision</a
                              >
                            </h2>
                          </div>
                          <div class="portfolio-list portfolio-two-list">
                            <ul class="d-flex tw-gap-205 flex-wrap">
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Python &amp; OpenCV</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >MediaPipe 3D Landmarks</a
                                >
                              </li>
                              <li>
                                <a
                                  class="text-uppercase text-white tw-text-sm fw-medium position-relative z-1 hover-bg-main-two-600 hover-border-main-two-600 hover-text-heading tw-transition-3"
                                  href="#projects"
                                  >Random Forest (98.9% Acc)</a
                                >
                              </li>
                            </ul>
                          </div>
                        </div>
                      </div>
                      <div class="service-three-thumb">
                        <a href="#projects"
                          ><img
                            src="assets/images/thumbs/proj-sign-language-ai.jpg"
                            alt="Sign Language AI"
                            style="width: 280px; height: 160px; object-fit: cover; border-radius: 8px;"
                        /></a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="portfolio-three-area'''
content = re.sub(old_service, new_service, content, flags=re.DOTALL)

# 7. Portfolio Section (portfolio-three-area) - All 6 Projects
old_portfolio = r'<section class="portfolio-three-area py-120 position-relative z-1">.*?</section>\s*<div class="feature-three-area'
new_portfolio = '''<section class="portfolio-three-area py-120 position-relative z-1" id="projects">
          <div class="portfolio-three-shape position-absolute top-0 z-n1">
            <h3 class="portfolio-three-shape-title">works</h3>
          </div>
          <div class="container tw-container-1800-px">
            <div class="row">
              <div class="col-xl-12">
                <div
                  class="portfolio-three-wrapper d-flex justify-content-between flex-wrap align-items-start position-relative z-1"
                >
                  <!-- Project 1: Clothing POS System -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >Clothing POS System</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >ELECTRON</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >REACT &amp; TS</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >SQLITE</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div>
                        <div class="portfolio-three-button">
                          <a
                            class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                            href="https://github.com/Abdobaki"
                            target="_blank"
                            title="View on GitHub"
                            ><i class="ph ph-arrow-up-right"></i
                          ></a>
                        </div>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-pos-clothing.jpg"
                          alt="Clothing POS System"
                      /></a>
                    </div>
                  </div>

                  <!-- Project 2: SkillBridge -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >SkillBridge Platform</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >REACT</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >TYPESCRIPT</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >SUPABASE</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="portfolio-three-button">
                        <a
                          class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                          href="https://github.com/Abdobaki"
                          target="_blank"
                          title="View on GitHub"
                          ><i class="ph ph-arrow-up-right"></i
                        ></a>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-skillbridge.jpg"
                          alt="SkillBridge Academic Platform"
                      /></a>
                    </div>
                  </div>

                  <!-- Project 3: HAIOS -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >HAIOS Operating System</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >GO (GOLANG)</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >NODE.JS &amp; REACT</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >N8N AUTOMATION</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="portfolio-three-button">
                        <a
                          class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                          href="https://github.com/Abdobaki"
                          target="_blank"
                          title="View on GitHub"
                          ><i class="ph ph-arrow-up-right"></i
                        ></a>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-haios.jpg"
                          alt="HAIOS Operating System"
                      /></a>
                    </div>
                  </div>

                  <!-- Project 4: Gym Management & POS -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >Gym Management &amp; POS</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >ELECTRON</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >REACT &amp; VITE</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >SQLITE</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="portfolio-three-button">
                        <a
                          class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                          href="https://github.com/Abdobaki"
                          target="_blank"
                          title="View on GitHub"
                          ><i class="ph ph-arrow-up-right"></i
                        ></a>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-gym-pos.jpg"
                          alt="Gym Management POS"
                      /></a>
                    </div>
                  </div>

                  <!-- Project 5: Digital Restaurant E-Menu -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >Digital Restaurant E-Menu</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >REACT</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >TYPESCRIPT</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >TAILWIND CSS</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="portfolio-three-button">
                        <a
                          class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                          href="https://github.com/Abdobaki"
                          target="_blank"
                          title="View on GitHub"
                          ><i class="ph ph-arrow-up-right"></i
                        ></a>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-restaurant-menu.jpg"
                          alt="Restaurant Digital Menu"
                      /></a>
                    </div>
                  </div>

                  <!-- Project 6: Sign Language AI -->
                  <div
                    class="portfolio-three-item tw-rounded-lg tw-mb-705 portfolio-wrapper"
                  >
                    <div
                      class="portfolio-three-wrap d-flex justify-content-between flex-wrap row-gap-2"
                    >
                      <div class="tw-mb-6">
                        <div>
                          <h2 class="tw-text-605 fw-medium tw-mb-4">
                            <a
                              class="hover-text-main-two-600"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              >Sign Language AI (24 Signs)</a
                            >
                          </h2>
                        </div>
                        <div class="portfolio-three-list portfolio-list">
                          <ul class="d-flex tw-gap-205 flex-wrap">
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >PYTHON &amp; OPENCV</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >MEDIAPIPE 3D</span
                              >
                            </li>
                            <li>
                              <span
                                class="text-uppercase text-heading fw-medium position-relative z-1 badge bg-light text-dark px-3 py-2"
                                >RANDOM FOREST</span
                              >
                            </li>
                          </ul>
                        </div>
                      </div>
                      <div class="portfolio-three-button">
                        <a
                          class="portfolio-three-btn tw-w-8 tw-h-8 lh-1 d-inline-flex justify-content-center align-items-center text-heading rounded-circle hover-bg-main-two-600 hover-text-white"
                          href="https://github.com/Abdobaki"
                          target="_blank"
                          title="View on GitHub"
                          ><i class="ph ph-arrow-up-right"></i
                        ></a>
                      </div>
                    </div>
                    <div
                      class="portfolio-thumb not-hide-cursor fw-bold mb-0 tw-rounded-lg shadow-sm"
                      data-cursor="View"
                    >
                      <a
                        class="d-block cursor-hide tw-rounded-lg"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                        ><img
                          class="w-100 tw-rounded-lg"
                          src="assets/images/thumbs/proj-sign-language-ai.jpg"
                          alt="Sign Language AI Recognition"
                      /></a>
                    </div>
                  </div>

                  <div
                    class="about-three-counter portfolio-three-counter d-inline-block position-absolute bottom-0 start-0"
                  >
                    <div class="tw-hover-btn-wrapper d-inline-block">
                      <a
                        class="tw-btn-circle tw-hover-btn-item tw-hover-btn tw-w-160-px tw-h-160-px lh-1 d-inline-flex justify-content-center align-items-center rounded-circle position-relative overflow-hidden"
                        href="https://github.com/Abdobaki"
                        target="_blank"
                      >
                        <span class="d-flex flex-column justify-content-center">
                          <span
                            class="text-heading fw-bold tw-transition-3 tw-text-2xl fw-semibold"
                            >Explore <br />
                            GitHub <i class="ph ph-arrow-up-right"></i
                          ></span>
                        </span>
                        <i class="tw-btn-circle-dot bg-main-two-600"></i>
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <div class="feature-three-area'''
content = re.sub(old_portfolio, new_portfolio, content, flags=re.DOTALL)

# 8. Feature / Experience Highlights Section
old_feature = r'<div class="feature-three-area py-120 position-relative z-1">.*?</div>\s*<section class="testimonial-three-area'
new_feature = '''<div class="feature-three-area py-120 position-relative z-1">
          <div class="container tw-container-1800-px">
            <div class="row">
              <div class="col-xl-12">
                <div class="feature-three-wrapper hover__widget">
                  <!-- Item 01 -->
                  <div
                    class="feature-three-single current hover__reveal-item"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <div
                      class="feature-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="feature-three-left d-flex align-items-center">
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-20"
                            >01</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-160-px"
                            >Education</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                            >Bachelor in Computer Science (2023 - 2026) - University of M\'sila</span
                          >
                        </div>
                      </div>
                      <div>
                        <span
                          class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                          >2023-2026</span
                        >
                      </div>
                    </div>
                    <div
                      class="hover__reveal-bg bg-img"
                      data-background-image="assets/images/thumbs/abdelbaki-about.jpg"
                    ></div>
                  </div>
                  <!-- Item 02 -->
                  <div
                    class="feature-three-single hover__reveal-item"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <div
                      class="feature-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="feature-three-left d-flex align-items-center">
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-20"
                            >02</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-160-px"
                            >Retail Domain</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                            >Retail Operations &amp; Inventory Management Experience</span
                          >
                        </div>
                      </div>
                      <div>
                        <span
                          class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                          >Operations</span
                        >
                      </div>
                    </div>
                    <div
                      class="hover__reveal-bg bg-img"
                      data-background-image="assets/images/thumbs/proj-pos-clothing.jpg"
                    ></div>
                  </div>
                  <!-- Item 03 -->
                  <div
                    class="feature-three-single hover__reveal-item"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <div
                      class="feature-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="feature-three-left d-flex align-items-center">
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-20"
                            >03</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-160-px"
                            >AI Vision</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                            >98.9% Test Accuracy on 24 ASL Signs (MediaPipe &amp; OpenCV)</span
                          >
                        </div>
                      </div>
                      <div>
                        <span
                          class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                          >ML Model</span
                        >
                      </div>
                    </div>
                    <div
                      class="hover__reveal-bg bg-img"
                      data-background-image="assets/images/thumbs/proj-sign-language-ai.jpg"
                    ></div>
                  </div>
                  <!-- Item 04 -->
                  <div
                    class="feature-three-single hover__reveal-item"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <div
                      class="feature-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="feature-three-left d-flex align-items-center">
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-20"
                            >04</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-160-px"
                            >Desktop Apps</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                            >High-Performance Offline-First POS Systems with SQLite &amp; Electron</span
                          >
                        </div>
                      </div>
                      <div>
                        <span
                          class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                          >Cross-Platform</span
                        >
                      </div>
                    </div>
                    <div
                      class="hover__reveal-bg bg-img"
                      data-background-image="assets/images/thumbs/proj-gym-pos.jpg"
                    ></div>
                  </div>
                  <!-- Item 05 -->
                  <div
                    class="feature-three-single hover__reveal-item"
                    data-aos="fade-up"
                    data-aos-duration="1000"
                    data-aos-delay="200"
                  >
                    <div
                      class="feature-three-item d-flex justify-content-between align-items-center"
                    >
                      <div class="feature-three-left d-flex align-items-center">
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-20"
                            >05</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block tw-w-160-px"
                            >Automation</span
                          >
                        </div>
                        <div>
                          <span
                            class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                            >HAIOS Agency Management &amp; n8n Webhook Pipeline Automation</span
                          >
                        </div>
                      </div>
                      <div>
                        <span
                          class="feature-three-text tw-text-605 fw-medium text-white tw-transition-3 d-inline-block"
                          >Systems</span
                        >
                      </div>
                    </div>
                    <div
                      class="hover__reveal-bg bg-img"
                      data-background-image="assets/images/thumbs/proj-haios.jpg"
                    ></div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <section class="testimonial-three-area'''
content = re.sub(old_feature, new_feature, content, flags=re.DOTALL)

# 9. Testimonial Section
old_testimonial = r'<section class="testimonial-three-area pt-120 tw-pb-22">.*?</section>\s*<section class="brand-three-area'
new_testimonial = '''<section class="testimonial-three-area pt-120 tw-pb-22">
          <div class="container tw-container-1800-px">
            <div class="row justify-content-center tw-mb-21">
              <div class="col-xl-10">
                <div class="text-center">
                  <h2
                    class="testimonial-three-title text-heading tw-text-15 tw-itm-title tw-itm-anim"
                  >
                    Client &amp; collaborator feedback highlighting architectural reliability, performance, and user-centric problem solving.
                  </h2>
                </div>
              </div>
            </div>
            <div class="row">
              <div class="col-xl-12">
                <div class="testimonial-three-slider position-relative z-1">
                  <div class="testimonial-three-active swiper-container">
                    <div class="swiper-wrapper">
                      <!-- item 1 -->
                      <div
                        class="testimonial-three-wrapper d-flex align-items-center tw-gap-9 tw-rounded-lg tw-mb-705 swiper-slide"
                        data-aos="fade-up"
                        data-aos-duration="1000"
                        data-aos-delay="200"
                      >
                        <div
                          class="testimonial-three-thumb position-relative z-1"
                        >
                          <img
                            class="w-100 h-100 tw-rounded-lg"
                            src="assets/images/thumbs/proj-pos-clothing.jpg"
                            alt="Clothing POS System Review"
                          />
                        </div>
                        <div class="testimonial-three-content w-100">
                          <div
                            class="d-flex align-items-center justify-content-between tw-mb-16"
                          >
                            <div>
                              <span
                                ><img
                                  src="assets/images/icons/testimonial-three-icon.svg"
                                  alt="icon"
                              /></span>
                            </div>
                            <div class="testimonial-three-review">
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                            </div>
                          </div>
                          <div class="tw-mb-15">
                            <p
                              class="testimonial-three-paragraph text-heading tw-text-2xl fw-semibold"
                            >
                              "Abdelbaki\'s custom POS system revolutionized our checkout and inventory management. It is extremely fast, works completely offline without a hitch, and eliminated barcode errors."
                            </p>
                          </div>
                          <div>
                            <h2 class="tw-text-2xl fw-medium">
                              Retail Operations Client
                            </h2>
                            <p class="tw-text-lg">Store Owner &amp; Inventory Lead</p>
                          </div>
                        </div>
                      </div>
                      <!-- item 2 -->
                      <div
                        class="testimonial-three-wrapper d-flex align-items-center tw-gap-9 tw-rounded-lg tw-mb-705 swiper-slide"
                        data-aos="fade-up"
                        data-aos-duration="1000"
                        data-aos-delay="300"
                      >
                        <div
                          class="testimonial-three-thumb position-relative z-1"
                        >
                          <img
                            class="w-100 h-100 tw-rounded-lg"
                            src="assets/images/thumbs/proj-skillbridge.jpg"
                            alt="SkillBridge Review"
                          />
                        </div>
                        <div class="testimonial-three-content w-100">
                          <div
                            class="d-flex align-items-center justify-content-between tw-mb-16"
                          >
                            <div>
                              <span
                                ><img
                                  src="assets/images/icons/testimonial-three-icon.svg"
                                  alt="icon"
                              /></span>
                            </div>
                            <div class="testimonial-three-review">
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                              <span class="text-heading tw-text-lg"><i class="ph-bold ph-star"></i></span>
                            </div>
                          </div>
                          <div class="tw-mb-15">
                            <p
                              class="testimonial-three-paragraph text-heading tw-text-2xl fw-semibold"
                            >
                              "Working with Abdelbaki on SkillBridge was outstanding. His mastery over React, TypeScript, and Supabase made the platform intuitive, secure, and blazingly fast."
                            </p>
                          </div>
                          <div>
                            <h2 class="tw-text-2xl fw-medium">
                              Academic Collaborator
                            </h2>
                            <p class="tw-text-lg">University Project Coordinator</p>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section class="brand-three-area'''
content = re.sub(old_testimonial, new_testimonial, content, flags=re.DOTALL)

# 10. Brand / Tech Stack Header Title
content = content.replace(
    '''<h2 class="brand-three-title tw-text-xl tw-char-animation">
                    Loved by Teams Around the World
                  </h2>''',
    '''<h2 class="brand-three-title tw-text-xl tw-char-animation">
                    Technologies &amp; Tools in My Engineering Stack
                  </h2>'''
)

# 11. Footer & Contact Form
old_footer = r'<section\s+class="footer-three-area pt-120 tw-pb-10 position-relative z-1">.*?</section>'
new_footer = '''<section
          class="footer-three-area pt-120 tw-pb-10 position-relative z-1"
          id="contact"
        >
          <div class="container tw-container-1800-px">
            <div class="row justify-content-between pb-120">
              <div class="col-xl-5 col-lg-6">
                <div
                  class="footer-three-top-left tw-me-25"
                  data-aos="fade-up"
                  data-aos-duration="1000"
                  data-aos-delay="200"
                >
                  <div class="tw-mb-9">
                    <h2 class="tw-text-15 text-white tw-char-animation">
                      Let’s build something exceptional together
                    </h2>
                  </div>
                  <div
                    class="d-inline-flex align-items-center tw-gap-6 tw-mb-10 flex-wrap"
                  >
                    <a
                      class="tw-text-2xl fw-medium text-main-600 hover-underline hover-text-white"
                      href="mailto:abdelbaki.m.28@gmail.com"
                      >abdelbaki.m.28@gmail.com</a
                    >
                    <span class="tw-text-2xl fw-medium text-main-600">//</span>
                    <a
                      class="tw-text-2xl fw-medium text-main-600 hover-underline hover-text-white"
                      href="tel:+213676865376"
                      >+213 676 86 53 76</a
                    >
                  </div>
                  <div
                    class="footer-three-top-info tw-p-705 tw-rounded-lg d-flex tw-gap-6 align-items-center"
                  >
                    <div class="footer-three-top-thumb tw-w-160-px">
                      <img
                        class="tw-rounded-lg w-100"
                        src="assets/images/thumbs/abdelbaki-about.jpg"
                        alt="Abdelbaki Nasri"
                        style="height: 140px; object-fit: cover;"
                      />
                    </div>
                    <div
                      class="footer-three-top-content d-flex justify-content-between flex-column"
                    >
                      <div>
                        <h3 class="tw-text-xl text-white tw-mb-2">
                          Abdelbaki Nasri
                        </h3>
                        <p class="text-white">Software Developer &amp; Systems Builder</p>
                        <p class="text-white-50 tw-text-sm tw-mb-2">M\'sila, Algeria</p>
                      </div>
                      <div class="footer-three-social">
                        <ul class="d-flex align-items-center tw-gap-2">
                          <li>
                            <a
                              class="tw-w-11 tw-h-101 lh-1 d-inline-flex align-items-center justify-content-center tw-rounded-lg tw-text-xl text-heading hover-bg-main-600 hover-text-heading bg-white"
                              href="https://github.com/Abdobaki"
                              target="_blank"
                              title="GitHub"
                              ><i class="ph ph-github-logo"></i
                            ></a>
                          </li>
                          <li>
                            <a
                              class="tw-w-11 tw-h-101 lh-1 d-inline-flex align-items-center justify-content-center tw-rounded-lg tw-text-xl text-heading hover-bg-main-600 hover-text-heading bg-white"
                              href="https://abdobaki.github.io/my portofilo"
                              target="_blank"
                              title="Live Portfolio"
                              ><i class="ph ph-globe"></i
                            ></a>
                          </li>
                          <li>
                            <a
                              class="tw-w-11 tw-h-101 lh-1 d-inline-flex align-items-center justify-content-center tw-rounded-lg tw-text-xl text-heading hover-bg-main-600 hover-text-heading bg-white"
                              href="mailto:abdelbaki.m.28@gmail.com"
                              title="Email"
                              ><i class="ph ph-envelope"></i
                            ></a>
                          </li>
                          <li>
                            <a
                              class="tw-w-11 tw-h-101 lh-1 d-inline-flex align-items-center justify-content-center tw-rounded-lg tw-text-xl text-heading hover-bg-main-600 hover-text-heading bg-white"
                              href="abdelbaki_cv.pdf"
                              download="Abdelbaki_Nasri_CV.pdf"
                              title="Download CV"
                              ><i class="ph ph-file-pdf"></i
                            ></a>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="col-xl-6 col-lg-6">
                <div
                  class="footer-three-form"
                  data-aos="fade-up"
                  data-aos-duration="1000"
                  data-aos-delay="300"
                >
                  <form action="mailto:abdelbaki.m.28@gmail.com" method="POST" enctype="text/plain">
                    <div class="row">
                      <div class="col-xl-12">
                        <div class="position-relative tw-mb-7">
                          <input
                            type="text"
                            name="name"
                            required
                            class="form-control bg-transparent shadow-none tw-rounded-lg text-white tw-ps-7 tw-pe-13 tw-placeholder-text-neutral-100 focus-border-main-600 tw-h-18 focus-tw-placeholder-text-hidden tw-placeholder-transition-2"
                            placeholder="Your Name"
                          />
                        </div>
                      </div>
                      <div class="col-xl-12">
                        <div class="position-relative tw-mb-7">
                          <input
                            type="email"
                            name="email"
                            required
                            class="form-control bg-transparent shadow-none tw-rounded-lg text-white tw-ps-7 tw-pe-13 tw-placeholder-text-neutral-100 focus-border-main-600 tw-h-18 focus-tw-placeholder-text-hidden tw-placeholder-transition-2"
                            placeholder="Email Address"
                          />
                        </div>
                      </div>
                      <div class="col-xl-12">
                        <div class="position-relative tw-mb-7">
                          <textarea
                            name="message"
                            required
                            class="form-control bg-transparent shadow-none tw-h-196-px tw-rounded-lg text-white tw-ps-7 tw-pe-13 tw-placeholder-text-neutral-100 focus-border-main-600 focus-tw-placeholder-text-hidden tw-placeholder-transition-2"
                            placeholder="Describe your project or inquiry"
                          ></textarea>
                        </div>
                      </div>
                      <div class="col-xl-12">
                        <div class="contact-button">
                          <button
                            type="submit"
                            class="tw-hover-btn bg-main-600 text-heading tw-text-xl fw-bold tw-py-4 tw-px-10 d-inline-flex justify-content-center w-100 hover-text-heading hover-bg-white tw-transition-3 tw-rounded-lg"
                          >
                            send message
                          </button>
                        </div>
                      </div>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <div class="footer-three-border tw-px-18 tw-mb-10">
            <div class="container-fluid gx-0">
              <div class="row">
                <div class="col-xl-12">
                  <div
                    class="footer-three-middile d-flex align-items-center justify-content-between"
                  >
                    <div
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="200"
                    >
                      <h4 class="tw-text-2xl text-white tw-mb-2">
                        Navigation
                      </h4>
                      <ul class="d-flex tw-gap-2 flex-wrap">
                        <li>
                          <a class="tw-text-lg text-white hover-text-main-two-600" href="#home"
                            >Home,</a
                          >
                        </li>
                        <li>
                          <a class="tw-text-lg text-white hover-text-main-two-600" href="#about"
                            >About Me,
                          </a>
                        </li>
                        <li>
                          <a class="tw-text-lg text-white hover-text-main-two-600" href="#services"
                            >Services &amp; Skills,
                          </a>
                        </li>
                        <li>
                          <a class="tw-text-lg text-white hover-text-main-two-600" href="#projects"
                            >Projects,
                          </a>
                        </li>
                        <li>
                          <a class="tw-text-lg text-white hover-text-main-two-600" href="#contact"
                            >Contact
                          </a>
                        </li>
                      </ul>
                    </div>
                    <div
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="300"
                    >
                      <a
                        class="footer-three-back-to-top tw-w-170 tw-h-170 lh-1 d-inline-flex justify-content-center align-items-center bg-main-two-600 text-white tw-text-3xl rounded-circle"
                        href="#home"
                        title="Back to Top"
                        ><i class="ph ph-arrow-up"></i
                      ></a>
                    </div>
                    <div
                      class="text-lg-end"
                      data-aos="fade-up"
                      data-aos-duration="1000"
                      data-aos-delay="400"
                    >
                      <h4 class="tw-text-2xl text-white tw-mb-2">
                        Abdelbaki Nasri
                      </h4>
                      <p class="tw-text-lg text-white">
                        &copy; 2026 Abdelbaki Nasri. All rights reserved.
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <div class="container tw-container-1800-px">
              <div class="row">
                <div class="col-xl-12">
                  <div class="footer-three-bottom">
                    <h5 class="footer-three-bottom-title text-white">
                      ABDELBAKI NASRI
                    </h5>
                  </div>
                </div>
              </div>
            </div>
          </div>
          <div>
            <img
              class="position-absolute top-0 start-0 z-n1"
              src="assets/images/shapes/footer-three-bg-shape.png"
              alt="shape"
            />
          </div>
        </section>'''
content = re.sub(old_footer, new_footer, content, flags=re.DOTALL)

with open('Portfolio/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Portfolio/index.html successfully updated with Abdelbaki Nasri personal information!')
