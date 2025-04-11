from fpdf import FPDF
from pathlib import Path
from io import BytesIO

class BadgePDF(FPDF):
    def __init__(self, bg_color):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.add_page()
        font_dir = Path(__file__).parent
        self.add_font("DejaVu", "", str(font_dir / "DejaVuSans.ttf"), uni=True)
        self.add_font("DejaVu", "B", str(font_dir / "DejaVuSans-Bold.ttf"), uni=True)
        self.set_font("DejaVu", size=12)
        self.bg_color = bg_color

    def draw_badge_box(self, badge_title, badge_desc, co2):
        self.set_fill_color(*self.bg_color)
        self.set_draw_color(*[c - 20 for c in self.bg_color])
        self.set_line_width(0.8)

        box_x = 30
        box_y = 40
        box_w = 150
        box_h = 100

        self.rect(box_x, box_y, box_w, box_h, style="FD")

        self.set_xy(box_x, box_y + 10)
        self.set_font("DejaVu", size=18)
        self.set_text_color(20, 100, 20)
        self.cell(box_w, 10, badge_title, ln=True, align="C")

        self.set_font("DejaVu", size=12)
        self.set_text_color(50, 50, 50)
        self.set_xy(box_x + 10, box_y + 25)
        self.multi_cell(box_w - 20, 8, badge_desc, align="C")

        self.set_text_color(0, 0, 0)
        self.set_xy(box_x, box_y + 80)
        self.set_font("DejaVu", size=12, style="B")
        self.cell(box_w, 10, f"🌍 Impronta stimata: {co2:.2f} kg di CO₂", ln=True, align="C")

def generate_badge_pdf(co2, lang, badge_data):
    # Colori personalizzati per badge
    color_map = {
        "Riduci": (255, 200, 200),
        "Neutrale": (255, 255, 200),
        "Sostenitore": (200, 255, 200),
        "EcoChampion": (180, 240, 180),
        "Asceta digitale": (230, 255, 230)
    }
    badge_name = badge_data['title'][lang]
    bg_color = color_map.get(badge_name, (230, 255, 230))

    pdf = BadgePDF(bg_color)
    badge_title = f"{badge_data['icon']} Badge: {badge_data['title'][lang]}"
    badge_desc = f"📊 Punteggio ambientale: {badge_data['score']} / 10\n💬 {badge_data['desc'][lang]}"
    pdf.draw_badge_box(badge_title, badge_desc, co2)

    buffer = BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer
