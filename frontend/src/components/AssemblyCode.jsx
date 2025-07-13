

const AssemblyCode = ({ data }) => {
  return (
    <div className="phase">
      <h2>Assembly Code</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default AssemblyCode;