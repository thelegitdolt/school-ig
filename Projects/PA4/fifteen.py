from Projects.PA4.graph import Graph, Vertex
import random


class Fifteen:
    def __init__(self):
        # Create the grapharoo
        self.tiles = Graph()
        
        # I'll just treat 16 as the empty space, because I don't want to rewrite range
        for i in range(1, 17):
            self.tiles.addVertex(i)
        
        self.starting_node = self.tiles.get_by_id(1)
        # Connect each node with the nodes that are orthogonal do it.
        for i in range(1, 17):
            orthogonals = {i + 4: 4, i - 4: -4, i + 1: 1, i - 1: -1}
            if i % 4 == 0:
                del orthogonals[i + 1]
            elif i % 4 == 1 and not i == 1:
                del orthogonals[i - 1]
            
            for orthogonal, weight in orthogonals.items():
                if orthogonal not in self.tiles:
                    continue
                
                self.tiles.addEdge(i, orthogonal, weight)
    
    def square_search(self):
        print('true')
        current_node: Vertex = self.starting_node
        transversal = [current_node.id]
        weight_map = {1: 1, 2: 1, 3: 1, 4: 4, 5: -1, 6: -1, 7: -1, 8: 4, 9: 1, 10: 1, 11: 1, 12: 4, 13: -1, 14: -1,
                      15: -1, 16: 0}
        map_ind_to_use = 1
        while len(transversal) < 16:
            if current_node.id == 16:
                print('HIIIIIII YES YES HIIII', self.tiles.vertList)
            for vertex, weight in current_node.connectedTo.items():
                if weight == weight_map[map_ind_to_use]:
                    map_ind_to_use += 1
                    transversal.append(vertex.id)
                    current_node = vertex
                    break
        transversal[4:8] = transversal[4:8][::-1]
        transversal[12:16] = transversal[12:16][::-1]
        return transversal
    
    # Gets visual representation of the board
    def gameplay_str(self):
        def int_map(num):
            if num == 16:
                return '  '
            elif num > 9:
                return num
            else:
                return f' {num}'
        board = \
            (("+---+---+---+---+\n"
              "|%s |%s |%s |%s |\n"
              "+---+---+---+---+\n"
              "|%s |%s |%s |%s |\n"
              "+---+---+---+---+\n"
              "|%s |%s |%s |%s |\n"
              "+---+---+---+---+\n"
              "|%s |%s |%s |%s |\n"
              "+---+---+---+---+")
             # Replace with empty space if 16
             # append space if under 10 to maintain formatting
             # else normal
             % tuple(map(int_map, self.square_search())))
        
        return board
    
    # Draws visual representation of board onto console
    def draw(self):
        print(self.gameplay_str())
    
    # swaps two elements
    def transpose(self, tile1_id: int, tile2_id: int):
        
        # find tiles by their element number
        tile1 = self.tiles.get_by_id(tile1_id)
        tile2 = self.tiles.get_by_id(tile2_id)
        if self.starting_node == tile1:
            self.starting_node = tile2
        elif self.starting_node == tile2:
            self.starting_node = tile1
        
        # make a copy of tile connection keys (can't modify dictionary while iterating through it)
        for ind, orths in enumerate(list(tile1.getConnections())):
            # get the original key
            orths_real = list(tile1.getConnections())[ind]
            for orth_orths, weight in dict(orths_real.connectedTo).items():
                # make the tiles connected to tile1 think they're connected to tile2
                if orth_orths.id == tile1.id:
                    orths_real.addNeighbor(tile2, weight)
                    orths_real.delNeighbor(tile1)
        
        # do the same thing but the other one
        for ind, orths in enumerate(list(tile2.getConnections())):
            orths_real = list(tile2.getConnections())[ind]
            for orth_orths, weight in dict(orths_real.connectedTo).items():
                if orth_orths.id == tile2.id:
                    orths_real.addNeighbor(tile1, weight)
                    orths_real.delNeighbor(tile2)
        
        tile1.connectedTo, tile2.connectedTo = tile2.connectedTo, tile1.connectedTo
        self.tiles.vertList[tile1_id], self.tiles.vertList[tile2_id] = self.tiles.vertList[tile2_id], \
            self.tiles.vertList[tile1_id]
        
        for vertex in dict(tile1.connectedTo).keys():
            if vertex == tile1:
                tile1.connectedTo[tile2] = tile1.connectedTo[vertex]
                del tile1.connectedTo[tile1]
        
        for vertex in dict(tile2.connectedTo).keys():
            if vertex == tile2:
                tile2.connectedTo[tile1] = tile2.connectedTo[vertex]
                del tile2.connectedTo[tile2]
    
    # sees if a tile can be moved (if it's next to the number 16)
    def is_valid_move(self, tile_id):
        # find tiles but their element number
        tile: Vertex = self.tiles.get_by_id(tile_id)
        if tile is None:
            print(tile_id)
        for orths in tile.getConnections():
            if orths.id == 16:
                # if the tile is connected to 16 then true
                return True
        
        return False
    
    def update(self, move_id):
        if not self.is_valid_move(move_id):
            return False
        
        self.transpose(move_id, 16)
    
    def shuffle(self, moves=200):
        for i in range(moves):
            tile = random.choice(list(self.tiles.get_by_id(16).getConnections()))
            self.update(tile.id)
    
    def is_solved(self):
        for key, val in self.tiles.vertList.items():
            if not key == val.id:
                return False
        return True
