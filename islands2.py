grid =[[1, 1, 1, 1, 0],
       [1, 1, 0, 1, 0],
       [1, 1, 0, 0, 0],
       [0, 0, 0, 0, 0]]

def find_islands(grid):
    island_count = 0
    for r_idx, col in enumerate(grid):
        for c_idx, v in enumerate(col):
            if v == 1:
                grid = dfs((r_idx, c_idx), grid)
                island_count += 1
    return island_count

def dfs(start, graph):
    """
    Base case: if there is a 1 next door, go visit it.
    """
    r_idx, c_idx = start
    max_w_idx = len(grid) - 1
    max_h_idx = len(grid[0]) - 1
    value = graph[r_idx][c_idx]
    graph[r_idx][c_idx] = 0
    if r_idx != max_w_idx and r_idx >= 0 and  c_idx >= 0 and c_idx != max_h_idx and value == 1:
        graph = dfs((r_idx + 1, c_idx), graph)
        graph = dfs((r_idx, c_idx + 1), graph)
        graph = dfs((r_idx - 1, c_idx), graph)
        graph = dfs((r_idx, c_idx - 1), graph)
    return graph




if __name__ == "__main__":
    n_islands = find_islands(grid)
    print(n_islands)
    print('win')
