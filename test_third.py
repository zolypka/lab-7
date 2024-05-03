from third import count_routes
import unittest

def count_routes(n, m):
    routes = [[0] * m for _ in range(n)]
    routes[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i != 0 or j != 0:
                routes[i][j] = routes[i - 1][j] + routes[i][j - 1]

    return routes[n - 1][m - 1]

class TestCountRoutes(unittest.TestCase):
    def test_count_routes(self):
        self.assertEqual(count_routes(2, 2), 2)
        self.assertEqual(count_routes(3, 3), 6)
        self.assertEqual(count_routes(4, 4), 20)

if __name__ == "__main__":
    unittest.main()