import tkinter as tk
from tkinter import ttk

class PredictedCSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python app")
        self.root.geometry("720x760")
        self.root.configure(bg="#f2e1e1")  # light pink background

        label_font = ("Times New Roman", 12)
        title_font = ("Times New Roman", 14, "bold")
        output_font = ("Times New Roman", 14, "bold")
        button_font = ("Times New Roman", 12, "bold")

        # ================= PANEL =================
        panel = tk.LabelFrame(
            root,
            text=" Mix Design Parameters ",
            font=title_font,
            bg="#f2e1e1",
            fg="black",
            padx=15,
            pady=15
        )
        panel.pack(padx=20, pady=20, fill="x")

        self.fields = [
            "Metakaolin (MK) (kg/m³)",
            "Sodium Hydroxide Solution (SHS) (kg/m³)",
            "Sodium Hydroxide Solution Molarity (SHSM) (M)",
            "Sodium Silicate Solution (SSS) (kg/m³)",
            "Water (W) (kg/m³)",
            "Water-to-Solid ratio (W/S)",
            "Sodium Oxide-to-Aluminum Oxide ratio (Na₂O/Al₂O₃)",
            "Silica-to-Alumina ratio (SiO₂/Al₂O₃)",
            "Water-to-Sodium Oxide ratio (H₂O/Na₂O)",
            "Coarse-to-Fine Aggregate ratio (CA/FA)",
            "Superplasticizer Dosage (SP) (kg/m³)",
            "Categorical Variable for Pre-Curing Strategies (PCC) (kg/m³)",
            "Curing Temperature (CT) (°C)",
            "Age (Days)"
        ]

        self.entries = []

        for i, field in enumerate(self.fields):
            lbl = tk.Label(panel, text=field, font=label_font, bg="#f2e1e1")
            lbl.grid(row=i, column=0, sticky="w", pady=6)

            ent = tk.Entry(panel, width=12, justify="center")
            ent.insert(0, "0")
            ent.grid(row=i, column=1, padx=20, pady=6)
            self.entries.append(ent)

        # ================= OUTPUT =================
        output_frame = tk.Frame(root, bg="#f2e1e1")
        output_frame.pack(pady=25)

        tk.Label(
            output_frame,
            text="Predicted Compressive Strength (CS) (MPa) :",
            font=output_font,
            bg="#f2e1e1"
        ).pack(side="left", padx=10)

        self.output_val = tk.Label(
            output_frame,
            text="---",
            font=output_font,
            bg="#f2e1e1"
        )
        self.output_val.pack(side="left")

        # ================= BUTTONS =================
        btn_frame = tk.Frame(root, bg="#f2e1e1")
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="Predict",
            font=button_font,
            bg="#6ed36e",
            width=12,
            command=self.predict
        ).grid(row=0, column=0, padx=40)

        tk.Button(
            btn_frame,
            text="Clear",
            font=button_font,
            bg="#e54848",
            width=12,
            command=self.clear
        ).grid(row=0, column=1, padx=40)

    # ================= FUNCTIONS =================
    def predict(self):
        try:
            x = [float(e.get()) for e in self.entries]
            x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14 = x


            y = (
                0.982418248
                + 0.00157127*x1 + 0.000131323*x2 + 0.0000231498*x3 + 0.000283136*x4
                - 0.008793083*x5 + 10.82395622*x6 - 30.57554886*x7 - 11.1330023*x8
                + 0.0000126636*x9 - 13.69234621*x10 + 3.366626356*x11
                + 0.014887229*x12 + 0.0000183579*x13 + 0.000012*x14

                - 0.00036*x1*x2 + 0.003893*x1*x3 + 0.000503*x1*x4
                + 0.001226*x1*x5 + 0.000169*x1*x6 + 0.000217*x1*x7
                + 0.0006*x1*x8 - 0.000174*x1*x9 - 0.0000876*x1*x10
                + 0.000321*x1*x11 - 0.000177*x1*x12 + 0.004973*x1*x13
                + 0.0000573*x1*x14

                + 0.011256*x2*x3 - 0.001038*x2*x4 - 0.002501*x2*x5
                + 0.000046*x2*x6 + 0.0000714*x2*x7 + 0.000255*x2*x8
                - 0.001381*x2*x9 + 0.034146*x2*x10 + 0.000222*x2*x11
                - 0.000114*x2*x12 - 0.000888*x2*x13 + 0.0000209*x2*x14

                - 0.024897*x3*x4 - 0.076875*x3*x5 + 29.685515*x3*x6
                + 0.00001741*x3*x7 + 0.00004644*x3*x8 + 0.0001627*x3*x9
                + 0.00007757*x3*x10 - 0.0000762*x3*x11 - 0.00001186*x3*x12
                - 0.161935*x3*x13 + 0.00001817*x3*x14

                - 0.001809*x4*x5 + 0.0000840586*x4*x6 + 0.00016466*x4*x7
                + 0.000151171*x4*x8 - 0.012119595*x4*x9 - 0.001464*x4*x10
                - 0.008606*x4*x11 - 0.000375*x4*x12 + 0.0072752*x4*x13
                + 0.0001654*x4*x14

                - 0.54394*x5*x6 + 0.6827603*x5*x7 - 0.0000204*x5*x8
                - 0.0000939*x5*x9 + 0.00001687*x5*x10 - 0.0000129*x5*x11
                - 0.0000731*x5*x12 - 0.000177*x5*x13 + 0.0015599*x5*x14

                + 1.4692051*x6*x7 + 22.306548*x6*x8 + 1.9006966*x6*x9
                + 0.0757717*x6*x10 - 0.949359*x6*x11 - 0.251866*x6*x12
                - 5.447204*x6*x13 - 0.001201*x6*x14

                - 0.173644*x7*x8 + 0.00001205*x7*x9 + 17.550286*x7*x10
                + 0.2174853*x7*x11 - 24.63378*x7*x12 + 0.00001899*x7*x13
                + 0.00001531*x7*x14

                + 0.0000299524*x8*x9 + 0.0000143283*x8*x10
                - 0.0000215287*x8*x11 + 3.025958515*x8*x12
                + 0.0000373312*x8*x13 + 0.0000247301*x8*x14

                + 0.000042*x9*x10 - 0.0000675*x9*x11 - 0.0000119*x9*x12
                + 0.0000418*x9*x13 + 0.0000598*x9*x14

                - 0.69727972946635*x10*x11 + 0.456091*x10*x12
                + 0.0000779*x10*x13 + 0.0000549041*x10*x14

                - 0.0000147853*x11*x12 - 0.000133774*x11*x13
                - 0.000242491*x11*x14

                - 0.0000212649*x12*x13 - 0.0000242265*x12*x14
                - 0.001261372*x13*x14

                - 0.253917537*(x5/x1)
                + 0.069602291*(x4/x1)
                - 0.010050256*(x5/(x1 + x3 + x4))
            )

            self.output_val.config(text=f"{y:.3f}")

        except Exception as e:
            self.output_val.config(text="Error")
            print(e)

    def clear(self):
        for e in self.entries:
            e.delete(0, tk.END)
            e.insert(0, "0")
        self.output_val.config(text="---")


# ================= RUN =================
if __name__ == "__main__":
    root = tk.Tk()
    app = PredictedCSApp(root)
    root.mainloop()