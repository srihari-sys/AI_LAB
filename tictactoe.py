import random

board = [" "] * 9


def show():
  for i in range(0, 9, 3):
    print(board[i], "|", board[i + 1], "|", board[i + 2])
  print()


def check_win(p):
  lines = [
      (0, 1, 2),
      (3, 4, 5),
      (6, 7, 8),  
      (0, 3, 6),
      (1, 4, 7),
      (2, 5, 8),  
      (0, 4, 8),
      (2, 4, 6),  
  ]
  return any(board[a] == board[b] == board[c] == p for a, b, c in lines)


show()

while True:
  pos = int(input("Enter position (0-8): "))
  if board[pos] != " ":
    print("Already taken! Try again.")
    continue
  board[pos] = "X"
  show()

  if check_win("X"):
    print("You win!")
    break
  if " " not in board:
    print("Draw!")
    break

  empty = [i for i in range(9) if board[i] == " "]
  comp_move = random.choice(empty)
  board[comp_move] = "O"
  print(f"Computer played at {comp_move}:")
  show()

  if check_win("O"):
    print("Computer wins!")
    break