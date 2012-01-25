
var w = 1000;
var h = 400;

var tree = d3.layout.tree()
.size([w-10, h-10])
.separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

diagonal = d3.svg.diagonal()

function drawTree(treeJsonUrl) { 
  console.log("loading " + treeJsonUrl)
  var radius = 8;
  var cursorRadius = radius * 3;
  var padding = 20;

  d3.json(treeJsonUrl, function(json) {
    var nodes = tree.nodes(json);

    // Clear old svg
    d3.select(".chart").select("svg").remove()
    // Init svg
    var vis = d3.select(".chart").append("svg")
    .attr("width", w)
    .attr("height", h)
    .style("padding", padding + "px")

    var svg = d3.select(".chart svg");
  
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
    .attr("id", function(d) { return "node-" + d.key})
    .attr("transform", function(d) { return "translate(" + d.x + "," +  d.y + ")"; })
    .attr("display", function(d) { if (d.key == "none") return "none"})
    .attr("pointer-events", "none");

    node.append("circle")
    .attr("r", radius)
    .attr("class", function(d) { if (d.colour == 1) return "red"; })

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
    .attr("class", "nodekey")
  });
}
