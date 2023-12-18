from scholarly import scholarly
from scholarly import ProxyGenerator

pg = ProxyGenerator()
pg.FreeProxies()
scholarly.use_proxy(pg)



def search_author(query):
    search_query = scholarly.search_author(query)
    first_author_result = next(search_query)
    return first_author_result
    scholarly.pprint(first_author_result)

if __name__ == "__main__":
    import sys
    print(search_author(sys.argv[1]))