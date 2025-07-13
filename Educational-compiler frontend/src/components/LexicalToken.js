import React from 'react';

const LexicalToken = ({ data }) => {
  return (
    <div className="phase">
      <h2>Lexical Token</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre> {/* Displaying data in a formatted way */}
    </div>
  );
};

export default LexicalToken;
