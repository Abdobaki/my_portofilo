import React from 'react';
import AnimatedSection from './AnimatedSection';
import { FiCode, FiShield, FiTarget } from 'react-icons/fi';
import profilePic from '../assets/picture.jpg';

export default function About() {
  return (
    <AnimatedSection id="about">
      <div className="section-header">
        <p className="section-label">// About Me</p>
        <h2 className="section-title">
          Get to Know <span className="gradient">Me</span>
        </h2>
      </div>
      <div className="about-grid">
        <div className="about-image">
          <div className="about-decoration" />
          <img
            src={profilePic}
            alt="Abdelbaki Nasri"
            className="about-avatar"
          />
        </div>
        <div className="about-text">
          <p>
            Hi! I'm <span className="highlight">Abdelbaki Nasri</span>, a Computer Science student
            with a burning passion for software development and cybersecurity. I believe
            technology has the power to change the world, and I want to be part of that change.
          </p>
          <p>
            My journey started with curiosity — taking apart how things work and rebuilding them
            better. Today, I channel that same energy into writing clean, efficient code and
            building applications that solve real problems.
          </p>
          <p>
            Beyond coding, I'm deeply fascinated by <span className="highlight">ethical hacking</span> and
            cybersecurity. I'm constantly learning about network security, penetration testing,
            and how to build systems that are both powerful and secure. My goal is to bridge
            development and security — building the future while keeping it safe.
          </p>
          <div className="about-stats">
            <div className="stat-item">
              <FiCode style={{ fontSize: '1.5rem', color: 'var(--accent-cyan)', marginBottom: '.5rem' }} />
              <div className="stat-number">10+</div>
              <div className="stat-label">Projects Built</div>
            </div>
            <div className="stat-item">
              <FiShield style={{ fontSize: '1.5rem', color: 'var(--accent-cyan)', marginBottom: '.5rem' }} />
              <div className="stat-number">5+</div>
              <div className="stat-label">Technologies</div>
            </div>
            <div className="stat-item">
              <FiTarget style={{ fontSize: '1.5rem', color: 'var(--accent-cyan)', marginBottom: '.5rem' }} />
              <div className="stat-number">∞</div>
              <div className="stat-label">Curiosity</div>
            </div>
          </div>
        </div>
      </div>
    </AnimatedSection>
  );
}
