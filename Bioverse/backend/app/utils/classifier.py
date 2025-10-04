def recommend_similar(data, query):
    query = query.lower()
    results = []
    for d in data:
        score = 0
        if query in d["title"].lower(): score += 2
        if query in d.get("description", "").lower(): score += 1
        if any(query in kw.lower() for kw in d.get("keywords", [])): score += 1
        if score > 0:
            results.append((score, d))
    results.sort(key=lambda x: x[0], reverse=True)
    return [r[1] for r in results[:5]]

