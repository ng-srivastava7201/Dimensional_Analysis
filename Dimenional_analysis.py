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
        output_label.config(text="Dimensions:  (enter something first)", fg='gray')
        return
    try:
        expr_str = raw
        expr_str = expr_str.replace('^', '**')

        for unit in sorted(unit_map.keys(), key=len, reverse=True):
            sym_name = str(unit_map[unit])         
            expr_str = expr_str.replace(unit, sym_name)

        local_syms = {str(s): s for s in unit_map.values()}
        result = sympify(expr_str, locals=local_syms)

        output_label.config(text=f"Dimensions:  {format_output(result)}", fg='#1D3557')

    except Exception as e:
        output_label.config(text=f"Invalid expression  ({e})", fg='#E63946')


window = tk.Tk()
window.title("Dimensional Analysis")
window.geometry("520x260")
window.config(bg='#C1D7C9')

tk.Label(window, text="Dimensional Analysis", bg='#C1D7C9', fg='#1D3557', font=("Helvetica", 15, "bold")).pack(pady=(14, 4))

tk.Label(window, text="Enter formula using:  kg  m  s  A  K  mol  cd   and  *  /  **", bg='#C1D7C9', fg='#457B9D', font=("Helvetica", 9)).pack()

tk.Label(window, text="e.g.   kg*m/s**2     A**2*s**4/(kg*m**2)     mol/s", bg='#C1D7C9', fg='#555', font=("Helvetica", 9, "italic")).pack(pady=(2, 8))

entry = tk.Entry(window, width=38, font=("Helvetica", 12), relief=tk.SOLID, bd=1)
entry.pack(ipady=4)
entry.focus_set()
entry.bind("<Return>", lambda _: get_dimensions())

tk.Button(window, text="Find Dimensions", command=get_dimensions,  bg='#457B9D', fg='white', font=("Helvetica", 11, "bold"),  relief=tk.FLAT, padx=12, pady=4, cursor="hand2").pack(pady=10)

output_label = tk.Label(window, text="Dimensions:", bg='#C1D7C9',    fg='#1D3557', font=("Courier", 13))
output_label.pack()

window.mainloop()