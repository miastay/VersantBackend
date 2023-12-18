from scholarly import scholarly
from scholarly import ProxyGenerator

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)


def search_author(query, max=10):
    print(query)
    search_query = scholarly.search_author(query)
    author_results = dict()
    for _ in range(max):
        try:
            nx = next(search_query)
            if nx:
                author_results[nx['scholar_id']] = nx
        except StopIteration:
            break
    return author_results
    scholarly.pprint(first_author_result)

if __name__ == "__main__":
    import sys
    print(search_author(sys.argv[1]))