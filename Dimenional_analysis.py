import tkinter as tk
from sympy import symbols, sympify

DIM_M, DIM_L, DIM_T, DIM_I, DIM_Th, DIM_N, DIM_Iv = symbols(
    'DIM_M DIM_L DIM_T DIM_I DIM_Th DIM_N DIM_Iv'
)

unit_map = {
    'kg':  DIM_M,
    'mol': DIM_N,
    'cd':  DIM_Iv,
    'm':   DIM_L,
    's':   DIM_T,
    'A':   DIM_I,
    'K':   DIM_Th,
}

dim_labels = {
    DIM_M:  'M',
    DIM_L:  'L',
    DIM_T:  'T',
    DIM_I:  'I',
    DIM_Th: 'Θ',
    DIM_N:  'N',
    DIM_Iv: 'J',
}

def format_output(expr):
    powers = expr.as_powers_dict()
    parts = []
    for dim in [DIM_M, DIM_L, DIM_T, DIM_I, DIM_Th, DIM_N, DIM_Iv]:
        power = powers.get(dim, 0)
        if power != 0:
            parts.append(f"{dim_labels[dim]}^{power}")
    return "[" + "  ".join(parts) + "]" if parts else "[Dimensionless]"


def get_dimensions():
    raw = entry.get().strip()
    if not raw:
        output_label.config(text="Enter a formula first!", fg='gray')
        return
    try:
        expr_str = raw.replace('^', '**')

        for unit in sorted(unit_map.keys(), key=len, reverse=True):
            expr_str = expr_str.replace(unit, str(unit_map[unit]))

        local_syms = {str(s): s for s in unit_map.values()}
        result = sympify(expr_str, locals=local_syms)

        output_label.config(
            text=f"{format_output(result)}",
            fg='#1D3557'
        )

    except Exception as e:
        output_label.config(text=f"Invalid expression ({e})", fg='#E63946')

def clear_input():
    entry.delete(0, tk.END)
    output_label.config(text="Dimensions will appear here", fg='#1D3557')

def on_enter(e):
    e.widget.config(bg="#5A8FB1")

def on_leave(e):
    e.widget.config(bg="#457B9D")
    
window = tk.Tk()
window.title("Dimensional Analysis")
window.geometry("520x260")
window.config(bg='#C1D7C9')

title = tk.Label(
    window,
    text="Dimensional Analysis Claculator",
    bg='#C1D7C9',
    fg='#1D3557',
    font=("Helvetica", 26, "bold")
)
title.pack(pady=20)
frame = tk.Frame(window, bg='#C1D7C9')
frame.pack(pady=10)

tk.Label(
    frame,
    text="Use units: kg, m, s, A, K, mol, cd   with operators *  /  **",
    bg='#C1D7C9',
    fg='#457B9D',
    font=("Helvetica", 14)
).pack()

tk.Label(
    frame,
    text="Example:  kg*m/s**2      A**2*s**4/(kg*m**2)      mol/s",
    bg='#C1D7C9',
    fg='#555',
    font=("Helvetica", 13, "italic")
).pack(pady=(5, 15))

entry = tk.Entry(
    frame,
    width=50,
    font=("Helvetica", 18),
    relief=tk.FLAT,
    bd=5,
    justify='center'
)
entry.pack(ipady=8)
entry.focus_set()
entry.bind("<Return>", lambda _: get_dimensions())

btn_frame = tk.Frame(frame, bg='#C1D7C9')
btn_frame.pack(pady=15)

find_btn = tk.Button(
    btn_frame,
    text="Find Dimensions",
    command=get_dimensions,
    bg='#457B9D',
    fg='white',
    font=("Helvetica", 14, "bold"),
    relief=tk.FLAT,
    padx=20,
    pady=8,
    cursor="hand2"
)
find_btn.grid(row=0, column=0, padx=10)

find_btn.bind("<Enter>", on_enter)
find_btn.bind("<Leave>", on_leave)

clear_btn = tk.Button(
    btn_frame,
    text="Clear",
    command=clear_input,
    bg='#E63946',
    fg='white',
    font=("Helvetica", 14, "bold"),
    relief=tk.FLAT,
    padx=20,
    pady=8,
    cursor="hand2"
)
clear_btn.grid(row=0, column=1, padx=10)

output_label = tk.Label(
    window,
    text="Dimensions will appear here",
    bg='#C1D7C9',
    fg='#1D3557',
    font=("Courier", 22, "bold")
)
output_label.pack(pady=20)

window.mainloop()
