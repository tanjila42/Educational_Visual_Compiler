import React, { useEffect, useState } from 'react';
import { getCompilerData } from './api'; // Import your API function
import LexicalToken from './LexicalToken';
import SymbolTable from './SymbolTable'; // If you have this component
import ParseTree from './ParseTree';
import AST from './AST';
import IR from './IR';
import AssemblyCode from './AssemblyCode';

const App = () => {
  const [compilerData, setCompilerData] = useState({
    lexical_token: [],
    symbol_table: [],
    parse_tree: {},
    ast: {},
    ir: {},
    assembly_code: {},
  });

  useEffect(() => {
    const fetchCompilerData = async () => {
      const data = await getCompilerData("your input code here"); // Replace with actual input or state
      setCompilerData(data);
    };

    fetchCompilerData();
  }, []); // Empty array to run this only once when the component mounts

  return (
    <div>
      <h1>Educational Visual Compiler</h1>
      
      <LexicalToken data={compilerData.lexical_token} />
      <SymbolTable data={compilerData.symbol_table} />
      <ParseTree data={compilerData.parse_tree} />
      <AST data={compilerData.ast} />
      <IR data={compilerData.ir} />
      <AssemblyCode data={compilerData.assembly_code} />
    </div>
  );
};

export default App;
