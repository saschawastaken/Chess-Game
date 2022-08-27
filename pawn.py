from figure import Figure

class Pawn(Figure):

    def __init__(self, grp):
        super().__init__(grp)
        self.firstMove = True

    def isMoveValid(self, current_pos, target_pos, positions):

        vertical_addon = -1
        if self.grp:
            vertical_addon = 1
        
        # Special move at beginning
        if self.firstMove and current_pos[0] + 2 * vertical_addon == target_pos[0] and current_pos[1] == target_pos[1]:
            self.firstMove = False
            return True

        # y
        if current_pos[0] + vertical_addon == target_pos[0]:
            # x
            if current_pos[1] + 1 == target_pos[1] and self.isOccupied(target_pos, positions, False) or current_pos[1] - 1 == target_pos[1] and self.isOccupied(target_pos, positions, False):
                self.firstMove = False
                return True
            # Pawn must not escape a fight, it always has to pick it
            elif current_pos[1] == target_pos[1] and not self.isOccupied(target_pos, positions, False) and not self.isOccupied((target_pos[0], target_pos[1] - 1), positions, False) and not self.isOccupied((target_pos[0], target_pos[1] + 1), positions, False):
                self.firstMove = False
                return True
                
        return False


