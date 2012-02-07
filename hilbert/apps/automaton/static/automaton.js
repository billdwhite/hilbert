
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
    force.charge(-1000)
    .linkDistance(10)
    .nodes(json.states)
    .links(json.transitions)
    .size([w, h])
    .start();

/*
    var link = vis.selectAll("line.link")
    .data(json.transitions)
    .enter().append("line")
    .attr("class", "link")
    .style("stroke", "#666")
    .style("stroke-width", "2px")
    .attr("x1", function(d) { return d.source.x;})
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; })
    
    link.append("title").text(function(d) { return d.input});
    link.append("text")
    .text("HI")
    
    link = vis.selectAll("line.link")
    link.data(json.transitions).exit().remove();
    */
    
    var link = vis.selectAll("g.link").data(json.transitions, function(d){return d.source.name + d.input});
    link.enter().append("g").attr("class", "link")
    link.append("line")
    .style("stroke", "#666")
    .style("stroke-width", "2px")
    .attr("x1", function(d) { return d.source.x;})
    .attr("y1", function(d) { return d.source.y; })
    .attr("x2", function(d) { return d.target.x; })
    .attr("y2", function(d) { return d.target.y; })
    .append("title").text(function(d) { return d.input});
    link.append("text").text(function(d) { return d.input; });
    link.exit().remove();
    
    var node = vis.selectAll("g.node")
    .data(json.states);
    
    node.enter().append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
    node.append("title")
    .text(function(d) { return d.name; });
    node.append("circle")
    .attr("r", 5)
    .style("fill", function(d) {
     if (d.initial) return "white";
     if (d.terminal) return "black";
     return "lightblue";
    });
    node.append("text")
    .attr("text-anchor", "middle")
    .attr("dy", ".3em")
    .attr("pointer-events", "none")
    .text(function(d) { return d.name; });
    node.call(force.drag);
    node.exit().remove();
    
    force.on("tick", function() {
      link.select("line")
      .attr("x1", function(d) { return d.source.x; })
      .attr("y1", function(d) { return d.source.y; })
      .attr("x2", function(d) { return d.target.x; })
      .attr("y2", function(d) { return d.target.y; });
      link.select("text")
      .attr("transform", function(d) {
        x = d.source.x + (d.target.x - d.source.x) / 2;
        y = d.source.y + (d.target.y - d.source.y) / 2;
        return "translate(" + x + "," + y + ")"; 
      })
      
      
      node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
    });
  });
}
