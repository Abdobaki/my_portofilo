import React from 'react';
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';
import AnimatedSection from './AnimatedSection';

const experiences = [
  {
    date: '2019 — 2023',
    title: 'Sales Assistant',
    company: 'Retail Experience',
    description:
      'Developed strong interpersonal and communication skills through direct customer interaction. Managed inventory, handled transactions, and consistently exceeded sales targets. This role sharpened my problem-solving abilities and taught me to think on my feet — skills that directly translate to software development.',
    skills: ['Communication', 'Problem Solving', 'Team Work', 'Customer Service', 'Time Management'],
  },
];

function TimelineItem({ exp, index }) {
  const [ref, inView] = useInView({ triggerOnce: true, threshold: 0.2 });

  return (
    <motion.div
      ref={ref}
      className="timeline-item"
      initial={{ opacity: 0, x: -30 }}
      animate={inView ? { opacity: 1, x: 0 } : {}}
      transition={{ duration: 0.6, delay: index * 0.2 }}
    >
      <div className="timeline-dot" />
      <span className="timeline-date">{exp.date}</span>
      <div className="timeline-content">
        <h3 className="timeline-title">{exp.title}</h3>
        <p className="timeline-company">{exp.company}</p>
        <p className="timeline-description">{exp.description}</p>
        <div className="timeline-skills">
          {exp.skills.map((s) => (
            <span key={s}>{s}</span>
          ))}
        </div>
      </div>
    </motion.div>
  );
}

export default function Experience() {
  return (
    <AnimatedSection id="experience">
      <div className="section-header">
        <p className="section-label">// Experience</p>
        <h2 className="section-title">
          My <span className="gradient">Journey</span>
        </h2>
        <p className="section-subtitle">
          The experiences that shaped my professional growth
        </p>
      </div>
      <div className="timeline">
        {experiences.map((exp, i) => (
          <TimelineItem key={exp.title} exp={exp} index={i} />
        ))}
      </div>
    </AnimatedSection>
  );
}
