import customtkinter as ctk


# =========================================================
# PREMIUM COLOR PALETTE
# =========================================================

# Primary Colors
ACCENT = "#2563EB"        # Modern blue
ACCENT_DARK = "#1E40AF"   # Dark blue for hover
ACCENT_LIGHT = "#EFF6FF"  # Light blue for backgrounds

PURPLE = "#7C3AED"        # Elegant purple
PURPLE_LIGHT = "#F3E8FF"  # Light purple

# Risk Level Colors
RISK_LOW = "#10B981"       # Green for low risk
RISK_MEDIUM = "#F59E0B"    # Orange for medium risk
RISK_HIGH = "#EF4444"      # Red for high risk

# Status Colors
SUCCESS = "#10B981"        # Green
WARNING = "#F59E0B"        # Orange
DANGER = "#EF4444"         # Red

# Base Colors
WHITE = "#FFFFFF"
BACKGROUND = "#F8FAFC"     # Professional light background
CARD = "#FFFFFF"
CARD_SHADOW_BG = "#F1F5F9"

# Text Colors
TEXT = "#0F172A"           # Deep black
TEXT_SECONDARY = "#64748B" # Medium gray
TEXT_TERTIARY = "#94A3B8"  # Light gray

# Borders
BORDER = "#E2E8F0"
BORDER_LIGHT = "#F1F5F9"


class ResultsView(ctk.CTkFrame):

    def __init__(
        self,
        parent,
        risk_level="High",
        probability=78.5,
        on_back=None
    ):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )

        self.on_back = on_back
        self.risk_level = risk_level
        self.probability = probability

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=1)

        self.create_header()
        self.create_result_card()
        self.create_explanation()
        self.create_actions()

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

        # Header background
        header_bg = ctk.CTkFrame(
            header,
            fg_color=ACCENT_LIGHT,
            corner_radius=16
        )

        header_bg.grid(row=0, column=0, sticky="ew")

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
            text="📊 Prediction Results",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=ACCENT,
            anchor="w"
        )

        title.grid(row=0, column=0, sticky="w", pady=(0, 5))

        # Subtitle
        subtitle = ctk.CTkLabel(
            header_content,
            text="Academic failure risk assessment based on student profile",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_SECONDARY,
            anchor="w"
        )

        subtitle.grid(row=1, column=0, sticky="w")

    # =========================================================
    # RESULT CARD - Enhanced Design
    # =========================================================

    def create_result_card(self):

        # Get colors
        risk_color = self.get_risk_color()
        risk_bg_color = self.get_risk_bg_color()

        # Main card
        card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=20,
            border_width=2,
            border_color=BORDER
        )

        card.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=40,
            pady=15
        )

        card.grid_columnconfigure(0, weight=1)

        # Top label
        label = ctk.CTkLabel(
            card,
            text="ESTIMATED ACADEMIC FAILURE RISK",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=TEXT_SECONDARY
        )

        label.grid(row=0, column=0, pady=(30, 15), padx=30)

        # Risk level badge
        badge_frame = ctk.CTkFrame(
            card,
            fg_color=risk_bg_color,
            corner_radius=12
        )

        badge_frame.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=30,
            pady=0
        )

        badge_frame.grid_columnconfigure(0, weight=1)

        risk_text = ctk.CTkLabel(
            badge_frame,
            text=self.risk_level.upper(),
            font=ctk.CTkFont(size=48, weight="bold"),
            text_color=risk_color
        )

        risk_text.grid(row=0, column=0, pady=(20, 5), padx=20)

        # Probability display
        prob_frame = ctk.CTkFrame(
            badge_frame,
            fg_color="transparent"
        )

        prob_frame.grid(row=1, column=0, sticky="ew", padx=20, pady=(5, 20))
        prob_frame.grid_columnconfigure(0, weight=1)

        probability_label = ctk.CTkLabel(
            prob_frame,
            text=f"{self.probability:.1f}%",
            font=ctk.CTkFont(size=40, weight="bold"),
            text_color=TEXT
        )

        probability_label.grid(row=0, column=0)

        # Progress bar for probability
        progress_bar = ctk.CTkProgressBar(
            prob_frame,
            height=8,
            corner_radius=4,
            fg_color=BORDER,
            progress_color=risk_color
        )

        progress_bar.grid(
            row=1,
            column=0,
            sticky="ew",
            pady=(12, 0)
        )

        # Set progress value
        progress_bar.set(self.probability / 100)

        # Description below progress bar
        prob_description = ctk.CTkLabel(
            prob_frame,
            text="Probability of academic failure",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_SECONDARY
        )

        prob_description.grid(row=2, column=0, pady=(8, 0))

    # =========================================================
    # EXPLANATION - Enhanced
    # =========================================================

    def create_explanation(self):

        card = ctk.CTkFrame(
            self,
            fg_color=CARD,
            corner_radius=20,
            border_width=2,
            border_color=BORDER
        )

        card.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=40,
            pady=15
        )

        card.grid_columnconfigure(0, weight=1)

        # Title with icon
        title_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        title_frame.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=25,
            pady=(25, 0)
        )

        title_frame.grid_columnconfigure(1, weight=1)

        title_icon = ctk.CTkLabel(
            title_frame,
            text="💡",
            font=ctk.CTkFont(size=20),
            fg_color="transparent"
        )

        title_icon.grid(row=0, column=0, padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text="Interpretation",
            font=ctk.CTkFont(size=18, weight="bold"),
            text_color=TEXT,
            anchor="w"
        )

        title.grid(row=0, column=1, sticky="ew")

        # Separator line
        separator = ctk.CTkFrame(
            card,
            height=1,
            fg_color=BORDER
        )

        separator.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=25,
            pady=(15, 0)
        )

        # Description
        description = ctk.CTkLabel(
            card,
            text=self.get_explanation(),
            font=ctk.CTkFont(size=13),
            text_color=TEXT,
            justify="left",
            anchor="nw",
            wraplength=850
        )

        description.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=25,
            pady=(20, 15)
        )

        # Recommendation box
        rec_color = self.get_risk_bg_color()
        rec_text_color = self.get_risk_color()

        rec_frame = ctk.CTkFrame(
            card,
            fg_color=rec_color,
            corner_radius=12
        )

        rec_frame.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 25)
        )

        rec_frame.grid_columnconfigure(0, weight=1)

        rec_icon = ctk.CTkLabel(
            rec_frame,
            text="🎯",
            font=ctk.CTkFont(size=18),
            fg_color="transparent"
        )

        rec_icon.grid(row=0, column=0, sticky="w", padx=15, pady=(15, 5))

        recommendation = ctk.CTkLabel(
            rec_frame,
            text=self.get_recommendation(),
            font=ctk.CTkFont(size=13, weight="bold"),
            text_color=rec_text_color,
            justify="left",
            anchor="w",
            wraplength=850
        )

        recommendation.grid(
            row=1,
            column=0,
            sticky="ew",
            padx=15,
            pady=(0, 15)
        )

    # =========================================================
    # ACTIONS - Premium Buttons
    # =========================================================

    def create_actions(self):

        frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        frame.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=40,
            pady=(15, 40)
        )

        frame.grid_columnconfigure(0, weight=1, uniform="buttons")
        frame.grid_columnconfigure(1, weight=2, uniform="buttons")

        # New Prediction Button
        back_button = ctk.CTkButton(
            frame,
            text="← New Prediction",
            height=48,
            corner_radius=11,
            fg_color=WHITE,
            hover_color=BORDER_LIGHT,
            border_width=2,
            border_color=BORDER,
            text_color=TEXT,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.go_back
        )

        back_button.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ew"
        )

        # Close Button
        close_button = ctk.CTkButton(
            frame,
            text="✕ Close Application",
            height=48,
            corner_radius=11,
            fg_color=ACCENT,
            hover_color=ACCENT_DARK,
            text_color=WHITE,
            font=ctk.CTkFont(size=13, weight="bold"),
            command=self.master.destroy
        )

        close_button.grid(
            row=0,
            column=1,
            padx=(10, 0),
            sticky="ew"
        )

    # =========================================================
    # RISK COLOR
    # =========================================================

    def get_risk_color(self):
        """Get the color for the risk level"""

        risk = self.risk_level.lower()

        if risk == "low":
            return RISK_LOW       # Green

        if risk == "medium":
            return RISK_MEDIUM    # Orange

        return RISK_HIGH          # Red

    # =========================================================
    # RISK BACKGROUND COLOR
    # =========================================================

    def get_risk_bg_color(self):
        """Get the background color for the risk badge"""

        risk = self.risk_level.lower()

        if risk == "low":
            return "#ECFDF5"      # Light green

        if risk == "medium":
            return "#FFFBEB"      # Light orange

        return "#FEF2F2"          # Light red

    # =========================================================
    # EXPLANATION TEXT
    # =========================================================

    def get_explanation(self):
        """Get the explanation text based on risk level"""

        risk = self.risk_level.lower()

        if risk == "low":
            return (
                "The model estimates a relatively low probability of "
                "academic failure based on the information provided. "
                "The student's academic, behavioral, and lifestyle profile "
                "appears generally positive with strong indicators of success."
            )

        if risk == "medium":
            return (
                "The model estimates a moderate probability of academic "
                "failure. Some academic, behavioral, health, or lifestyle "
                "factors may require attention and regular monitoring. "
                "This level of risk suggests the need for preventive support."
            )

        return (
            "The model estimates a high probability of academic failure. "
            "Several factors in the student profile may require attention. "
            "Early academic support, intervention, and monitoring are strongly "
            "recommended to help improve outcomes."
        )

    # =========================================================
    # RECOMMENDATION TEXT
    # =========================================================

    def get_recommendation(self):
        """Get the recommendation text based on risk level"""

        risk = self.risk_level.lower()

        if risk == "low":
            return (
                "✓ Continue maintaining healthy study, sleep, technology, "
                "and academic habits. Regular monitoring is encouraged."
            )

        if risk == "medium":
            return (
                "⚠ Monitor academic performance and consider additional "
                "academic or wellbeing support. Schedule regular check-ins."
            )

        return (
            "🔴 Strongly consider early academic support, review study habits, "
            "and monitor wellbeing-related factors. Professional guidance is recommended."
        )

    # =========================================================
    # GO BACK
    # =========================================================

    def go_back(self):
        """Go back to prediction form"""

        if self.on_back:
            self.on_back()