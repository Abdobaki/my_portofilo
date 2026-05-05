import React, { useState } from 'react';
import AnimatedSection from './AnimatedSection';
import { FiMail, FiLinkedin, FiGithub, FiSend } from 'react-icons/fi';

const contactItems = [
  {
    icon: <FiMail />,
    label: 'Email',
    value: 'abdelbaki.nasri@email.com',
    href: 'mailto:abdelbaki.nasri@email.com',
  },
  {
    icon: <FiLinkedin />,
    label: 'LinkedIn',
    value: 'Abdelbaki Nasri',
    href: 'https://linkedin.com/in/',
  },
  {
    icon: <FiGithub />,
    label: 'GitHub',
    value: '@abdelbaki-nasri',
    href: 'https://github.com/',
  },
];

export default function Contact() {
  const [form, setForm] = useState({ name: '', email: '', message: '' });
  const [sent, setSent] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setSent(true);
    setTimeout(() => setSent(false), 3000);
    setForm({ name: '', email: '', message: '' });
  };

  return (
    <AnimatedSection id="contact">
      <div className="section-header">
        <p className="section-label">// Contact</p>
        <h2 className="section-title">
          Let's <span className="gradient">Connect</span>
        </h2>
        <p className="section-subtitle">
          Have a project in mind or just want to chat? Feel free to reach out!
        </p>
      </div>
      <div className="contact-grid">
        <div className="contact-info">
          <p>
            I'm always open to new opportunities, collaborations, and interesting
            conversations. Whether you have a question or just want to say hi,
            I'll try my best to get back to you!
          </p>
          {contactItems.map((item) => (
            <a
              key={item.label}
              href={item.href}
              className="contact-item"
              target="_blank"
              rel="noopener noreferrer"
            >
              <div className="contact-icon">{item.icon}</div>
              <div className="contact-detail">
                <h4>{item.label}</h4>
                <span>{item.value}</span>
              </div>
            </a>
          ))}
        </div>
        <form className="contact-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <input
              type="text"
              placeholder="Your Name"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <input
              type="email"
              placeholder="Your Email"
              value={form.email}
              onChange={(e) => setForm({ ...form, email: e.target.value })}
              required
            />
          </div>
          <div className="form-group">
            <textarea
              placeholder="Your Message"
              value={form.message}
              onChange={(e) => setForm({ ...form, message: e.target.value })}
              required
            />
          </div>
          <button type="submit" className="btn btn-primary btn-submit">
            {sent ? '✓ Message Sent!' : <><FiSend /> Send Message</>}
          </button>
        </form>
      </div>
    </AnimatedSection>
  );
}
