import React from "react";

const SymbolTable = ({ data }) => {
  return (
    <div className="phase">
      <h2>Symbol Table</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default SymbolTable;