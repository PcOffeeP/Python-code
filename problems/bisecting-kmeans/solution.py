from __future__ import annotations

Point = tuple[float, float]

TOLERANCE = 1e-12
MAX_ITERATIONS = 1000


def dist2(p1: Point, p2: Point) -> float:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def centroid(points: list[Point]) -> Point:
    length = len(points)
    center_x = sum(x for x, _ in points) / length
    center_y = sum(y for _, y in points) / length
    return center_x, center_y


def calc_sse(points: list[Point]) -> float:
    center = centroid(points)
    return sum(dist2(point, center) for point in points)


def split_cluster(points: list[Point]) -> tuple[list[Point], list[Point]]:
    center_1 = max(points, key=lambda point: point[0])
    center_2 = min(points, key=lambda point: point[0])
    old_tags: list[int] | None = None

    for _ in range(MAX_ITERATIONS):
        cluster_1: list[Point] = []
        cluster_2: list[Point] = []
        tags: list[int] = []

        for point in points:
            distance_1 = dist2(point, center_1)
            distance_2 = dist2(point, center_2)

            if distance_1 < distance_2:
                cluster_1.append(point)
                tags.append(0)
            else:
                cluster_2.append(point)
                tags.append(1)

        new_center_1 = centroid(cluster_1)
        new_center_2 = centroid(cluster_2)
        tags_unchanged = old_tags == tags
        centers_unchanged = (
            dist2(center_1, new_center_1) < TOLERANCE
            and dist2(center_2, new_center_2) < TOLERANCE
        )

        if tags_unchanged and centers_unchanged:
            break

        center_1 = new_center_1
        center_2 = new_center_2
        old_tags = tags

    return cluster_1, cluster_2


def bisecting_kmeans(points: list[Point], target_count: int) -> list[list[Point]]:
    if not points:
        raise ValueError("点集不能为空")
    if not 1 <= target_count <= len(points):
        raise ValueError("target_count 必须在 1 与点数量之间")

    clusters = [points]

    while len(clusters) < target_count:
        best_gain = -1.0
        best_index = -1
        best_children: tuple[list[Point], list[Point]] | None = None

        for index, cluster in enumerate(clusters):
            if len(cluster) <= 1:
                continue

            child_1, child_2 = split_cluster(cluster)
            gain = calc_sse(cluster) - calc_sse(child_1) - calc_sse(child_2)

            if gain > best_gain:
                best_gain = gain
                best_index = index
                best_children = child_1, child_2
            elif abs(gain - best_gain) < TOLERANCE:
                if len(cluster) > len(clusters[best_index]):
                    best_index = index
                    best_children = child_1, child_2

        if best_children is None:
            raise ValueError("没有可继续拆分的簇")

        clusters.pop(best_index)
        clusters.extend(best_children)
        sizes = sorted((len(cluster) for cluster in clusters), reverse=True)
        print(*sizes)

    return clusters


def main() -> None:
    target_count = int(input())
    point_count = int(input())
    points = [tuple(map(float, input().split())) for _ in range(point_count)]
    bisecting_kmeans(points, target_count)


if __name__ == "__main__":
    main()
