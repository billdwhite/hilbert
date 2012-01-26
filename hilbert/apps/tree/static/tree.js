
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

function drawTree(treeJsonUrl) { 
  console.log("loading " + treeJsonUrl)
  d3.json(treeJsonUrl, function(json) {
    
    var nodes = tree.nodes(json);

    // Clear old svg
    //d3.select(".chart").select("svg").remove()
    // Init svg

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
    .data(tree.links(nodes), function(d) {
      var id = d.source.key
      if (d.target.key == d.source.children[0].key) {
        id = id + "L"
      } else if (d.target.key == d.source.children[1].key){
        id = id + "R"
      }
      if (d.target.key == "none") {
        id = id + "none"
      }
      return id
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
    .attr("d", diagonal)

    link.exit().remove();
    
    var node = vis.selectAll("g.node")
    .data(nodes, function(d) {
      return d.key + "_" + d.colour;
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
    
    node.transition()
    .duration(1000)
    .attr("transform", function(d){return "translate(" + d.x + "," +  d.y + ")";})
    
    node.exit().remove();
    
    // custom sort to make sure edges are drawn below nodes.
    d3.selectAll(".chartelem").sort(function(x,y) {
      xEdge = x.source != null;
      yEdge = y.source != null;
      if (xEdge && !yEdge) {
        return -1
      } else if (yEdge && !xEdge){
        return 1
      } else { 
        if (x<y) return -1;
        if (x>y) return 1;
        return 0;
      }
    });
  });
}
