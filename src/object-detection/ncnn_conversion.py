from ultralytics import YOLO

# Load a YOLO11 PyTorch model
model = YOLO("yolo11n.pt")

# Export the model to NCNN format
model.export(format="ncnn")  # creates 'yolo11n_ncnn_model'

ncnn_model = YOLO("yolo11n_ncnn_model")