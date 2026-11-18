"""
Maps for the game, new maps can be added here without changing any other code
Everything is written as a fraction of the window (0.5 = halfway across) instead of in pixels,
this way the map stretches to fit whatever size the window is
Walls are (x, y, width, height)
"""

LEVEL_1 = {
    "name": "Arena",
    "player_spawn": (0.1, 0.5), # Not used yet, for when the player is added
    "npc_spawns": [(0.9, 0.5)], # Not used yet, for when the NPC is added
    "walls": [
        (0.467, 0.384, 0.066, 0.232), # Middle pillar
        (0.265, 0.174, 0.119, 0.046), # Top left
        (0.265, 0.780, 0.119, 0.046), # Bottom left
        (0.616, 0.174, 0.119, 0.046), # Top right
        (0.616, 0.780, 0.119, 0.046), # Bottom right
        (0.198, 0.418, 0.026, 0.163), # Left cover
        (0.776, 0.418, 0.026, 0.163), # Right cover
    ],
}
