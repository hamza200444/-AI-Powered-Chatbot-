"""Graphical (Tkinter) interface for the university chatbot."""

import tkinter as tk
from datetime import datetime
from tkinter import Canvas, Frame, Scrollbar, messagebox

from chatbot.main.model import load_intents, prepare_data, train_model
from chatbot.main.response import get_bot_response
from speech_output import speak

# ── Theme ─────────────────────────────────────────────────────────────────────
COLORS = {
    "bg": "#f0f4f8",
    "header": "#1e3a5f",
    "header_sub": "#94a3b8",
    "user_bubble": "#2563eb",
    "user_text": "#ffffff",
    "bot_bubble": "#ffffff",
    "bot_text": "#1e293b",
    "bot_border": "#e2e8f0",
    "input_bg": "#ffffff",
    "input_border": "#cbd5e1",
    "accent": "#2563eb",
    "accent_hover": "#1d4ed8",
    "chip_bg": "#e0e7ff",
    "chip_fg": "#1e40af",
    "chip_hover": "#c7d2fe",
    "status": "#64748b",
    "typing": "#94a3b8",
    "scrollbar": "#cbd5e1",
}

FONT = "Segoe UI"
QUICK_TOPICS = [
    "Admission process",
    "Fee structure",
    "Scholarships",
    "Courses offered",
    "Hostel facility",
    "Library info",
    "Exam schedule",
    "Contact details",
]

# ── Load model once ───────────────────────────────────────────────────────────
_intents = load_intents()
_corpus, _labels, _responses = prepare_data(_intents)
_classifier, _vectorizer = train_model(_corpus, _labels)

_is_typing = False
_typing_frame = None


def _timestamp():
    return datetime.now().strftime("%H:%M")


def _scroll_to_bottom():
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1.0)


def _on_mousewheel(event):
    chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


def add_bubble(text, is_user=False):
    """Insert a styled chat bubble (user = right/blue, bot = left/white)."""
    row = Frame(chat_frame, bg=COLORS["bg"])
    row.pack(fill="x", padx=12, pady=4)

    inner = Frame(row, bg=COLORS["bg"])
    inner.pack(anchor="e" if is_user else "w")

    if is_user:
        bubble = Frame(inner, bg=COLORS["user_bubble"], padx=14, pady=10)
        bubble.pack(anchor="e")
        tk.Label(
            bubble,
            text=text,
            bg=COLORS["user_bubble"],
            fg=COLORS["user_text"],
            font=(FONT, 11),
            wraplength=340,
            justify="left",
        ).pack(anchor="w")
        tk.Label(
            row,
            text=f"You  ·  {_timestamp()}",
            bg=COLORS["bg"],
            fg=COLORS["status"],
            font=(FONT, 8),
        ).pack(anchor="e", padx=4)
    else:
        bubble = Frame(
            inner,
            bg=COLORS["bot_bubble"],
            highlightbackground=COLORS["bot_border"],
            highlightthickness=1,
            padx=14,
            pady=10,
        )
        bubble.pack(anchor="w")
        tk.Label(
            bubble,
            text=text,
            bg=COLORS["bot_bubble"],
            fg=COLORS["bot_text"],
            font=(FONT, 11),
            wraplength=340,
            justify="left",
        ).pack(anchor="w")
        tk.Label(
            row,
            text=f"University Assistant  ·  {_timestamp()}",
            bg=COLORS["bg"],
            fg=COLORS["status"],
            font=(FONT, 8),
        ).pack(anchor="w", padx=4)


def show_typing():
    global _typing_frame
    hide_typing()
    row = Frame(chat_frame, bg=COLORS["bg"])
    row.pack(fill="x", padx=12, pady=4)
    _typing_frame = row
    bubble = Frame(
        row,
        bg=COLORS["bot_bubble"],
        highlightbackground=COLORS["bot_border"],
        highlightthickness=1,
        padx=14,
        pady=8,
    )
    bubble.pack(anchor="w")
    tk.Label(
        bubble,
        text="● ● ●",
        bg=COLORS["bot_bubble"],
        fg=COLORS["typing"],
        font=(FONT, 10),
    ).pack()
    _scroll_to_bottom()


def hide_typing():
    global _typing_frame
    if _typing_frame and _typing_frame.winfo_exists():
        _typing_frame.destroy()
    _typing_frame = None


def set_status(msg):
    status_label.config(text=msg)


def send_message(text=None):
    global _is_typing
    if _is_typing:
        return

    user_input = (text if text is not None else user_entry.get()).strip()
    if not user_input:
        return

    user_entry.delete(0, tk.END)
    add_bubble(user_input, is_user=True)
    _scroll_to_bottom()

    _is_typing = True
    send_btn.config(state="disabled", bg=COLORS["status"])
    set_status("Thinking...")
    show_typing()
    root.update()

    def deliver():
        global _is_typing
        hide_typing()
        try:
            reply = get_bot_response(user_input, _classifier, _vectorizer, _responses)
        except Exception as exc:
            reply = f"Sorry, something went wrong: {exc}"
        add_bubble(reply, is_user=False)
        _scroll_to_bottom()
        set_status("Ready — ask about admissions, fees, courses, and more")
        try:
            speak(reply, verbose=False)
        except Exception:
            pass
        _is_typing = False
        send_btn.config(state="normal", bg=COLORS["accent"])
        user_entry.focus_set()

    root.after(450, deliver)


def clear_chat():
    if messagebox.askyesno("Clear chat", "Remove all messages?"):
        for widget in chat_frame.winfo_children():
            widget.destroy()
        add_bubble(
            "Chat cleared. How can I help you today?",
            is_user=False,
        )
        set_status("Chat cleared")


def on_enter(event):
    send_message()
    return "break"


# ── Window ────────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("University Assistant — ML Chatbot")
root.geometry("480x720")
root.minsize(420, 600)
root.configure(bg=COLORS["bg"])

# Header
header = Frame(root, bg=COLORS["header"], height=72)
header.pack(fill="x")
header.pack_propagate(False)

header_inner = Frame(header, bg=COLORS["header"])
header_inner.pack(fill="both", expand=True, padx=16, pady=12)

tk.Label(
    header_inner,
    text="🎓 University Assistant",
    bg=COLORS["header"],
    fg="white",
    font=(FONT, 16, "bold"),
).pack(anchor="w")

tk.Label(
    header_inner,
    text="ML Chatbot · Admissions · Fees · Courses · Campus",
    bg=COLORS["header"],
    fg=COLORS["header_sub"],
    font=(FONT, 9),
).pack(anchor="w", pady=(2, 0))

clear_btn = tk.Button(
    header,
    text="Clear",
    command=clear_chat,
    bg="#334155",
    fg="white",
    font=(FONT, 9),
    relief="flat",
    padx=10,
    pady=2,
    cursor="hand2",
    activebackground="#475569",
    activeforeground="white",
)
clear_btn.place(relx=1.0, rely=0.5, anchor="e", x=-14)

# Chat area
chat_outer = Frame(root, bg=COLORS["bg"])
chat_outer.pack(fill="both", expand=True, padx=0, pady=0)

chat_canvas = Canvas(chat_outer, bg=COLORS["bg"], highlightthickness=0, bd=0)
scrollbar = Scrollbar(
    chat_outer,
    orient="vertical",
    command=chat_canvas.yview,
    bg=COLORS["bg"],
    troughcolor=COLORS["bg"],
    activebackground=COLORS["scrollbar"],
)
chat_frame = Frame(chat_canvas, bg=COLORS["bg"])

chat_frame.bind(
    "<Configure>",
    lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")),
)
chat_window = chat_canvas.create_window((0, 0), window=chat_frame, anchor="nw")

def _resize_chat(event):
    chat_canvas.itemconfig(chat_window, width=event.width)

chat_canvas.bind("<Configure>", _resize_chat)
chat_canvas.configure(yscrollcommand=scrollbar.set)
chat_canvas.pack(side="left", fill="both", expand=True, padx=(8, 0), pady=8)
scrollbar.pack(side="right", fill="y", pady=8)

chat_canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Quick topics
quick_frame = Frame(root, bg=COLORS["bg"])
quick_frame.pack(fill="x", padx=10, pady=(0, 4))

tk.Label(
    quick_frame,
    text="Quick questions:",
    bg=COLORS["bg"],
    fg=COLORS["status"],
    font=(FONT, 9),
).pack(anchor="w", padx=4, pady=(0, 4))

chips_row = Frame(quick_frame, bg=COLORS["bg"])
chips_row.pack(fill="x")

for topic in QUICK_TOPICS:
    chip = tk.Button(
        chips_row,
        text=topic,
        command=lambda t=topic: send_message(t),
        bg=COLORS["chip_bg"],
        fg=COLORS["chip_fg"],
        font=(FONT, 8),
        relief="flat",
        padx=8,
        pady=4,
        cursor="hand2",
        activebackground=COLORS["chip_hover"],
        activeforeground=COLORS["chip_fg"],
    )
    chip.pack(side="left", padx=3, pady=2)

# Input area
input_outer = Frame(root, bg=COLORS["bg"])
input_outer.pack(fill="x", padx=12, pady=(4, 8))

input_box = Frame(
    input_outer,
    bg=COLORS["input_bg"],
    highlightbackground=COLORS["input_border"],
    highlightthickness=1,
)
input_box.pack(fill="x", side="left", expand=True)

user_entry = tk.Entry(
    input_box,
    font=(FONT, 12),
    bg=COLORS["input_bg"],
    fg=COLORS["bot_text"],
    relief="flat",
    insertbackground=COLORS["accent"],
)
user_entry.pack(fill="x", padx=12, pady=10)
user_entry.bind("<Return>", on_enter)

send_btn = tk.Button(
    input_outer,
    text="Send ➤",
    command=send_message,
    bg=COLORS["accent"],
    fg="white",
    font=(FONT, 11, "bold"),
    relief="flat",
    padx=16,
    pady=10,
    cursor="hand2",
    activebackground=COLORS["accent_hover"],
    activeforeground="white",
)
send_btn.pack(side="right", padx=(8, 0))

# Status bar
status_label = tk.Label(
    root,
    text="Ready — type a message or tap a quick question",
    bg=COLORS["bg"],
    fg=COLORS["status"],
    font=(FONT, 8),
)
status_label.pack(pady=(0, 8))

# Welcome message
add_bubble(
    "Hello! I'm your University Assistant.\n\n"
    "I can help with admissions, fees, scholarships, courses, hostel, "
    "library, exams, and contact information.\n\n"
    "Type below or use the quick buttons!",
    is_user=False,
)

user_entry.focus_set()

if __name__ == "__main__":
    root.mainloop()
