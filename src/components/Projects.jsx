import React from 'react';
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';
import AnimatedSection from './AnimatedSection';
import { FiGithub, FiExternalLink } from 'react-icons/fi';

const projects = [
  {
    title: 'Gym Management App',
    description:
      'A full-featured desktop application for managing gym memberships, tracking sessions, handling payments, and monitoring member activity with a modern UI.',
    tech: ['React', 'Electron', 'SQLite', 'Node.js'],
    icon: '🏋️',
    github: '#',
    demo: '#',
  },
  {
    title: 'Responsive Web Applications',
    description:
      'Collection of modern, responsive web applications built with a focus on clean design, performance optimization, and seamless user experiences across all devices.',
    tech: ['HTML5', 'CSS3', 'JavaScript', 'React'],
    icon: '🌐',
    github: '#',
    demo: '#',
  },
  {
    title: 'Python Mini Projects',
    description:
      'A series of Python projects including automation scripts, data processing tools, and utility applications that demonstrate algorithmic thinking and clean code practices.',
    tech: ['Python', 'Automation', 'Algorithms'],
    icon: '🐍',
    github: '#',
  },
  {
    title: 'Hand Gesture Mouse Controller',
    description:
      'An innovative computer vision project that allows users to control their mouse cursor using hand gestures, leveraging real-time video processing and ML-based hand tracking.',
    tech: ['Python', 'OpenCV', 'MediaPipe', 'NumPy'],
    icon: '🖐️',
    github: '#',
    demo: '#',
  },
];

function ProjectCard({ project, index }) {
  const [ref, inView] = useInView({ triggerOnce: true, threshold: 0.1 });

  return (
    <motion.div
      ref={ref}
      className="project-card"
      initial={{ opacity: 0, y: 40 }}
      animate={inView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5, delay: index * 0.15 }}
    >
      <div className="project-image">
        <span className="project-image-icon">{project.icon}</span>
        <div className="project-image-overlay" />
      </div>
      <div className="project-info">
        <h3 className="project-title">{project.title}</h3>
        <p className="project-description">{project.description}</p>
        <div className="project-tech">
          {project.tech.map((t) => (
            <span key={t}>{t}</span>
          ))}
        </div>
        <div className="project-links">
          {project.github && (
            <a href={project.github} className="project-link" target="_blank" rel="noopener noreferrer">
              <FiGithub /> Code
            </a>
          )}
          {project.demo && (
            <a href={project.demo} className="project-link" target="_blank" rel="noopener noreferrer">
              <FiExternalLink /> Demo
            </a>
          )}
        </div>
      </div>
    </motion.div>
  );
}

export default function Projects() {
  return (
    <AnimatedSection id="projects">
      <div className="section-header">
        <p className="section-label">// Projects</p>
        <h2 className="section-title">
          Featured <span className="gradient">Work</span>
        </h2>
        <p className="section-subtitle">
          A selection of projects that showcase my skills and passion for building
        </p>
      </div>
      <div className="projects-grid">
        {projects.map((p, i) => (
          <ProjectCard key={p.title} project={p} index={i} />
        ))}
      </div>
    </AnimatedSection>
  );
}
