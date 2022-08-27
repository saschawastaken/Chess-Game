from figure import Figure

class Knight(Figure):

    def isMoveValid(self, current_pos, target_pos, positions):
        movements = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

        for movement in movements:
            if current_pos[0] + movement[0] == target_pos[0] and current_pos[1] + movement[1] == target_pos[1]:
                if positions[target_pos[0]][target_pos[1]] != None:
                    
                    if positions[target_pos[0]][target_pos[1]].grp == self.grp:
                        return False
                return True

        return False