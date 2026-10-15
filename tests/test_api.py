from fastapi.testclient import TestClient

from sorting_lab.main import app

client = TestClient(app)


def test_health() -> None:
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


def test_methods() -> None:
    res = client.get("/methods")
    assert res.status_code == 200
    data = res.json()
    ids = {m["id"] for m in data["methods"]}
    assert ids == {"bubble", "selection", "insertion", "merge", "quick", "heap", "tim"}
    for method in data["methods"]:
        assert method["name"]
        assert method["complexity_best"]
        assert method["complexity_average"]
        assert method["complexity_worst"]
        assert isinstance(method["stable"], bool)
        assert method["blurb"]
        assert len(method["blurb"]) > 10


def test_methods_quadratic_average() -> None:
    res = client.get("/methods")
    by_id = {m["id"]: m for m in res.json()["methods"]}
    for mid in ("bubble", "selection", "insertion"):
        avg = by_id[mid]["complexity_average"]
        assert "n²" in avg or "n^2" in avg


def test_sort_single() -> None:
    res = client.post("/sort", json={"sequence": [5, 3, 1], "method": "merge"})
    assert res.status_code == 200
    body = res.json()
    assert len(body["results"]) == 1
    assert body["results"][0]["sorted"] == [1, 3, 5]


def test_sort_all() -> None:
    res = client.post("/sort", json={"sequence": [2, 1], "method": "all"})
    assert res.status_code == 200
    assert len(res.json()["results"]) == 7


def test_sort_unknown_method_422() -> None:
    res = client.post("/sort", json={"sequence": [1], "method": "radix"})
    assert res.status_code == 422


def test_sort_non_integer_422() -> None:
    res = client.post("/sort", json={"sequence": [1, "x"], "method": "bubble"})
    assert res.status_code == 422


def test_sort_oversize_422() -> None:
    res = client.post("/sort", json={"sequence": list(range(10_001)), "method": "bubble"})
    assert res.status_code == 422


def test_docs_available() -> None:
    res = client.get("/docs")
    assert res.status_code == 200


def test_index_portuguese() -> None:
    res = client.get("/")
    assert res.status_code == 200
    assert "Sorting Lab" in res.text
    assert "Ordenar" in res.text
    assert 'id="method-blurb"' in res.text


def test_app_js_has_educational_ux() -> None:
    res = client.get("/app.js")
    assert res.status_code == 200
    body = res.text
    assert "Complexidade (médio)" in body
    assert "Estável" in body
    assert "needsLargeNWarning" in body
    assert "method-blurb" in body or "methodBlurbEl" in body
