from Projects.PA4.graph import Graph, Vertex
import random


# Hi I'm up at 2:40 am writing comments because you apparently get 35 out of 40 if you don't.
class Fifteen:
    weight_map = {1: 1, 2: 1, 3: 1, 4: 4, 5: -1, 6: -1, 7: -1, 8: 4, 9: 1, 10: 1, 11: 1, 12: 4, 13: -1, 14: -1,
                  15: -1, 16: 0}
    
    def __init__(self):
        # Create the grapharoo
        self.tiles = Graph()
        
        # I'll just treat 16 as the empty space, because I don't want to rewrite range
        for i in range(1, 17):
            self.tiles.addVertex(i)
        
        self.starting_node = self.tiles.get_by_id(1)
        # Connect each node with the nodes that are orthogonal do it.
        # Edges are weighted depending on the direction they are from the base node
        for i in range(1, 17):
            orthogonals = {i + 4: 4, i - 4: -4, i + 1: 1, i - 1: -1}
            if i % 4 == 0:
                # 12 is not connected to 13
                del orthogonals[i + 1]
            elif i % 4 == 1 and not i == 1:
                # 9 is not connected to 8
                del orthogonals[i - 1]
            
            for orthogonal, weight in orthogonals.items():
                # the -3 and 17 tile does not exist and will never exist
                if orthogonal not in self.tiles:
                    continue
                
                # Edges are weighted according to their directions.
                # This will help me with my custom trademarked Square Search:tm:
                # Do not steal.
                self.tiles.addEdge(i, orthogonal, weight)
    
    # function that traverses through the graph but better because i don't trust "bread" first search
    def square_search(self):
        current_node: Vertex = self.starting_node
        traversal = [current_node.id]
        
        # the path is hardcoded, though the hardcode is probably easily extendable
        # If you want to make a game called "Twenty-Five"
        
        # Basically you draw a snake. 1 2 3 4 then when you run out of room you go down to 8
        # and then after that you do 8 7 6 5 and go down from 5 to 9 and then you do 9 10 11 12 etc etc
        # this is an easily generalizable algorithm but I don't feel like it.
        map_ind_to_use = 1
        while len(traversal) < 16:
            for vertex, weight in current_node.connectedTo.items():
                # Only go the direction assigned by the hardcoded dictionary
                if weight == Fifteen.weight_map[map_ind_to_use]:
                    map_ind_to_use += 1
                    traversal.append(vertex.id)
                    current_node = vertex
                    break
        # this returns 1 2 3 4 8 7 6 5 so those parts are flipped
        traversal[4:8] = traversal[4:8][::-1]
        # This part is also generalizable with some creative list splicing
        traversal[12:16] = traversal[12:16][::-1]
        # But I'm not here to do that today.
        return traversal
    
    # Gets visual representation of the board
    def gameplay_str(self):
        # Replace with empty space if 16
        # append space if under 10 to maintain formatting
        # else normal
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
             % tuple(map(int_map, self.square_search())))
        
        return board
    
    # Draws visual representation of board onto console
    def draw(self):
        print(self.gameplay_str())
    
    # hacky code that swaps two elements. Bless no private variables
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
        
        # make tile1 and tile2 think they are each other
        tile1.connectedTo, tile2.connectedTo = tile2.connectedTo, tile1.connectedTo
        self.tiles.vertList[tile1_id], self.tiles.vertList[tile2_id] = self.tiles.vertList[tile2_id], \
            self.tiles.vertList[tile1_id]
        
        # swap out instances of tiles connecting to themselves
        for vertex in dict(tile1.connectedTo).keys():
            if vertex == tile1:
                tile1.connectedTo[tile2] = tile1.connectedTo[vertex]
                # You would not be able to delete stuff from
                # the heavily abstracted pseudo-dictionaries if this was
                # Programming Abstractions in Java.
                # God bless.
                del tile1.connectedTo[tile1]
        
        for vertex in dict(tile2.connectedTo).keys():
            if vertex == tile2:
                tile2.connectedTo[tile1] = tile2.connectedTo[vertex]
                del tile2.connectedTo[tile2]
    
    # sees if a tile can be moved (if it's next to the number 16)
    def is_valid_move(self, tile_id):
        # find tiles but their element number
        tile: Vertex = self.tiles.get_by_id(tile_id)
        for orths in tile.getConnections():
            if orths.id == 16:
                # if the tile is connected to 16 then true
                return True
        
        return False
    
    # Attempts to swap a number with the empty space
    def update(self, move_id):
        # if it's a valid move then swap it with 16
        if not self.is_valid_move(move_id):
            # Return false so game.py knows whether it worked or not
            return False
        
        # Call robust, soundly implemented transpose function
        self.transpose(move_id, 16)
        return True
    
    # does 200 random moves on the starting grid to randomize it
    def shuffle(self, moves=200):
        for i in range(moves):
            # finds a random tile that is next to 16, and then update it
            tile = random.choice(list(self.tiles.get_by_id(16).getConnections()))
            # This should never throw an error
            self.update(tile.id)
    
    def is_solved(self):
        # Square search should return 1 to 16 in order if tiles are solved
        return self.square_search() == list(range(1, 17))
    