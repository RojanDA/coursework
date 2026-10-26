
import tkinter as tk
from tkinter import messagebox, ttk
import heapq
import time
import copy
from typing import List, Tuple, Dict, Optional

# Constants
N = 3
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)


class EightPuzzleSolverUI:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title('8-Puzzle Solver Using A* Search')
        self.root.resizable(False, False)

        # State variables
        self.current_state: Tuple[int, ...] = GOAL_STATE
        self.solution_path: List[Tuple[int, ...]] = []
        self.solution_moves: List[str] = []
        self.nodes_expanded = 0
        self.search_time = 0.0
        self.animation_speed = tk.DoubleVar(value=500)  # milliseconds
        self.animation_running = False

        # UI Building
        self.create_widgets()

    def create_widgets(self):
        # Top frame for board and controls
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.grid(row=0, column=0, sticky='nsew')

        # Board frame
        board_frame = ttk.LabelFrame(top_frame, text='Puzzle Board', padding=10)
        board_frame.grid(row=0, column=0, rowspan=2, padx=(0, 10))

        self.cells = []
        for r in range(N):
            for c in range(N):
                lbl = tk.Label(board_frame, text='', width=4, height=2,
                               font=('Helvetica', 24), relief='ridge', bg='white')
                lbl.grid(row=r, column=c, padx=3, pady=3)
                self.cells.append(lbl)

        # Input frame
        input_frame = ttk.LabelFrame(top_frame, text='Input / Controls', padding=10)
        input_frame.grid(row=0, column=1, sticky='nw')

        ttk.Label(input_frame, text='Enter 9 numbers (0-8), 0=blank:').grid(row=0, column=0, columnspan=3, sticky='w')
        self.entry_vars = [tk.StringVar() for _ in range(9)]
        for i in range(9):
            e = ttk.Entry(input_frame, width=3, textvariable=self.entry_vars[i], justify='center', font=('Helvetica', 12))
            e.grid(row=1 + i // 3, column=i % 3, padx=2, pady=2)

        # Buttons for samples
        samples_frame = ttk.Frame(input_frame)
        samples_frame.grid(row=5, column=0, columnspan=3, pady=(8, 0))
        ttk.Button(samples_frame, text='Easy', command=lambda: self.load_sample('easy')).grid(row=0, column=0, padx=3)
        ttk.Button(samples_frame, text='Medium', command=lambda: self.load_sample('medium')).grid(row=0, column=1, padx=3)
        ttk.Button(samples_frame, text='Hard', command=lambda: self.load_sample('hard')).grid(row=0, column=2, padx=3)
        ttk.Button(samples_frame, text='Unsolvable', command=lambda: self.load_sample('unsolvable')).grid(row=0, column=3, padx=3)

        # Action buttons
        actions_frame = ttk.Frame(input_frame)
        actions_frame.grid(row=6, column=0, columnspan=3, pady=(8, 0))
        self.solve_btn = ttk.Button(actions_frame, text='Solve', command=self.solve_puzzle)
        self.solve_btn.grid(row=0, column=0, padx=3)
        self.animate_btn = ttk.Button(actions_frame, text='Animate Solution', command=self.start_animation)
        self.animate_btn.grid(row=0, column=1, padx=3)
        ttk.Button(actions_frame, text='Step Forward', command=self.step_forward).grid(row=0, column=2, padx=3)
        ttk.Button(actions_frame, text='Reset', command=self.reset_puzzle).grid(row=0, column=3, padx=3)
        ttk.Button(actions_frame, text='Clear', command=self.clear_board).grid(row=0, column=4, padx=3)

        ttk.Label(input_frame, text='Animation speed (ms):').grid(row=7, column=0, columnspan=2, sticky='w', pady=(6, 0))
        ttk.Scale(input_frame, from_=100, to=1000, variable=self.animation_speed, orient='horizontal').grid(row=7, column=2, columnspan=1, sticky='we')

        # Results frame
        results_frame = ttk.LabelFrame(top_frame, text='Results / Statistics', padding=10)
        results_frame.grid(row=1, column=1, sticky='nsew')

        self.result_text = tk.Text(results_frame, width=40, height=12, wrap='word', font=('Consolas', 10))
        self.result_text.grid(row=0, column=0)
        self.result_text.insert('end', 'Algorithm: A* Search\nHeuristic: Manhattan Distance\n')
        self.result_text.config(state='disabled')

        # Status bar
        self.status_var = tk.StringVar(value='Ready')
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief='sunken', anchor='w')
        status_bar.grid(row=2, column=0, sticky='we')

        # Initialize board to goal
        self.set_state(GOAL_STATE)

    # ----------------- UI helpers -----------------
    def set_state(self, state: Tuple[int, ...]):
        """Set the current state and update UI fields and board display."""
        self.current_state = tuple(state)
        for i, val in enumerate(self.current_state):
            txt = ' ' if val == 0 else str(val)
            lbl = self.cells[i]
            lbl.config(text=txt)
            # highlight blank differently
            if val == 0:
                lbl.config(bg='#ffdede')
            else:
                lbl.config(bg='white')

        # Update entry widgets
        for i, var in enumerate(self.entry_vars):
            var.set(str(self.current_state[i]))

    def update_board_ui(self, state: Tuple[int, ...]):
        """Update only the visual board (used during animation)."""
        for i, val in enumerate(state):
            txt = ' ' if val == 0 else str(val)
            lbl = self.cells[i]
            lbl.config(text=txt)
            if val == 0:
                lbl.config(bg='#ffdede')
            else:
                lbl.config(bg='white')

    # ----------------- Input / validation -----------------
    def read_input_state(self) -> Optional[Tuple[int, ...]]:
        """Read the 9 entry boxes and return a state tuple or None if invalid."""
        try:
            nums = [int(var.get()) for var in self.entry_vars]
        except ValueError:
            messagebox.showerror('Invalid input', 'Please enter integers only (0-8).')
            return None

        if not self.validate_state(nums):
            return None

        return tuple(nums)

    def validate_state(self, nums: List[int]) -> bool:
        """Validate that nums contains integers 0..8 exactly once."""
        if len(nums) != 9:
            messagebox.showerror('Invalid input', 'Please enter exactly 9 numbers.')
            return False
        if any(n < 0 or n > 8 for n in nums):
            messagebox.showerror('Invalid input', 'Numbers must be between 0 and 8.')
            return False
        if sorted(nums) != list(range(9)):
            messagebox.showerror('Invalid input', 'Numbers must include each of 0..8 exactly once.')
            return False
        return True

    # ----------------- Sample puzzles -----------------
    def load_sample(self, name: str):
        samples = {
            'easy': (1,2,3,4,5,6,7,0,8),
            'medium': (1,2,3,4,0,6,7,5,8),
            'hard': (8,6,7,2,5,4,3,0,1),
            'unsolvable': (1,2,3,4,5,6,8,7,0)
        }
        state = samples.get(name, GOAL_STATE)
        self.set_state(state)
        self.status_var.set(f'Loaded sample: {name}')

    # ----------------- Solvability -----------------
    def count_inversions(self, state: Tuple[int, ...]) -> int:
        arr = [x for x in state if x != 0]
        inv = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i] > arr[j]:
                    inv += 1
        return inv

    def is_solvable(self, state: Tuple[int, ...]) -> bool:
        """For 3x3 puzzle, solvable if inversion count is even."""
        return self.count_inversions(state) % 2 == 0

    # ----------------- Heuristic and neighbors -----------------
    def manhattan_distance(self, state: Tuple[int, ...]) -> int:
        dist = 0
        for i, val in enumerate(state):
            if val == 0:
                continue
            target = val - 1
            r1, c1 = divmod(i, N)
            r2, c2 = divmod(target, N)
            dist += abs(r1 - r2) + abs(c1 - c2)
        return dist

    def get_neighbors(self, state: Tuple[int, ...]) -> List[Tuple[Tuple[int, ...], str]]:
        neighbors = []
        zero = state.index(0)
        r, c = divmod(zero, N)
        moves = [(-1,0,'Up'), (1,0,'Down'), (0,-1,'Left'), (0,1,'Right')]
        for dr, dc, action in moves:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                ni = nr * N + nc
                new_state = list(state)
                new_state[zero], new_state[ni] = new_state[ni], new_state[zero]
                neighbors.append((tuple(new_state), action))
        return neighbors

    # ----------------- A* Search -----------------
    def a_star_search(self, start: Tuple[int, ...]) -> Optional[Dict]:
        """Return dict with path, moves, nodes_expanded, time if solution found, otherwise None."""
        if start == GOAL_STATE:
            return {
                'path': [start],
                'moves': [],
                'nodes_expanded': 0,
                'time': 0.0
            }

        open_heap = []  # (f, g, counter, state)
        counter = 0
        g_scores = {start: 0}
        f_start = self.manhattan_distance(start)
        heapq.heappush(open_heap, (f_start, 0, counter, start))

        came_from: Dict[Tuple[int, ...], Tuple[Optional[Tuple[int, ...]], Optional[str]]] = {}
        closed = set()
        nodes_expanded = 0

        t0 = time.time()
        while open_heap:
            f, g, _, current = heapq.heappop(open_heap)
            if current in closed:
                continue
            if current == GOAL_STATE:
                elapsed = time.time() - t0
                path, moves = self.reconstruct_path(came_from, current)
                return {
                    'path': path,
                    'moves': moves,
                    'nodes_expanded': nodes_expanded,
                    'time': elapsed
                }

            closed.add(current)
            nodes_expanded += 1

            for neighbor, action in self.get_neighbors(current):
                tentative_g = g + 1
                if neighbor in closed:
                    continue
                if tentative_g < g_scores.get(neighbor, float('inf')):
                    came_from[neighbor] = (current, action)
                    g_scores[neighbor] = tentative_g
                    f_score = tentative_g + self.manhattan_distance(neighbor)
                    counter += 1
                    heapq.heappush(open_heap, (f_score, tentative_g, counter, neighbor))

        return None

    def reconstruct_path(self, came_from: Dict[Tuple[int, ...], Tuple[Optional[Tuple[int, ...]], Optional[str]]],
                         current: Tuple[int, ...]) -> Tuple[List[Tuple[int, ...]], List[str]]:
        path = [current]
        moves = []
        while True:
            parent, action = came_from.get(current, (None, None))
            if parent is None:
                break
            moves.append(action if action else '')
            current = parent
            path.append(current)
        path.reverse()
        moves.reverse()
        return path, moves

    # ----------------- Solve / UI glue -----------------
    def solve_puzzle(self):
        state = self.read_input_state()
        if state is None:
            return

        self.set_state(state)

        if not self.is_solvable(state):
            messagebox.showinfo('Unsolvable', 'This puzzle is not solvable.')
            self.status_var.set('Puzzle not solvable')
            self.result_text.config(state='normal')
            self.result_text.delete('1.0', 'end')
            self.result_text.insert('end', 'Algorithm: A* Search\nHeuristic: Manhattan Distance\n')
            self.result_text.insert('end', 'Solution Found: No (unsolvable)\n')
            self.result_text.config(state='disabled')
            return

        # Run A*
        self.status_var.set('Solving...')
        self.root.update_idletasks()
        res = self.a_star_search(state)
        if res is None:
            messagebox.showinfo('No solution', 'No solution found.')
            self.status_var.set('No solution')
            return

        self.solution_path = res['path']
        self.solution_moves = res['moves']
        self.nodes_expanded = res['nodes_expanded']
        self.search_time = res['time']

        # Update results panel
        self.display_results()
        self.status_var.set('Solved')

    def display_results(self):
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', 'Algorithm: A* Search\n')
        self.result_text.insert('end', 'Heuristic: Manhattan Distance\n')
        self.result_text.insert('end', f'Initial State: {self.solution_path[0]}\n')
        self.result_text.insert('end', f'Goal State: {GOAL_STATE}\n')
        self.result_text.insert('end', f'Solution Found: Yes\n')
        self.result_text.insert('end', f'Total Moves: {len(self.solution_moves)}\n')
        self.result_text.insert('end', f'Nodes Expanded: {self.nodes_expanded}\n')
        self.result_text.insert('end', f'Time Taken: {self.search_time:.6f} seconds\n')
        self.result_text.insert('end', f'Path Cost: {len(self.solution_moves)}\n')
        self.result_text.config(state='disabled')

    # ----------------- Animation -----------------
    def start_animation(self):
        if not self.solution_path:
            messagebox.showinfo('No solution', 'Please solve the puzzle first.')
            return
        if self.animation_running:
            return
        self.animation_running = True
        self.solve_btn.config(state='disabled')
        self.animate_btn.config(state='disabled')
        self._animate_index = 0
        self._animate_step()

    def _animate_step(self):
        if not self.animation_running:
            return
        if self._animate_index >= len(self.solution_path):
            self.animation_running = False
            self.solve_btn.config(state='normal')
            self.animate_btn.config(state='normal')
            self.status_var.set('Animation finished')
            return

        state = self.solution_path[self._animate_index]
        self.update_board_ui(state)
        # update status and result area with step info
        step_info = f'Step: {self._animate_index} / {len(self.solution_path)-1}\n'
        if self._animate_index > 0:
            move = self.solution_moves[self._animate_index-1]
            step_info += f'Move: {move}\n'
        else:
            step_info += 'Move: -\n'
        self.status_var.set(step_info.strip())

        self._animate_index += 1
        ms = int(self.animation_speed.get())
        self.root.after(ms, self._animate_step)

    def step_forward(self):
        if not self.solution_path:
            messagebox.showinfo('No solution', 'Please solve the puzzle first.')
            return
        if not hasattr(self, '_step_index'):
            self._step_index = 0
        if self._step_index >= len(self.solution_path):
            self._step_index = 0
        state = self.solution_path[self._step_index]
        self.update_board_ui(state)
        self.status_var.set(f'Step {self._step_index} / {len(self.solution_path)-1}')
        self._step_index += 1

    # ----------------- Reset / Clear -----------------
    def reset_puzzle(self):
        self.set_state(GOAL_STATE)
        self.result_text.config(state='normal')
        self.result_text.delete('1.0', 'end')
        self.result_text.insert('end', 'Algorithm: A* Search\nHeuristic: Manhattan Distance\n')
        self.result_text.config(state='disabled')
        self.solution_path = []
        self.solution_moves = []
        self.status_var.set('Reset to goal state')

    def clear_board(self):
        for var in self.entry_vars:
            var.set('')
        for lbl in self.cells:
            lbl.config(text='', bg='white')
        self.status_var.set('Cleared')


def main():
    root = tk.Tk()
    app = EightPuzzleSolverUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()


