import pygame
import sys
import math
import asyncio
import os

# ---- Fonts ---------
FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

# ── Constants ────────────────────────────────────────────────────────────────
WINDOW_W, WINDOW_H = 1200, 820
FPS = 60

THEMES = {
    "light": {
        "BG":           (245, 247, 250),
        "SIDEBAR_BG":   (225, 230, 240),
        "CARD_BG":      (255, 255, 255),
        "CARD_BORDER":  (150, 160, 180),
        "CARD_GIVEN":   (235, 243, 255),
        "SLOT_BG":      (210, 215, 225),
        "SLOT_BORDER":  (150, 160, 180),
        "DIVIDER":      (150, 160, 180),
        "TEXT_DARK":    ( 30,  40,  60),
        "TEXT_MID":     ( 90, 100, 120),
        "TEXT_GHOST":   (195, 205, 220),
        "ACCENT":       ( 70, 130, 200),
        "DRAG_COL":     ( 70, 130, 200),
        "BTN_BG":       ( 70, 130, 200),
        "BTN_DISABLED": (180, 190, 205),
        "BTN_TEXT":     (255, 255, 255),
        "INPUT_BG":     (255, 255, 255),
        "INPUT_BORDER": (150, 160, 180),
        "INSTR_BG":     (210, 215, 228),
        "INSTR_TEXT":   ( 40,  50,  70),
        "GREEN":        ( 50, 160,  80),
        "GREEN_BG":     (230, 248, 235),
        "RED":          (200,  60,  60),
        "RED_BG":       (252, 235, 235),
        "ORANGE":       (200, 120,  30),
        "ORANGE_BG":    (255, 243, 225),
        "HIGHLIGHT":    (200, 220, 255),
        "TOGGLE_BG":    (200, 210, 225),
        "TOGGLE_TEXT":  ( 30,  40,  60),
        "WELCOME_BG":   (235, 240, 250),
        "CARD_ROW_BG":  (255, 255, 255),
        "CARD_ROW_HOV": (230, 238, 255),
        "CARD_ROW_BDR": (180, 190, 210),
        "DOT_DONE":     ( 50, 160,  80),
        "DOT_EMPTY":    (200, 210, 225),
    },
    "dark": {
        "BG":           ( 28,  31,  46),
        "SIDEBAR_BG":   ( 36,  40,  58),
        "CARD_BG":      ( 48,  53,  74),
        "CARD_BORDER":  ( 72,  80, 108),
        "CARD_GIVEN":   ( 42,  60,  98),
        "SLOT_BG":      ( 40,  45,  64),
        "SLOT_BORDER":  ( 68,  76, 104),
        "DIVIDER":      ( 60,  67,  92),
        "TEXT_DARK":    (224, 228, 242),
        "TEXT_MID":     (148, 160, 195),
        "TEXT_GHOST":   ( 80,  90, 120),
        "ACCENT":       ( 90, 148, 220),
        "DRAG_COL":     ( 90, 148, 220),
        "BTN_BG":       ( 65, 118, 200),
        "BTN_DISABLED": ( 52,  58,  82),
        "BTN_TEXT":     (224, 228, 242),
        "INPUT_BG":     ( 44,  50,  70),
        "INPUT_BORDER": ( 68,  76, 104),
        "INSTR_BG":     ( 32,  36,  52),
        "INSTR_TEXT":   (180, 192, 222),
        "GREEN":        ( 72, 185, 110),
        "GREEN_BG":     ( 24,  52,  36),
        "RED":          (220,  90,  90),
        "RED_BG":       ( 56,  24,  24),
        "ORANGE":       (210, 148,  55),
        "ORANGE_BG":    ( 54,  38,  14),
        "HIGHLIGHT":    ( 44,  76, 140),
        "TOGGLE_BG":    ( 50,  58,  84),
        "TOGGLE_TEXT":  (200, 212, 240),
        "WELCOME_BG":   ( 24,  28,  42),
        "CARD_ROW_BG":  ( 36,  42,  60),
        "CARD_ROW_HOV": ( 48,  58,  88),
        "CARD_ROW_BDR": ( 60,  70,  98),
        "DOT_DONE":     ( 72, 185, 110),
        "DOT_EMPTY":    ( 55,  62,  88),
    },
}

def apply_theme(name):
    return dict(THEMES[name])

T = apply_theme("light")
def c(key): return T[key]

# Cancellation highlight colours (shared across themes)
CANCEL_COLORS = [
    (220,  80,  80), (80, 160,  80), (200, 130,  30),
    (130,  80, 200), ( 30, 170, 180), (200,  80, 160),
]

SIDEBAR_W  = 180
CHAIN_COLS = 5
COL_W      = 160
COL_H      = 180
CHAIN_TOP  = 230
CARD_W     = 80
CARD_H     = 40
SLOT_W     = 144
SLOT_H     = 64
COL_GAP    = 40
INSTR_H    = 52
ANS_TOP    = CHAIN_TOP + COL_H + 70
ANS_NUM_W  = 150
ANS_UNIT_W = 110
ANS_H      = 44
CHAIN_LEFT = SIDEBAR_W + 50


# ── Demo problem bank — one problem per problem type ──────────────────────────
#
# Types covered:
#   1. Unit Conversions          250 mg → g
#   2. Med Dosing – Single-step  500 mg order, 250 mg/tablet
#   3. Med Dosing – Multi-step   1 g order, 500 mg/capsule (g→mg→capsules)
#   4. Wt-Based – Single-step    5 mg/kg, 60 kg patient
#   5. Wt-Based – Multi-step     10 mg/kg/day q8h, 30 kg, 100 mg/5 mL
#   6. IV Therapy – Single-step  500 mL over 4 hr → mL/hr
#   7. IV Therapy – Multi-step   120 mL over 1 hr, 20 gtt/mL → gtt/min
#   8. Critical Care             Dopamine 400 mg/250 mL, 4 mcg/kg/min, 50 kg
#
CATEGORIES = [
    {
        "name": "Unit Conversions",
        "tiers": [
            {
                "name": None,
                "problems": [
                    {
                        "text": "Convert  250 mg  to  g",
                        "answer": 0.25,
                        "ans_unit_num": "g", "ans_unit_den": "",
                        "given": "250",
                        "number_cards": ["250", "1", "1000"],
                        "unit_cards":   ["mg", "g"],
                        "rounding": {"rule": "hundredth",
                                     "note": "Round to the nearest hundredth."},
                    },
                ],
            },
        ],
    },
    {
        "name": "Medication Dosing",
        "tiers": [
            {
                "name": "Single-step",
                "problems": [
                    {
                        # Chain: 500 mg/1  ×  1 tablet/250 mg  =  2 tablets
                        "text": "Order: 500 mg.  Supply: 250 mg/tablet.  How many tablets?",
                        "answer": 2,
                        "ans_unit_num": "tablets", "ans_unit_den": "",
                        "given": "500",
                        "number_cards": ["500", "1", "250"],
                        "unit_cards":   ["mg", "tablets"],
                        "rounding": {"rule": "half",
                                     "note": "Round to nearest whole or half tablet."},
                    },
                ],
            },
            {
                "name": "Multi-step",
                "problems": [
                    {
                        # Chain: 1 g/1  ×  1000 mg/1 g  ×  1 capsule/500 mg  =  2 capsules
                        "text": "Order: 1 g.  Supply: 500 mg/capsule.  How many capsules?",
                        "answer": 2,
                        "ans_unit_num": "capsules", "ans_unit_den": "",
                        "given": "1",
                        "number_cards": ["1", "1000", "500", "1"],
                        "unit_cards":   ["g", "mg", "capsules"],
                        "rounding": {"rule": "whole",
                                     "note": "Round to the nearest whole capsule."},
                    },
                ],
            },
        ],
    },
    {
        "name": "Weight-Based Dosing",
        "tiers": [
            {
                "name": "Single-step",
                "problems": [
                    {
                        # Chain: 60 kg/1  ×  5 mg/1 kg  =  300 mg
                        "text": "Order: 5 mg/kg.  Patient: 60 kg.  How many mg?",
                        "answer": 300,
                        "ans_unit_num": "mg", "ans_unit_den": "",
                        "given": "60",
                        "number_cards": ["60", "5", "1"],
                        "unit_cards":   ["kg", "mg"],
                        "rounding": {"rule": "whole",
                                     "note": "Round to the nearest whole mg."},
                    },
                ],
            },
            {
                "name": "Multi-step",
                "problems": [
                    {
                        # Chain: 30 kg/1  ×  10 mg/kg/day  ×  1 day/3 doses
                        #        ×  5 mL/100 mg  =  5 mL
                        "text": ("Order: 10 mg/kg/day every 8 hours.  "
                                 "Patient: 30 kg.  Supply: 100 mg/5 mL.  "
                                 "mL per dose?"),
                        "answer": 5.0,
                        "ans_unit_num": "mL", "ans_unit_den": "",
                        "given": "30",
                        "number_cards": ["30", "10", "3", "5", "100", "1"],
                        "unit_cards":   ["kg", "mg", "day", "doses", "mL"],
                        "rounding": {"rule": "tenth",
                                     "note": "Round to the nearest tenth of a mL."},
                    },
                ],
            },
        ],
    },
    {
        "name": "IV Therapy",
        "tiers": [
            {
                "name": "Single-step",
                "problems": [
                    {
                        # Chain: 500 mL / 4 hr  =  125 mL/hr
                        "text": "Infuse 500 mL over 4 hours.  What is the rate in mL/hr?",
                        "answer": 125,
                        "ans_unit_num": "mL", "ans_unit_den": "hr",
                        "given": "500",
                        "number_cards": ["500", "4", "1"],
                        "unit_cards":   ["mL", "hr"],
                        "rounding": {"rule": "whole",
                                     "note": "Round to the nearest whole mL/hr."},
                    },
                ],
            },
            {
                "name": "Multi-step",
                "problems": [
                    {
                        # Chain: 120 mL/1  ×  1/60 min  ×  20 gtt/mL  =  40 gtt/min
                        # (time conversion collapses: 120 ÷ 60 × 20 = 40)
                        "text": ("Infuse 120 mL over 1 hour.  "
                                 "Drop factor: 20 gtt/mL.  gtt/min?"),
                        "answer": 40,
                        "ans_unit_num": "gtt", "ans_unit_den": "min",
                        "given": "120",
                        "number_cards": ["120", "60", "20", "1"],
                        "unit_cards":   ["mL", "hr", "min", "gtt"],
                        "rounding": {"rule": "whole",
                                     "note": "Round to the nearest whole drop per minute."},
                    },
                ],
            },
        ],
    },
    {
        "name": "Critical Care",
        "tiers": [
            {
                "name": None,
                "problems": [
                    {
                        # Chain: 50 kg/1  ×  4 mcg/kg/min  ×  60 min/1 hr
                        #        ×  1 mg/1000 mcg  ×  250 mL/400 mg  =  7.5 mL/hr
                        "text": ("Dopamine 400 mg/250 mL.  "
                                 "Order: 4 mcg/kg/min.  "
                                 "Patient: 50 kg.  mL/hr?"),
                        "answer": 7.5,
                        "ans_unit_num": "mL", "ans_unit_den": "hr",
                        "given": "50",
                        "number_cards": ["50", "4", "60", "250", "400", "1000", "1"],
                        "unit_cards":   ["kg", "mcg", "min", "hr", "mg", "mL"],
                        "rounding": {"rule": "tenth",
                                     "note": "Round to the nearest tenth of a mL/hr."},
                    },
                ],
            },
        ],
    },
]


# ── Rounding helpers ──────────────────────────────────────────────────────────
ROUND_STEPS = {"whole": 1.0, "half": 0.5, "tenth": 0.1, "hundredth": 0.01}

def round_to_step(value, step):
    return round(round(value / step) * step, 10)

def check_rounding(student_val, correct_val, rule):
    step = ROUND_STEPS.get(rule, 0.01)
    expected_rounded = round_to_step(correct_val, step)
    if abs(student_val - expected_rounded) < step * 0.01:
        return "correct"
    if correct_val != 0 and abs(student_val - correct_val) / abs(correct_val) < 0.05:
        return "rounding"
    return "wrong"


# ── Unit cancellation ─────────────────────────────────────────────────────────
def cancel_units(slots):
    num_units, den_units = [], []
    for col in slots:
        num_units.extend(col[0]["units"])
        den_units.extend(col[1]["units"])
    remaining_num = list(num_units)
    remaining_den = list(den_units)
    cancelled = []
    for u in list(remaining_num):
        if u in remaining_den:
            remaining_num.remove(u)
            remaining_den.remove(u)
            cancelled.append(u)
    return remaining_num, remaining_den, cancelled


def get_cancellation_pairs(slots):
    """Return list of (unit, col_a, half_a, col_b, half_b) for each cancelled pair."""
    pairs = []
    from collections import defaultdict
    positions = defaultdict(list)
    for col_i, col in enumerate(slots):
        for half_i, half in enumerate(col):
            for u in half["units"]:
                positions[u].append((col_i, half_i))

    used = defaultdict(int)
    num_units, den_units = [], []
    for col in slots:
        num_units.extend(col[0]["units"])
        den_units.extend(col[1]["units"])

    remaining_num = list(num_units)
    remaining_den = list(den_units)
    pair_list = []
    color_idx = 0
    for u in list(remaining_num):
        if u in remaining_den:
            remaining_num.remove(u)
            remaining_den.remove(u)
            pair_list.append((u, CANCEL_COLORS[color_idx % len(CANCEL_COLORS)]))
            color_idx += 1
    return pair_list


# ── Layout helpers ────────────────────────────────────────────────────────────
def chain_col_rect(col):
    x = CHAIN_LEFT + col * (COL_W + COL_GAP)
    return pygame.Rect(x, CHAIN_TOP, COL_W, COL_H)

def slot_rect(col, half):
    r = chain_col_rect(col)
    mid_y = r.y + r.h // 2
    sx = r.x + (COL_W - SLOT_W) // 2
    sy = r.y + 6 if half == 0 else mid_y + 6
    return pygame.Rect(sx, sy, SLOT_W, SLOT_H)

def find_font(names, size, bold=False):
    variant = "NotoSans-Bold.ttf" if bold else "NotoSans-Regular.ttf"
    path = os.path.join(FONT_DIR, variant)
    if os.path.exists(path):
        return pygame.font.Font(path, size)
    return pygame.font.Font(None, size)


def unit_expression(units):
    if not units:
        return ""
    return " · ".join(units)


# ── Draw helpers ──────────────────────────────────────────────────────────────
def draw_slot(surface, rect, slot, font, highlight=False, cancel_map=None):
    has_number  = bool(slot["number"])
    has_units   = bool(slot["units"])
    has_content = has_number or has_units

    bg = c("HIGHLIGHT") if highlight else c("INPUT_BG")
    pygame.draw.rect(surface, bg, rect, border_radius=6)
    border_col = c("ACCENT") if has_content else c("SLOT_BORDER")
    border_w   = 2           if has_content else 1
    if highlight:
        border_col = c("ACCENT")
        border_w   = 2
    pygame.draw.rect(surface, border_col, rect, border_w, border_radius=6)

    if has_content:
        parts = []
        if has_number:
            parts.append((slot["number"], c("TEXT_DARK")))
        for u in slot["units"]:
            col_color = c("ACCENT")
            if cancel_map and u in cancel_map:
                col_color = cancel_map[u]
            parts.append((u, col_color))
        if len(slot["units"]) > 1:
            joined = " · ".join(slot["units"])
            unit_col = c("ACCENT")
            if cancel_map:
                cx = rect.centerx
                num_parts = []
                if has_number:
                    num_parts.append((slot["number"], c("TEXT_DARK")))
                for u in slot["units"]:
                    uc = cancel_map.get(u, c("ACCENT")) if cancel_map else c("ACCENT")
                    num_parts.append((u, uc))
                sep = font.render(" · ", True, c("TEXT_MID"))
                total_w = sum(font.size(p[0])[0] for p in num_parts)
                total_w += sep.get_width() * (len(slot["units"]) - 1)
                if has_number:
                    total_w += 8
                cx = rect.centerx - total_w // 2
                for idx, (txt, col_c) in enumerate(num_parts):
                    s = font.render(txt, True, col_c)
                    surface.blit(s, s.get_rect(midleft=(cx, rect.centery)))
                    cx += s.get_width()
                    if idx < len(num_parts) - 1:
                        if idx == 0 and has_number:
                            cx += 8
                        else:
                            surface.blit(sep, sep.get_rect(midleft=(cx, rect.centery)))
                            cx += sep.get_width()
                return
            parts = [(slot["number"], c("TEXT_DARK"))] if has_number else []
            parts.append((joined, unit_col))

        total_w = sum(font.size(p[0])[0] for p in parts) + 8 * (len(parts) - 1)
        cx = rect.centerx - total_w // 2
        for txt, col_c in parts:
            s = font.render(txt, True, col_c)
            surface.blit(s, s.get_rect(midleft=(cx, rect.centery)))
            cx += s.get_width() + 8


def draw_floating_card(surface, text, font, mx, my):
    t = font.render(text, True, c("BTN_TEXT"))
    w = max(t.get_width() + 20, CARD_W)
    r = pygame.Rect(mx - w//2, my - CARD_H//2, w, CARD_H)
    pygame.draw.rect(surface, c("DRAG_COL"), r, border_radius=6)
    surface.blit(t, t.get_rect(center=r.center))

def draw_text_input(surface, rect, text, font, active, ghost=""):
    pygame.draw.rect(surface, c("INPUT_BG"), rect, border_radius=6)
    pygame.draw.rect(surface, c("ACCENT") if active else c("INPUT_BORDER"),
                     rect, 2, border_radius=6)
    display = text if text else ghost
    col     = c("TEXT_DARK") if text else c("TEXT_GHOST")
    t = font.render(display, True, col)
    surface.blit(t, (rect.x + 8, rect.y + (rect.h - t.get_height()) // 2))

def draw_button(surface, rect, label, font, enabled=True, color=None):
    bg = color if color else (c("BTN_BG") if enabled else c("BTN_DISABLED"))
    pygame.draw.rect(surface, bg, rect, border_radius=6)
    t = font.render(label, True, c("BTN_TEXT"))
    surface.blit(t, t.get_rect(center=rect.center))

def draw_feedback_box(surface, rect, text, font, fg, bg):
    pygame.draw.rect(surface, bg,  rect, border_radius=6)
    pygame.draw.rect(surface, fg,  rect, 1, border_radius=6)
    t = font.render(text, True, fg)
    surface.blit(t, t.get_rect(midleft=(rect.x + 12, rect.centery)))


def compute_chain(slots):
    num, den = 1.0, 1.0
    any_n = False
    for col in slots:
        for half_idx, half in enumerate(col):
            if half["number"]:
                try:
                    v = float(half["number"])
                    any_n = True
                    if half_idx == 0: num *= v
                    else:             den *= v
                except ValueError:
                    pass
    if not any_n or den == 0: return None
    return num / den

def sidebar_card_rects(problem):
    cards = []
    for i, u in enumerate(problem["unit_cards"]):
        row, col = divmod(i, 2)
        r = pygame.Rect(10 + col*(CARD_W+6), 58 + row*(CARD_H+8), CARD_W, CARD_H)
        cards.append((u, r, "unit"))
    unit_rows = (len(problem["unit_cards"]) + 1) // 2
    num_label_y = 58 + unit_rows * (CARD_H + 8) + 10
    for i, n in enumerate(problem["number_cards"]):
        row, col = divmod(i, 2)
        r = pygame.Rect(10 + col*(CARD_W+6),
                        num_label_y + 22 + row*(CARD_H+8), CARD_W, CARD_H)
        cards.append((n, r, "number"))
    return cards, num_label_y

def run_check(slots, inputs, problem):
    lines = []
    rule  = problem["rounding"]["rule"]
    step  = ROUND_STEPS.get(rule, 0.01)
    remaining_num, remaining_den, cancelled = cancel_units(slots)
    exp_unit_num = problem["ans_unit_num"].strip().lower()
    exp_unit_den = problem["ans_unit_den"].strip().lower()
    stu_num = [u.lower() for u in remaining_num]
    stu_den = [u.lower() for u in remaining_den]
    units_ok = (sorted(stu_num) == sorted([exp_unit_num] if exp_unit_num else []) and
                sorted(stu_den) == sorted([exp_unit_den] if exp_unit_den else []))
    ans_str      = inputs["ans_num"].strip()
    ans_unit_str = inputs["ans_unit"].strip().lower()
    num_status = "missing"
    if ans_str:
        try:
            student_val = float(ans_str)
            num_status  = check_rounding(student_val, problem["answer"], rule)
        except ValueError:
            num_status = "invalid"
    expected_unit_str = exp_unit_num + ("/" + exp_unit_den if exp_unit_den else "")
    ans_unit_ok = (ans_unit_str == expected_unit_str)
    all_correct = units_ok and num_status == "correct" and ans_unit_ok
    if all_correct:
        lines.append(("Correct!", c("GREEN"), c("GREEN_BG")))
    else:
        if num_status == "correct" and ans_unit_ok and not units_ok:
            lines.append(("Double check your units in the factor chain.", c("RED"), c("RED_BG")))
        elif units_ok and ans_unit_ok and num_status == "wrong":
            lines.append(("Double check your calculations.", c("RED"), c("RED_BG")))
        elif units_ok and ans_unit_ok and num_status == "rounding":
            exp_rounded = round_to_step(problem["answer"], step)
            lines.append((f"Check your rounding — expected {exp_rounded:g}.", c("ORANGE"), c("ORANGE_BG")))
        elif not ans_unit_ok and num_status == "correct":
            lines.append(("Double check your answer unit.", c("RED"), c("RED_BG")))
        else:
            lines.append(("Double check your units and calculations.", c("RED"), c("RED_BG")))
        if num_status == "rounding" and units_ok:
            exp_rounded = round_to_step(problem["answer"], step)
            lines.append((f"Expected: {exp_rounded:g} {expected_unit_str}", c("ORANGE"), c("ORANGE_BG")))
    return lines, all_correct


# ── Intro screen drawing ──────────────────────────────────────────────────────

def wrap_text(text, font, max_width):
    """Word-wrap text into lines fitting max_width."""
    words = text.split()
    lines, current = [], ""
    for w in words:
        test = (current + " " + w).strip()
        if font.size(test)[0] <= max_width:
            current = test
        else:
            if current:
                lines.append(current)
            current = w
    if current:
        lines.append(current)
    return lines


def draw_intro_shell(surface, fonts, theme_name, step, total_steps, title,
                     btn_left=None, btn_mid=None, btn_right=None):
    """Draw the shared chrome for intro screens. Returns button rects."""
    surface.fill(c("WELCOME_BG"))
    W, H = surface.get_size()

    dot_y = 28
    total_w = total_steps * 20 - 8
    dot_x0 = W // 2 - total_w // 2
    for i in range(total_steps):
        col = c("ACCENT") if i == step else c("DOT_EMPTY")
        pygame.draw.circle(surface, col, (dot_x0 + i * 20, dot_y), 6)

    t = fonts["lg"].render(title, True, c("TEXT_DARK"))
    surface.blit(t, t.get_rect(centerx=W // 2, y=50))

    pygame.draw.line(surface, c("DIVIDER"), (80, 92), (W - 80, 92), 1)

    tog_r = pygame.Rect(W - 150, 10, 130, 30)
    pygame.draw.rect(surface, c("TOGGLE_BG"), tog_r, border_radius=6)
    tog_lbl = "Mode: Light" if theme_name == "dark" else "Mode: Dark"
    t = fonts["xs"].render(tog_lbl, True, c("TOGGLE_TEXT"))
    surface.blit(t, t.get_rect(center=tog_r.center))

    btn_h, btn_y = 42, H - 64
    rects = {}

    if btn_left:
        r = pygame.Rect(80, btn_y, 140, btn_h)
        pygame.draw.rect(surface, c("TOGGLE_BG"), r, border_radius=8)
        t = fonts["sm"].render(btn_left, True, c("TEXT_DARK"))
        surface.blit(t, t.get_rect(center=r.center))
        rects["left"] = r

    if btn_mid:
        r = pygame.Rect(W // 2 - 90, btn_y, 180, btn_h)
        pygame.draw.rect(surface, c("TOGGLE_BG"), r, border_radius=8)
        t = fonts["sm"].render(btn_mid, True, c("TEXT_MID"))
        surface.blit(t, t.get_rect(center=r.center))
        rects["mid"] = r

    if btn_right:
        r = pygame.Rect(W - 220, btn_y, 140, btn_h)
        pygame.draw.rect(surface, c("BTN_BG"), r, border_radius=8)
        t = fonts["sm"].render(btn_right, True, c("BTN_TEXT"))
        surface.blit(t, t.get_rect(center=r.center))
        rects["right"] = r

    return rects, tog_r


def draw_intro_title(surface, fonts, theme_name):
    """Screen 0 — Title / landing."""
    W, H = surface.get_size()
    surface.fill(c("WELCOME_BG"))

    tog_r = pygame.Rect(W - 150, 14, 130, 30)
    pygame.draw.rect(surface, c("TOGGLE_BG"), tog_r, border_radius=6)
    t = fonts["xs"].render("Mode: Light" if theme_name == "dark" else "Mode: Dark",
                           True, c("TOGGLE_TEXT"))
    surface.blit(t, t.get_rect(center=tog_r.center))

    t = fonts["lg"].render("Nursing Math", True, c("TEXT_DARK"))
    surface.blit(t, t.get_rect(centerx=W // 2, y=180))
    t = fonts["md"].render("Dimensional Analysis — Demo", True, c("ACCENT"))
    surface.blit(t, t.get_rect(centerx=W // 2, y=222))

    tagline = ("One example of each problem type. "
               "Build the unit-cancellation chain, then check your answer.")
    for i, line in enumerate(wrap_text(tagline, fonts["sm"], 620)):
        t = fonts["sm"].render(line, True, c("TEXT_MID"))
        surface.blit(t, t.get_rect(centerx=W // 2, y=290 + i * 28))

    start_r = pygame.Rect(W // 2 - 160, 400, 150, 50)
    skip_r  = pygame.Rect(W // 2 + 20,  400, 180, 50)

    pygame.draw.rect(surface, c("BTN_BG"),    start_r, border_radius=8)
    pygame.draw.rect(surface, c("TOGGLE_BG"), skip_r,  border_radius=8)

    t = fonts["btn"].render("Learn How", True, c("BTN_TEXT"))
    surface.blit(t, t.get_rect(center=start_r.center))
    t = fonts["sm"].render("Skip to Problems", True, c("TEXT_MID"))
    surface.blit(t, t.get_rect(center=skip_r.center))

    return {"start": start_r, "skip": skip_r, "toggle": tog_r}


def draw_intro_what(surface, fonts, theme_name):
    """Screen 1 — Step 1: Identify relevant information."""
    W, H = surface.get_size()
    rects, tog_r = draw_intro_shell(
        surface, fonts, theme_name, step=0, total_steps=4,
        title="Step 1: Identify Relevant Information",
        btn_left=None, btn_mid="Skip to Problems", btn_right="Next"
    )
    rects["toggle"] = tog_r

    body_x, body_w = 100, W - 200
    y = 108

    t = fonts["sm"].render("Every problem gives you a starting value and a target unit. Find them first.", True, c("TEXT_MID"))
    surface.blit(t, t.get_rect(centerx=W // 2, y=y))
    y += 40

    examples = [
        ("Unit conversion",   "250 mg",                              "g"),
        ("Oral medication",   "Order 500 mg, supply 250 mg/tablet",  "tablets"),
        ("Weight-based dose", "5 mg/kg, patient 60 kg",              "mg"),
        ("IV therapy",        "500 mL over 4 hr",                    "mL/hr"),
    ]

    col_type_x   = body_x
    col_given_x  = body_x + 190
    col_target_x = body_x + 620

    for label, x in [("Problem type", col_type_x), ("Given", col_given_x), ("Target unit", col_target_x)]:
        t = fonts["btn"].render(label, True, c("ACCENT"))
        surface.blit(t, (x, y))
    y += 28
    pygame.draw.line(surface, c("DIVIDER"), (body_x, y), (body_x + body_w, y), 1)
    y += 10

    for prob_type, given, target in examples:
        row_r = pygame.Rect(body_x - 8, y - 4, body_w + 16, 34)
        pygame.draw.rect(surface, c("SLOT_BG"), row_r, border_radius=6)
        t = fonts["sm"].render(prob_type, True, c("TEXT_DARK"))
        surface.blit(t, (col_type_x, y + 6))
        t = fonts["sm"].render(given, True, c("TEXT_MID"))
        surface.blit(t, (col_given_x, y + 6))
        t = fonts["btn"].render(target, True, c("ACCENT"))
        surface.blit(t, (col_target_x, y + 6))
        y += 42

    return rects


def draw_intro_notation(surface, fonts, theme_name):
    """Screen 2 — Step 2: Write information as factors."""
    W, H = surface.get_size()
    rects, tog_r = draw_intro_shell(
        surface, fonts, theme_name, step=1, total_steps=4,
        title="Step 2: Write Information as Factors",
        btn_left="Back", btn_mid="Skip to Problems", btn_right="Next"
    )
    rects["toggle"] = tog_r

    body_x = 100
    y = 108

    t = fonts["sm"].render("Every piece of information becomes a fraction. Every number needs a unit — top or bottom.", True, c("TEXT_MID"))
    surface.blit(t, t.get_rect(centerx=W // 2, y=y))
    y += 50

    frac_w, frac_h = 130, 60
    gap = 40

    def draw_frac(sx, sy, num, den, num_col=None, den_col=None):
        fr = pygame.Rect(sx, sy, frac_w, frac_h)
        pygame.draw.rect(surface, c("SLOT_BG"), fr, border_radius=8)
        pygame.draw.rect(surface, c("SLOT_BORDER"), fr, 1, border_radius=8)
        mid_y = sy + frac_h // 2
        pygame.draw.line(surface, c("DIVIDER"), (sx + 10, mid_y), (sx + frac_w - 10, mid_y), 2)
        t_n = fonts["sm"].render(num, True, num_col or c("ACCENT"))
        t_d = fonts["sm"].render(den, True, den_col or c("TEXT_MID"))
        surface.blit(t_n, t_n.get_rect(centerx=sx + frac_w // 2, centery=sy + frac_h // 4))
        surface.blit(t_d, t_d.get_rect(centerx=sx + frac_w // 2, centery=sy + frac_h * 3 // 4))

    t = fonts["btn"].render("Writing a supply rate as a factor:", True, c("ACCENT"))
    surface.blit(t, (body_x, y))
    y += 32

    ex1_x = body_x + 20
    draw_frac(ex1_x, y, "250 mg", "1 tablet")
    t = fonts["sm"].render('Supply: 250 mg per tablet', True, c("TEXT_MID"))
    surface.blit(t, (ex1_x + frac_w + 20, y + frac_h // 2 - 10))
    y += frac_h + 30

    t = fonts["btn"].render("Flip a factor when you need the unit on the other side:", True, c("ACCENT"))
    surface.blit(t, (body_x, y))
    y += 32

    ex2_x = body_x + 20
    draw_frac(ex2_x, y, "250 mg", "1 tablet")
    t = fonts["md"].render("or", True, c("TEXT_MID"))
    surface.blit(t, t.get_rect(midleft=(ex2_x + frac_w + 14, y + frac_h // 2)))
    draw_frac(ex2_x + frac_w + gap + 30, y, "1 tablet", "250 mg")
    t = fonts["sm"].render("Same relationship — just flipped. Choose whichever makes units cancel.", True, c("TEXT_MID"))
    surface.blit(t, (ex2_x, y + frac_h + 10))
    y += frac_h + 50

    tip_r = pygame.Rect(body_x, y, W - body_x * 2, 44)
    pygame.draw.rect(surface, c("ORANGE_BG"), tip_r, border_radius=8)
    pygame.draw.rect(surface, c("ORANGE"), tip_r, 1, border_radius=8)
    tip = "Tip: A whole number like 500 mg becomes  500 mg / 1  — the denominator is always 1."
    t = fonts["sm"].render(tip, True, c("ORANGE"))
    surface.blit(t, t.get_rect(midleft=(body_x + 16, tip_r.centery)))

    return rects


def draw_intro_chain(surface, fonts, theme_name):
    """Screen 3 — How the chain works (annotated diagram)."""
    W, H = surface.get_size()
    rects, tog_r = draw_intro_shell(
        surface, fonts, theme_name, step=2, total_steps=4,
        title="Step 3: Arrange Factors to Cancel Units",
        btn_left="Back", btn_mid="Skip to Problems", btn_right="Next"
    )
    rects["toggle"] = tog_r

    col_w, col_h, gap = 150, 120, 30
    n_cols = 3
    total_chain_w = n_cols * col_w + (n_cols - 1) * gap
    cx = W // 2 - total_chain_w // 2
    cy = 145

    example_cols = [
        {"num": "250", "num_unit": "mg", "den": "1",    "den_unit": ""},
        {"num": "1",   "num_unit": "g",  "den": "1000", "den_unit": "mg"},
        {"num": "",    "num_unit": "g",  "den": "",     "den_unit": ""},
    ]
    labels = ["Given value", "Conversion factor", "Result unit"]
    annot  = [
        "Start with what you're given\n",
        "Identify the conversion factor: (g to mg).\n",
        "Place mg on bottom to cancel.",
        "mg cancels\nOnly g remains",
    ]

    for i, col in enumerate(example_cols):
        x = cx + i * (col_w + gap)
        col_rect = pygame.Rect(x, cy, col_w, col_h)

        pygame.draw.rect(surface, c("SLOT_BG"), col_rect, border_radius=8)
        pygame.draw.rect(surface, c("SLOT_BORDER"), col_rect, 1, border_radius=8)

        mid_y = cy + col_h // 2

        num_str = (col["num"] + "  " + col["num_unit"]).strip()
        t = fonts["sm"].render(num_str, True, c("ACCENT"))
        surface.blit(t, t.get_rect(centerx=x + col_w // 2, centery=cy + col_h // 4))

        pygame.draw.line(surface, c("DIVIDER"), (x + 10, mid_y), (x + col_w - 10, mid_y), 2)

        den_str = (col["den"] + "  " + col["den_unit"]).strip()
        if den_str:
            col_c = c("RED") if col["den_unit"] == "mg" else c("TEXT_MID")
            t = fonts["sm"].render(den_str, True, col_c)
            surface.blit(t, t.get_rect(centerx=x + col_w // 2, centery=cy + col_h * 3 // 4))

        if i < n_cols - 1:
            sep = "×" if i < n_cols - 2 else "="
            t = fonts["md"].render(sep, True, c("TEXT_MID"))
            surface.blit(t, t.get_rect(centerx=x + col_w + gap // 2, centery=cy + col_h // 2))

        t = fonts["xs"].render(labels[i], True, c("TEXT_MID"))
        surface.blit(t, t.get_rect(centerx=x + col_w // 2, y=cy - 20))

        ann_y = cy + col_h + 12
        for line in annot[i].split("\n"):
            t = fonts["xs"].render(line, True, c("TEXT_MID"))
            surface.blit(t, t.get_rect(centerx=x + col_w // 2, y=ann_y))
            ann_y += 18

    cancel_y = cy + col_h + 80
    msg = "The 'mg' in column 1 numerator and column 2 denominator cancel — they divide to 1."
    for line in wrap_text(msg, fonts["sm"], W - 240):
        t = fonts["sm"].render(line, True, c("TEXT_DARK"))
        surface.blit(t, t.get_rect(centerx=W // 2, y=cancel_y))
        cancel_y += 26

    rule_r = pygame.Rect(W // 2 - 280, cancel_y + 10, 560, 64)
    pygame.draw.rect(surface, c("GREEN_BG"), rule_r, border_radius=8)
    pygame.draw.rect(surface, c("GREEN"), rule_r, 1, border_radius=8)
    line1 = "250 mg   ×   1 g / 1000 mg   =   0.25 g"
    line2 = "multiply numerators ÷ multiply denominators"
    t1 = fonts["btn"].render(line1, True, c("GREEN"))
    t2 = fonts["xs"].render(line2, True, c("GREEN"))
    surface.blit(t1, t1.get_rect(centerx=W // 2, centery=rule_r.centery - 10))
    surface.blit(t2, t2.get_rect(centerx=W // 2, centery=rule_r.centery + 16))

    return rects


def draw_intro_example(surface, fonts, theme_name):
    """Screen 4 — Worked example with step-by-step explanation."""
    W, H = surface.get_size()
    rects, tog_r = draw_intro_shell(
        surface, fonts, theme_name, step=3, total_steps=4,
        title="Step 4: Calculate the Result",
        btn_left="Back", btn_mid=None, btn_right="Go to Problems"
    )
    rects["toggle"] = tog_r

    body_x, body_w = 120, W - 240
    y = 110

    prob_bg = pygame.Rect(body_x, y, body_w, 44)
    pygame.draw.rect(surface, c("HIGHLIGHT"), prob_bg, border_radius=8)
    pygame.draw.rect(surface, c("ACCENT"), prob_bg, 1, border_radius=8)
    t = fonts["btn"].render("Problem: Convert 250 mg to g", True, c("ACCENT"))
    surface.blit(t, t.get_rect(midleft=(body_x + 16, prob_bg.centery)))
    y += 62

    steps = [
        ("Step 1 — Write down what you know",
         None,
         [("250 mg", "1", "")],
         "Place 250 in the numerator of column 1, and mg as the unit."),
        ("Step 2 — Identify the conversion factor",
         None,
         [("250 mg", "1", ""), ("1 g", "1000 mg", "")],
         "Place 1 g on top (your target unit) and 1000 mg on the bottom. "
         "The mg units now appear in both a numerator and a denominator."),
        ("Step 3 — Cancel and calculate",
         None,
         [("250 mg", "1", ""), ("1 g", "1000 mg", ""), ("0.25 g", "", "=")],
         "The mg units cancel. Multiply across the top and divide by the bottom. "
         "Your answer is 0.25 g."),
    ]

    frac_w, frac_h = 110, 54
    frac_gap = 28

    for heading, _, fracs, explanation in steps:
        t = fonts["btn"].render(heading, True, c("ACCENT"))
        surface.blit(t, (body_x, y))
        y += 30

        fx = body_x + 16
        for fi, (num, den, prefix) in enumerate(fracs):
            if prefix:
                t = fonts["md"].render(prefix, True, c("TEXT_MID"))
                surface.blit(t, t.get_rect(midleft=(fx, y + frac_h // 2)))
                fx += t.get_width() + 8
            fr = pygame.Rect(fx, y, frac_w, frac_h)
            pygame.draw.rect(surface, c("SLOT_BG"), fr, border_radius=6)
            pygame.draw.rect(surface, c("SLOT_BORDER"), fr, 1, border_radius=6)
            mid_y = y + frac_h // 2
            t_num = fonts["sm"].render(num, True, c("ACCENT"))
            surface.blit(t_num, t_num.get_rect(centerx=fx + frac_w // 2, centery=y + frac_h // 4))
            pygame.draw.line(surface, c("DIVIDER"), (fx + 8, mid_y), (fx + frac_w - 8, mid_y), 2)
            if den:
                col_d = c("RED") if "mg" in den and fi > 0 else c("TEXT_MID")
                t_den = fonts["sm"].render(den, True, col_d)
                surface.blit(t_den, t_den.get_rect(centerx=fx + frac_w // 2, centery=y + frac_h * 3 // 4))
            fx += frac_w + frac_gap
            if fi < len(fracs) - 1:
                sep = fracs[fi + 1][2] if fracs[fi + 1][2] else "×"
                if sep != "=":
                    t = fonts["md"].render(sep, True, c("TEXT_MID"))
                    surface.blit(t, t.get_rect(midleft=(fx - frac_gap + 4, y + frac_h // 2)))

        y += frac_h + 10

        for line in wrap_text(explanation, fonts["sm"], body_w - 16):
            t = fonts["sm"].render(line, True, c("TEXT_MID"))
            surface.blit(t, (body_x + 16, y))
            y += 22
        y += 14


    tip_r = pygame.Rect(body_x, y, body_w, 44)
    pygame.draw.rect(surface, c("ORANGE_BG"), tip_r, border_radius=8)
    pygame.draw.rect(surface, c("ORANGE"), tip_r, 1, border_radius=8)
    tip = "Tip: If units don't cancel cleanly, flip the conversion factor and try again."
    t = fonts["sm"].render(tip, True, c("ORANGE"))
    surface.blit(t, t.get_rect(midleft=(body_x + 16, tip_r.centery)))

    return rects



# ── Welcome screen ────────────────────────────────────────────────────────────
def draw_welcome(screen, fonts, progress, hover_key, theme_name, hover_dot=None):
    font_title = fonts["lg"]
    font_sub   = fonts["md"]
    font_sm    = fonts["sm"]
    font_xs    = fonts["xs"]

    screen.fill(c("WELCOME_BG"))

    t = font_title.render("Nursing Math — Demo", True, c("TEXT_DARK"))
    screen.blit(t, t.get_rect(centerx=WINDOW_W//2, y=40))
    t = font_sm.render("One example of each problem type", True, c("TEXT_MID"))
    screen.blit(t, t.get_rect(centerx=WINDOW_W//2, y=82))

    row_rects = {}
    dot_rects = {}
    y = 130
    for cat in CATEGORIES:
        t = font_sub.render(cat["name"], True, c("TEXT_DARK"))
        screen.blit(t, (200, y))
        y += 34

        for tier in cat["tiers"]:
            key = (cat["name"], tier["name"])
            probs     = tier["problems"]
            done      = progress.get(key, [])
            n_done    = sum(1 for d in done if d)
            row_h = 48
            row_r = pygame.Rect(180, y, WINDOW_W - 380, row_h)
            row_rects[key] = row_r

            is_hov = (hover_key == key)
            bg = c("CARD_ROW_HOV") if is_hov else c("CARD_ROW_BG")
            pygame.draw.rect(screen, bg, row_r, border_radius=8)
            pygame.draw.rect(screen, c("CARD_ROW_BDR"), row_r, 1, border_radius=8)

            lbl = tier["name"] if tier["name"] else "Problem"
            t = font_sm.render(lbl, True, c("TEXT_DARK"))
            screen.blit(t, t.get_rect(midleft=(row_r.x + 20, row_r.centery)))

            dot_x = row_r.right - 20 - len(probs) * 22
            for i, prob in enumerate(probs):
                done_i = done[i] if i < len(done) else False
                col_dot = c("DOT_DONE") if done_i else c("DOT_EMPTY")
                dot_cx = dot_x + i*22
                dot_cy = row_r.centery
                dot_r = pygame.Rect(dot_cx - 10, dot_cy - 10, 20, 20)
                dot_rects[(cat["name"], tier["name"], i)] = dot_r
                if dot_r.collidepoint(hover_dot if hover_dot else (-1, -1)):
                    pygame.draw.circle(screen, c("ACCENT"), (dot_cx, dot_cy), 10, 2)
                pygame.draw.circle(screen, col_dot, (dot_cx, dot_cy), 8)
                if done_i:
                    pygame.draw.circle(screen, c("BTN_TEXT"), (dot_cx, dot_cy), 4)

            score_t = font_xs.render(f"{n_done}/{len(probs)}", True, c("TEXT_MID"))
            screen.blit(score_t, score_t.get_rect(midright=(dot_x - 14, row_r.centery)))

            y += row_h + 8
        y += 10

    tog_r = pygame.Rect(WINDOW_W - 150, 20, 130, 32)
    pygame.draw.rect(screen, c("TOGGLE_BG"), tog_r, border_radius=6)
    tog_lbl = "Mode: Light" if theme_name == "dark" else "Mode: Dark"
    t = font_xs.render(tog_lbl, True, c("TOGGLE_TEXT"))
    screen.blit(t, t.get_rect(center=tog_r.center))

    back_r = pygame.Rect(20, WINDOW_H - 54, 100, 36)
    pygame.draw.rect(screen, c("TOGGLE_BG"), back_r, border_radius=8)
    pygame.draw.rect(screen, c("DIVIDER"), back_r, 1, border_radius=8)
    t = font_xs.render("Back", True, c("TEXT_MID"))
    screen.blit(t, t.get_rect(center=back_r.center))

    return row_rects, dot_rects, tog_r, back_r


# ── Main ──────────────────────────────────────────────────────────────────────
async def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H))
    pygame.display.set_caption("Nursing Math – DA Demo")
    clock = pygame.time.Clock()
    await asyncio.sleep(0)

    pygame.key.set_repeat(400, 50)
    fonts = {
        "lg":   find_font(["Georgia", "DejaVuSerif"], 26, bold=True),
        "prob": find_font(["Georgia", "DejaVuSerif"], 20, bold=False),
        "md":   find_font(["Georgia", "DejaVuSerif"], 22, bold=True),
        "sm":   find_font(["Arial",   "DejaVuSans"],  16),
        "xs":   find_font(["Arial",   "DejaVuSans"],  13),
        "btn":  find_font(["Arial",   "DejaVuSans"],  17, bold=True),
    }
    font_lg  = fonts["lg"]
    font_prob  = fonts["prob"]
    font_md  = fonts["md"]
    font_sm  = fonts["sm"]
    font_xs  = fonts["xs"]
    font_btn = fonts["btn"]

    theme_name = "light"

    progress = {}
    for cat in CATEGORIES:
        for tier in cat["tiers"]:
            key = (cat["name"], tier["name"])
            progress[key] = [False] * len(tier["problems"])

    screen_mode   = "title"
    active_cat    = None
    active_tier   = None
    active_prob_i = 0
    problem       = None

    def load_problem(cat_name, tier_name, prob_i):
        nonlocal active_cat, active_tier, active_prob_i, problem
        active_cat    = cat_name
        active_tier   = tier_name
        active_prob_i = prob_i
        for cat in CATEGORIES:
            if cat["name"] == cat_name:
                for tier in cat["tiers"]:
                    if tier["name"] == tier_name:
                        problem = tier["problems"][prob_i]
                        return

    def reset_game():
        nonlocal slots, inputs, active_input, feedback_lines, attempted, calc_result
        nonlocal show_cancellation, cancel_pairs, how_to_open
        slots = [[{"number": "", "units": []} for _ in range(2)] for _ in range(CHAIN_COLS)]
        inputs = {"ans_num": "", "ans_unit": ""}
        active_input = None
        feedback_lines = []
        attempted = False
        calc_result = None
        show_cancellation = False
        cancel_pairs = []
        how_to_open = False

    slots = [[{"number": "", "units": []} for _ in range(2)] for _ in range(CHAIN_COLS)]
    inputs = {"ans_num": "", "ans_unit": ""}
    active_input = None
    feedback_lines = []
    attempted = False
    calc_result = None
    show_cancellation = False
    cancel_pairs = []
    how_to_open = False
    drag_label = drag_kind = None
    drag_mx = drag_my = 0

    ans_num_rect  = pygame.Rect(CHAIN_LEFT,             ANS_TOP+26, ANS_NUM_W,  ANS_H)
    ans_unit_rect = pygame.Rect(ans_num_rect.right+12,  ANS_TOP+26, ANS_UNIT_W, ANS_H)
    check_rect    = pygame.Rect(ans_unit_rect.right+20, ANS_TOP+26, 100,        ANS_H)
    next_rect     = pygame.Rect(check_rect.right+14,    ANS_TOP+26, 100,        ANS_H)
    back_rect     = pygame.Rect(4, WINDOW_H-INSTR_H-80, SIDEBAR_W-8, 36)
    calc_rect     = pygame.Rect(CHAIN_LEFT+90,          CHAIN_TOP-46, 130, 36)
    cancel_rect   = pygame.Rect(CHAIN_LEFT+230,         CHAIN_TOP-46, 150, 36)
    toggle_rect   = pygame.Rect(WINDOW_W-160, 14, 140, 32)
    reset_rect    = pygame.Rect(CHAIN_LEFT+390,         CHAIN_TOP-46, 90,  36)
    howto_rect    = pygame.Rect(4, WINDOW_H-INSTR_H-36, SIDEBAR_W-8, 30)
    instr_rect    = pygame.Rect(0, WINDOW_H-INSTR_H, WINDOW_W, INSTR_H)
    rounding_note_y = ans_num_rect.bottom + 8

    hover_key = None
    hover_dot = None

    while True:
        mx, my = pygame.mouse.get_pos()

        # ── Intro screens ─────────────────────────────────────────────────────
        if screen_mode == "title":
            btn_rects = draw_intro_title(screen, fonts, theme_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if btn_rects["toggle"].collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    elif btn_rects["start"].collidepoint(ex, ey):
                        screen_mode = "intro_what"
                    elif btn_rects["skip"].collidepoint(ex, ey):
                        screen_mode = "welcome"
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        if screen_mode == "intro_what":
            btn_rects = draw_intro_what(screen, fonts, theme_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if btn_rects["toggle"].collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    elif btn_rects.get("mid") and btn_rects["mid"].collidepoint(ex, ey):
                        screen_mode = "welcome"
                    elif btn_rects.get("right") and btn_rects["right"].collidepoint(ex, ey):
                        screen_mode = "intro_notation"
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        if screen_mode == "intro_notation":
            btn_rects = draw_intro_notation(screen, fonts, theme_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if btn_rects["toggle"].collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    elif btn_rects.get("left") and btn_rects["left"].collidepoint(ex, ey):
                        screen_mode = "intro_what"
                    elif btn_rects.get("mid") and btn_rects["mid"].collidepoint(ex, ey):
                        screen_mode = "welcome"
                    elif btn_rects.get("right") and btn_rects["right"].collidepoint(ex, ey):
                        screen_mode = "intro_chain"
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        if screen_mode == "intro_chain":
            btn_rects = draw_intro_chain(screen, fonts, theme_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if btn_rects["toggle"].collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    elif btn_rects.get("left") and btn_rects["left"].collidepoint(ex, ey):
                        screen_mode = "intro_notation"
                    elif btn_rects.get("mid") and btn_rects["mid"].collidepoint(ex, ey):
                        screen_mode = "welcome"
                    elif btn_rects.get("right") and btn_rects["right"].collidepoint(ex, ey):
                        screen_mode = "intro_example"
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        if screen_mode == "intro_example":
            btn_rects = draw_intro_example(screen, fonts, theme_name)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if btn_rects["toggle"].collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    elif btn_rects.get("left") and btn_rects["left"].collidepoint(ex, ey):
                        screen_mode = "intro_chain"
                    elif btn_rects.get("right") and btn_rects["right"].collidepoint(ex, ey):
                        screen_mode = "welcome"
            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        # ── Welcome screen ────────────────────────────────────────────────────
        if screen_mode == "welcome":
            row_rects, dot_rects, tog_r, back_r = draw_welcome(
                screen, fonts, progress, hover_key, theme_name, hover_dot)

            hover_key = None
            hover_dot = None
            for key, r in row_rects.items():
                if r.collidepoint(mx, my):
                    hover_key = key
            for dkey, dr in dot_rects.items():
                if dr.collidepoint(mx, my):
                    hover_dot = (dr.centerx, dr.centery)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    ex, ey = event.pos
                    if back_r.collidepoint(ex, ey):
                        screen_mode = "title"
                    elif tog_r.collidepoint(ex, ey):
                        theme_name = "dark" if theme_name == "light" else "light"
                        T.update(apply_theme(theme_name))
                    dot_clicked = False
                    for (cat_name, tier_name, prob_i), dr in dot_rects.items():
                        if dr.collidepoint(ex, ey):
                            load_problem(cat_name, tier_name, prob_i)
                            reset_game()
                            screen_mode = "game"
                            dot_clicked = True
                            break
                    if not dot_clicked:
                        for key, r in row_rects.items():
                            if r.collidepoint(ex, ey):
                                cat_name, tier_name = key
                                load_problem(cat_name, tier_name, 0)
                                reset_game()
                                screen_mode = "game"

            pygame.display.flip()
            clock.tick(FPS)
            await asyncio.sleep(0)
            continue

        # ── Game screen ───────────────────────────────────────────────────────
        game_dot_rects = {}
        for cat in CATEGORIES:
            if cat["name"] == active_cat:
                for tier in cat["tiers"]:
                    if tier["name"] == active_tier:
                        n = len(tier["problems"])
                        dot_y = WINDOW_H - INSTR_H - 30
                        dot_x = 14
                        for i in range(n):
                            dcx, dcy = dot_x + i*20, dot_y
                            game_dot_rects[i] = pygame.Rect(dcx - 9, dcy - 9, 18, 18)

        hovered_slot = None
        for col in range(CHAIN_COLS):
            for half in range(2):
                if slot_rect(col, half).collidepoint(mx, my):
                    hovered_slot = (col, half)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if event.type == pygame.MOUSEMOTION:
                if drag_label:
                    drag_mx, drag_my = event.pos

            if event.type == pygame.MOUSEBUTTONDOWN:
                ex, ey = event.pos

                ev_slot = None
                for col in range(CHAIN_COLS):
                    for half in range(2):
                        if slot_rect(col, half).collidepoint(ex, ey):
                            ev_slot = (col, half)

                if event.button == 1:
                    all_ui = [back_rect, check_rect, calc_rect, cancel_rect,
                              reset_rect, toggle_rect, next_rect, howto_rect,
                              ans_num_rect, ans_unit_rect]
                    on_ui = any(r.collidepoint(ex, ey) for r in all_ui)
                    on_card = False
                    cards, _ = sidebar_card_rects(problem)
                    for _, r, _ in cards:
                        if r.collidepoint(ex, ey):
                            on_card = True
                            break

                    if ans_num_rect.collidepoint(ex, ey):
                        active_input = "ans_num"
                    elif ans_unit_rect.collidepoint(ex, ey):
                        active_input = "ans_unit"
                    elif not on_ui and not on_card and ev_slot is None:
                        active_input = None

                    dot_clicked = False
                    for prob_i, dr in game_dot_rects.items():
                        if dr.collidepoint(ex, ey):
                            load_problem(active_cat, active_tier, prob_i)
                            reset_game()
                            dot_clicked = True
                            break
                    if not dot_clicked:
                        if back_rect.collidepoint(ex, ey):
                            screen_mode = "welcome"
                        elif check_rect.collidepoint(ex, ey):
                            attempted = True
                            calc_result = None
                            feedback_lines, correct = run_check(slots, inputs, problem)
                            if correct:
                                pkey = (active_cat, active_tier)
                                if pkey in progress:
                                    progress[pkey][active_prob_i] = True
                            cancel_pairs = get_cancellation_pairs(slots)
                            if cancel_pairs:
                                show_cancellation = True
                        elif calc_rect.collidepoint(ex, ey):
                            result = compute_chain(slots)
                            calc_result = (f"{result:g}" if result is not None else None)
                        elif cancel_rect.collidepoint(ex, ey):
                            show_cancellation = not show_cancellation
                            cancel_pairs = get_cancellation_pairs(slots)
                        elif reset_rect.collidepoint(ex, ey):
                            reset_game()
                        elif toggle_rect.collidepoint(ex, ey):
                            theme_name = "dark" if theme_name == "light" else "light"
                            T.update(apply_theme(theme_name))
                        elif next_rect.collidepoint(ex, ey) and attempted:
                            screen_mode = "welcome"
                        elif howto_rect.collidepoint(ex, ey):
                            how_to_open = not how_to_open
                        elif ev_slot is None and drag_label is None:
                            for label, r, kind in cards:
                                if r.collidepoint(ex, ey):
                                    drag_label = label
                                    drag_kind  = kind
                                    drag_mx, drag_my = ex, ey
                                    break

                elif event.button == 3:
                    if ev_slot:
                        col, half = ev_slot
                        s = slots[col][half]
                        if s["units"]:    s["units"].pop()
                        elif s["number"]: s["number"] = ""

            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if drag_label is not None:
                    ex, ey = event.pos
                    drop_slot = None
                    for col in range(CHAIN_COLS):
                        for half in range(2):
                            if slot_rect(col, half).collidepoint(ex, ey):
                                drop_slot = (col, half)
                    if drop_slot:
                        col, half = drop_slot
                        s = slots[col][half]
                        if drag_kind == "number": s["number"] = drag_label
                        else:                     s["units"].append(drag_label)
                    drag_label = drag_kind = None

            if event.type == pygame.KEYDOWN:
                if active_input:
                    ikey = active_input
                    if event.key == pygame.K_BACKSPACE:
                        inputs[ikey] = inputs[ikey][:-1]
                    elif event.key == pygame.K_TAB:
                        order = ["ans_num", "ans_unit"]
                        active_input = order[(order.index(ikey)+1) % len(order)]
                    elif event.key == pygame.K_RETURN:
                        active_input = None
                    else:
                        if ikey == "ans_num" and event.unicode in "0123456789.":
                            inputs[ikey] += event.unicode
                        elif ikey == "ans_unit" and (event.unicode.isalpha()
                                                     or event.unicode in "/()-"):
                            inputs[ikey] += event.unicode

        # ── Draw game ─────────────────────────────────────────────────────────
        screen.fill(c("BG"))

        pygame.draw.rect(screen, c("TOGGLE_BG"), toggle_rect, border_radius=6)
        tog_lbl = "Mode: Light" if theme_name == "dark" else "Mode: Dark"
        t = font_xs.render(tog_lbl, True, c("TOGGLE_TEXT"))
        screen.blit(t, t.get_rect(center=toggle_rect.center))

        pygame.draw.rect(screen, c("SIDEBAR_BG"), (0, 0, SIDEBAR_W, WINDOW_H))
        pygame.draw.line(screen, c("DIVIDER"), (SIDEBAR_W, 0), (SIDEBAR_W, WINDOW_H), 2)
        screen.blit(font_btn.render("Units",   True, c("TEXT_MID")), (14, 36))

        cards, num_label_y = sidebar_card_rects(problem)
        screen.blit(font_btn.render("Numbers", True, c("TEXT_MID")), (14, num_label_y - 4))
        for label, r, kind in cards:
            pygame.draw.rect(screen, c("CARD_BG"),     r, border_radius=6)
            pygame.draw.rect(screen, c("CARD_BORDER"), r, 1, border_radius=6)
            t = font_sm.render(label, True, c("TEXT_DARK"))
            screen.blit(t, t.get_rect(center=r.center))

        draw_button(screen, back_rect, "Back", font_btn, enabled=True,
                    color=c("TOGGLE_BG"))

        prob_text = problem["text"]
        last_period = prob_text.rfind(".  ")
        if last_period != -1 and "?" in prob_text:
            given_part    = prob_text[:last_period + 1].strip()
            question_part = prob_text[last_period + 3:].strip()
        else:
            given_part    = ""
            question_part = prob_text.strip()

        ty = 125
        if given_part:
            t = font_prob.render(given_part, True, c("TEXT_DARK"))
            screen.blit(t, (CHAIN_LEFT, ty))
            ty += 28
        t = font_sm.render(question_part, True, c("TEXT_MID"))
        screen.blit(t, (CHAIN_LEFT, ty))

        draw_button(screen, calc_rect,   "Calculate",    font_btn, enabled=True)
        cancel_color = c("ACCENT") if show_cancellation else c("TOGGLE_BG")
        draw_button(screen, cancel_rect, "Cancellation", font_btn, enabled=True,
                    color=cancel_color)
        draw_button(screen, reset_rect,  "Reset",        font_btn, enabled=True,
                    color=c("RED"))

        cancel_map = {}
        if show_cancellation and cancel_pairs:
            for u, col_c in cancel_pairs:
                cancel_map[u] = col_c

        for col in range(CHAIN_COLS):
            r = chain_col_rect(col)
            pygame.draw.rect(screen, c("SLOT_BG"),     r, border_radius=8)
            pygame.draw.rect(screen, c("SLOT_BORDER"), r, 1, border_radius=8)
            mid_y = r.y + r.h // 2
            for half in range(2):
                sr     = slot_rect(col, half)
                is_hov = (hovered_slot == (col, half)) and drag_label is not None
                draw_slot(screen, sr, slots[col][half], font_sm,
                          highlight=is_hov,
                          cancel_map=cancel_map if show_cancellation else None)
            pygame.draw.line(screen, c("DIVIDER"), (r.x+10, mid_y), (r.right-10, mid_y), 2)
            if col < CHAIN_COLS - 1:
                t = font_md.render("x", True, c("TEXT_MID"))
                screen.blit(t, t.get_rect(center=(r.right+COL_GAP//2, r.centery)))

        screen.blit(font_sm.render("Answer:", True, c("TEXT_MID")), (CHAIN_LEFT, ANS_TOP-2))
        draw_text_input(screen, ans_num_rect,  inputs["ans_num"],  font_md,
                        active_input=="ans_num",  ghost="value")
        draw_text_input(screen, ans_unit_rect, inputs["ans_unit"], font_sm,
                        active_input=="ans_unit", ghost="unit")
        draw_button(screen, check_rect, "Check", font_btn)
        draw_button(screen, next_rect,  "Next",  font_btn, enabled=attempted)

        t = font_xs.render(problem["rounding"]["note"], True, c("TEXT_MID"))
        screen.blit(t, (CHAIN_LEFT, rounding_note_y))

        fb_y = rounding_note_y + 24
        for text, fg, bg in feedback_lines:
            fb_rect = pygame.Rect(CHAIN_LEFT, fb_y, 580, 34)
            draw_feedback_box(screen, fb_rect, text, font_sm, fg, bg)
            fb_y += 42

        if show_cancellation and cancel_pairs:
            lx = CHAIN_LEFT
            t = font_sm.render("Cancelled: ", True, c("TEXT_MID"))
            screen.blit(t, (lx, fb_y))
            lx += t.get_width() + 4
            for u, col_c in cancel_pairs:
                text_height = font_sm.get_height()
                pygame.draw.circle(screen, col_c, (lx+6, fb_y + text_height//2), 6)
                t = font_sm.render(u, True, col_c)
                screen.blit(t, (lx+16, fb_y))
                lx += t.get_width() + 30
            fb_y += 22

        if calc_result:
            cr_rect = pygame.Rect(CHAIN_LEFT, fb_y + 4, 320, 40)
            pygame.draw.rect(screen, c("HIGHLIGHT"), cr_rect, border_radius=6)
            pygame.draw.rect(screen, c("ACCENT"), cr_rect, 2, border_radius=6)
            lbl = font_sm.render("Calculated result:", True, c("TEXT_MID"))
            val = font_md.render(calc_result, True, c("ACCENT"))
            screen.blit(lbl, lbl.get_rect(midleft=(cr_rect.x + 12, cr_rect.centery - 1)))
            screen.blit(val, val.get_rect(midright=(cr_rect.right - 12, cr_rect.centery)))

        # Progress dots (sidebar, bottom)
        game_dot_rects = {}
        key = (active_cat, active_tier)
        if key in progress:
            done_list = progress[key]
            for cat in CATEGORIES:
                if cat["name"] == active_cat:
                    for tier in cat["tiers"]:
                        if tier["name"] == active_tier:
                            n = len(tier["problems"])
                            dot_y = WINDOW_H - INSTR_H - 30
                            dot_x = 14
                            for i in range(n):
                                col_dot = c("DOT_DONE") if (i < len(done_list) and done_list[i]) else c("DOT_EMPTY")
                                dcx, dcy = dot_x + i*20, dot_y
                                game_dot_rects[i] = pygame.Rect(dcx - 9, dcy - 9, 18, 18)
                                if game_dot_rects[i].collidepoint(mx, my):
                                    pygame.draw.circle(screen, c("ACCENT"), (dcx, dcy), 10, 2)
                                pygame.draw.circle(screen, col_dot, (dcx, dcy), 7)
                                if i == active_prob_i:
                                    pygame.draw.circle(screen, c("ACCENT"), (dcx, dcy), 7, 2)

        pygame.draw.rect(screen, c("INSTR_BG"), instr_rect)
        pygame.draw.line(screen, c("DIVIDER"), (0, instr_rect.y), (WINDOW_W, instr_rect.y), 1)
        instr = ("Drag cards into the factor chain.  Right-click a slot to remove a card.  "
                 "Enter your answer and unit, then click Check.")
        t = font_sm.render(instr, True, c("INSTR_TEXT"))
        screen.blit(t, t.get_rect(centery=instr_rect.centery, x=20))

        if drag_label:
            draw_floating_card(screen, drag_label, font_sm, drag_mx, drag_my)

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)


asyncio.run(main())
