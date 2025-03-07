import numpy as np
import plotly.graph_objects as go

class EstadoCuantico:
    def __init__(self, vector_estado):
        self.vector_estado = np.array(vector_estado, dtype=complex)
        self.normalizar()

    def normalizar(self):
        norma = np.linalg.norm(self.vector_estado)
        if norma != 0:
            self.vector_estado /= norma

    def representar_bloch(self):
        theta = 2 * np.arccos(np.abs(self.vector_estado[0]))
        phi = np.angle(self.vector_estado[1]) - np.angle(self.vector_estado[0])

        bx = np.sin(theta) * np.cos(phi)
        by = np.sin(theta) * np.sin(phi)
        bz = np.cos(theta)

        # esfera de bloch
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 50)
        x = np.outer(np.cos(u), np.sin(v))
        y = np.outer(np.sin(u), np.sin(v))
        z = np.outer(np.ones(np.size(u)), np.cos(v))

        fig = go.Figure()

        # poner esfera de bloch
        fig.add_trace(go.Surface(z=z, x=x, y=y, opacity=0.3, colorscale='blues'))

        # agregar el vector de estado
        fig.add_trace(go.Scatter3d(x=[0, bx], y=[0, by], z=[0, bz],
                                   marker=dict(size=4, color='red'),
                                   line=dict(width=5, color='red'),
                                   name="Estado CUantico"))

        # visicion 3D
        fig.update_layout(scene=dict(
            xaxis_title="X",
            yaxis_title="Y",
            zaxis_title="Z",
            aspectmode="cube"
        ))

        fig.show()

# suministrar el estado cuantica
while True:
    try:
        entrada = input("estado cauntico a representar(a,b) donde a y b pertecen a los reales: ")
        estado_usuario = eval(entrada)  # Convierte la entrada en tupla/lista
        if not isinstance(estado_usuario, (list, tuple)) or len(estado_usuario) != 2:
            raise ValueError("el estado esta dado por dos numeros: a y b")
        estado = EstadoCuantico(estado_usuario)
        break
    except Exception as e:
        print(f"estado no valido: {e}.ingrese otro estado.")

estado.representar_bloch()