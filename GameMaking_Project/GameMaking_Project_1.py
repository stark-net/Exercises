import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
LIGHT_GRAY = (211,211,211)
DARK_GRAY = (120, 124, 126)

FONT = pygame.font.SysFont('Arial', 40)
SMALL_FONT = pygame.font.SysFont('Arial', 30)

WIDTH = 600
HEIGHT = 750
GRID_SIZE = 5

MAX_TRIES = 6
with open('5_letter_words.txt') as f:
    WORD_LIST = [line.strip().lower() for line in f if len(line.strip()) == 5]

FILTERED_WORD_LIST = [word for word in WORD_LIST if len(word) == GRID_SIZE]

class WordleGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption('wordle')
        
        self.clock = pygame.time.Clock()
        self.word_to_guess = random.choice(FILTERED_WORD_LIST)
        self.guesses = []
        self.current_guess = ""
        self.attempts = 0
        self.score = 0
        self.running = True
        self.user_quit = False
        self.state = "menu"
        self.start_rect = None
        self.help_rect = None
        self.quit_rect = None
        self.invalid_guess = False
        self.invalid_timer = 0
        self.did_win = False
        
    def draw_grid(self):
        for row in range(MAX_TRIES):
            for col in range(GRID_SIZE):
                pygame.draw.rect(self.screen, LIGHT_GRAY, (col * 100 + 50, row * 100 + 140, 90, 90)) 
                pygame.draw.rect(self.screen, BLACK, (col * 100 + 50, row * 100 + 140, 90, 90), 3)
                
    def draw_text(self, text, x, y, font, color, center = True):
        label = font.render(text, True, color)
        text_rect = label.get_rect()
        if center:
            text_rect.center = (x,y)
        else:
            text_rect.topleft = (x,y)
        
        self.screen.blit(label, text_rect)
        
    def draw_guesses(self):
        for i, guess in enumerate(self.guesses):
            letter_colors = [DARK_GRAY] * GRID_SIZE
            word_letters = list(self.word_to_guess)
            
            for j in range(GRID_SIZE):
                if guess[j] == self.word_to_guess[j]:
                    letter_colors[j] = GREEN
                    word_letters[j] = None
            
            for j in range(GRID_SIZE):
                if letter_colors[j] == DARK_GRAY and guess[j] in word_letters:
                    letter_colors[j] = YELLOW
                    word_letters[word_letters.index(guess[j])] = None
            
            for j, letter in enumerate(guess):
                rect_x = 50 + j * 100
                rect_y = 140 + i * 100
                rect_center_x = rect_x + 45
                rect_center_y = rect_y + 45
                
                rect_color = letter_colors[j]
                
                pygame.draw.rect(self.screen, rect_color, (rect_x, rect_y, 90, 90))
                pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 90, 90), 3)
                
                self.draw_text(letter.upper(), rect_center_x, rect_center_y, FONT, BLACK)
            
    def draw_ui(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, DARK_GRAY, self.screen.get_rect(), 6)
        self.draw_text("Type your word and press Enter...", WIDTH // 2, 60, SMALL_FONT, BLACK)
        self.draw_grid()
        self.draw_guesses()
        
        for i, letter in enumerate(self.current_guess):
            rect_x = 50 + i * 100
            rect_y = 140 + self.attempts * 100
            rect_center_x = rect_x + 45
            rect_center_y = rect_y + 45
            
            pygame.draw.rect(self.screen, LIGHT_GRAY, (rect_x, rect_y, 90, 90))
            pygame.draw.rect(self.screen, BLACK, (rect_x, rect_y, 90, 90), 3)
            
            self.draw_text(letter.upper(), rect_center_x, rect_center_y, FONT, BLACK)
        
        if self.invalid_guess:
            if pygame.time.get_ticks() - self.invalid_timer < 2000:
                self.draw_text("Not a valid word!", WIDTH // 2, HEIGHT - 50, SMALL_FONT, RED)
            else:
                self.invalid_guess = False
        pygame.display.update()
                
    def handle_input(self, event):
        if not self.running:
            return
        elif event.key == pygame.K_RETURN and len(self.current_guess) == GRID_SIZE:
            if self.current_guess not in FILTERED_WORD_LIST:
                self.invalid_guess = True
                self.invalid_timer = pygame.time.get_ticks()
                self.current_guess = ""
                return
            self.guesses.append(self.current_guess)
            if self.current_guess == self.word_to_guess:
                self.score += 50
                self.did_win = True
                self.running = False
            else:
                self.attempts += 1
                if self.attempts == MAX_TRIES:
                    self.running = False
            self.current_guess = ""
        elif event.key == pygame.K_BACKSPACE:
            self.current_guess = self.current_guess[:-1]
        elif event.unicode.isalpha() and len(self.current_guess) < GRID_SIZE:
            self.current_guess += event.unicode.lower()
                
    def is_button_clicked(self, rect, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if rect.collidepoint(event.pos):
                return True
        return False
    
    def draw_menu(self):
        self.screen.fill(WHITE)
        self.draw_text('WORDLE', WIDTH // 2, 100, FONT, BLACK)
        self.start_rect = pygame.Rect(WIDTH // 2 - 100, 250, 200, 60)
        self.help_rect = pygame.Rect(WIDTH // 2 - 100, 350, 200, 60)
        self.quit_rect = pygame.Rect(WIDTH // 2 - 100, 450, 200, 60)
        
        self.draw_button(self.start_rect, 'Start Game')
        self.draw_button(self.help_rect, 'Help')
        self.draw_button(self.quit_rect, 'Quit')
        
        pygame.display.update()
        
    def handle_menu_input(self, event):
        if self.is_button_clicked(self.start_rect, event):
            self.word_to_guess = random.choice(FILTERED_WORD_LIST)
            self.guesses = []
            self.current_guess = ""
            self.attempts = 0
            self.running = True
            self.state = "game"
        elif self.is_button_clicked(self.help_rect, event):
            self.state = "help"
        elif self.is_button_clicked(self.quit_rect, event):
            self.user_quit = True
            
    def draw_help(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, DARK_GRAY, self.screen.get_rect(), 6)
        self.draw_text('HOW TO PLAY',  WIDTH // 2, 50, FONT, BLACK)
        
        help_lines = [
            "Guess the hidden 5-letter word.",
            "Green: correct letter, correct place.",
            "Yellow: correct letter, wrong place.",
            "Gray: letter not in word.",
            "You have 6 tries."
            ]
        
        y = 120
        for i, line in enumerate(help_lines):
            self.draw_text(line, WIDTH // 2, y, SMALL_FONT, BLACK)
            y += 40
            
        self.back_rect = pygame.Rect(WIDTH // 2 - 100, 500, 200, 60)
        self.draw_button(self.back_rect, 'BACK')
        pygame.display.update()
        
    def handle_help_input(self, event):
        if self.is_button_clicked(self.back_rect, event):
            self.state = "menu"
            
    def draw_button(self, rect, text):
        mouse_pos = pygame.mouse.get_pos()
        hover = rect.collidepoint(mouse_pos)
        fill_color = LIGHT_GRAY if not hover else (180, 180, 180)
        pygame.draw.rect(self.screen, fill_color, rect)
        pygame.draw.rect(self.screen, DARK_GRAY, rect, 2)
        center_x, center_y = rect.center
        self.draw_text(text, center_x, center_y, SMALL_FONT, BLACK)
        
    def game_over_screen(self):
        self.screen.fill(WHITE)
        pygame.draw.rect(self.screen, DARK_GRAY, self.screen.get_rect(), 6)
        if self.user_quit:
            result_text = "Game Ended Early!"
        
        elif self.did_win:
            result_text = "You Won!"
            
        else:
            result_text = f"You Lost! Word was: {self.word_to_guess.upper()}"
        self.draw_text(result_text, WIDTH // 2, 250, SMALL_FONT, BLACK)
        self.draw_text(f"Final Score: {self.score}", WIDTH // 2, 300, SMALL_FONT, BLACK)
        pygame.display.update()
        pygame.time.wait(3000)
        self.state = "menu"
    
    def run(self):
        pygame.display.update()
        while not self.user_quit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.user_quit = True
                elif self.state == "menu":
                    self.handle_menu_input(event)
                elif self.state == "help":
                    self.handle_help_input(event)
                elif self.state == "game":
                    if event.type == pygame.KEYDOWN:
                        self.handle_input(event)
                        
                    if not self.running:
                        self.game_over_screen()
            if self.state == "menu":
                self.draw_menu()
            elif self.state == "help":
                self.draw_help()
            elif self.state == "game":
                self.draw_ui()
            pygame.display.update()
            self.clock.tick(30)
            
        pygame.quit()
if __name__ == "__main__":
    game = WordleGame()
    game.run()