class WaterBasin:

    def distribute_rainwater(self, altitudes):
        rows, cols = len(altitudes), len(altitudes[0])
        destination = [[None] * cols for _ in range(rows)]
        basin_sizes = {}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find_destination(r, c):
            if destination[r][c] is not None:
                return destination[r][c]

            # Assume the current cell is the destination
            lowest = (r, c)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and altitudes[nr][nc] < altitudes[lowest[0]][lowest[1]]:
                    lowest = (nr, nc)

            # If this cell flows to a lower neighbor, recurse
            if lowest != (r, c):
                destination[r][c] = find_destination(lowest[0], lowest[1])
            else:
                destination[r][c] = (r, c)

            return destination[r][c]

        # Compute the destination for each cell
        for r in range(rows):
            for c in range(cols):
                find_destination(r, c)

        # Count the size of each basin
        for r in range(rows):
            for c in range(cols):
                basin = destination[r][c]
                if basin not in basin_sizes:
                    basin_sizes[basin] = 0
                basin_sizes[basin] += 1

        # Fill the result grid
        water_flow = [[basin_sizes[destination[r][c]] for c in range(cols)] for r in range(rows)]
        return water_flow

    def main(self):
        altitudes = [
            [3, 3, 2, 1],
            [2, 3, 3, 1],
            [1, 3, 2, 1]
        ]
        result = self.distribute_rainwater(altitudes)
        for row in result:
            print(row)


water = WaterBasin()
water.main()