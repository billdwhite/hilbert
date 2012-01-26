
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
var tree = d3.layout.tree()
  .size([w-10, h-10])
  .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });
var diagonal = d3.svg.diagonal();
var vis = null;
var svg = null;

function initChart() {
  vis = d3.select(".chart").append("svg")
  .attr("width", w)
  .attr("height", h)
  .style("padding", padding + "px")
  
  svg = d3.select(".chart svg");
  
  svg.append("g").attr("class","edges")
  svg.append("g").attr("class","nodes")
}

function drawTree(treeJsonUrl) { 
  console.log("loading " + treeJsonUrl)
  d3.json(treeJsonUrl, function(json) {
    
    var nodes = tree.nodes(json);

    // Clear old svg
    //d3.select(".chart").select("svg").remove()
    // Init svg
  
    /*
    // create cursor
    svg.style("cursor", "none");
    svg.append("g")
    .attr("class","cursor")
    .attr("transform", "translate(0,0)")
    .append("circle")
    .attr("r", cursorRadius)
    var cursor = svg.select("g.cursor")
    
    // move cursor
    svg.on("mousemove", function(){
      cursor.attr("transform","translate("+d3.svg.mouse(this) +")")
    });
    */

    var link = vis.select(".edges").selectAll("path.link")
    .data(tree.links(nodes), function(d) {
      var id = d.target.key
      if (d.target.key != "none") {
        return d.target.key
      }
    });
    
    link.enter().append("path")
    .attr("class", "chartelem link")
    .attr("display", function(link) {
      if (link.target.key == "none") {
        return "none";
      }
    })
    .attr("d", diagonal);

    link.transition()
    .duration(1000)
    .attr("d", diagonal);

    link.exit().remove();
    
    var node = vis.select(".nodes").selectAll("g.node")
    .data(nodes, function(d) {
      return d.key;
    });
    
    node.enter()
    .append("g")
    .attr("class", "chartelem node")
    .attr("id", function(d) { return "node-" + d.key})
    .attr("transform", function(d) { return "translate(" + d.x + "," +  d.y + ")"; })
    .attr("display", function(d) { if (d.key == "none") return "none"})
    .attr("pointer-events", "none");

    node.append("circle")
    .attr("r", radius)
    .attr("class", function(d) { if (d.colour == 1) return "red"; });

    node.append("circle")
    .attr("r", cursorRadius)
    .style("fill", "none")
    .attr("pointer-events", "all")
    .style("visibility","hidden")
    .on("click", function(d,i) {
      //circle = d3.select(this.parentNode).select("circle")
      //circle.attr("class", "red")
    });
    
    node.append("text").text(function(d){return d.key;})
    .attr("transform", "translate(0,3)")
    .attr("style", "text-anchor: middle")
    .attr("class", "nodekey");
    
    node.transition()
    .duration(1000)
    .attr("transform", function(d){return "translate(" + d.x + "," +  d.y + ")";});
    
    node.exit().remove();
  });
}
