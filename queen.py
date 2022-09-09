from figure import Figure

class Queen(Figure):

    def isMoveValid(self, current_pos, target_pos, positions):
    
        # '1' range
        movements = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for movement in movements:
            if current_pos[0] + movement[0] == target_pos[0] and current_pos[1] + movement[1] == target_pos[1]:
                if positions[target_pos[0]][target_pos[1]] != None:
                    
                    if positions[target_pos[0]][target_pos[1]].grp == self.grp:
                        return False
                return True

        # horizontal '1-n' range
        if current_pos[0] == target_pos[0] and current_pos[1] != target_pos[1]:
            
            horizontal_addon = 1
            if current_pos[1] > target_pos[1]:
                horizontal_addon = -1
            
            max_movement_range = range(abs(current_pos[1] - target_pos[1]) + 1)[1:]

            # Iterate through everything except own figure
            for movement_range in max_movement_range:
                
                position = positions[current_pos[0]][current_pos[1] + movement_range * horizontal_addon]

                if position != None:
                    return position.grp != self.grp and movement_range == len(max_movement_range)

            return True
        
        # vertical '1-n' range
        if current_pos[0] != target_pos[0] and current_pos[1] == target_pos[1]:

            vertical_addon = 1
            if current_pos[0] > target_pos[0]:
                vertical_addon = -1

            max_movement_range = range(abs(current_pos[0] - target_pos[0]) + 1)[1:]
            
            # Iterate through everything except own figure
            for movement_range in max_movement_range:
                
                position = positions[current_pos[0] + movement_range * vertical_addon][current_pos[1]]

                if position != None:
                    # if its an enemy and the last movement in range, it works
                    return position.grp != self.grp and movement_range == len(max_movement_range)
                    
            return True

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
            
            max_movement_range = range(max_movement_range + 1)[1:]
            
            for movement_range in max_movement_range:
                position = positions[current_pos[0] + vertical_addition * movement_range][current_pos[1] + horizontal_addition * movement_range]

                if position != None:
                    # if its an enemy and the last movement in range, it works
                    return position.grp != self.grp and movement_range == len(max_movement_range)

            return True

        return False