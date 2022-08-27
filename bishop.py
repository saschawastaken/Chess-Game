from figure import Figure

class Bishop(Figure):
    
    def isMoveValid(self, current_pos, target_pos, positions):        
        if abs(current_pos[0] - target_pos[0]) == abs(current_pos[1] - target_pos[1]):
            
            vertical_addition = 1
            if current_pos[0] > target_pos[0]:
                vertical_addition = -1
            
            horizontal_addition = 1
            if current_pos[1] > target_pos[1]:
                horizontal_addition = -1
            
            pos = [current_pos[0], current_pos[1]]

            while tuple(pos) != target_pos:

                print(pos)

                pos[0] += vertical_addition
                pos[1] += horizontal_addition
                

                if positions[pos[0]][pos[1]] != None:
                    print(positions[pos[0]][pos[1]])
                    return False

            return True