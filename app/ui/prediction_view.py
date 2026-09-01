import customtkinter as ctk
from tkinter import messagebox

from app.models.prediction_request import PredictionRequest
from app.services.prediction_service import PredictionService


# =========================================================
# PREMIUM COLOR PALETTE
# =========================================================

# Primary Colors - Modern Blue & Purple
ACCENT = "#2563EB"        # Modern blue
ACCENT_DARK = "#1E40AF"   # Dark blue for hover
ACCENT_LIGHT = "#EFF6FF"  # Light blue for backgrounds

PURPLE = "#7C3AED"        # Elegant purple
PURPLE_LIGHT = "#F3E8FF"  # Light purple

# Gender Colors
MALE_COLOR = "#3B82F6"    # Blue for male
FEMALE_COLOR = "#EC4899"  # Pink for female

# Status Colors
SUCCESS = "#10B981"       # Green
WARNING = "#F59E0B"       # Orange
DANGER = "#EF4444"        # Red

# Base Colors
WHITE = "#FFFFFF"
BACKGROUND = "#F8FAFC"    # Professional light background
CARD = "#FFFFFF"
CARD_SHADOW_BG = "#F1F5F9"

# Text Colors
TEXT = "#0F172A"          # Deep black
TEXT_SECONDARY = "#64748B" # Medium gray
TEXT_TERTIARY = "#94A3B8"  # Light gray

# Borders
BORDER = "#E2E8F0"
BORDER_LIGHT = "#F1F5F9"


class PredictionView(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        on_prediction=None
    ):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )

        self.on_prediction = on_prediction

        # =====================================================
        # PREDICTION SERVICE
        # =====================================================

        try:
            self.prediction_service = PredictionService()
            self.model_loaded = True
        except Exception as error:
            self.prediction_service = None
            self.model_loaded = False
            print("Prediction service initialization failed:")
            print(error)

        # =====================================================
        # MAIN GRID
        # =====================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=1)

        # =====================================================
        # UI
        # =====================================================

        self.create_header()
        self.create_form()

    # =========================================================
    # HEADER - Premium Style
    # =========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=40,
            pady=(35, 10)
        )

        header.grid_columnconfigure(0, weight=1)

        # Gradient-like background frame
        header_bg = ctk.CTkFrame(
            header,
            fg_color=ACCENT_LIGHT,
            corner_radius=16
        )

        header_bg.grid(
            row=0,
            column=0,
            sticky="ew",
            columnspan=2
        )

        header_content = ctk.CTkFrame(
            header_bg,
            fg_color="transparent"
        )

        header_content.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=25,
            pady=20
        )

        header_content.grid_columnconfigure(0, weight=1)

        # Title
        title = ctk.CTkLabel(
            header_content,
            text="🎓 Academic Risk Analyzer",
            font=ctk.CTkFont(
                size=28,
                weight="bold"
            ),
            text_color=ACCENT,
            anchor="w"
        )

        title.grid(
            row=0,
            column=0,
            sticky="w",
            pady=(0, 5)
        )

        # Subtitle
        subtitle = ctk.CTkLabel(
            header_content,
            text="AI-powered prediction for identifying students at risk of academic failure",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_SECONDARY,
            anchor="w"
        )

        subtitle.grid(
            row=1,
            column=0,
            sticky="w"
        )

        # Status Badge
        badge_text = (
            "✓ Model Ready"
            if self.model_loaded
            else "⚠ Model Error"
        )

        badge_color = (
            "#D0F0C0"
            if self.model_loaded
            else "#FFE0E0"
        )

        badge_text_color = (
            SUCCESS
            if self.model_loaded
            else DANGER
        )

        badge = ctk.CTkLabel(
            header_content,
            text=badge_text,
            height=30,
            corner_radius=8,
            fg_color=badge_color,
            text_color=badge_text_color,
            font=ctk.CTkFont(
                size=10,
                weight="bold"
            ),
            padx=12,
            pady=6
        )

        badge.grid(
            row=0,
            column=1,
            rowspan=2,
            padx=(20, 0),
            sticky="e"
        )

    # =========================================================
    # FORM - Enhanced
    # =========================================================

    def create_form(self):

        self.form_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=CARD,
            corner_radius=20,
            border_width=2,
            border_color=BORDER,
            scrollbar_fg_color=BORDER_LIGHT,
            scrollbar_button_color=ACCENT,
            scrollbar_button_hover_color=ACCENT_DARK
        )

        self.form_frame.grid(
            row=2,
            column=0,
            sticky="nsew",
            padx=40,
            pady=(0, 35)
        )

        # =====================================================
        # FORM COLUMNS
        # =====================================================

        self.form_frame.grid_columnconfigure(
            0,
            weight=1,
            uniform="form_column"
        )

        self.form_frame.grid_columnconfigure(
            1,
            weight=1,
            uniform="form_column"
        )

        # =====================================================
        # STUDENT INFORMATION
        # =====================================================

        self.create_section_title("📋 Student Information", row=0)

        self.create_age_field()        # Row 1, Col 0
        self.create_gender_field()     # Row 1, Col 1

        # =====================================================
        # TECHNOLOGY & DAILY USAGE
        # =====================================================

        self.create_section_title("💻 Technology & Daily Usage", row=2)

        self.create_education_field()     # Row 3, Col 0
        self.create_social_media_field()  # Row 3, Col 1

        self.create_ai_usage_field()      # Row 4, Col 0
        self.create_sleep_field()         # Row 4, Col 1

        # =====================================================
        # HEALTH & LIFESTYLE
        # =====================================================

        self.create_section_title("❤️ Health & Lifestyle", row=5)

        self.create_activity_field()       # Row 6, Col 0
        self.create_mental_health_field()  # Row 6, Col 1

        self.create_physical_health_field()# Row 7, Col 0
        self.create_isolation_field()      # Row 7, Col 1

        # =====================================================
        # ACADEMIC FACTORS
        # =====================================================

        self.create_section_title("🎯 Academic Factors", row=8)

        self.create_burnout_field()              # Row 9, Col 0
        self.create_academic_performance_field() # Row 9, Col 1

        # =====================================================
        # INFORMATION NOTE
        # =====================================================

        self.create_info_note()

        # =====================================================
        # BUTTONS
        # =====================================================

        self.create_buttons()

    # =========================================================
    # INFO NOTE - Enhanced Design
    # =========================================================

    def create_info_note(self):

        note_container = ctk.CTkFrame(
            self.form_frame,
            fg_color=PURPLE_LIGHT,
            corner_radius=12,
            border_width=1,
            border_color=PURPLE
        )

        note_container.grid(
            row=10,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(25, 5)
        )

        note_container.grid_columnconfigure(0, weight=1)

        note_icon = ctk.CTkLabel(
            note_container,
            text="ℹ️",
            font=ctk.CTkFont(size=18),
            text_color=PURPLE,
            fg_color="transparent"
        )

        note_icon.grid(
            row=0,
            column=0,
            sticky="nw",
            padx=15,
            pady=(12, 0)
        )

        note = ctk.CTkLabel(
            note_container,
            text=(
                "Important: Daily-hour fields are separate estimates. "
                "Activities like AI usage and social media may overlap."
            ),
            font=ctk.CTkFont(size=11),
            text_color=TEXT,
            justify="left",
            anchor="nw",
            wraplength=850
        )

        note.grid(
            row=0,
            column=1,
            sticky="ew",
            padx=(0, 15),
            pady=12,
            columnspan=1
        )

        note_container.grid_columnconfigure(1, weight=1)

    # =========================================================
    # SECTION TITLE - Premium Style
    # =========================================================

    def create_section_title(self, text, row):

        container = ctk.CTkFrame(
            self.form_frame,
            fg_color="transparent"
        )

        container.grid(
            row=row,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(28, 12)
        )

        container.grid_columnconfigure(1, weight=1)

        # Accent line
        line = ctk.CTkFrame(
            container,
            width=4,
            height=24,
            corner_radius=2,
            fg_color=ACCENT
        )

        line.grid(
            row=0,
            column=0,
            padx=(0, 12),
            sticky="ns"
        )

        # Title
        title = ctk.CTkLabel(
            container,
            text=text,
            font=ctk.CTkFont(
                size=16,
                weight="bold"
            ),
            text_color=TEXT,
            anchor="w"
        )

        title.grid(
            row=0,
            column=1,
            sticky="w"
        )

    # =========================================================
    # FIELD HELPER - Enhanced
    # =========================================================

    def create_field_label(self, text, hint, row, column, icon=""):

        frame = ctk.CTkFrame(
            self.form_frame,
            fg_color="transparent"
        )

        frame.grid(
            row=row,
            column=column,
            sticky="ew",
            padx=20,
            pady=(10, 12)
        )

        frame.grid_columnconfigure(1, weight=1)

        # Icon (if provided)
        if icon:
            icon_label = ctk.CTkLabel(
                frame,
                text=icon,
                font=ctk.CTkFont(size=14),
                text_color=ACCENT,
                fg_color="transparent"
            )

            icon_label.grid(
                row=0,
                column=0,
                sticky="w",
                padx=(0, 8)
            )

        # Main label
        label = ctk.CTkLabel(
            frame,
            text=text,
            font=ctk.CTkFont(
                size=13,
                weight="bold"
            ),
            text_color=TEXT,
            anchor="w"
        )

        label.grid(
            row=0,
            column=0 if not icon else 1,
            sticky="ew"
        )

        # Hint label
        hint_label = ctk.CTkLabel(
            frame,
            text=hint,
            font=ctk.CTkFont(size=10),
            text_color=TEXT_TERTIARY,
            anchor="w"
        )

        hint_label.grid(
            row=1,
            column=0 if not icon else 1,
            sticky="ew",
            pady=(3, 8)
        )

        return frame

    # =========================================================
    # AGE - SPINNER CONTROL
    # =========================================================

    def create_age_field(self):

        frame = self.create_field_label(
            "Age",
            "Years • Range: 15–100",
            1,
            0,
            "👤"
        )

        # Container for spinner
        spinner_frame = ctk.CTkFrame(frame, fg_color="transparent")
        spinner_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        spinner_frame.grid_columnconfigure(1, weight=1)

        # Minus button
        self.age_minus_btn = ctk.CTkButton(
            spinner_frame,
            text="−",
            width=50,
            height=44,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            hover_color=ACCENT_LIGHT,
            text_color=ACCENT,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=lambda: self._decrease_age()
        )
        self.age_minus_btn.grid(row=0, column=0, padx=(0, 8))

        # Entry field
        self.age_entry = ctk.CTkEntry(
            spinner_frame,
            height=44,
            placeholder_text="21",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY,
            font=ctk.CTkFont(size=14, weight="bold"),
            justify="center"
        )
        self.age_entry.grid(row=0, column=1, sticky="ew", padx=8)
        self.age_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.age_entry))
        self.age_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.age_entry))
        self.age_entry.insert(0, "21")

        # Plus button
        self.age_plus_btn = ctk.CTkButton(
            spinner_frame,
            text="+",
            width=50,
            height=44,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            hover_color=ACCENT_LIGHT,
            text_color=ACCENT,
            font=ctk.CTkFont(size=18, weight="bold"),
            command=lambda: self._increase_age()
        )
        self.age_plus_btn.grid(row=0, column=2, padx=(8, 0))

    def _increase_age(self):
        try:
            current = int(self.age_entry.get())
            if current < 100:
                self.age_entry.delete(0, "end")
                self.age_entry.insert(0, str(current + 1))
        except:
            self.age_entry.delete(0, "end")
            self.age_entry.insert(0, "21")

    def _decrease_age(self):
        try:
            current = int(self.age_entry.get())
            if current > 15:
                self.age_entry.delete(0, "end")
                self.age_entry.insert(0, str(current - 1))
        except:
            self.age_entry.delete(0, "end")
            self.age_entry.insert(0, "21")

    # =========================================================
    # GENDER - COLOR CODED
    # =========================================================

    def create_gender_field(self):

        frame = self.create_field_label(
            "Gender",
            "Select one option",
            1,
            1,
            "⚧️"
        )

        self.gender_combo = ctk.CTkComboBox(
            frame,
            height=44,
            values=["Male", "Female"],
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            button_color=MALE_COLOR,
            button_hover_color="#1E40AF",
            text_color=TEXT,
            dropdown_text_color=TEXT
        )

        self.gender_combo.set("Male")
        self.gender_combo.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        self.gender_combo.bind("<FocusIn>", lambda e: self._on_combo_focus_in(self.gender_combo))
        self.gender_combo.bind("<FocusOut>", lambda e: self._on_combo_focus_out(self.gender_combo))
        self.gender_combo.bind("<<ComboboxSelected>>", lambda e: self._update_gender_color())

    def _update_gender_color(self):
        gender = self.gender_combo.get()
        if gender == "Male":
            self.gender_combo.configure(button_color=MALE_COLOR)
        else:
            self.gender_combo.configure(button_color=FEMALE_COLOR)

    # =========================================================
    # EDUCATION
    # =========================================================

    def create_education_field(self):

        frame = self.create_field_label(
            "Education Level",
            "Select current education level",
            3,
            0,
            "🎓"
        )

        self.education_combo = ctk.CTkComboBox(
            frame,
            height=44,
            values=["High School", "Undergraduate", "Graduate"],
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            button_color=ACCENT,
            button_hover_color=ACCENT_DARK,
            text_color=TEXT,
            dropdown_text_color=TEXT
        )

        self.education_combo.set("Undergraduate")
        self.education_combo.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        self.education_combo.bind("<FocusIn>", lambda e: self._on_combo_focus_in(self.education_combo))
        self.education_combo.bind("<FocusOut>", lambda e: self._on_combo_focus_out(self.education_combo))

    # =========================================================
    # SOCIAL MEDIA
    # =========================================================

    def create_social_media_field(self):

        frame = self.create_field_label(
            "Daily Social Media Usage",
            "Hours/day • Range: 0–16",
            3,
            1,
            "📱"
        )

        self.social_media_entry = ctk.CTkEntry(
            frame,
            height=44,
            placeholder_text="e.g. 4.5",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )

        self.social_media_entry.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        self.social_media_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.social_media_entry))
        self.social_media_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.social_media_entry))
        self.social_media_entry.insert(0, "4.5")

    # =========================================================
    # AI USAGE - WITH PROGRESS BAR
    # =========================================================

    def create_ai_usage_field(self):

        frame = self.create_field_label(
            "Daily AI Tool Usage",
            "Hours/day • Range: 0–12",
            4,
            0,
            "🤖"
        )

        # Entry and progress
        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.ai_usage_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 2.0",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.ai_usage_entry.grid(row=0, column=0, sticky="ew")
        self.ai_usage_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.ai_usage_entry))
        self.ai_usage_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.ai_usage_entry))
        self.ai_usage_entry.bind("<KeyRelease>", lambda e: self._update_ai_progress())
        self.ai_usage_entry.insert(0, "2.0")

        # Progress bar
        self.ai_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=ACCENT
        )
        self.ai_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.ai_progress.set(2.0 / 12)

    def _update_ai_progress(self):
        try:
            value = float(self.ai_usage_entry.get())
            if 0 <= value <= 12:
                self.ai_progress.set(value / 12)
            else:
                self.ai_progress.set(0)
        except:
            self.ai_progress.set(0)

    # =========================================================
    # SLEEP - WITH PROGRESS BAR
    # =========================================================

    def create_sleep_field(self):

        frame = self.create_field_label(
            "Sleep Duration",
            "Hours/night • Range: 3–14",
            4,
            1,
            "😴"
        )

        # Entry and progress
        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.sleep_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 7.5",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.sleep_entry.grid(row=0, column=0, sticky="ew")
        self.sleep_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.sleep_entry))
        self.sleep_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.sleep_entry))
        self.sleep_entry.bind("<KeyRelease>", lambda e: self._update_sleep_progress())
        self.sleep_entry.insert(0, "7.5")

        # Progress bar
        self.sleep_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=ACCENT
        )
        self.sleep_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.sleep_progress.set((7.5 - 3) / (14 - 3))

    def _update_sleep_progress(self):
        try:
            value = float(self.sleep_entry.get())
            if 3 <= value <= 14:
                self.sleep_progress.set((value - 3) / (14 - 3))
            else:
                self.sleep_progress.set(0)
        except:
            self.sleep_progress.set(0)

    # =========================================================
    # PHYSICAL ACTIVITY - WITH PROGRESS BAR
    # =========================================================

    def create_activity_field(self):

        frame = self.create_field_label(
            "Physical Activity",
            "Hours/day • Range: 0–8",
            6,
            0,
            "🏃"
        )

        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.activity_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 1.0",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.activity_entry.grid(row=0, column=0, sticky="ew")
        self.activity_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.activity_entry))
        self.activity_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.activity_entry))
        self.activity_entry.bind("<KeyRelease>", lambda e: self._update_activity_progress())
        self.activity_entry.insert(0, "1.0")

        self.activity_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=SUCCESS
        )
        self.activity_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.activity_progress.set(1.0 / 8)

    def _update_activity_progress(self):
        try:
            value = float(self.activity_entry.get())
            if 0 <= value <= 8:
                self.activity_progress.set(value / 8)
            else:
                self.activity_progress.set(0)
        except:
            self.activity_progress.set(0)

    # =========================================================
    # MENTAL HEALTH - WITH PROGRESS BAR
    # =========================================================

    def create_mental_health_field(self):

        frame = self.create_field_label(
            "Mental Health Score",
            "Score • Range: 0–100",
            6,
            1,
            "🧠"
        )

        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.mental_health_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 65",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.mental_health_entry.grid(row=0, column=0, sticky="ew")
        self.mental_health_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.mental_health_entry))
        self.mental_health_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.mental_health_entry))
        self.mental_health_entry.bind("<KeyRelease>", lambda e: self._update_mental_progress())
        self.mental_health_entry.insert(0, "65")

        self.mental_health_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=ACCENT
        )
        self.mental_health_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.mental_health_progress.set(65 / 100)

    def _update_mental_progress(self):
        try:
            value = float(self.mental_health_entry.get())
            if 0 <= value <= 100:
                self.mental_health_progress.set(value / 100)
            else:
                self.mental_health_progress.set(0)
        except:
            self.mental_health_progress.set(0)

    # =========================================================
    # PHYSICAL HEALTH - WITH PROGRESS BAR
    # =========================================================

    def create_physical_health_field(self):

        frame = self.create_field_label(
            "Physical Health Score",
            "Score • Range: 0–100",
            7,
            0,
            "💪"
        )

        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.physical_health_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 80",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.physical_health_entry.grid(row=0, column=0, sticky="ew")
        self.physical_health_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.physical_health_entry))
        self.physical_health_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.physical_health_entry))
        self.physical_health_entry.bind("<KeyRelease>", lambda e: self._update_physical_progress())
        self.physical_health_entry.insert(0, "80")

        self.physical_health_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=SUCCESS
        )
        self.physical_health_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.physical_health_progress.set(80 / 100)

    def _update_physical_progress(self):
        try:
            value = float(self.physical_health_entry.get())
            if 0 <= value <= 100:
                self.physical_health_progress.set(value / 100)
            else:
                self.physical_health_progress.set(0)
        except:
            self.physical_health_progress.set(0)

    # =========================================================
    # SOCIAL ISOLATION - WITH PROGRESS BAR
    # =========================================================

    def create_isolation_field(self):

        frame = self.create_field_label(
            "Social Isolation Score",
            "Score • Range: 0–100",
            7,
            1,
            "🤝"
        )

        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.isolation_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 35",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.isolation_entry.grid(row=0, column=0, sticky="ew")
        self.isolation_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.isolation_entry))
        self.isolation_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.isolation_entry))
        self.isolation_entry.bind("<KeyRelease>", lambda e: self._update_isolation_progress())
        self.isolation_entry.insert(0, "35")

        self.isolation_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=WARNING
        )
        self.isolation_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.isolation_progress.set(35 / 100)

    def _update_isolation_progress(self):
        try:
            value = float(self.isolation_entry.get())
            if 0 <= value <= 100:
                self.isolation_progress.set(value / 100)
            else:
                self.isolation_progress.set(0)
        except:
            self.isolation_progress.set(0)

    # =========================================================
    # BURNOUT
    # =========================================================

    def create_burnout_field(self):

        frame = self.create_field_label(
            "Burnout Level",
            "Select student's burnout level",
            9,
            0,
            "⚡"
        )

        self.burnout_combo = ctk.CTkComboBox(
            frame,
            height=44,
            values=["Low", "Medium", "High"],
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            button_color=ACCENT,
            button_hover_color=ACCENT_DARK,
            text_color=TEXT,
            dropdown_text_color=TEXT
        )

        self.burnout_combo.set("Low")
        self.burnout_combo.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        self.burnout_combo.bind("<FocusIn>", lambda e: self._on_combo_focus_in(self.burnout_combo))
        self.burnout_combo.bind("<FocusOut>", lambda e: self._on_combo_focus_out(self.burnout_combo))

    # =========================================================
    # ACADEMIC PERFORMANCE - WITH PROGRESS BAR
    # =========================================================

    def create_academic_performance_field(self):

        frame = self.create_field_label(
            "Academic Performance Score",
            "Score • Range: 0–100",
            9,
            1,
            "📊"
        )

        entry_frame = ctk.CTkFrame(frame, fg_color="transparent")
        entry_frame.grid(row=2, column=0 if True else 1, sticky="ew", columnspan=2)
        entry_frame.grid_columnconfigure(0, weight=1)

        self.performance_entry = ctk.CTkEntry(
            entry_frame,
            height=44,
            placeholder_text="e.g. 78",
            border_color=BORDER,
            border_width=1.5,
            corner_radius=10,
            fg_color=BORDER_LIGHT,
            text_color=TEXT,
            placeholder_text_color=TEXT_TERTIARY
        )
        self.performance_entry.grid(row=0, column=0, sticky="ew")
        self.performance_entry.bind("<FocusIn>", lambda e: self._on_entry_focus_in(self.performance_entry))
        self.performance_entry.bind("<FocusOut>", lambda e: self._on_entry_focus_out(self.performance_entry))
        self.performance_entry.bind("<KeyRelease>", lambda e: self._update_performance_progress())
        self.performance_entry.insert(0, "78")

        self.performance_progress = ctk.CTkProgressBar(
            entry_frame,
            height=6,
            corner_radius=3,
            fg_color=BORDER,
            progress_color=SUCCESS
        )
        self.performance_progress.grid(row=1, column=0, sticky="ew", pady=(6, 0))
        self.performance_progress.set(78 / 100)

    def _update_performance_progress(self):
        try:
            value = float(self.performance_entry.get())
            if 0 <= value <= 100:
                self.performance_progress.set(value / 100)
            else:
                self.performance_progress.set(0)
        except:
            self.performance_progress.set(0)

    # =========================================================
    # FOCUS EFFECTS
    # =========================================================

    def _on_entry_focus_in(self, entry):
        entry.configure(border_color=ACCENT, fg_color=WHITE)

    def _on_entry_focus_out(self, entry):
        entry.configure(border_color=BORDER, fg_color=BORDER_LIGHT)

    def _on_combo_focus_in(self, combo):
        combo.configure(border_color=ACCENT, fg_color=WHITE)

    def _on_combo_focus_out(self, combo):
        combo.configure(border_color=BORDER, fg_color=BORDER_LIGHT)

    # =========================================================
    # BUTTONS - Premium Design
    # =========================================================

    def create_buttons(self):

        frame = ctk.CTkFrame(
            self.form_frame,
            fg_color="transparent"
        )

        frame.grid(
            row=11,
            column=0,
            columnspan=2,
            sticky="ew",
            padx=20,
            pady=(30, 35)
        )

        frame.grid_columnconfigure(0, weight=1, uniform="buttons")
        frame.grid_columnconfigure(1, weight=2, uniform="buttons")

        # Reset Button
        self.reset_button = ctk.CTkButton(
            frame,
            text="↺ Reset Form",
            height=48,
            corner_radius=11,
            fg_color=WHITE,
            hover_color=BORDER_LIGHT,
            border_width=2,
            border_color=BORDER,
            text_color=TEXT,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.reset_form
        )

        self.reset_button.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ew"
        )

        # Predict Button
        self.predict_button = ctk.CTkButton(
            frame,
            text="✨ Predict Academic Risk  →",
            height=48,
            corner_radius=11,
            fg_color=ACCENT,
            hover_color=ACCENT_DARK,
            text_color=WHITE,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.predict
        )

        self.predict_button.grid(
            row=0,
            column=1,
            padx=(10, 0),
            sticky="ew"
        )

    # =========================================================
    # VALIDATION
    # =========================================================

    def get_number(
        self,
        entry,
        field_name,
        minimum,
        maximum
    ):

        value = entry.get().strip()

        if not value:
            raise ValueError(f"{field_name} is required.")

        try:
            number = float(value)
        except ValueError:
            raise ValueError(
                f"{field_name} must contain a valid number.\n\n"
                f"Example: {minimum if minimum > 0 else 2}"
            )

        if number < minimum or number > maximum:
            raise ValueError(
                f"{field_name} is outside the allowed range.\n\n"
                f"Allowed range: {minimum}–{maximum}"
            )

        return number

    # =========================================================
    # VALIDATE FORM
    # =========================================================

    def validate_form(self):

        age = self.get_number(
            self.age_entry,
            "Age",
            15,
            100
        )

        social_media = self.get_number(
            self.social_media_entry,
            "Daily Social Media Usage",
            0,
            16
        )

        ai_usage = self.get_number(
            self.ai_usage_entry,
            "Daily AI Tool Usage",
            0,
            12
        )

        sleep = self.get_number(
            self.sleep_entry,
            "Sleep Duration",
            3,
            14
        )

        activity = self.get_number(
            self.activity_entry,
            "Physical Activity",
            0,
            8
        )

        mental_health = self.get_number(
            self.mental_health_entry,
            "Mental Health Score",
            0,
            100
        )

        physical_health = self.get_number(
            self.physical_health_entry,
            "Physical Health Score",
            0,
            100
        )

        isolation = self.get_number(
            self.isolation_entry,
            "Social Isolation Score",
            0,
            100
        )

        performance = self.get_number(
            self.performance_entry,
            "Academic Performance Score",
            0,
            100
        )

        return {
            "age": age,
            "gender": self.gender_combo.get(),
            "education_level": self.education_combo.get(),
            "social_media_hours": social_media,
            "ai_usage_hours": ai_usage,
            "sleep_hours": sleep,
            "physical_activity_hours": activity,
            "mental_health_score": mental_health,
            "physical_health_score": physical_health,
            "social_isolation_score": isolation,
            "burnout_level": self.burnout_combo.get(),
            "academic_performance_score": performance
        }

    # =========================================================
    # RESET
    # =========================================================

    def reset_form(self):

        entries = [
            self.age_entry,
            self.social_media_entry,
            self.ai_usage_entry,
            self.sleep_entry,
            self.activity_entry,
            self.mental_health_entry,
            self.physical_health_entry,
            self.isolation_entry,
            self.performance_entry
        ]

        for entry in entries:
            entry.delete(0, "end")

        self.age_entry.insert(0, "21")
        self.social_media_entry.insert(0, "4.5")
        self.ai_usage_entry.insert(0, "2.0")
        self.sleep_entry.insert(0, "7.5")
        self.activity_entry.insert(0, "1.0")
        self.mental_health_entry.insert(0, "65")
        self.physical_health_entry.insert(0, "80")
        self.isolation_entry.insert(0, "35")
        self.performance_entry.insert(0, "78")

        self.gender_combo.set("Male")
        self.gender_combo.configure(button_color=MALE_COLOR)
        self.education_combo.set("Undergraduate")
        self.burnout_combo.set("Low")

        # Reset progress bars
        self._update_ai_progress()
        self._update_sleep_progress()
        self._update_activity_progress()
        self._update_mental_progress()
        self._update_physical_progress()
        self._update_isolation_progress()
        self._update_performance_progress()

    # =========================================================
    # CREATE PREDICTION REQUEST
    # =========================================================

    def create_prediction_request(self, data):

        return PredictionRequest(
            age=data["age"],
            gender=data["gender"],
            education_level=data["education_level"],
            social_media_hours=data["social_media_hours"],
            ai_usage_hours=data["ai_usage_hours"],
            sleep_hours=data["sleep_hours"],
            physical_activity_hours=data["physical_activity_hours"],
            mental_health_score=data["mental_health_score"],
            physical_health_score=data["physical_health_score"],
            social_isolation_score=data["social_isolation_score"],
            burnout_level=data["burnout_level"],
            academic_performance_score=data["academic_performance_score"]
        )

    # =========================================================
    # PREDICT
    # =========================================================

    def predict(self):

        try:
            if not self.model_loaded:
                messagebox.showerror(
                    "Model Error",
                    (
                        "The prediction model could not be loaded.\n\n"
                        "Please check:\n"
                        "• random_forest_model.pkl\n"
                        "• preprocessor.pkl\n"
                        "• prediction_service.py"
                    )
                )
                return

            data = self.validate_form()
            request = self.create_prediction_request(data)

            print("\n" + "=" * 60)
            print("STUDENT DATA")
            print("=" * 60)

            for key, value in data.items():
                print(f"{key}: {value}")

            print("=" * 60)

            result = self.prediction_service.predict(request)

            print("\n" + "=" * 60)
            print("REAL MODEL PREDICTION")
            print("=" * 60)

            print(f"Prediction : {result.prediction}")
            print(f"Risk Level : {result.risk_level}")

            if result.probability is not None:
                print(f"Probability: {result.probability:.2f}%")

            print("=" * 60)

            if self.on_prediction:
                self.on_prediction(
                    result.risk_level,
                    result.probability
                )

        except ValueError as error:
            messagebox.showerror(
                "Invalid Input",
                str(error)
            )

        except FileNotFoundError as error:
            messagebox.showerror(
                "Model Files Missing",
                str(error)
            )

        except Exception as error:
            print("\nPrediction Error:")
            print(error)
            messagebox.showerror(
                "Prediction Error",
                str(error)
            )