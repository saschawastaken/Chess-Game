from figure import Figure

class Bishop(Figure):
    
    def isMoveValid(self, current_pos, target_pos, positions):     
        """   
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

            return True"""

            # diagonal movement
        if abs(current_pos[0] - target_pos[0]) == abs(current_pos[1] - target_pos[1]):
            vertical_addition = 1
            if current_pos[0] > target_pos[0]:
                vertical_addition = -1
            
            horizontal_addition = 1
            if current_pos[1] > target_pos[1]:
                horizontal_addition = -1
            
            pos = [current_pos[0], current_pos[1]]

            max_movement_range = 0

            while tuple(pos) != target_pos:
                max_movement_range += 1

                pos[0] += vertical_addition
                pos[1] += horizontal_addition

                """
                position = positions[pos[0]][pos[1]]

                if  position != None:
                
                    print(position)
                    return False
                """
            
            max_movement_range = range(max_movement_range + 1)[1:]

            print('mf' + str(max_movement_range))
            
            for movement_range in max_movement_range:
                position = positions[current_pos[0] + vertical_addition * movement_range][current_pos[1] + horizontal_addition * movement_range]

                if position != None:
                    # if its an enemy and the last movement in range, it works
                    print(str(movement_range) + ' | ' + str(len(max_movement_range)))
                    return position.grp != self.grp and movement_range == len(max_movement_range)

            return True

        return False