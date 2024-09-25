from flask import Flask, request, jsonify
from graph import Graph

app = Flask(__name__)
graph = Graph()

@app.route('/add_edge', methods=['POST'])
def add_edge():
    data = request.json
    graph.add_edge(data['from'], data['to'], data['cost'])
    return jsonify({"message": "Edge added successfully"}), 201

@app.route('/mst', methods=['GET'])
def get_mst():
    mst = graph.prim_mst()  # or use graph.kruskal_mst()
    return jsonify(mst)

if __name__ == '__main__':
    app.run(debug=True)
