import { useEffect } from 'react';
import * as d3 from 'd3';

const ParseTree = ({ data }) => {
  useEffect(() => {
    // Create the D3 visualization only when data is available
    if (data) {
      const width = 800;
      const height = 600;

      // Create the SVG container
      const svg = d3.select("#parseTree")
        .attr("width", width)
        .attr("height", height);

      // D3 Tree Layout Setup
      const treeLayout = d3.tree().size([height, width - 100]);

      // Hierarchical structure for the tree
      const root = d3.hierarchy(data);
      treeLayout(root);

      // Links (lines between nodes)
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

      // Nodes (circles)
      svg.selectAll('.node')
        .data(root.descendants())
        .enter().append('circle')
        .attr('class', 'node')
        .attr('cx', d => d.x)
        .attr('cy', d => d.y)
        .attr('r', 5)
        .attr('fill', '#69b3a2');

      // Text labels for nodes
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
      <h2>Parse Tree</h2>
      <svg id="parseTree"></svg>
    </div>
  );
};

export default ParseTree;