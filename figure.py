class Figure():
    
    def __init__(self, grp):
        # 1 = White, 0 = Black
        self.grp = grp

    def isOccupied(self, target_pos_tuple, positions, includeFriendly=True):
        target_pos_list = list(target_pos_tuple)
        if target_pos_tuple[0] > 7: target_pos_list[0] = 7
        if target_pos_tuple[1] > 7: target_pos_list[1] = 7
        if includeFriendly: return positions[target_pos_list[0]][target_pos_list[1]] != None
        else: return positions[target_pos_list[0]][target_pos_list[1]] != None and positions[target_pos_list[0]][target_pos_list[1]].grp != self.grp