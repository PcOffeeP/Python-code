
def dist2(p1:list, p2:list) -> float:
    '''
    计算两点之间的距离。
    '''
    return (p1[0] - p2[0]) **2 + (p1[1] - p2[1]) **2

def centroid(points:list) -> tuple:
    l = len(points)
    cx = sum(x for x, y in points) / l
    cy = sum(y for x, y in points) / l
    return cx, cy

def calc_sse(points):
    center = centroid(points)
    sse = 0

    for point in points:
        sse += dist2(point, center)

    return sse

def split_cluster(points):
    c1 = max(points, key=lambda p: p[0])
    c2 = min(points, key=lambda p: p[0])
    old_tag = None

    for _ in range(1000):
        cluster0 = []
        cluster1 = []
        tag = []

        for point in points:
            d1 = dist2(point, c1)
            d2 = dist2(point, c2)

            if d1 < d2:
                cluster0.append(point)
                tag.append(0)
            else:
                cluster1.append(point)
                tag.append(1)

        new_c1 = centroid(cluster0)
        new_c2 = centroid(cluster1)

        tag_same = (old_tag == tag)
        center_same = (
            dist2(c1, new_c1) < 1e-12 and dist2(c2, new_c2) < 1e-12
        )

        if tag_same and center_same:
            break
        c1 = new_c1
        c2 = new_c2
        old_tag = tag

    return cluster0, cluster1

