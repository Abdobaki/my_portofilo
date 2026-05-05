import React from 'react';
import { motion } from 'framer-motion';

export default function Loader() {
  return (
    <motion.div
      className="loader-wrapper"
      exit={{ opacity: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="loader-content">
        <div className="loader-logo">AN</div>
        <div className="loader-bar">
          <div className="loader-bar-fill" />
        </div>
      </div>
    </motion.div>
  );
}
