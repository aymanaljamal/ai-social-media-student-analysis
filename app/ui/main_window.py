import customtkinter as ctk

from app.ui.prediction_view import PredictionView
from app.ui.about_view import AboutView
from app.ui.results_view import ResultsView


# =========================================================
# APPLICATION COLORS
# =========================================================

RED = "#D62828"
RED_DARK = "#B71C1C"
RED_LIGHT = "#FDECEC"

WHITE = "#FFFFFF"
BACKGROUND = "#F7F7F8"
CARD = "#FFFFFF"

TEXT = "#171717"
TEXT_SECONDARY = "#6B7280"
BORDER = "#E5E7EB"


class MainWindow(ctk.CTk):

    def __init__(self):

        # Appearance must be configured before creating widgets
        ctk.set_appearance_mode("Light")
        ctk.set_default_color_theme("blue")

        super().__init__()

        # =====================================================
        # WINDOW
        # =====================================================

        self.title("Student Risk AI")
        self.geometry("1250x800")
        self.minsize(1050, 700)

        self.configure(
            fg_color=BACKGROUND
        )

        # =====================================================
        # MAIN GRID
        # =====================================================

        self.grid_columnconfigure(
            0,
            weight=0
        )

        self.grid_columnconfigure(
            1,
            weight=1
        )

        self.grid_rowconfigure(
            0,
            weight=1
        )

        # =====================================================
        # CREATE UI
        # =====================================================

        self.create_sidebar()
        self.create_content_area()

        self.show_prediction_view()

    # =========================================================
    # SIDEBAR
    # =========================================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self,
            width=245,
            corner_radius=0,
            fg_color=WHITE
        )

        self.sidebar.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.sidebar.grid_propagate(False)

        self.sidebar.grid_rowconfigure(
            5,
            weight=1
        )

        # -----------------------------------------------------
        # LOGO
        # -----------------------------------------------------

        logo_container = ctk.CTkFrame(
            self.sidebar,
            fg_color=RED,
            corner_radius=16,
            width=58,
            height=58
        )

        logo_container.grid(
            row=0,
            column=0,
            padx=25,
            pady=(30, 12),
            sticky="w"
        )

        logo_container.grid_propagate(False)

        logo_icon = ctk.CTkLabel(
            logo_container,
            text="AI",
            text_color=WHITE,
            font=ctk.CTkFont(
                size=18,
                weight="bold"
            )
        )

        logo_icon.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        # -----------------------------------------------------
        # BRAND
        # -----------------------------------------------------

        brand = ctk.CTkLabel(
            self.sidebar,
            text="STUDENT RISK",
            font=ctk.CTkFont(
                size=22,
                weight="bold"
            ),
            text_color=TEXT
        )

        brand.grid(
            row=1,
            column=0,
            padx=25,
            sticky="w"
        )

        subtitle = ctk.CTkLabel(
            self.sidebar,
            text="AI Academic Assessment",
            font=ctk.CTkFont(
                size=12
            ),
            text_color=TEXT_SECONDARY
        )

        subtitle.grid(
            row=2,
            column=0,
            padx=25,
            pady=(2, 35),
            sticky="w"
        )

        # -----------------------------------------------------
        # NAVIGATION
        # -----------------------------------------------------

        self.prediction_button = ctk.CTkButton(
            self.sidebar,
            text="  Prediction",
            anchor="w",
            height=46,
            corner_radius=10,
            font=ctk.CTkFont(
                size=14,
                weight="bold"
            ),
            fg_color=RED,
            hover_color=RED_DARK,
            text_color=WHITE,
            command=self.show_prediction_view
        )

        self.prediction_button.grid(
            row=3,
            column=0,
            padx=20,
            pady=6,
            sticky="ew"
        )

        self.about_button = ctk.CTkButton(
            self.sidebar,
            text="  About Project",
            anchor="w",
            height=46,
            corner_radius=10,
            font=ctk.CTkFont(
                size=14
            ),
            fg_color="transparent",
            hover_color=RED_LIGHT,
            text_color=TEXT_SECONDARY,
            command=self.show_about_view
        )

        self.about_button.grid(
            row=4,
            column=0,
            padx=20,
            pady=6,
            sticky="ew"
        )

        # -----------------------------------------------------
        # VERSION
        # -----------------------------------------------------

        version = ctk.CTkLabel(
            self.sidebar,
            text="Student Risk AI\nVersion 1.0.0",
            font=ctk.CTkFont(
                size=11
            ),
            text_color=TEXT_SECONDARY,
            justify="left"
        )

        version.grid(
            row=6,
            column=0,
            padx=25,
            pady=(10, 25),
            sticky="sw"
        )

    # =========================================================
    # CONTENT AREA
    # =========================================================

    def create_content_area(self):

        self.content_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color=BACKGROUND
        )

        self.content_frame.grid(
            row=0,
            column=1,
            sticky="nsew"
        )

        self.content_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.content_frame.grid_rowconfigure(
            0,
            weight=1
        )

    # =========================================================
    # CLEAR CONTENT
    # =========================================================

    def clear_content(self):

        for widget in self.content_frame.winfo_children():
            widget.destroy()

    # =========================================================
    # PREDICTION VIEW
    # =========================================================

    def show_prediction_view(self):

        self.clear_content()

        self.prediction_button.configure(
            fg_color=RED,
            text_color=WHITE
        )

        self.about_button.configure(
            fg_color="transparent",
            text_color=TEXT_SECONDARY
        )

        view = PredictionView(
            self.content_frame,
            on_prediction=self.show_results_view
        )

        view.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # =========================================================
    # RESULTS VIEW
    # =========================================================

    def show_results_view(
        self,
        risk_level="High",
        probability=78.5
    ):

        self.clear_content()

        self.prediction_button.configure(
            fg_color=RED,
            text_color=WHITE
        )

        self.about_button.configure(
            fg_color="transparent",
            text_color=TEXT_SECONDARY
        )

        view = ResultsView(
            self.content_frame,
            risk_level=risk_level,
            probability=probability,
            on_back=self.show_prediction_view
        )

        view.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

    # =========================================================
    # ABOUT VIEW
    # =========================================================

    def show_about_view(self):

        self.clear_content()

        self.prediction_button.configure(
            fg_color="transparent",
            text_color=TEXT_SECONDARY
        )

        self.about_button.configure(
            fg_color=RED,
            text_color=WHITE
        )

        view = AboutView(
            self.content_frame
        )

        view.grid(
            row=0,
            column=0,
            sticky="nsew"
        )