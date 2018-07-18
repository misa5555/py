from collections import defaultdict
from collections import Counter

store = defaultdict(set)


def handleUserQuery(user, query):
    tmp = []
    relevant_queries = []
    for u, qs in store.items():
        if query in store[u]:
            tmp += list(qs - set([query]))
    if not tmp:
        store[user].add(query)
        return 0
    most_common = Counter(tmp).most_common(1)
    max_count = most_common[0][1]
    for k, v in Counter(tmp).most_common():
        if v == max_count:
            relevant_queries.append(k)

    store[user].add(query)
    return str(max_count) + ' ' + ' '.join(relevant_queries)
# print(handleUserQuery("A", "java"))
# print(handleUserQuery("B", "python"))
# print(handleUserQuery("B", "java"))
# print(handleUserQuery("A", "software_engineer"))
# print(handleUserQuery("C", "truck_driver"))
# print(handleUserQuery("B", "software_engineer"))
# print(handleUserQuery("A", "python"))

print(handleUserQuery("A", "retail"))
print(handleUserQuery("A", "sales"))
print(handleUserQuery("A", "restaurant"))
print(handleUserQuery("B", "retail"))
print(handleUserQuery("B", "sales"))
print(handleUserQuery("B", "part_time"))
print(handleUserQuery("C", "part_time"))
print(handleUserQuery("C", "cashier"))
print(handleUserQuery("C", "retail"))
