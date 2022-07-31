use std::fs;

fn main() {
    let file = fs::read_to_string("../day12.txt").expect("Cannot read file");
    let contents: Vec<&str> = file.split("\r\n").collect();

    let mut init: Vec<String> = Vec::new();
    let mut node_points: Vec<String> = Vec::new();
    let mut stop: Vec<String> = Vec::new();

    for content in contents {
        if content.contains("start") {
            init.push(content.to_string().replace("start", "").replace("-", ""));
        }
        else if content.contains("end") {
            stop.push(content.to_string().replace("end", "").replace("-", ""));
        }
        else if content != "" {
            node_points.push(content.to_string());
        }
    }

    let mut total: i32 = 0;
    for i in init {
        println!("{}", format!("{}{}", i, "="));
        total+= add_nodes(i, node_points.clone(), stop.clone(), Vec::new(), 0);
    }
    println!("{}", total);
}

fn add_nodes(i: String, nodes: Vec<String>, stop: Vec<String>, mut avoid: Vec<String>, mut total: i32) -> i32 {
    if i == i.to_lowercase() {
        avoid.push(i.clone());
    }

    if stop.contains(&i) {
        total+=1;
    }

    for n in &nodes {
        let point: String = n.replace(&i,"").replace("-","");
        if n.contains(&i) && !avoid.iter().any(|v| v == &point) {
            total += add_nodes(point, nodes.clone(), stop.clone(), avoid.clone(), 0);
        }
    }
    return total;
}
