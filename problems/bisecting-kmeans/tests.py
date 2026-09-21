import io
import unittest
from contextlib import redirect_stdout

from solution import bisecting_kmeans, calc_sse, centroid, dist2


class BisectingKMeansTests(unittest.TestCase):
    def run_clustering(self, points, target_count):
        output = io.StringIO()
        with redirect_stdout(output):
            clusters = bisecting_kmeans(points, target_count)
        return clusters, output.getvalue().strip().splitlines()

    def test_normal_case(self):
        points = [(-3.0, 0.0), (-2.0, 0.0), (-1.0, 0.0),
                  (5.0, 0.0), (6.0, 0.0), (7.0, 0.0)]
        clusters, lines = self.run_clustering(points, 2)
        self.assertEqual(sorted(map(len, clusters), reverse=True), [3, 3])
        self.assertEqual(lines, ["3 3"])

    def test_edge_case_two_points(self):
        clusters, lines = self.run_clustering([(0.0, 0.0), (1.0, 1.0)], 2)
        self.assertEqual(sorted(map(len, clusters), reverse=True), [1, 1])
        self.assertEqual(lines, ["1 1"])

    def test_equal_gain_tie_is_deterministic(self):
        points = [(-2.0, 0.0), (-1.0, 0.0), (1.0, 0.0), (2.0, 0.0)]
        clusters, lines = self.run_clustering(points, 3)
        self.assertEqual(sorted(map(len, clusters), reverse=True), [2, 1, 1])
        self.assertEqual(lines, ["2 2", "2 1 1"])

    def test_minimal_case_requires_no_split(self):
        point = (2.0, -1.0)
        clusters, lines = self.run_clustering([point], 1)
        self.assertEqual(clusters, [[point]])
        self.assertEqual(lines, [])

    def test_distance_centroid_and_sse(self):
        points = [(0.0, 0.0), (2.0, 0.0)]
        self.assertEqual(dist2(points[0], points[1]), 4.0)
        self.assertEqual(centroid(points), (1.0, 0.0))
        self.assertEqual(calc_sse(points), 2.0)


if __name__ == "__main__":
    unittest.main()

