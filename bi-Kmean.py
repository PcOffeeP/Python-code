
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

def bisecting_kmeans(points, N):
    clusters = [points]

    best_gain = -1
    best_index = -1
    best_children = None

    while len(clusters) < N:
        # 1. 遍历当前所有 cluster
        for i, cluster in enumerate(clusters):
            # 2. 每个 cluster 都调用 split_cluster() 试拆
            child1, child2 = split_cluster(cluster)
            # 3. 计算：
            #    gain = parent_sse - child1_sse - child2_sse
            gain = calc_sse(cluster) - calc_sse(child1) - calc_sse(child2)
            # 4. 保存 gain 最大的候选
            if gain > best_gain:
                best_gain = gain
                best_index = i
                best_children = (child1, child2)

        # 5. 真正删除 parent，加入两个 children
        if best_children:
            clusters.pop(best_index)
            clusters.extend(best_children)
    return clusters

if __name__ == '__main__':
    points = input("请输入点集（格式：x1,y1;x2,y2;...）：")
    clusters = bisecting_kmeans(points, 3)
    print(clusters)