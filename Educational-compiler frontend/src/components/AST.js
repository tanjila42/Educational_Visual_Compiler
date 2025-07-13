import React, { useEffect } from 'react';
import * as d3 from 'd3';

const AST = ({ data }) => {
  useEffect(() => {
    if (data) {
      const width = 800;
      const height = 600;

      const svg = d3.select("#ast")
        .attr("width", width)
        .attr("height", height);

      const treeLayout = d3.tree().size([height, width - 100]);
      const root = d3.hierarchy(data);
      treeLayout(root);

      svg.selectAll('.link')
        .data(root.links())
        .enter().append('line')
        .attr('class', 'link')
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y)
        .attr('stroke', '#ccc')
        .attr('stroke-width', 2);

      svg.selectAll('.node')
        .data(root.descendants())
        .enter().append('circle')
        .attr('class', 'node')
        .attr('cx', d => d.x)
        .attr('cy', d => d.y)
        .attr('r', 5)
        .attr('fill', '#ff6347');

      svg.selectAll('.text')
        .data(root.descendants())
        .enter().append('text')
        .attr('class', 'text')
        .attr('x', d => d.x + 10)
        .attr('y', d => d.y - 10)
        .text(d => d.data.name)
        .attr('font-size', '12px')
        .attr('fill', '#333');
    }
  }, [data]);

  return (
    <div className="phase">
      <h2>Abstract Syntax Tree (AST)</h2>
      <svg id="ast"></svg>
    </div>
  );
};

export default AST;