from figure import Figure
class Rook(Figure):

    def isMoveValid(self, current_pos, target_pos, positions):        
        """
        if current_pos[0] == target_pos[0] and current_pos[1] != target_pos[1]:
            max_movement_range = abs(current_pos[1] - target_pos[1])
            print("diff x: " + str(max_movement_range))
            
            # Iterate through everything except own figure
            for i in range(max_movement_range)[1:]:
                if positions[current_pos[0]][i] != None:
                    if positions[current_pos[0]][i].grp == self.grp:
                        print(positions[current_pos[0]][i])
                        return False
                    
            return True

        if current_pos[0] != target_pos[0] and current_pos[1] == target_pos[1]:
            
            max_movement_range = abs(current_pos[0] - target_pos[0])
            print("diff y: " + str(max_movement_range))

            # Iterate through everything except own figure
            for i in range(max_movement_range)[1:]:
                if positions[i][current_pos[1]] != None:
                    if positions[i][current_pos[1]].grp == self.grp:
                        print(positions[i][current_pos[1]])
                        return False
                    
            return True
        """
        """
        vertical_addon = -1
        if self.grp:
            vertical_addon = 1


        # '1' range
        movements = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

        for movement in movements:
            if current_pos[0] + movement[0] == target_pos[0] and current_pos[1] + movement[1] == target_pos[1]:
                if positions[target_pos[0]][target_pos[1]] != None:
                    
                    if positions[target_pos[0]][target_pos[1]].grp == self.grp:
                        print('TRUE')
                        return False
                return True
        
        # horizontal '1-n' range
        if current_pos[0] == target_pos[0] and current_pos[1] != target_pos[1]:
            
            max_movement_range = range(abs(current_pos[0] - target_pos[0]))[1:]

            # Iterate through everything except own figure
            for movement_range in max_movement_range:
                
                position = positions[current_pos[0]][current_pos[1] + movement_range * vertical_addon]

                if position != None:
                    if position.grp != self.grp: continue

                    return False
                        
            return True
        
        # vertical '1-n' range
        if current_pos[0] != target_pos[0] and current_pos[1] == target_pos[1]:
            
            max_movement_range = range(abs(current_pos[0] - target_pos[0]))[1:]

            # Iterate through everything except own figure
            for movement_range in max_movement_range:
                
                position = positions[current_pos[0] + movement_range * vertical_addon][current_pos[1]]

                if position != None:
                    if position.grp != self.grp: continue

                    return False
                        
            return True

        return False
        """

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
                    """
                    if position.grp != self.grp:
                        if movement_range == len(max_movement_range):
        
                            return True
        
                    return False
                    """    
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
                    """
                    if position.grp != self.grp:
                        if movement_range == len(max_movement_range):
        
                            return True
        
                    return False
                    """    
            return True