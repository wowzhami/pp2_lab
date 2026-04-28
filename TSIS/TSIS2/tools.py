def flood_fill(surf, x, y, new_col):
    target_col = surf.get_at((x, y))
    if target_col == new_col: return
    q = [(x, y)]
    while q:
        if len(q) > 10000: break # Защита от зависания
        cx, cy = q.pop(0)
        if 0 <= cx < 800 and 0 <= cy < 600 and surf.get_at((cx, cy)) == target_col:
            surf.set_at((cx, cy), new_col)
            q.extend([(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)])
