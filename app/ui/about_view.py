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


class AboutView(ctk.CTkFrame):

    def __init__(self, parent):

        super().__init__(
            parent,
            fg_color=BACKGROUND
        )

        # =====================================================
        # SCROLLABLE CONTAINER
        # =====================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=BACKGROUND,
            scrollbar_fg_color=BORDER_LIGHT,
            scrollbar_button_color=ACCENT,
            scrollbar_button_hover_color=ACCENT_DARK,
            corner_radius=0
        )

        self.scrollable_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Create content
        self.create_header()
        self.create_project_card()
        self.create_how_it_works()
        self.create_information_card()

    # =========================================================
    # HEADER - Premium Style
    # =========================================================

    def create_header(self):

        header = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color="transparent"
        )

        header.grid(
            row=0,
            column=0,
            sticky="ew",
            padx=40,
            pady=(35, 15)
        )

        header.grid_columnconfigure(0, weight=1)

        # Title with icon
        title_frame = ctk.CTkFrame(
            header,
            fg_color="transparent"
        )

        title_frame.pack(anchor="w")

        title_icon = ctk.CTkLabel(
            title_frame,
            text="ℹ️",
            font=ctk.CTkFont(size=32),
            fg_color="transparent"
        )

        title_icon.pack(side="left", padx=(0, 12))

        title = ctk.CTkLabel(
            title_frame,
            text="About the Project",
            font=ctk.CTkFont(size=32, weight="bold"),
            text_color=TEXT
        )

        title.pack(side="left", anchor="w")

        # Subtitle
        subtitle = ctk.CTkLabel(
            header,
            text="Machine Learning application for identifying students at academic risk",
            font=ctk.CTkFont(size=13),
            text_color=TEXT_SECONDARY
        )

        subtitle.pack(anchor="w", pady=(8, 0))

    # =========================================================
    # PROJECT CARD - Enhanced
    # =========================================================

    def create_project_card(self):

        card = ctk.CTkFrame(
            self.scrollable_frame,
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
            pady=(15, 10)
        )

        card.grid_columnconfigure(0, weight=1)

        # Badge
        badge = ctk.CTkLabel(
            card,
            text="🤖 MACHINE LEARNING PROJECT",
            height=32,
            corner_radius=8,
            fg_color=ACCENT_LIGHT,
            text_color=ACCENT,
            font=ctk.CTkFont(size=11, weight="bold")
        )

        badge.grid(
            row=0,
            column=0,
            sticky="w",
            padx=25,
            pady=(22, 12)
        )

        # Title
        title = ctk.CTkLabel(
            card,
            text="Academic Risk Analyzer",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=TEXT
        )

        title.grid(
            row=1,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 10)
        )

        # Subtitle
        subtitle = ctk.CTkLabel(
            card,
            text="AI Impact on Student Health & Academic Success",
            font=ctk.CTkFont(size=12),
            text_color=TEXT_SECONDARY
        )

        subtitle.grid(
            row=2,
            column=0,
            sticky="w",
            padx=25,
            pady=(0, 15)
        )

        # Description
        description = ctk.CTkLabel(
            card,
            text=(
                "This application uses Machine Learning to estimate the risk of academic "
                "failure using student behavioral, health, social media, AI usage, and "
                "academic performance data. The model analyzes complex patterns in student "
                "data to provide actionable insights for early intervention."
            ),
            font=ctk.CTkFont(size=13),
            text_color=TEXT,
            justify="left",
            anchor="nw",
            wraplength=850
        )

        description.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 20)
        )

        # Model Info Card
        model_card = ctk.CTkFrame(
            card,
            fg_color=ACCENT_LIGHT,
            corner_radius=12,
            border_width=1,
            border_color=ACCENT
        )

        model_card.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=25,
            pady=(0, 25)
        )

        model_card.grid_columnconfigure(1, weight=1)

        # Model icon
        model_icon = ctk.CTkLabel(
            model_card,
            text="🧠",
            font=ctk.CTkFont(size=20),
            fg_color="transparent"
        )

        model_icon.grid(row=0, column=0, padx=15, pady=12)

        # Model details
        model_label = ctk.CTkLabel(
            model_card,
            text="Machine Learning Model",
            font=ctk.CTkFont(size=11, weight="bold"),
            text_color=ACCENT,
            anchor="w"
        )

        model_label.grid(row=0, column=1, sticky="w", pady=(12, 2))

        model = ctk.CTkLabel(
            model_card,
            text="Random Forest Classifier with 12 input features",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color=TEXT,
            anchor="w"
        )

        model.grid(row=1, column=1, sticky="w", pady=(0, 12))

    # =========================================================
    # HOW IT WORKS - Enhanced
    # =========================================================

    def create_how_it_works(self):

        card = ctk.CTkFrame(
            self.scrollable_frame,
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
            pady=10
        )

        card.grid_columnconfigure(1, weight=1)

        # Title with icon
        title_frame = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        title_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            padx=25,
            pady=(25, 20)
        )

        title_icon = ctk.CTkLabel(
            title_frame,
            text="⚙️",
            font=ctk.CTkFont(size=24),
            fg_color="transparent"
        )

        title_icon.pack(side="left", padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text="How It Works",
            font=ctk.CTkFont(size=22, weight="bold"),
            text_color=TEXT
        )

        title.pack(side="left", anchor="w")

        # Steps
        steps = [
            ("📝", "Enter Student Data", "Provide behavioral, health, technology, and academic information."),
            ("🤖", "Machine Learning", "The trained Random Forest model analyzes the provided features."),
            ("📊", "Risk Assessment", "The model estimates the probability of academic failure."),
            ("📈", "View Results", "The application displays the predicted risk level and probability.")
        ]

        for index, (icon, step_title, description) in enumerate(steps):

            row = index + 1

            # Step number badge with color
            colors = [ACCENT, PURPLE, WARNING, SUCCESS]
            step_color = colors[index % len(colors)]

            number_label = ctk.CTkLabel(
                card,
                text=f"{index + 1:02d}",
                width=48,
                height=48,
                corner_radius=24,
                fg_color=step_color,
                text_color=WHITE,
                font=ctk.CTkFont(size=13, weight="bold")
            )

            number_label.grid(
                row=row,
                column=0,
                padx=(25, 18),
                pady=12,
                sticky="nw"
            )

            # Text Container
            text_frame = ctk.CTkFrame(
                card,
                fg_color="transparent"
            )

            text_frame.grid(
                row=row,
                column=1,
                sticky="ew",
                padx=(0, 25),
                pady=12
            )

            text_frame.grid_columnconfigure(1, weight=1)

            # Icon
            icon_label = ctk.CTkLabel(
                text_frame,
                text=icon,
                font=ctk.CTkFont(size=18),
                fg_color="transparent"
            )

            icon_label.grid(row=0, column=0, padx=(0, 10))

            # Step title
            step_label = ctk.CTkLabel(
                text_frame,
                text=step_title,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=TEXT,
                anchor="w"
            )

            step_label.grid(row=0, column=1, sticky="w")

            # Description
            description_label = ctk.CTkLabel(
                text_frame,
                text=description,
                font=ctk.CTkFont(size=12),
                text_color=TEXT_SECONDARY,
                justify="left",
                anchor="nw",
                wraplength=750
            )

            description_label.grid(
                row=1,
                column=0,
                columnspan=2,
                sticky="ew",
                pady=(4, 0)
            )

    # =========================================================
    # INFORMATION CARD - Enhanced
    # =========================================================

    def create_information_card(self):

        card = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color=CARD,
            corner_radius=20,
            border_width=2,
            border_color=BORDER
        )

        card.grid(
            row=3,
            column=0,
            sticky="ew",
            padx=40,
            pady=(10, 40)
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
            sticky="w",
            padx=25,
            pady=(22, 15)
        )

        title_icon = ctk.CTkLabel(
            title_frame,
            text="👤",
            font=ctk.CTkFont(size=22),
            fg_color="transparent"
        )

        title_icon.pack(side="left", padx=(0, 10))

        title = ctk.CTkLabel(
            title_frame,
            text="Project Information & Contact",
            font=ctk.CTkFont(size=20, weight="bold"),
            text_color=TEXT
        )

        title.pack(side="left", anchor="w")

        # Separator
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
            pady=(0, 18)
        )

        # Contact Info Items
        info_items = [
            ("💻", "GitHub", "github.com/aymanaljamal"),
            ("📧", "Email", "ayman.aljamal2017@gmail.com"),
            ("🎓", "University", "Birzeit University"),
            ("🔬", "Focus", "AI, Machine Learning, Data Science")
        ]

        for index, (icon, label, value) in enumerate(info_items):
            row = index + 2

            # Item container
            item_frame = ctk.CTkFrame(
                card,
                fg_color=BORDER_LIGHT,
                corner_radius=10
            )

            item_frame.grid(
                row=row,
                column=0,
                sticky="ew",
                padx=25,
                pady=6
            )

            item_frame.grid_columnconfigure(1, weight=1)

            # Icon
            icon_label = ctk.CTkLabel(
                item_frame,
                text=icon,
                font=ctk.CTkFont(size=16),
                fg_color="transparent"
            )

            icon_label.grid(row=0, column=0, padx=12, pady=10)

            # Label
            label_widget = ctk.CTkLabel(
                item_frame,
                text=label,
                font=ctk.CTkFont(size=11, weight="bold"),
                text_color=TEXT_SECONDARY,
                anchor="w"
            )

            label_widget.grid(row=0, column=1, sticky="w")

            # Value
            value_widget = ctk.CTkLabel(
                item_frame,
                text=value,
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=TEXT,
                anchor="w"
            )

            value_widget.grid(
                row=1,
                column=1,
                sticky="w",
                padx=(0, 12),
                pady=(0, 8)
            )

        # Footer
        footer = ctk.CTkLabel(
            card,
            text=(
                "© 2024 Academic Risk Analyzer. This application is designed to help identify "
                "students at risk of academic failure and provide actionable insights for intervention. "
                "All predictions should be used in conjunction with professional academic advising."
            ),
            font=ctk.CTkFont(size=11),
            text_color=TEXT_TERTIARY,
            justify="center",
            anchor="center",
            wraplength=800
        )

        footer.grid(
            row=6,
            column=0,
            sticky="ew",
            padx=25,
            pady=(20, 20)
        )