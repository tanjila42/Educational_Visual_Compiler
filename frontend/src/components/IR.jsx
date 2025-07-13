const IR = ({ data }) => {
  return (
    <div className="phase">
      <h2>Intermediate Representation (IR)</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default IR;