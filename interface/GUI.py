import tkinter as tk
from tkinter import ttk

from PIL import Image, ImageTk

from genetic_algorithm import GeneticAlgorithm


class GeneticAlgorithmGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Genetic Algorithm")

        self.function_var = tk.StringVar()
        self.init_population_var = tk.IntVar()
        self.generations_var = tk.IntVar()
        self.probability_of_gen_var = tk.DoubleVar()
        self.probability_of_ind_var = tk.DoubleVar()
        self.probability_of_crs_var = tk.DoubleVar()
        self.maximum_population_var = tk.IntVar()
        self.a_var = tk.DoubleVar()
        self.b_var = tk.DoubleVar()
        self.resolution_var = tk.DoubleVar()
        self.min_or_max_var = tk.BooleanVar()
        self.image_label = tk.Label(self.root)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="F(x):").grid(row=0, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.function_var).grid(row=0, column=1, columnspan=2)

        tk.Label(self.root, text="Initial Population:").grid(row=1, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.init_population_var).grid(row=1, column=1)

        tk.Label(self.root, text="Maximum Population:").grid(row=1, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.maximum_population_var).grid(row=1, column=3)

        tk.Label(self.root, text="Probability of Gen:").grid(row=2, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.probability_of_gen_var).grid(row=2, column=1)

        tk.Label(self.root, text="Probability of Ind:").grid(row=2, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.probability_of_ind_var).grid(row=2, column=3)

        tk.Label(self.root, text="Generations:").grid(row=3, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.generations_var).grid(row=3, column=1)

        tk.Label(self.root, text="Resolution:").grid(row=3, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.resolution_var).grid(row=3, column=3)

        tk.Label(self.root, text="a").grid(row=4, column=0, sticky="w")
        tk.Entry(self.root, textvariable=self.a_var).grid(row=4, column=1)

        tk.Label(self.root, text="b").grid(row=4, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.b_var).grid(row=4, column=3)

        ttk.Radiobutton(self.root, text="Maximizar", variable=self.min_or_max_var, value=True).grid(row=6, column=2,
                                                                                                    sticky="w")
        ttk.Radiobutton(self.root, text="Minimizar", variable=self.min_or_max_var, value=False).grid(row=6, column=3,
                                                                                                     sticky="w")
        tk.Label(self.root, text="Probability of Crz:").grid(row=7, column=2, sticky="w")
        tk.Entry(self.root, textvariable=self.probability_of_crs_var).grid(row=7, column=3)

        tk.Button(self.root, text="Run Genetic Algorithm", command=self.run_genetic_algorithm).grid(row=10, column=0,
                                                                                                    columnspan=4)
        self.image_label.grid(row=11, column=0, columnspan=4)
        self.root.mainloop()

    def run_genetic_algorithm(self):
        principal_function = self.function_var.get()
        original_population = self.init_population_var.get()
        generations = self.generations_var.get()
        probability_of_gen = self.probability_of_gen_var.get()
        probability_of_ind = self.probability_of_ind_var.get()
        maximum_population = self.maximum_population_var.get()
        a = self.a_var.get()
        b = self.b_var.get()
        resolution = self.resolution_var.get()
        min_or_max = self.min_or_max_var.get()
        genetic_algorithm = GeneticAlgorithm(
            principal_function=principal_function,
            original_population=original_population,
            generations=generations,
            probability_of_gen=probability_of_gen,
            probability_of_ind=probability_of_ind,
            maximum_population=maximum_population,
            a=a,
            b=b,
            resolution=resolution,
            min_or_max=min_or_max
        )
        genetic_algorithm.start()
        self.load_image()

    def init_values(self):
        #6 * (np.log(0.1 + x**3))+ np.cos(x**2)
        self.function_var.set("(x**3) -(x**3)*math.cos(5*x)")
        self.init_population_var.set(5)
        self.generations_var.set(10)
        self.probability_of_gen_var.set(0.2)
        self.probability_of_ind_var.set(0.4)
        self.maximum_population_var.set(20)
        self.a_var.set(0)
        self.b_var.set(2)
        self.resolution_var.set(0.05)

    def load_image(self):
        image_path = "../graphics/fitness/statistic-fitness-graphic.png"  # Reemplaza con la ruta de tu imagen
        original_image = Image.open(image_path)

        resized_image = original_image.resize((640, 400))
        photo = ImageTk.PhotoImage(resized_image)

        self.image_label.configure(image=photo)
        self.image_label.image = photo


root = tk.Tk()
app = GeneticAlgorithmGUI(root)
