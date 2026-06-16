# Estructura básica de inferencia con TripoSR
# from tsr.system import TSR
import torch

model = TSR.from_pretrained("stabilityai/TripoSR", torch_dtype=torch.float16)
model.to("cuda") # Lo corres en tu tarjeta gráfica
# Luego pasas la imagen y exportas el archivo .obj o .glb
