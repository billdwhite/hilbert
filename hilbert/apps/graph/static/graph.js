
function randOrd(){
  return (Math.round(Math.random())-0.5);
}

function randomSequence(N) {
  seq = new Array();
  for (i = 1; i <= N; i++) {
    seq.push(i);
  }
  seq.sort(randOrd);
  return seq;
}

var w = 1000;
var h = 400;
var radius = 8;
var cursorRadius = radius * 3;
var padding = 20;

var force = d3.layout.force()
    
var vis = null;
var svg = null;

function initChart() {
  vis = d3.select(".chart").append("svg")
  .attr("width", w)
  .attr("height", h)
  //.style("padding", padding + "px")
  
  svg = d3.select(".chart svg");
  
  svg.append("g").attr("class","edges")
  svg.append("g").attr("class","nodes")
}

function drawGraph(url) { 
  console.log("loading " + url)
  d3.json(url, function(json) {
    force.charge(-220)
    .linkDistance(10)
    .nodes(json.nodes)
    .links(json.links)
    .size([w, h])
    .start();

    var link = vis.selectAll("line.link")
    .data(json.links);
    
    link.enter()
    .append("line")
    .attr("class", "link")
    .style("stroke-width", function(d) { return Math.sqrt(d.value); })
    .attr("x1", function(d) { return d.source.x; })
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; });
    link.exit().remove();
    
    var node = vis.selectAll("circle.node").data(json.nodes)
    node.enter().append("circle")
    .attr("class", "node")
    .attr("cx", function(d) { return d.x; })
    .attr("cy", function(d) { return d.y; })
    .attr("r", 5)
    .style("fill", "lightblue") 
    .call(force.drag);
    node.append("title")
    .text(function(d) { return d.name; });

    node.exit().remove();
    
    force.on("tick", function() {
      link.attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });
      
      node.attr("cx", function(d) { return d.x; })
      .attr("cy", function(d) { return d.y; });
    });
  });
}
