/**
 * Contact Form & Toast Notifications
 * Powered by EmailJS with graceful fallback
 */

// Toast notification helper
function showToast(title, message, type = 'success') {
  const container = document.getElementById('toast-container');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast-message active toast-${type}`;
  
  let iconClass = 'ph-bold ph-check-circle';
  let iconColor = '#16a34a';
  if (type === 'danger') {
    iconClass = 'ph-bold ph-x-circle';
    iconColor = '#dc2626';
  } else if (type === 'warning') {
    iconClass = 'ph-bold ph-warning-circle';
    iconColor = '#d97706';
  } else if (type === 'info') {
    iconClass = 'ph-bold ph-info';
    iconColor = '#0284c7';
  }

  toast.innerHTML = `
    <div class="toast-message__content">
      <span class="toast-message__icon" style="color: ${iconColor};">
        <i class="${iconClass}"></i>
      </span>
      <div class="toast-message__text-wrap flex-grow-1">
        <h6 class="toast-message__title font-heading">${title}</h6>
        <p class="toast-message__text mb-0">${message}</p>
      </div>
      <button type="button" class="toast-message__close" aria-label="Close">
        <i class="ph ph-x"></i>
      </button>
    </div>
    <div class="progress__bar"></div>
  `;

  container.appendChild(toast);

  // Close button handler
  const closeBtn = toast.querySelector('.toast-message__close');
  if (closeBtn) {
    closeBtn.addEventListener('click', function () {
      toast.classList.remove('active');
      setTimeout(() => toast.remove(), 400);
    });
  }

  // Auto-dismiss after 4.5 seconds
  setTimeout(function () {
    if (toast.parentNode) {
      toast.classList.remove('active');
      setTimeout(() => toast.remove(), 400);
    }
  }, 4500);
}

document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contact-form');
  if (!form) return;

  /**
   * EMAILJS CONFIGURATION:
   * To connect your personal EmailJS account:
   * 1. Sign up at https://www.emailjs.com (free)
   * 2. Create an Email Service (e.g. Gmail) -> get SERVICE_ID
   * 3. Create an Email Template -> get TEMPLATE_ID
   * 4. Go to Account > API Keys -> get PUBLIC_KEY
   * Replace the placeholders below:
   */
  const EMAILJS_PUBLIC_KEY = window.EMAILJS_PUBLIC_KEY || "YOUR_EMAILJS_PUBLIC_KEY";
  const EMAILJS_SERVICE_ID = window.EMAILJS_SERVICE_ID || "YOUR_SERVICE_ID";
  const EMAILJS_TEMPLATE_ID = window.EMAILJS_TEMPLATE_ID || "YOUR_TEMPLATE_ID";

  const isConfigured = EMAILJS_PUBLIC_KEY !== "YOUR_EMAILJS_PUBLIC_KEY" && window.emailjs;

  if (isConfigured) {
    emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();

    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn ? submitBtn.innerHTML : 'Send Message';

    const name = form.elements['name'] ? form.elements['name'].value.trim() : '';
    const email = form.elements['email'] ? form.elements['email'].value.trim() : '';
    const message = form.elements['message'] ? form.elements['message'].value.trim() : '';

    if (!name || !email || !message) {
      showToast('Validation Error', 'Please complete all fields before sending.', 'warning');
      return;
    }

    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.innerHTML = 'Sending... <i class="ph ph-spinner tw-animate-spin"></i>';
    }

    if (isConfigured) {
      emailjs.sendForm(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, form)
        .then(function () {
          showToast('Message Sent!', 'Thank you! Abdelbaki will get back to you shortly.', 'success');
          form.reset();
        })
        .catch(function (err) {
          console.error('EmailJS Error:', err);
          showToast('Send Failed', 'Could not send directly. Redirecting to mail client...', 'warning');
          window.location.href = `mailto:abdelbaki.m.28@gmail.com?subject=Portfolio%20Inquiry%20from%20${encodeURIComponent(name)}&body=${encodeURIComponent(message + '\n\nFrom: ' + name + ' (' + email + ')')}`;
        })
        .finally(function () {
          if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
          }
        });
    } else {
      // Graceful instant fallback: prepare email client and notify user
      showToast('Ready to Send', 'Launching email client to send message to Abdelbaki.', 'info');
      setTimeout(function () {
        window.location.href = `mailto:abdelbaki.m.28@gmail.com?subject=Portfolio%20Inquiry%20from%20${encodeURIComponent(name)}&body=${encodeURIComponent(message + '\n\nFrom: ' + name + ' (' + email + ')')}`;
        form.reset();
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
      }, 700);
    }
  });
});
