def project01(grid):
    grid[0][4].make_barrier()
    grid[1][4].make_barrier()

    grid[10][0].make_barrier()
    grid[10][1].make_barrier()

    grid[3][2].make_barrier()
    grid[3][3].make_barrier()
    grid[4][3].make_barrier()
    grid[5][3].make_barrier()
    grid[4][1].make_barrier()

    grid[0][8].make_barrier()
    grid[1][8].make_barrier()
    grid[1][9].make_barrier()
    grid[2][9].make_barrier()
    grid[2][10].make_barrier()
    grid[3][10].make_barrier()
    grid[2][7].make_barrier()

    grid[12][1].make_barrier()
    grid[13][2].make_barrier()
    grid[14][2].make_barrier()
    grid[14][0].make_barrier()

    grid[17][2].make_barrier()
    grid[19][1].make_barrier()
    grid[19][3].make_barrier()

    grid[23][1].make_barrier()
    grid[23][0].make_barrier()

    grid[5][12].make_barrier()
    grid[6][11].make_barrier()
    grid[6][9].make_barrier()
    grid[6][10].make_barrier()

    grid[8][4].make_barrier()
    grid[8][3].make_barrier()

    grid[22][4].make_barrier()
    grid[23][5].make_barrier()

    grid[14][20].make_barrier()
    grid[20][20].make_barrier()

    grid[1][13].make_barrier()
    grid[0][14].make_barrier()
    grid[2][15].make_barrier()
    grid[1][17].make_barrier()
    grid[7][7].make_barrier()
    grid[5][6].make_barrier()

    grid[11][9].make_barrier()
    grid[10][8].make_barrier()
    grid[11][7].make_barrier()
    grid[11][6].make_barrier()
    grid[10][6].make_barrier()

    grid[4][18].make_barrier()
    grid[2][17].make_barrier()
    grid[9][11].make_barrier()
    grid[9][12].make_barrier()
    grid[11][11].make_barrier()
    grid[10][13].make_barrier()
    grid[11][14].make_barrier()
    grid[12][14].make_barrier()
    grid[13][15].make_barrier()
    grid[14][13].make_barrier()
    grid[20][17].make_barrier()
    grid[21][16].make_barrier()
    grid[22][17].make_barrier()
    grid[21][18].make_barrier()
    grid[18][17].make_barrier()
    grid[19][17].make_barrier()
    grid[16][15].make_barrier()
    grid[18][15].make_barrier()
    grid[6][15].make_barrier()
    grid[9][15].make_barrier()
    grid[8][16].make_barrier()
    grid[9][18].make_barrier()
    grid[9][17].make_barrier()
    grid[7][17].make_barrier()
    grid[7][18].make_barrier()
    grid[17][9].make_barrier()
    grid[18][12].make_barrier()
    grid[17][12].make_barrier()
    grid[16][12].make_barrier()
    grid[23][13].make_barrier()
    grid[23][11].make_barrier()
    grid[21][12].make_barrier()
    grid[21][11].make_barrier()
    grid[22][9].make_barrier()
    grid[20][8].make_barrier()
    grid[21][6].make_barrier()
    grid[12][18].make_barrier()
    grid[10][20].make_barrier()

    for col in range(24):
        for row in range(21, 24):
            grid[col][row].make_barrier()

    grid[0][0].make_start()
    grid[23][20].make_end()
    return grid[0][0], grid[23][20]