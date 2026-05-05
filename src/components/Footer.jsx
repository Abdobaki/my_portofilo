import React from 'react';
import { FiGithub, FiLinkedin, FiMail, FiHeart } from 'react-icons/fi';

const socials = [
  { icon: <FiGithub />, href: 'https://github.com/', label: 'GitHub' },
  { icon: <FiLinkedin />, href: 'https://linkedin.com/in/', label: 'LinkedIn' },
  { icon: <FiMail />, href: 'mailto:abdelbaki.nasri@email.com', label: 'Email' },
];

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-logo">Abdelbaki Nasri</div>
        <div className="footer-socials">
          {socials.map((s) => (
            <a
              key={s.label}
              href={s.href}
              className="footer-social"
              target="_blank"
              rel="noopener noreferrer"
              aria-label={s.label}
            >
              {s.icon}
            </a>
          ))}
        </div>
        <p className="footer-text">
          © {new Date().getFullYear()} Abdelbaki Nasri. Built with{' '}
          <span className="heart"><FiHeart style={{ verticalAlign: 'middle' }} /></span>{' '}
          and React
        </p>
      </div>
    </footer>
  );
}
