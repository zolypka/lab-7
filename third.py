def count_routes(n, m):
    routes = [[0] * m for _ in range(n)]
    routes[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i != 0 or j != 0:
                routes[i][j] = routes[i - 1][j] + routes[i][j - 1]

    return routes[n - 1][m - 1]

def get_user_input():
    n = int(input("number of lines: "))
    m = int(input("number of columns: "))
    return n, m

if __name__ == "__main__":
    n, m = get_user_input()
    print(f"number of routes from A to B: {count_routes(n, m)}")