import React from 'react';
import { motion } from 'framer-motion';
import { useInView } from 'react-intersection-observer';
import AnimatedSection from './AnimatedSection';
import {
  SiC, SiCplusplus, SiPython, SiHtml5, SiCss, SiJavascript,
  SiReact, SiGit, SiGithub, SiSqlite, SiElectron, SiLinux,
} from 'react-icons/si';
import { FiShield, FiCode, FiGlobe, FiTool, FiBookOpen } from 'react-icons/fi';

const categories = [
  {
    title: 'Programming',
    icon: <FiCode />,
    skills: [
      { name: 'C', icon: <SiC />, level: 75 },
      { name: 'C++', icon: <SiCplusplus />, level: 70 },
      { name: 'Python', icon: <SiPython />, level: 80 },
    ],
  },
  {
    title: 'Web Development',
    icon: <FiGlobe />,
    skills: [
      { name: 'HTML5', icon: <SiHtml5 />, level: 90 },
      { name: 'CSS3', icon: <SiCss />, level: 85 },
      { name: 'JavaScript', icon: <SiJavascript />, level: 80 },
      { name: 'React', icon: <SiReact />, level: 75 },
    ],
  },
  {
    title: 'Tools & Platforms',
    icon: <FiTool />,
    skills: [
      { name: 'Git', icon: <SiGit />, level: 80 },
      { name: 'GitHub', icon: <SiGithub />, level: 85 },
      { name: 'SQLite', icon: <SiSqlite />, level: 70 },
      { name: 'Electron', icon: <SiElectron />, level: 65 },
    ],
  },
  {
    title: 'Currently Learning',
    icon: <FiBookOpen />,
    skills: [
      { name: 'Cybersecurity', icon: <FiShield />, level: 50 },
      { name: 'Linux', icon: <SiLinux />, level: 55 },
      { name: 'Networking', icon: <FiGlobe />, level: 45 },
    ],
  },
];

function SkillBar({ level, inView }) {
  return (
    <div className="skill-bar-container">
      <motion.div
        className="skill-bar"
        initial={{ width: 0 }}
        animate={inView ? { width: `${level}%` } : {}}
        transition={{ duration: 1.2, ease: 'easeOut' }}
      />
    </div>
  );
}

function SkillCategory({ category, index }) {
  const [ref, inView] = useInView({ triggerOnce: true, threshold: 0.2 });

  return (
    <motion.div
      ref={ref}
      className="skill-category"
      initial={{ opacity: 0, y: 30 }}
      animate={inView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5, delay: index * 0.15 }}
    >
      <div className="skill-category-header">
        <div className="skill-category-icon">{category.icon}</div>
        <h3 className="skill-category-title">{category.title}</h3>
      </div>
      <div className="skill-list">
        {category.skills.map((skill) => (
          <div className="skill-item" key={skill.name}>
            <span className="skill-name">
              <span className="icon">{skill.icon}</span>
              {skill.name}
            </span>
            <SkillBar level={skill.level} inView={inView} />
          </div>
        ))}
      </div>
    </motion.div>
  );
}

export default function Skills() {
  return (
    <AnimatedSection id="skills">
      <div className="section-header">
        <p className="section-label">// Skills</p>
        <h2 className="section-title">
          My <span className="gradient">Tech Stack</span>
        </h2>
        <p className="section-subtitle">
          Technologies and tools I work with to bring ideas to life
        </p>
      </div>
      <div className="skills-grid">
        {categories.map((cat, i) => (
          <SkillCategory key={cat.title} category={cat} index={i} />
        ))}
      </div>
    </AnimatedSection>
  );
}
