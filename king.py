from figure import Figure

class King(Figure):

    def isMoveValid(self, current_pos, target_pos, positions):
        movements = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for movement in movements:
            if current_pos[0] + movement[0] == target_pos[0] and current_pos[1] + movement[1] == target_pos[1]:
                if positions[target_pos[0]][target_pos[1]] != None:
                    
                    if positions[target_pos[0]][target_pos[1]].grp == self.grp:
                        print('TRUE')
                        return False
                return True

        return False