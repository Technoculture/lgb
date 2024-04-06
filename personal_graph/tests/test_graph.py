"""
Unit test for high level apis
"""

from personal_graph.models import Node, EdgeInput
from personal_graph.graph import Graph


def test_add_node(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()
    node = Node(
        id=1,
        attribute={"name": "Jack", "body": "Jack is Joe's cousin brother"},
        label="relative",
    )
    assert graph.add_node(node) is None


def test_add_nodes(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()
    nodes = [
        Node(
            id=1,
            attribute={"body": "Jerry loses her weight 10kg last week."},
            label="Diabetes",
        ),
        Node(
            id=2,
            attribute={"name": "Bob", "body": "Bob is feeling stressed and tensed."},
            label="Stress",
        ),
    ]

    assert graph.add_nodes(nodes) is None


def test_add_edge(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    node1 = Node(
        id=3,
        label="relative",
        attribute={
            "name": "Alice",
            "body": "Alice is Jack's cousin sister. She lives in CA.",
        },
    )
    node2 = Node(
        id=4, label="CA", attribute={"body": "CA has a lot of greenery and indians."}
    )

    edge = EdgeInput(
        source=node1, target=node2, label="KNOWS", attribute={"since": "2015"}
    )

    assert graph.add_edge(edge) is None


def test_add_edges(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    node1 = Node(id=3, label="Person", attribute={"name": "Alice", "age": "30"})
    node2 = Node(id=4, label="Person", attribute={"name": "Bob", "age": "25"})
    node3 = Node(
        id=1,
        label="Diabetes",
        attribute={"body": "Continuous urination and weight loss"},
    )
    node4 = Node(
        id=2,
        label="Dizziness",
        attribute={"body": "Jack is feeling stressed and feeling quite dizzy."},
    )

    edge1 = EdgeInput(
        source=node1, target=node2, label="KNOWS", attribute={"since": "2015"}
    )

    edge2 = EdgeInput(
        source=node3, target=node2, label="KNOWS", attribute={"since": "2015"}
    )
    edge3 = EdgeInput(
        source=node1, target=node4, label="KNOWS", attribute={"since": "2015"}
    )

    assert graph.add_edges([edge1, edge2, edge3]) is None


def test_update_node(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    node = Node(id=1, attribute={"name": "Jack"}, label="relative")

    assert graph.update_node(node) is None


def test_update_nodes(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    nodes = [
        Node(id=1, attribute={"name": "Jack"}, label="relative"),
        Node(id=2, attribute={"name": "Jill"}, label="relative"),
    ]

    assert graph.update_nodes(nodes) is None


def test_remove_node(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    assert graph.remove_node(1) is None


def test_remove_nodes(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    assert graph.remove_node([1, 6, 8]) is None


def test_search_node(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    assert graph.search_node(1) is not None


def test_traverse(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    assert graph.traverse(1, 2) is not None


def test_insert():
    graph = Graph()

    assert graph.insert("Alice has suffocation at night.")


def test_search_query():
    graph = Graph()

    assert graph.search_query("Suffocation problem.")


def test_merge_by_similarity(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()
    test_add_nodes(mock_atomic, mock_db_connection_and_cursor)

    assert graph.merge_by_similarity(0.9) is None


def test_find_nodes_like(mock_atomic, mock_db_connection_and_cursor):
    graph = Graph()

    assert graph.find_nodes_like("relative", 0.9) is not None
