import heapq

import heapq

def min_cost_to_connect_cables(cables):
    """
    Calculates the minimum cost to connect all cables.

    Args:
        cables (list): A list of integers representing the lengths of cables.

    Returns:
        int: The minimum cost to connect all cables.

    Raises:
        None

    Examples:
        >>> min_cost_to_connect_cables([2, 4, 6, 8])
        36
        >>> min_cost_to_connect_cables([1, 3, 5, 7, 9])
        54
    """
    heapq.heapify(cables)
    
    total_cost = 0
    
    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        cost = first + second
        total_cost += cost
        
        heapq.heappush(cables, cost)
    
    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(cables))
