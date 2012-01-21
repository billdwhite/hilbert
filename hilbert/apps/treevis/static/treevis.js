
var w = 1000;
var h = 400;

var tree = d3.layout.tree()
.size([w-10, h-10])
.separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

diagonal = d3.svg.diagonal()

function drawTree(treeJsonUrl) { 
  console.log("loading " + treeJsonUrl)

  d3.select(".chart").select("svg").remove()
  
  var vis = d3.select(".chart").append("svg")
  .attr("width", w)
  .attr("height", h)
  .append("g")
  
  d3.json(treeJsonUrl, function(json) {
    var nodes = tree.nodes(json);

    var link = vis.selectAll("path.link")
    .data(tree.links(nodes))
    .enter().append("path")
    .attr("class", "link")
    .attr("display", function(link) {
      if (link.target.key == "none") {
        return "none";
      }
    })
    .attr("d", diagonal);

    var node = vis.selectAll("g.node")
    .data(nodes)
    .enter().append("g")
    .attr("class", "node")
    .attr("transform", function(d) { return "translate(" + d.x + "," +  d.y + ")"; })
    .attr("display", function(d) { if (d.key == "none") return "none"})

    node.append("circle")
    .attr("r", 8)
    .attr("class", function(d) { if (d.colour == 1) return "red"; })
    
    node.append("text").text(function(d){return d.key;})
    .attr("transform", "translate(0,3)")
    .attr("style", "text-anchor: middle")
    .attr("class", "nodekey");
  });
}
