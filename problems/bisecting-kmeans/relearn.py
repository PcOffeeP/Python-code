def count_dist(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def assign_points(points, centroids):
    cluster0 = []
    cluster1 = []
    for point in points:
        dist0 = count_dist(point, centroids[0])
        dist1 = count_dist(point, centroids[1])
        if dist0 <= dist1:
            cluster0.append(point)
        else:
            cluster1.append(point)
    return [cluster0, cluster1]

def compute_centroid(cluster, old_centroid):
    if not cluster:
        return old_centroid
    x_sum = sum(point[0] for point in cluster)
    y_sum = sum(point[1] for point in cluster)
    return (x_sum / len(cluster), y_sum / len(cluster))

points = [(1, 1), (8, 8), (2, 2), (9, 9), (5, 5)]
centers = [(0, 0), (10, 10)]
esp = 1e-6

for _ in range(100):  # Iterate a few times to refine the clusters
    cluster0, cluster1 = assign_points(points, centers)

    print("Cluster 0:", cluster0)
    print("Cluster 1:", cluster1)

    new_centers = [compute_centroid(cluster0, centers[0]), compute_centroid(cluster1, centers[1])]
    print("New Centers:", new_centers)

    centers = new_centers
    if count_dist(new_centers[0], centers[0]) < esp**2 and count_dist(new_centers[1], centers[1]) < esp**2:
        break  # Stop if centers do not change significantly

print("Final Centers:", centers)
