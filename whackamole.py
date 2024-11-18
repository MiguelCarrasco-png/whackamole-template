import pygame
import random


def main():
    BOARD_ROWS = 16
    BOARD_COLS = 20
    LINE_COLOR = "dark blue"
    SQUARE_SIZE = 32
    WIDTH = 640
    HEIGHT = 512

    # Initial position of the mole
    mole_row = 0
    mole_col = 0

    pygame.init()
    try:
        # Load resources
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos #Coordinates
                    row = y // SQUARE_SIZE
                    col = x // SQUARE_SIZE
                    # Check if mole was clicked
                    if row == mole_row and col == mole_col:
                        mole_row = random.randrange(0, BOARD_ROWS)
                        mole_col = random.randrange(0, BOARD_COLS)

            # Fill screen with background color
            screen.fill("light green")

            # Draw the grid
            for i in range(1, BOARD_ROWS):
                pygame.draw.line(
                    screen, LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE)
                )
            for i in range(1, BOARD_COLS):
                pygame.draw.line(
                    screen, LINE_COLOR,
                    (i * SQUARE_SIZE, 0),
                    (i * SQUARE_SIZE, HEIGHT)
                )

            # Draw the mole
            mole_x = mole_col * SQUARE_SIZE
            mole_y = mole_row * SQUARE_SIZE
            screen.blit(mole_image, (mole_x, mole_y))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
